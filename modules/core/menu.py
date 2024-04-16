import keyboard
from colorama import Fore, Back, Style
import modules.core.utils as utils_module
import modules.core.game as game_module
import modules.entities.player as player_module
import modules.entities.enemy as enemy_module
import modules.items.weapon as weapon_module
import modules.items.armor as armor_module
import modules.items.item as item_module


def main_menu() -> str:
    main_menu_options = [
        {'label': 'Novo Jogo', 'value': 'new_game'},
        {'label': 'Placar de Líderes', 'value': 'leaderboard'},
        {'label': 'Configurações', 'value': 'configs'},
        {'label': 'Créditos', 'value': 'credits'},
        {'label': 'Sair', 'value': 'exit'}
    ]

    game_data = game_module.load_status()
    player_data = player_module.load_status()

    if game_data is not None and player_data is not None:
        main_menu_options.insert(0, {'label': 'Continuar Jogo', 'value': 'continue_game'})

    highlighted_option = 0
    while True:
        utils_module.clear()
        utils_module.game_banner()
        print()
        show_menu(highlighted_option, main_menu_options)
        key_pressed, highlighted_option = circular_menu(highlighted_option, len(main_menu_options))
        if key_pressed == 'enter':
            utils_module.beep(800, 0.2)
            utils_module.clear()
            return main_menu_options[highlighted_option]['value']
        else:
            if key_pressed not in ('up', 'down'):
                utils_module.beep(150, 0.2)

def show_menu(highlighted_option: int, menu_options: list):
    for index, menu_option in enumerate(menu_options, start=0):
        label   = f"  {menu_option['label']}  "
        padding = utils_module.centered_text_padding(label)
        print(Fore.WHITE + Back.RESET + padding, end='', sep='')

        if highlighted_option == index:
            print(Fore.BLACK + Back.WHITE, end='', sep='')

        print(label + Fore.WHITE + Back.RESET)

def circular_menu(selected_option: int, menu_lenght: int) -> tuple[str, int]:
    while True:
        while keyboard.is_pressed('enter') or keyboard.is_pressed('down') or keyboard.is_pressed('up'):
            pass

        key_pressed = keyboard.read_event(suppress=True)
        
        if key_pressed.event_type == keyboard.KEY_UP:
            if key_pressed.name == 'down':
                utils_module.beep(800, 0.2)
                selected_option = (selected_option + 1) % menu_lenght
            elif key_pressed.name == 'up':
                utils_module.beep(800, 0.2)
                selected_option = (selected_option - 1) % menu_lenght     
            return key_pressed.name, selected_option

def show_2d_menu(highlighted_option: dict, menu_options: list):
    for row in menu_options:
        for column in row:
            label   = f"  {column['label']}  "
            padding = utils_module.centered_text_padding(label, 24)
            print(Fore.WHITE + Back.RESET + padding, end='', sep='')

            if highlighted_option['row'] == menu_options.index(row) and highlighted_option['column'] == row.index(column):
                print(Fore.BLACK + Back.WHITE, end='', sep='')

            print(label + Fore.WHITE + Back.RESET + padding, end='', sep='')
        print()

def circular_2d_menu(selected_option: dict, menu_row_lenght: int,  menu_column_lenght: int) -> tuple[str, int]:
    while True:
        while keyboard.is_pressed('enter') or keyboard.is_pressed('down') or keyboard.is_pressed('up') or keyboard.is_pressed('left') or keyboard.is_pressed('right'):
            pass

        key_pressed = keyboard.read_event(suppress=True)
        
        if key_pressed.event_type == keyboard.KEY_UP:
            if key_pressed.name == 'down':
                utils_module.beep(800, 0.2)
                selected_option['row'] = (selected_option['row'] + 1) % menu_row_lenght
            elif key_pressed.name == 'up':
                utils_module.beep(800, 0.2)
                selected_option['row'] = (selected_option['row'] - 1) % menu_row_lenght  
            elif key_pressed.name == 'right':
                utils_module.beep(800, 0.2)
                selected_option['column'] = (selected_option['column'] + 1) % menu_column_lenght  
            elif key_pressed.name == 'left':
                utils_module.beep(800, 0.2)
                selected_option['column'] = (selected_option['column'] - 1) % menu_column_lenght     
            return key_pressed.name, selected_option

