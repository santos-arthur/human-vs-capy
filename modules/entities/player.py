from colorama import Fore, Back, Style
import modules.core.save as save_module
import modules.core.utils as utils_module
import modules.core.menu as menu_module
import modules.items.enchant as enchant_module
import modules.items.armor as armor_module
import modules.entities.enemy as enemy_module
import random

PLAYER_DATA_FILE = 'saves/playerData.json'

def save_status(player_data: dict):
    save_module.save_status(player_data, PLAYER_DATA_FILE)

def load_status():
    return save_module.load_status(PLAYER_DATA_FILE)

def wipe_status():
    save_module.wipe_status(PLAYER_DATA_FILE)

def create_player(name: str, max_hp: int = 10, cur_hp: int = 10, strength: int = 1, dexterity: int = 1, max_actions: int = 2, actions: int = 2, max_weapons: int = 2, weapons: list = [], armor: dict = {}, items: list = [], points: int = 0) -> dict:
    return {
        'name':         name,
        'max_hp':       max_hp,
        'cur_hp':       cur_hp,
        'strength':     strength,
        'dexterity':    dexterity,
        'max_actions':  max_actions,
        'actions':      actions,
        'max_weapons':  max_weapons,
        'weapons':      weapons,
        'armor':        armor,
        'items':        items,
        'points':       points,
    }

def get_armor_class(player_data: dict):
    return 10 + player_data['dexterity'] + player_data['armor']['armor_modifier']

def show_card(player_data: dict, game_data: dict):

    armor_class = get_armor_class(player_data)

    print("╔" + "═" * 46 + "╗")
    
    text_padding = utils_module.centered_text_padding(player_data['name'], 46)
    second_padding = " " * ( 46 - len(player_data['name']) - len(text_padding))
    print("║" + text_padding + player_data['name'] + second_padding + "║")
    
     
    print("╠" + "═" * 16 + "╦" + "═" * 12 + "╦" + "═" * 16 + "╣")
    
    if ((player_data['cur_hp'] * 100) / player_data["max_hp"]) > 50:
        hp_color = Fore.GREEN
    elif ((player_data['cur_hp'] * 100) / player_data["max_hp"]) > 25:
        hp_color = Fore.YELLOW
    else:
        hp_color = Fore.RED

    hp_text = str(player_data["cur_hp"]) + "/" + str(player_data["max_hp"])
    
    armor_class = str(get_armor_class(player_data))

    if ((player_data['actions'] * 100) / player_data["max_actions"]) > 50:
        actions_color = Fore.GREEN
    elif ((player_data['actions'] * 100) / player_data["max_actions"]) > 25:
        actions_color = Fore.YELLOW
    else:
        actions_color = Fore.RED

    actions_text = str(player_data["actions"]) + "/" + str(player_data["max_actions"])

    print("║ Vida: " + hp_color + hp_text + Fore.RESET + " " * (9 - len(hp_text)) +  "║ Defesa: " + Fore.CYAN + armor_class + Fore.RESET + " " * (3 - len(armor_class)) + "║ Ações: " + actions_color + actions_text + Fore.RESET + " " * (8 - len(actions_text)) + "║")
    
    print("╠" + "═" * 10 + "╦"  + "═" * 5 + "╩" + "═" * 4 + "╦"  + "═" * 7 + "╩" + "═" * 3 + "╦" + "═" * 12 + "╣")

    strength = str(player_data['strength'])
    dexterity = str(player_data['dexterity'])
    level = str(game_data['level'])
    points = str(player_data['points'])
    
    print("║ FOR: " + Fore.CYAN + strength + Fore.RESET + " " * (4 - len(strength)) + "║ VEL: " + Fore.CYAN + dexterity + Fore.RESET + " " * (4 - len(dexterity)) + "║ Nível: " + Fore.CYAN + level + Fore.RESET + " " * (3 - len(level)) + "║ Pontos: " + Fore.CYAN + points + Fore.RESET + " " * (3 - len(points)) + "║")
    
    print("╚" + "═" * 10 + "╩" + "═" * 10  + "╩" + "═" * 11  + "╩" + "═" * 12 + "╝")
    


def attack_rolls(player_data: dict, attack_weapon: dict, enemy_data: dict, game_data: dict):
    roll = random.randint(1, 20)
    attack_hits = roll + player_data['strength'] + attack_weapon['modifier'] + (5 if game_data['difficulty'] == 0 else 0) >= enemy_data['armor_class']
    critical_hit = roll == 20

    damage = 0

    if attack_hits:
        damage = sum(random.randint(1, attack_weapon['damage_dice']) for _ in range(attack_weapon['dice_amount']))
        damage += player_data['strength'] + attack_weapon['modifier']
        if critical_hit:
            damage += attack_weapon['damage_dice']

    return {
        'attack_hits': attack_hits,
        'critical_hit': critical_hit,
        'damage': damage
    }

