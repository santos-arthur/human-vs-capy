import modules.core.utils as utils_module
import modules.core.menu as menu_module
import modules.core.save as save_module
import modules.core.leaderboard as leaderboard_module
import modules.entities.player as player_module
import modules.entities.enemy as enemy_module
import modules.items.armor as armor_module
import modules.items.loot as loot_module
import random
import time

GAME_DATA_FILE = 'saves/gameData.json'

def save_status(game_data: dict):
    save_module.save_status(game_data, GAME_DATA_FILE)

def load_status():
    return save_module.load_status(GAME_DATA_FILE)

def wipe_status():
    save_module.wipe_status(GAME_DATA_FILE)


def new_game():
    wipe_status()
    player_module.wipe_status()
    loot_module.wipe_status()
    enemy_module.wipe_status()

    utils_module.clear()
    time.sleep(0.5)
    print("Seja Bem-Vindo ao Human vs Capy, um simulador muito realisata de matar capivara.")
    print()
    time.sleep(0.5)
    print("Caso você seja um fiscal do IBAMA, vá embora agora, não tem nada pra você aqui!")
    print()
    time.sleep(0.5)
    print("Todavia, se você for uma pessoa que nutre profundo ódio contra as Capivaras, este jogo é pra você!")
    print()
    time.sleep(0.5)
    print("Aqui você irá enfrentar diversas capivaras em 10 Níveis diferentes. Algumas capivaras são mais fortes que outras, então tome muito cuidado.")
    print()
    time.sleep(0.5)
    print("Matar capivaras lhe concede pontos e a chance de ganhar novos itens e melhorias para o seu personagem.")
    print()
    time.sleep(0.5)
    utils_module.press_any_key()
    utils_module.clear()
    time.sleep(0.5)
    
    name = menu_module.get_player_name()

    difficulty = menu_module.get_game_difficulty()

    game_data = {
        'difficulty': difficulty,
        'level': 0,
        'enemies_defeated': 0,
        'enemies_remaining_in_level': 0,
    }

    save_status(game_data)

    player_data = player_module.create_player(name=name, armor=armor_module.clothes())

    player_module.save_status(player_data)

    run_game()

