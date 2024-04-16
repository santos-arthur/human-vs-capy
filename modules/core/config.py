import modules.core.save as save_module
import modules.core.utils as utils_module
import modules.core.leaderboard as leaderboard_module
import modules.core.menu as menu_module
import keyboard
from colorama import Fore, Back, Style


CONFIG_DATA_FILE = 'resources/config.json'

def set_configs(configs):
    save_module.save_status(configs, CONFIG_DATA_FILE)

def get_configs() -> dict:
    return save_module.load_status(CONFIG_DATA_FILE)

def configs_menu():
    config_options = menu_module.get_config_menu_options()
    highlighted_option = 0
    while True:
        config_data = get_configs()
        utils_module.clear()
        utils_module.centered_print("CONFIGURAÇÕES")
        print()
        show_configs(config_options, config_data, highlighted_option)
        key_pressed, highlighted_option = menu_module.circular_menu(highlighted_option, len(config_options))
        if key_pressed == 'enter' and config_options[highlighted_option]['type'] == 'button':
            utils_module.beep(800, 0.2)
            match config_options[highlighted_option]['value']:
                case 'reset_leaderboard':
                    if menu_module.confirm_menu_action("Deseja mesmo apagar o histórico?"):
                        leaderboard_module.wipe_status()
                case 'reset_configs':
                    if menu_module.confirm_menu_action("Deseja mesmo redefinir as configurações?"):
                        reset_configs()
                case 'adjust_screen':
                    adjust_screen()
                case 'exit':
                    break
        elif key_pressed == 'left' and config_options[highlighted_option]['type'] == 'bar' and config_data[config_options[highlighted_option]['value']] > config_options[highlighted_option]['min']:
            utils_module.beep(800, 0.2)
            config_data[config_options[highlighted_option]['value']] -= config_options[highlighted_option]['step']
            set_configs(config_data)
        elif key_pressed == 'right' and config_options[highlighted_option]['type'] == 'bar' and config_data[config_options[highlighted_option]['value']] < config_options[highlighted_option]['max']:
            utils_module.beep(800, 0.2)
            config_data[config_options[highlighted_option]['value']] += config_options[highlighted_option]['step']
            set_configs(config_data)
        elif key_pressed not in ('up', 'down'):
            utils_module.beep(150, 0.2)

def show_configs(configs: list, config_data: list, highlighted_option: int):
    for index, config in enumerate(configs,start=0):
        if config['type'] == 'button':
            label   = f"  {config['label']}  "
            padding = utils_module.centered_text_padding(label)
            print(Fore.WHITE + Back.RESET + padding, end='', sep='')

            if highlighted_option == index:
                print(Fore.BLACK + Back.WHITE, end='', sep='')

            print(label + Fore.WHITE + Back.RESET)
        elif config['type'] == 'bar':
            option_delta = config['max'] - config['min']
            bar_size = option_delta / config['step']
            value = config_data[config['value']]
            relative_value = (value / config['step'])
            label = f"  {config['label']}:  "
            filled_bar = "█" * max(0, int(relative_value))
            unfilled_bar = "▓" * max(0, int(bar_size - relative_value))

            
            padding = utils_module.centered_text_padding(label + filled_bar + unfilled_bar + "  ")
            print(Fore.WHITE + Back.RESET + padding, end='', sep='')

            if highlighted_option == index:
                print(Fore.BLACK + Back.WHITE, end='', sep='')

            print(label + Fore.GREEN + filled_bar + Fore.RED + unfilled_bar + "  " + Fore.WHITE + Back.RESET)

def reset_configs():
    set_configs(
        {
            "volume": 50
        }    
    )

def adjust_screen():
    utils_module.clear()
    lines = 30
    columns = 48
    print(Fore.BLACK + Back.WHITE, end='', sep='')
    for line in range(1, lines):
        if line == 2:
            text = "ASSISTENTE DE CONFIGURACAO DE TELA"
            padding = utils_module.centered_text_padding(text)
            print(padding + text + " " * (columns - len(text) - len(padding)))
        elif line == 4:
            text = "Ajuste o seu console até"
            padding = utils_module.centered_text_padding(text)
            print(padding + text + " " * (columns - len(text) - len(padding)))
        elif line == 5:
            text = "em destaque nesta tela."
            padding = utils_module.centered_text_padding(text)
            print(padding + text + " " * (columns - len(text) - len(padding)))
        else:
            print(" " * columns)

    text = "Aperte qualquer tecla para continuar."
    padding = utils_module.centered_text_padding(text)
    
    print(padding + text + " " * (columns - len(text) - len(padding)))
    while True:
        keyPressed = keyboard.read_event(suppress=True)
        if keyPressed.event_type == keyboard.KEY_UP:
            utils_module.beep(800, 0.2)
            break
            