def attack(player_data: dict, attack_weapon: dict, enemy_data: dict, game_data: dict):
    player_attack_rolls = attack_rolls(player_data, attack_weapon, enemy_data, game_data)
    player_data['actions'] -= attack_weapon['actions']

    if player_attack_rolls['attack_hits']:
        text = 'VOCÊ REALIZA UM GOLPE CRÍTICO!' if player_attack_rolls['critical_hit'] else 'Você acerta um golpe no inimigo!'
        utils_module.centered_print(text)
        print()
        
        utils_module.centered_print(f"Você causa {player_attack_rolls['damage']} de dano!")
        print()

        if attack_weapon['enchant'] is not None:
            attack_effect = enchant_module.apply_effect(player_data, attack_weapon, enemy_data)

            long_text = ''

            if attack_effect['damage'] > 0:
                long_text = f"E o encanamtento mágico da sua arma causou {attack_effect['damage']} de dano adicional!"
                player_attack_rolls['damage'] += attack_effect['damage']
            elif attack_effect['heal'] > 0:
                long_text = f"E o encanamtento mágico da sua arma lhe curou {attack_effect['heal']}!"
                player_data['cur_hp']  += attack_effect['heal']
            elif attack_effect['frozen']:
                long_text = f"E o encanamtento mágico da sua arma congelou o seu inimigo!"
                enemy_data['frozen'] = True

            if long_text is not '':
                for line in utils_module.split_into_lines(long_text, 38):
                    utils_module.centered_print(line)


        enemy_data['cur_hp'] -= min(player_attack_rolls['damage'], enemy_data['cur_hp'])
    else:
        utils_module.centered_print('Você errou o ataque!')
        
    
    save_status(player_data)
    enemy_module.save_status(enemy_data)

def give_item(player_data: dict, item: dict):
    match item['type']:
        case 'weapon':
            player_data['weapons'].append(item['item'])

            if len(player_data['weapons']) > player_data['max_weapons']:
                menu_module.clear_weapon_inventory(player_data)

        case 'armor':
            menu_options = menu_module.get_boolean_menu_options()
            highlighted_option = 0
            while True:
                utils_module.clear()
                utils_module.centered_print("Deseja trocar sua armadura atual?")
                print()
                utils_module.centered_print("ATUAL")
                armor_module.show_armor(player_data['armor'])
                print()
                utils_module.centered_print("NOVA")
                armor_module.show_armor(item['item'])
                print()
                menu_module.show_menu(highlighted_option, menu_options)
                key_pressed, highlighted_option = menu_module.circular_menu(highlighted_option, len(menu_options))
                if key_pressed not in ('up', 'down', 'enter'):
                    utils_module.beep(150, 0.2)
                elif key_pressed == 'enter':
                    utils_module.beep(800, 0.2)
                    utils_module.clear()
                    if menu_options[highlighted_option]['value']:
                        player_data['armor'] = item['item']
                        break

        case 'item':
            item_id = item['item']['id']
            for player_item in player_data['items']:
                if player_item['id'] == item_id:
                    player_item['amount'] += 1
                    return
                
            item['item']['amount'] = 1
            player_data['items'].append(item['item'])

def show_inventory(player_data: dict, game_data: dict):
    while True:
        item = menu_module.show_inventory(player_data, game_data)
        if item is None:
            break
        
        utils_module.clear()
        use_item(player_data, item)
        print()
        utils_module.press_any_key()

def use_item(player_data: dict, item: dict) -> bool:
    if player_data['actions'] <= 0:
        utils_module.centered_print("Você não tem mais ações para usar este item!")
        return False
    
    player_data['actions'] -= 1

    value = 0
    if item['dice_amount'] > 0:
        values = [random.randint(1, item['dice']) for _ in range(item['dice_amount'])]
        value += sum(values)
    value += item['modifier']

    match item['attr']:
        case 'cur_hp':
            value = min(value, (player_data['max_hp'] - player_data['cur_hp']))
            player_data['cur_hp'] += value
            utils_module.centered_print(f"Você foi curado em {value} pontos de VIDA!")
        case 'max_hp':
            player_data['max_hp'] += value
            player_data['cur_hp'] += value
            utils_module.centered_print(f"Você ganhou {value} pontos de VIDA MÁXIMA!")
        case 'strength':
            player_data['strength'] += value
            utils_module.centered_print(f"Você ganhou {value} pontos de FORÇA!")
        case 'dexterity':
            player_data['dexterity'] += value
            utils_module.centered_print(f"Você ganhou {value} pontos de DESTREZA!")
        case 'max_actions':
            player_data['max_actions'] += value
            player_data['actions'] += value
            utils_module.centered_print(f"Você ganhou {value} AÇÕES MÁXIMAS!")        
        case 'actions':
            player_data['actions'] += value
            utils_module.centered_print(f"Você ganhou {value} AÇÕES neste turno!")

    if item['amount'] > 1:
        item['amount'] -= 1
    else:
        player_data['items'].remove(item)
    
    save_status(player_data)
    return True