def get_boolean_menu_options() -> list:
    return [
        {'label': 'SIM', 'value': True},
        {'label': 'NÃO', 'value': False},
    ]

def get_player_name() -> str:
    name = input("Para começarmos, qual seu nome? ")
    menu_options = get_boolean_menu_options()
    highlighted_option = 0

    while True:
        utils_module.clear()
        utils_module.centered_print(f"Você se chama {name}?")
        
        show_menu(highlighted_option, menu_options)
        key_pressed, highlighted_option = circular_menu(highlighted_option, len(menu_options))
        if key_pressed not in ('up', 'down', 'enter'):
            utils_module.beep(150, 0.2)
        elif key_pressed == 'enter':
            utils_module.beep(800, 0.2)
            utils_module.clear()
            if menu_options[highlighted_option]['value']:
                return name
            else:
                utils_module.clear()
                name = input("Então, qual seu nome? ")

def get_game_difficulty() -> int:
    menu_options = [
        {'label': 'Fácil', 'value': 0},
        {'label': 'Médio', 'value': 1},
        {'label': 'Difícil', 'value': 2},
    ]
    highlighted_option = 0

    while True:
        utils_module.clear()
        utils_module.centered_print(f"Selecione a dificuldade:")

        show_menu(highlighted_option, menu_options)
        key_pressed, highlighted_option = circular_menu(highlighted_option, len(menu_options))
        if key_pressed not in ('up', 'down', 'enter'):
            utils_module.beep(150, 0.2)
        elif key_pressed == 'enter':
            utils_module.beep(800, 0.2)
            utils_module.clear()
            if confirm_menu_action(f"Deseja jogar na dificulade {menu_options[highlighted_option]['label']}?"):
                return menu_options[highlighted_option]['value']

def confirm_menu_action(text: str) -> bool:
     
    menu_options = get_boolean_menu_options()
    highlighted_option = 0
    while True:
        utils_module.clear()
        utils_module.centered_print(text)
        
        show_menu(highlighted_option, menu_options)
        key_pressed, highlighted_option = circular_menu(highlighted_option, len(menu_options))
        if key_pressed not in ('up', 'down', 'enter'):
            utils_module.beep(150, 0.2)
        elif key_pressed == 'enter':
            utils_module.beep(800, 0.2)
            utils_module.clear()
            return menu_options[highlighted_option]['value']
        
def actions_menu(player_data: dict, enemy_data: dict, game_data: dict) -> str:
    actions_menu_options = [
        [{'label': 'Atacar', 'value': 'attack'},{'label': 'Visualizar Inimigo', 'value': 'show_enemy'}],
        [{'label': 'Inventário', 'value': 'show_inventory'},{'label': 'Passar Turno', 'value': 'end_turn'}]
    ]

    highlighted_option = { 'row': 0, 'column': 0 }
    while True:        
        utils_module.clear()
        utils_module.centered_print('SEU TURNO')
        player_module.show_card(player_data, game_data)
        utils_module.centered_print("INIMIGO")
        enemy_module.show_card(enemy_data, False)
        print()
        utils_module.centered_print('SELECIONE SUA AÇÃO')
        print()
        show_2d_menu(highlighted_option, actions_menu_options)
        key_pressed, highlighted_option = circular_2d_menu(highlighted_option, len(actions_menu_options), len(actions_menu_options[0]))
        if key_pressed == 'enter':
            utils_module.beep(800, 0.2)
            utils_module.clear()
            return actions_menu_options[highlighted_option['row']][highlighted_option['column']]['value']
        else:
            if key_pressed not in ('up', 'down', 'left', 'right'):
                utils_module.beep(150, 0.2)        

