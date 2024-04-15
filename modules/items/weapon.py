import random
from colorama import Fore, Back, Style
import modules.items.enchant as enchant_module
import modules.items.loot as loot_module
import modules.core.utils as utils_module

def create_weapon(name: str, description: str, damage_dice: int, dice_amount: int, modifier: int, actions: int, enchant: dict, rarity: int = 0) -> dict:
    return {
        'name':         name,
        'description':  description,
        'damage_dice':   damage_dice,
        'dice_amount':   dice_amount,
        'modifier':     modifier,
        'actions':      actions,
        'enchant':      enchant,
        'rarity':       rarity
    }

def hand() -> dict:
    return create_weapon(
        name='Mãos',
        description='Suas mãos, dê socos, tapas ou aponte o dedo do meio. Desmoralizar também é uma maneira de causar dano!',
        damage_dice=4,
        dice_amount=1,
        modifier=0,
        actions=1,
        enchant=None
    )

def get_random_weapon(game_data: dict, rarity: int) -> dict:
    weights = loot_module.get_loot_weights(game_data)
    weapon_groups = weapons_scafold()

    weapon_group = random.choices(weapon_groups, weights)[0]
    
    item = random.choice(weapon_group)

    item['modifier'] += rarity
    item['rarity'] = rarity

    roll = random.randint(1,100)
    if rarity == 1 and roll <= 30:
        item['enchant'] = enchant_module.get_random_enchant()
    elif rarity == 2 and roll <= 70:
        item['enchant'] = enchant_module.get_random_enchant()
    elif rarity == 3:
        item['enchant'] = enchant_module.get_random_enchant()

    return item

def show_weapon(weapon: dict):
    print("╔" + "═" * 46 + "╗")
    
    text_padding = utils_module.centered_text_padding(weapon['name'], 46)
    second_padding = " " * ( 46 - len(weapon['name']) - len(text_padding))
    print("║" + text_padding + weapon['name'] + second_padding + "║")
    
    print("╠" + "═" * 23 + "╦" +  "═" * 22 + "╣")

    rarity_name = ''
    match weapon['rarity']:
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

    bonus = '+' + str(weapon['modifier'])

    enchant_name = ''
    if weapon['enchant'] is None:
        enchant_name = 'NENHUM'
        enchant_color = Fore.RESET
    else:
        match weapon['enchant']['type']:
            case 0:
                enchant_name = 'FOGO'
                enchant_color = Fore.YELLOW
            case 1:
                enchant_name = 'GELO'
                enchant_color = Fore.CYAN
            case 2:
                enchant_name = 'SANGUE'
                enchant_color = Fore.RED

    print("║ Raridade: " +  rarity_color + rarity_name + Fore.RESET + " " * (12 - len(rarity_name)) + "║ Poder: " + enchant_color + enchant_name + Fore.RESET + " " * (14 - len(enchant_name)) + "║")
    
    print("╠═══╦" + "═" * 13 + "╦" +  "═" * 5 + "╩" +  "═" * 6 + "╦" +  "═" * 11 + "╦═══╣")
    
    damage = str(weapon['dice_amount']) + 'd' + str(weapon['damage_dice'])
    bonus = '+' + str(weapon['modifier'])
    actions = str(weapon['actions'])
    
    print("║   ║ Dano: " +  Fore.CYAN + damage + Fore.RESET + " " * (6 - len(damage)) + "║ Bônus: " + Fore.CYAN + bonus + Fore.RESET + " " * (4 - len(bonus)) + "║ Ações: " + Fore.CYAN + actions + Fore.RESET + " " * (3 - len(actions)) + "║   ║")
   
    print("╠═══╩" + "═" * 13 + "╩" +  "═" * 12 + "╩" +  "═" * 11 + "╩═══╣")

    if weapon['enchant'] is not None:
        text = 'PODER:'
        text_padding = utils_module.centered_text_padding(text, 46)
        second_padding = " " * ( 46 - len(text) - len(text_padding))
        print("║" + text_padding + text + second_padding + "║")

        enchat_description_lines = utils_module.split_into_lines(weapon['enchant']["description"], 40)

        for line in enchat_description_lines:   
            text_padding = utils_module.centered_text_padding(line, 46)
            second_padding = " " * ( 46 - len(line) - len(text_padding))
            print("║" + text_padding + line + second_padding + "║")
            
        print("╠" + "═" * 46 + "╣")

    description_lines = utils_module.split_into_lines(weapon["description"], 40)

    for line in description_lines:   
        text_padding = utils_module.centered_text_padding(line, 46)
        second_padding = " " * ( 46 - len(line) - len(text_padding))
        print("║" + text_padding + line + second_padding + "║")
    
    print("╚" + "═" * 46 + "╝")