def run_game():
    while True:
        player_data = player_module.load_status()
        game_data = load_status()
        
        if len(player_data['weapons']) > player_data['max_weapons']: #Validação para quando fecha o game enquanto limpa o inventário
            menu_module.clear_weapon_inventory(player_data)

        if game_data['level'] == 0 or game_data['enemies_remaining_in_level'] == 0:
            if game_data['level'] >= 1:
                utils_module.clear()
                utils_module.show_congratulations()
                print()
                utils_module.centered_print("Você passou de nível!")
                print()
                utils_module.centered_print("As capivaras deste nível devem ser")
                utils_module.centered_print("ainda mais fortes que as outras!")
                print()
                utils_module.press_any_key()
            game_data = new_level(game_data)
            pass
        elif (game_data['level'] == 10 and game_data['enemies_remaining_in_level'] == 0) or (player_data['cur_hp'] <= 0):
            end_game(game_data, player_data)
            break
        
        
        enemy_data = enemy_module.load_status()

        if enemy_data is None:
            enemy_data = enemy_module.get_random_enemy(
                difficulty=game_data['difficulty'],
                level=game_data['level'],
                points=player_data['points']
            )
            enemy_module.save_status(enemy_data)
            utils_module.clear()
            long_text = f"Um(a) {enemy_data['name']} selvagem apareceu!"
            for line in utils_module.split_into_lines(long_text, 30):
                utils_module.centered_print(line)
            print()
            utils_module.press_any_key()
        
        enemy_alive = enemy_data['cur_hp'] > 0
            

        while enemy_alive:
            
            while True: #Player Turn
                if enemy_data['cur_hp'] <= 0:
                    enemy_alive = False
                    break
                player_data = player_module.load_status()
                enemy_data  = enemy_module.load_status()
                action = menu_module.actions_menu(player_data, enemy_data, game_data)
                match action:
                    case 'attack':
                        attack_weapon = menu_module.attacks_menu(player_data, enemy_data, game_data)
                        if attack_weapon is not None:
                            player_module.attack(player_data, attack_weapon, enemy_data, game_data)
                            print()
                            utils_module.press_any_key()
                    case 'show_enemy':
                        enemy_module.show_card(enemy_data, True)
                        print()
                        utils_module.press_any_key()
                    case 'show_inventory':
                        player_module.show_inventory(player_data, game_data)
                    case 'end_turn':
                        utils_module.clear()
                        utils_module.centered_print('Você passou o seu turno!')
                        print()
                        utils_module.press_any_key()
                        player_data['actions'] = player_data['max_actions']
                        player_module.save_status(player_data)
                        break

            enemy_data = enemy_module.load_status()

            if enemy_data['cur_hp'] > 0:
                while True: #Enemy turn
                    player_data = player_module.load_status()
                    enemy_data  = enemy_module.load_status()
                    utils_module.clear()
                    if enemy_data['frozen']:
                        utils_module.centered_print(f"{enemy_data['name']} está congelado!")
                        print()
                        utils_module.centered_print(f"{enemy_data['name']} perde seu turno!")
                        print()
                        enemy_data['frozen'] == False
                        enemy_module.save_status(enemy_data)
                        utils_module.press_any_key()
                        break
                    elif enemy_data['actions'] == 0:
                        utils_module.centered_print(f"Acabou o turno de {enemy_data['name']}.")
                        print()
                        enemy_data['actions'] = enemy_data['max_actions']
                        enemy_module.save_status(enemy_data)
                        utils_module.press_any_key()
                        break

                    if player_data['cur_hp'] > 0:
                        enemy_module.attack(enemy_data, player_data)
                    else:
                        enemy_alive = False
                        break

                    utils_module.press_any_key()
                    utils_module.clear()
                    player_module.show_card(player_data, game_data)
                    utils_module.centered_print('INIMIGO')
                    enemy_module.show_card(enemy_data)
                    print()
                    utils_module.press_any_key()
                enemy_data['actions'] = enemy_data['max_actions']
                enemy_module.save_status(enemy_data)

        if player_data['cur_hp'] <= 0:
            end_game(game_data, player_data)
            break
        
        enemy_data = enemy_module.load_status()
        player_data = player_module.load_status()
        utils_module.clear()
        utils_module.centered_print(f"Parabéns! Você derrotou {enemy_data['name']}!")
        print()

        enemy_loot = loot_module.load_status()

        if enemy_loot is None:
            enemy_loot = loot_module.get_random_loot(game_data)
            loot_module.save_status(enemy_loot)
        
        utils_module.press_any_key()
        if menu_module.loot_menu(enemy_data, enemy_loot):
            player_module.give_item(player_data, enemy_loot)
        else:
            utils_module.centered_print("Você deixa o item para trás!") 
        
        game_data['enemies_defeated'] += 1
        game_data['enemies_remaining_in_level'] -= 1

        enemy_module.wipe_status()
        loot_module.wipe_status()
        player_module.save_status(player_data)
        save_status(game_data)

def new_level(game_data: dict) -> dict:
    game_data['level'] += 1
    game_data['enemies_remaining_in_level'] = enemies_in_level(difficulty=game_data['difficulty'], level=game_data['level'])

    return game_data

def enemies_in_level(difficulty: int, level: int) -> int:
    if level == 1:
        enemies = 1
    elif level <= 3:
        enemies = int(random.choices([1,2], weights=[0.7, 0.3])[0])
    elif level <= 6:
        enemies = int(random.choices([2,3], weights=[0.6, 0.4])[0])
    elif level <= 9:
        enemies = int(random.choices([3,4], weights=[0.5, 0.5])[0])
    else:
        enemies = 5
    
    enemies += difficulty

    return enemies

def end_game(game_data: dict, player_data: dict):
    leaderboard_module.add_to_leaderboard(game_data, player_data)
    if player_data['cur_hp'] > 0:
        utils_module.show_congratulations()
        print()
        utils_module.centered_print("Você matou todas as capivaras")
        utils_module.centered_print("que viu pela frente!")
        print()
        utils_module.centered_print("Agora corre, que o IBAMA tá chegando!")
        print()
    else:
        utils_module.show_lose()
        print()
        utils_module.centered_print("As capivaras são implacáveis!")
        print()
        utils_module.centered_print("Você lutou bravamente!")
        utils_module.centered_print("Mas caiu morto como um saco de merda")
        print()
    
    utils_module.press_any_key()
    
    
