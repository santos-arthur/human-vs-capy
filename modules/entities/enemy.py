from colorama import Fore, Back, Style
import modules.core.save as save_module
import modules.entities.player as player_module
import modules.core.utils as utils_module
import random

ENEMY_DATA_FILE = 'saves/enemyData.json'

def save_status(enemy_data: dict):
    save_module.save_status(enemy_data, ENEMY_DATA_FILE)

def load_status():
    return save_module.load_status(ENEMY_DATA_FILE)

def wipe_status():
    save_module.wipe_status(ENEMY_DATA_FILE)

def get_random_enemy(difficulty: int, level: int, points: int) -> dict:
    enemy_list = get_all_enemies()

    match difficulty:
        case 0:
            roll = random.randint(1, 10)
            roll += int(level * 2)
            roll += int(points * 0.75)
        case 1:
            roll = random.randint(1, 20)
            roll += int(level * 3)
            roll += int(points * 0.5)
        case 2:
            roll = random.randint(1, 30)
            roll += int(level * 4)
            roll += int(points * 0.3)
    
    if roll <= 15:
        enemy_id = 0
    elif roll <= 30:
        enemy_id = 1
    elif roll <= 60:
        enemy_id = 2
    elif roll <= 100:
        enemy_id = 3
    else:
        enemy_id = 4
        
    return enemy_list[enemy_id]

def get_all_enemies():
    return [
        {
            'id': 0,
            'name': 'Capivara Comum',
            'description': 'Só uma capivarinha comum!',
            'max_hp': 5,
            'cur_hp': 5,
            'actions': 1,
            'max_actions': 1,
            'attacks': [
                {
                    'name': 'Mordida',
                    'damage_dice': 4,
                    'dice_amount': 1,
                    'modifier': 0,
                    'actions': 1,
                }
            ],
            'armor_class': 8,
            'points': 1,
            'frozen': False
        },
        {
            'id': 1,
            'name': 'Capivara Comandante',
            'description': 'Uma capivara que comanda as outras? Ela grita em capivarês "Cadê minhas capivarinhas?" e todas as outras gritam "Cri-Cri-Cri-Cri".',
            'max_hp': 8,
            'cur_hp': 8,
            'actions': 2,
            'max_actions': 2,
            'attacks': [
                {
                    'name': 'Mordida',
                    'damage_dice': 4,
                    'dice_amount': 2,
                    'modifier': 1,
                    'actions': 1,
                },
                {
                    'name': 'Arranhão',
                    'damage_dice': 6,
                    'dice_amount': 1,
                    'modifier': 2,
                    'actions': 2,
                },
            ],
            'armor_class': 10,
            'points': 2,
            'frozen': False
        },
        {
            'id': 2,
            'name': 'Capivara Gigante',
            'description': 'Uma Capivara normal. Pera, ela estava muito longe, é uma Capivara do tamanho de um ELEFANTE.',
            'max_hp': 20,
            'cur_hp': 20,
            'actions': 1,
            'max_actions': 1,
            'attacks': [
                {
                    'name': 'Mordida',
                    'damage_dice': 4,
                    'dice_amount': 2,
                    'modifier': 2,
                    'actions': 1,
                },
                {
                    'name': 'Pisão',
                    'damage_dice': 6,
                    'dice_amount': 1,
                    'modifier': 2,
                    'actions': 1,
                },
            ],
            'armor_class': 14,
            'points': 4,
            'frozen': False
        },
        {
            'id': 3,
            'name': 'Capivara de Ataque',
            'description': 'Uma Capivara montada por outra Capivara segurando uma lança. A Capivara de baixo parece ainda mais butral que a de cima!',
            'max_hp': 16,
            'cur_hp': 16,
            'actions': 3,
            'max_actions': 3,
            'attacks': [
                {
                    'name': 'Estocada com a Lança',
                    'damage_dice': 6,
                    'dice_amount': 2,
                    'modifier': 2,
                    'actions': 1,
                },
                {
                    'name': 'Cabeçada',
                    'damage_dice': 8,
                    'dice_amount': 2,
                    'modifier': 1,
                    'actions': 1,
                },
            ],
            'armor_class': 8,
            'points': 6,
            'frozen': False
        },
        {
            'id': 4,
            'name': 'Capivara Dragão',
            'description': 'Uma Capivara bem grande. MAS ELA TEM ASAS E COSPE FOGO?',
            'max_hp': 50,
            'cur_hp': 50,
            'actions': 6,
            'max_actions': 6,
            'attacks': [
                {
                    'name': 'Baforada de Fogo',
                    'damage_dice': 12,
                    'dice_amount': 4,
                    'modifier': 5,
                    'actions': 3,
                },
                {
                    'name': 'Mordida',
                    'damage_dice': 8,
                    'dice_amount': 4,
                    'modifier': 5,
                    'actions': 1,
                },
                {
                    'name': 'Arranhão',
                    'damage_dice': 6,
                    'dice_amount': 5,
                    'modifier': 5,
                    'actions': 1,
                },
                {
                    'name': 'Rabada',
                    'damage_dice': 4,
                    'dice_amount': 4,
                    'modifier': 3,
                    'actions': 2,
                },
            ],
            'armor_class': 16,
            'points': 10,
            'frozen': False
        },
    ]