def weapons_scafold() -> list: 
    return[
        [
            {
                'name':         'Adaga',
                'description':  'Uma lâmina afiada, eu não guardaria no bolso, melhor ter um lugar mais seguro pra deixá-la.',
                'damage_dice':  4,
                'dice_amount':  1,
                'modifier':     0,
                'actions':      1,
                'enchant':      None
            },
            {
                'name':         'Martelo',
                'description':  'Pra quem só conhece martelo, todo problema é prego!',
                'damage_dice':  4,
                'dice_amount':  1,
                'modifier':     0,
                'actions':      1,
                'enchant':      None
            },
        ],
        [
            {
                'name':         'Espada Curta',
                'description':  'Uma espada, só que curta. O tamanho da sua espada não importa, meu guerreiro, mas sim o que você faz com ela!',
                'damage_dice':  6,
                'dice_amount':  1,
                'modifier':     0,
                'actions':      1,
                'enchant':      None
            },
            {
                'name':         'Lança',
                'description':  'LANÇAMENTO: Empresa lança uma nova lança que você lança!',
                'damage_dice':  6,
                'dice_amount':  1,
                'modifier':     0,
                'actions':      1,
                'enchant':      None
            },
            {
                'name':         'Porrete',
                'description':  'Como diria o capitão caverna! Unga Bunga, CAPITÃO CAVEEEERRRNAAAAAA!',
                'damage_dice':  6,
                'dice_amount':  1,
                'modifier':     0,
                'actions':      1,
                'enchant':      None
            },
        ],
        [
            {
                'name':         'Espada Grande',
                'description':  'Uma espada, bem grande. Mas nem só de tamanho vive a espada!',
                'damage_dice':  8,
                'dice_amount':  2,
                'modifier':     0,
                'actions':      2,
                'enchant':      None
            },
            {
                'name':         'Espada Longa',
                'description':  'Uma arma bem comprida, mas tu quer fazer oq com uma espada desse tamanho?',
                'damage_dice':  4,
                'dice_amount':  4,
                'modifier':     0,
                'actions':      2,
                'enchant':      None
            },
        ],
        [
            {
                'name':         'Machado de Batalha',
                'description':  'Um machadão brabo daqueles de vilão de história medieval. Talvez você seja o vilão dessa história?',
                'damage_dice':  12,
                'dice_amount':  2,
                'modifier':     1,
                'actions':      3,
                'enchant':      None
            },
            {
                'name':         'Martelo de Guerra',
                'description':  'Então martela, martela, martela o martelão! Levanta a mãozinha na palma da mão! É o bonde do tigrão.',
                'damage_dice':  8,
                'dice_amount':  3,
                'modifier':     1,
                'actions':      3,
                'enchant':      None
            },
        ],
        [
            {
                'name':         'Lança de Montaria',
                'description':  'Esta incrível lança de montaria acompanha uma capivara domesticada para ser utilizada como montaria, olha que conveniente!',
                'damage_dice':  12,
                'dice_amount':  3,
                'modifier':     4,
                'actions':      4,
                'enchant':      None
            },
        ]
    ]