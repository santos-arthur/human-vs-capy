import random
import modules.items.loot as loot_module
import modules.core.utils as utils_module
from colorama import Fore, Back, Style

def create_armor(name: str, description: str, armor_modifier: int = 0, rarity: int = 0) -> dict:
    return {
        'name': name,
        'description': description,
        'armor_modifier': armor_modifier,
        'rarity': rarity
    }

def clothes() -> dict:
    return create_armor(
        name='Roupas Comuns',
        description='Suas roupas mesmo. Olhe pra baixo, é isso que você está vestindo.',
        armor_modifier=0,
        rarity=0
    )

def get_random_armor(game_data: dict) -> dict:
    weights = loot_module.get_loot_weights(game_data)
    armor_groups = armors_scafold()

    armor_group = random.choices(armor_groups, weights)[0]
    
    item = random.choice(armor_group)

    return item

def show_armor(armor: dict):
    print("╔" + "═" * 46 + "╗")
    
    text_padding = utils_module.centered_text_padding(armor['name'], 46)
    second_padding = " " * ( 46 - len(armor['name']) - len(text_padding))
    print("║" + text_padding + armor['name'] + second_padding + "║")
    
    print("╠" + "═" * 23 + "╦" +  "═" * 22 + "╣")

    rarity_name = ''

    match armor['rarity']:
        case 0:
            rarity_name = 'COMUM'
            rarity_color = Fore.GREEN
        case 1:
            rarity_name = 'INCOMUM'
            rarity_color = Fore.BLUE
        case 2:
            rarity_name = 'RARO'
            rarity_color = Fore.MAGENTA
        case 3:
            rarity_name = 'LENDÁRIO'
            rarity_color = Fore.YELLOW

    bonus = '+' + str(armor['armor_modifier'])

    print("║ Raridade: " +  rarity_color + rarity_name + Fore.RESET + " " * (12 - len(rarity_name)) + "║ Bônus: " + Fore.LIGHTCYAN_EX + bonus + Fore.RESET + " " * (14 - len(bonus)) + "║")
    
    print("╠" + "═" * 23 + "╩" +  "═" * 22 + "╣")

    description_lines = utils_module.split_into_lines(armor["description"], 40)

    for line in description_lines:   
        text_padding = utils_module.centered_text_padding(line, 46)
        second_padding = " " * ( 46 - len(line) - len(text_padding))
        print("║" + text_padding + line + second_padding + "║")
    
    print("╚" + "═" * 46 + "╝")

def armors_scafold() -> list:
    return [
        [
            {
                'name': 'Camiseta',
                'description': 'Uma camiseta do Fã Clube das Capivaras, você vai mesmo usar isso?',
                'armor_modifier': 0,
                'rarity': 0
            }
        ],
        [
            {
                'name': 'Armadura de Couro',
                'description': 'Uma armadura feita com couro de Capivara. Além de proteger, intimida elas!',
                'armor_modifier': 1,
                'rarity': 0
            },
            {
                'name': 'Gibão de Pele',
                'description': 'Um colete de pele reforçado feito com pele de animais de grande porte. Talvez de uma capivara bem grande?',
                'armor_modifier': 2,
                'rarity': 0
            },
        ],
        [
            {
                'name': 'Cotas de Malha',
                'description': 'Um colete de anéis de metal! Muito útil para parar as moridas das capivaras.',
                'armor_modifier': 3,
                'rarity': 1
            },
            {
                'name': 'Armadura de Placas',
                'description': 'Uma armadura feita de placas de metal resistente! Ideal para enfrentar até as capivaras mais furiosas.',
                'armor_modifier': 4,
                'rarity': 1
            },
        ],
        [
            {
                'name': 'Armadura Completa',
                'description': 'Uma armadura quase impenetrável! A não ser por uma pequena brecha no joelho.',
                'armor_modifier': 5,
                'rarity': 2
            },
            {
                'name': 'Tanguinha de Texugo',
                'description': 'Isso é tudo que um guerreiro precisa. Tem até um lugar para colocar flores.',
                'armor_modifier': 6,
                'rarity': 2
            },
        ],
        [
            {
                'name': 'Armadura de Escamas',
                'description': 'Uma armadura feita com escamas de dragão! Mas, espera aí, essas escamas tem pelo?',
                'armor_modifier': 7,
                'rarity': 3
            },
            {
                'name': 'Armadura de Diamantes',
                'description': 'Alguém resolveu cobrir uma armadura inteira com diamantes! Isso é muito caro, mas por algum motivo estranho, as capivaras parecem ter dificuldade de acertar ataques contra ela.',
                'armor_modifier': 8,
                'rarity': 3
            },
        ]
    ]