def show_card(enemy_data: dict, show_detailed: bool = False):
    
    capy_art = open(f"resources/art_capy_{enemy_data['id']}.txt", "r").read()

    print("╔" + "═" * 46 + "╗")
    
    text_padding = utils_module.centered_text_padding(enemy_data['name'], 46)
    second_padding = " " * ( 46 - len(enemy_data['name']) - len(text_padding))
    print("║" + text_padding + enemy_data['name'] + second_padding + "║")
    
    print("╠" + "═" * 16 + "╦" + "═" * 12 + "╦" + "═" * 16 + "╣")
    
    if ((enemy_data['cur_hp'] * 100) / enemy_data["max_hp"]) > 60:
        hp_color = Fore.GREEN
    elif ((enemy_data['cur_hp'] * 100) / enemy_data["max_hp"]) > 20:
        hp_color = Fore.YELLOW
    else:
        hp_color = Fore.RED

    hp_text = str(enemy_data["cur_hp"]) + "/" + str(enemy_data["max_hp"])
    
    armor_class = str(enemy_data["armor_class"])

    if ((enemy_data['actions'] * 100) / enemy_data["max_actions"]) > 50:
        actions_color = Fore.GREEN
    elif ((enemy_data['actions'] * 100) / enemy_data["max_actions"]) > 25:
        actions_color = Fore.YELLOW
    else:
        actions_color = Fore.RED

    actions_text = str(enemy_data["actions"]) + "/" + str(enemy_data["max_actions"])

    print("║ Vida: " + hp_color + hp_text + Fore.RESET + " " * (9 - len(hp_text)) +  "║ Defesa: " + Fore.CYAN + armor_class + Fore.RESET + " " * (3 - len(armor_class)) + "║ Ações: " + actions_color + actions_text + Fore.RESET + " " * (8 - len(actions_text)) + "║")
    
    print("╠" + "═" * 7 + "╦"  + "═" * 8 + "╩" + "═" * 7 + "╦"  + "═" * 4 + "╩" + "═" * 8 + "╦" + "═" * 7 + "╣")

    points = str(enemy_data['points'])
    
    frozen_text = 'SIM' if enemy_data['frozen'] else 'NÃO'
    frozen_color = Fore.GREEN if enemy_data['frozen'] else Fore.RED
    print("║       ║ Congelado: " + frozen_color + frozen_text + Fore.RESET + " " * (4 - len(frozen_text)) + "║ Pontos: " + Fore.CYAN + points + Fore.RESET + " " * (4 - len(points)) + "║       ║")
    
    if not show_detailed:
        print("╚" + "═" * 7 + "╩"  + "═" * 16 + "╩"  + "═" * 13 + "╩" + "═" * 7 + "╝")
    else:
        print("╠" + "═" * 7 + "╩"  + "═" * 16 + "╩"  + "═" * 13 + "╩" + "═" * 7 + "╣")

        for linha in capy_art.split('\n'):
            print("║" + " " * 16 + linha + " " * (46 - 16 - len(linha)) + "║")
        
        print("╠" + "═" * 46 + "╣")
        
        description_lines = utils_module.split_into_lines(enemy_data["description"], 40)

        for line in description_lines:   
            text_padding = utils_module.centered_text_padding(line, 46)
            second_padding = " " * ( 46 - len(line) - len(text_padding))
            print("║" + text_padding + line + second_padding + "║")
        
        print("╚" + "═" * 46 + "╝")

def attack(enemy_data: dict, player_data: dict):
    enemy_attacks = enemy_data['attacks']
    
    while (enemy_attack := random.choice(enemy_attacks))['actions'] > enemy_data['actions']:
        pass
    
    enemy_data['actions'] -= enemy_attack['actions']
    roll = random.randint(1, 20)
    attackHits = roll + enemy_attack['modifier'] >= player_module.get_armor_class(player_data)
    criticalHit = roll == 20
    damage = 0
    long_text = f"{enemy_data['name']} usou o ataque {enemy_attack['name']}"
    text = utils_module.split_into_lines(long_text, 36)
    for line in text:
        utils_module.centered_print(line)
    print()
    if attackHits:
        damage = sum(random.randint(1, enemy_attack['damage_dice']) for _ in range(enemy_attack['dice_amount']))
        damage += enemy_attack['modifier']
        if criticalHit:
            damage += enemy_attack['damage_dice']            
            utils_module.centered_print(f"{enemy_data['name']} causou um acerto crítico!")
            print()
        
        utils_module.centered_print(f"{enemy_data['name']} lhe causou {damage} de dano!")
        print()
        
        player_data['cur_hp'] -= min(damage, player_data['cur_hp'])
    else:
        utils_module.centered_print(f"{enemy_data['name']} errou o ataque!")
        print()

    player_module.save_status(player_data)
    save_status(enemy_data)