def show_attacks_menu(attacks_menu_options: list, highlighted_option: int, player_data: dict):
    
    print("╔" + "═" * 20 + "╦" + "═" * 9 + "╦" + "═" * 7 + "╦" + "═" * 7 + "╗")
    print("║ Nome" + " " * 15 + "║ Dano    ║ Ações ║ Poder ║")
    for id, weapon in enumerate(attacks_menu_options, start=0):
        print("╠" + "═" * 20 + "╬" + "═" * 9 + "╬" + "═" * 7 + "╬" + "═" * 7 + "╣")

        
        name    = str(weapon['name'])
        actions = str(weapon['actions'])
        enchant = 'NÃO' if weapon['enchant'] is None else 'SIM'
        damage = str(weapon['dice_amount']) + "d" + str(weapon['damage_dice'])
        if weapon['modifier'] < 0:
            damage += '-'
        else:
            damage += '+'
        
        damage += str(weapon['modifier'] + player_data['strength']) 

        if highlighted_option == id:
            print(Fore.BLACK + Back.WHITE, end='', sep='')
        print("║ " + name + " " * (19 - len(name)) + "║ " + damage + " " * (8 - len(damage)) + "║ " + actions + " " * (6 - len(actions)) + "║ " + enchant + " " * (6 - len(enchant)) + "║")
    
        print(Fore.WHITE + Back.RESET, end='', sep='')

    print("╚" + "═" * 20 + "╩" + "═" * 9 + "╩" + "═" * 7 + "╩" + "═" * 7 + "╝")

def attacks_menu(player_data: dict, enemy_data: dict, game_data: dict) -> str:
    attacks_menu_options = [
        weapon_module.hand()
    ]

    for weapon in player_data['weapons']:
        attacks_menu_options.append(weapon)

    highlighted_option = 0
    while True:        
        utils_module.clear()
        utils_module.centered_print('SEU TURNO')
        player_module.show_card(player_data, game_data)
        utils_module.centered_print('INIMIGO')
        enemy_module.show_card(enemy_data, False)
        print()
        utils_module.centered_print('SELECIONE SEU ATAQUE')
        print()
        show_attacks_menu(attacks_menu_options, highlighted_option, player_data)
        utils_module.centered_print('Backspace: Voltar | I: Mais Informações')
        key_pressed, highlighted_option = circular_menu(highlighted_option, len(attacks_menu_options))
        if key_pressed == 'enter':
            utils_module.beep(800, 0.2)
            utils_module.clear()
            if player_data['actions'] < attacks_menu_options[highlighted_option]['actions']:
                utils_module.centered_print('Você não tem ações para este ataque!')
                print()
                utils_module.press_any_key()
            elif confirm_menu_action(f"Deseja atacar com {attacks_menu_options[highlighted_option]['name']}?"):
                return attacks_menu_options[highlighted_option]
        elif key_pressed == 'backspace':
            utils_module.beep(800, 0.2)
            return None
        elif key_pressed == 'i':
            utils_module.beep(800, 0.2)
            utils_module.clear()
            weapon_module.show_weapon(attacks_menu_options[highlighted_option])
            print()
            utils_module.press_any_key()
        else:
            if key_pressed not in ('up', 'down', 'backspace', 'i'):
                utils_module.beep(150, 0.2)

def loot_menu(enemy_data: dict, enemy_loot: dict) -> bool:
    menu_options = get_boolean_menu_options()
    highlighted_option = 0
    while True:
        utils_module.clear()
        long_text = f"{enemy_data['name']} deixou cair isso enquanto morria:"
        text = utils_module.split_into_lines(long_text, 36)
        for line in text:
            utils_module.centered_print(line)
        print()
        match enemy_loot['type']:
            case 'weapon':
                weapon_module.show_weapon(enemy_loot['item'])
            case 'armor':
                armor_module.show_armor(enemy_loot['item'])
            case 'item':
                item_module.show_item(enemy_loot['item'])
        print()
        utils_module.centered_print('Deseja ficar com este item?')
        
        show_menu(highlighted_option, menu_options)
        key_pressed, highlighted_option = circular_menu(highlighted_option, len(menu_options))
        if key_pressed not in ('up', 'down', 'enter'):
            utils_module.beep(150, 0.2)
        elif key_pressed == 'enter':
            utils_module.beep(800, 0.2)
            utils_module.clear()
            return menu_options[highlighted_option]['value']   


def clear_weapon_inventory(player_data: dict):
    highlighted_option = 0
    while len(player_data['weapons']) > player_data['max_weapons']:
        utils_module.clear()
        utils_module.centered_print("Você está carregando armas demais!")
        utils_module.centered_print("Escolha uma arma para deixar para trás:")
        show_attacks_menu(player_data['weapons'], highlighted_option)
        utils_module.centered_print('I: Mais Informações')
        key_pressed, highlighted_option = circular_menu(highlighted_option, len(player_data['weapons']))
        if key_pressed == 'enter':
            utils_module.beep(800, 0.2)
            utils_module.clear()
            if confirm_menu_action(f"Deseja largar {player_data['weapons'][highlighted_option]['name']}?"):
                player_data['weapons'].pop(highlighted_option)
                player_module.save_status(player_data)
                return
        elif key_pressed == 'i':
            utils_module.clear()
            utils_module.beep(800, 0.2)
            weapon_module.show_weapon(player_data['weapons'][highlighted_option])
            print()
            utils_module.press_any_key()
        else:
            if key_pressed not in ('up', 'down', 'i'):
                utils_module.beep(150, 0.2)

def show_inventory_menu(items: list, highlighted_option: int):
    print("╔" + "═" * 5 + "╦" + "═" * 40 + "╗")
    print("║ QTD ║ Item" + " " * 35 + "║")
    for id, item in enumerate(items, start=0):
        print("╠" + "═" * 5 + "╬" + "═" * 40 + "╣")

        name   = str(item['name'])
        amount = str(item['amount'])

        if highlighted_option == id:
            print(Fore.BLACK + Back.WHITE, end='', sep='')

        print("║ " + amount + " " * (4 - len(amount)) + "║ " + name + " " * (39 - len(name)) + "║")   
        
        print(Fore.WHITE + Back.RESET, end='', sep='')

    print("╚" + "═" * 5 + "╩" + "═" * 40 + "╝")

def show_inventory(player_data: dict, game_data: dict) -> dict:
    items = player_data['items']
    highlighted_option = 0

    if items == []:
        utils_module.centered_print('Seu inventário está vazio!')
        print()
        utils_module.press_any_key()
    else:
        while True:
            utils_module.clear()
            player_module.show_card(player_data, game_data)
            utils_module.centered_print('INVENTÁRIO')
            print()
            show_inventory_menu(items, highlighted_option)
            utils_module.centered_print('Backspace: Voltar | I: Mais Informações')
            key_pressed, highlighted_option = circular_menu(highlighted_option, len(items))
            if key_pressed == 'enter':
                utils_module.beep(800, 0.2)
                utils_module.clear()
                if confirm_menu_action(f"Deseja usar {items[highlighted_option]['name']}?"):
                    return items[highlighted_option]
            elif key_pressed == 'backspace':
                utils_module.beep(800, 0.2)
                return None
            elif key_pressed == 'i':
                utils_module.beep(800, 0.2)
                item_module.show_item(items[highlighted_option])
                print()
                utils_module.press_any_key()
            else:
                if key_pressed not in ('up', 'down', 'backspace', 'i'):
                    utils_module.beep(150, 0.2)