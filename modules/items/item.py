import random
import modules.core.utils as utils_module
from colorama import Fore, Back, Style

def get_random_item(rarity: int) -> dict:
    item_groups = items_scafold()

    item_group = item_groups[rarity]

    item = random.choice(item_group)
    
    item['rarity'] = rarity

    return item

def show_item(item: dict):
    utils_module.clear()
    print("╔" + "═" * 46 + "╗")
    
    text_padding = utils_module.centered_text_padding(item['name'], 46)
    second_padding = " " * ( 46 - len(item['name']) - len(text_padding))
    print("║" + text_padding + item['name'] + second_padding + "║")
    
    print("╠" + "═" * 23 + "╦" +  "═" * 22 + "╣")

    rarity_name = ''

    match item['rarity']:
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

    value = ''
    if item['dice_amount'] > 0:
        value = str(item['dice_amount']) + "d" + str(item['dice'])
    value += "+" + str(item['modifier'])

    match item['attr']:
        case 'cur_hp':
            attribute = 'VIDA'
        case 'max_hp':
            attribute = 'VIDA MÁXIMA'
        case 'strength':
            attribute = 'FORÇA'
        case 'dexterity':
            attribute = 'VELOCIDADE'
        case 'actions':
            attribute = 'AÇÕES'
        case 'max_actions':
            attribute = 'AÇÕES MÁXIMAS'

    print("║ Raridade: " +  rarity_color + rarity_name + Fore.RESET + " " * (12 - len(rarity_name)) + "║ Valor: " + Fore.LIGHTCYAN_EX + value + Fore.RESET + " " * (14 - len(value)) + "║")
    
    print("╠" + "═" * 23 + "╩" +  "═" * 22 + "╣")

    description_lines = utils_module.split_into_lines(item["description"], 40)

    for line in description_lines:   
        text_padding = utils_module.centered_text_padding(line, 46)
        second_padding = " " * ( 46 - len(line) - len(text_padding))
        print("║" + text_padding + line + second_padding + "║")
    
    print("╚" + "═" * 46 + "╝")

def items_scafold():
    commom_items = [
        {
            "id":           "commom_healing",
            "name":         "Poção de Cura",
            "description":  "Um pequeno frasco com um líquido vermelho. Dizem que é feita com sangue de capivara.",
            "attr":         "cur_hp",
            "dice":         4,
            "dice_amount":   2,
            "modifier":     2,
        },
        {
            "id":           "commom_max_hp",
            "name":         "Elixir da Vitalidade",
            "description":  "Um elixir capaz de aumentar a VIDA MÁXIMA. Um fraco com um líquido verde limão, parece radioativo.",
            "attr":         "max_hp",
            "dice":         0,
            "dice_amount":   0,
            "modifier":     5,
        },
    ]
    
    uncommom_items = [
        {
            "id":           "uncommom_healing",
            "name":         "Poção de Cura Maior",
            "description":  "Um frasco redondo com um líquido vermelho. Ele parece esquentar o vidro da garrafa até uma temperatura agradável.",
            "attr":         "cur_hp",
            "dice":         4,
            "dice_amount":   4,
            "modifier":     4,
        },
        {
            "id":           "uncommom_max_hp",
            "name":         "Elixir da Vitalidade Maior",
            "description":  "Um elixir capaz de aumentar a VIDA MÁXIMA. Um frasco com um líquido verde meio gosmento. Eu não tomaria isso não.",
            "attr":         "max_hp",
            "dice":         0,
            "dice_amount":   0,
            "modifier":     10,
        },
        {
            "id":           "uncommom_strength",
            "name":         "Elixir da Força",
            "description":  "Um elixir capaz de aumentar a FORÇA. É um líquido azul e de cheiro que remete ao café, um café bem forte.",
            "attr":         "strength",
            "dice":         0,
            "dice_amount":   0,
            "modifier":     1,
        },
        {
            "id":           "uncommom_dexterity",
            "name":         "Elixir da Velocidade",
            "description":  "Um elixir capaz de aumentar a VELOCIDADE. É um líquido amarelo claro, reluz na luz parecendo com pequenas partículas de ouro no meio.",
            "attr":         "dexterity",
            "dice":         0,
            "dice_amount":   0,
            "modifier":     1,
        },
        {
            "id":           "uncommom_actions",
            "name":         "Pergaminho de Ataque",
            "description":  "Um pergaminho capaz de aumentar a quantidade de AÇÕES neste turno. Há somente desenhos que lembram artes ruprestes de homens matando capivaras.",
            "attr":         "actions",
            "dice":         0,
            "dice_amount":   0,
            "modifier":     2,
        }
    ]

    rare_items = [
        {
            "id":           "rare_healing",
            "name":         "Poção de Cura Superior",
            "description":  "Um frasco grande e quadrado com um líquido vermelho. Tem cheiro de café da manhã e a temperatura de uma manhã de sol no inverno.",
            "attr":         "cur_hp",
            "dice":         4,
            "dice_amount":   8,
            "modifier":     8,
        },
        {
            "id":           "rare_max_hp",
            "name":         "Elixir da Vitalidade Superior",
            "description":  "Um elixir capaz de aumentar a VIDA MÁXIMA. Um frasco grande com um líquido verde. Estrengthanhamente isso tem cheiro de maçã verde!",
            "attr":         "max_hp",
            "dice":         0,
            "dice_amount":   0,
            "modifier":     15,
        },
        {
            "id":           "rare_strength",
            "name":         "Elixir da Força Maior",
            "description":  "Um elixir capaz de aumentar a FORÇA. O líquido parece as vezes subir pelas pardes do frasco e tentar abrir a tampa sozinho.",
            "attr":         "strength",
            "dice":         0,
            "dice_amount":   0,
            "modifier":     2,
        },
        {
            "id":           "rare_dexterity",
            "name":         "Elixir da Velocidade Maior",
            "description":  "Um elixir capaz de aumentar a VELOCIDADE. É um líquido amarelo claro que parece ser muito fino, pois ele se move muito rapidamente dentro do frasco.",
            "attr":         "dexterity",
            "dice":         0,
            "dice_amount":   0,
            "modifier":     2,
        },
        {
            "id":           "rare_max_actions",
            "name":         "Pergaminho de Combate",
            "description":  "Um pergaminho capaz de aumentar a quantidade de AÇÕES MÁXIMAS. Repeleto de técnicas avançadas e táticas de combate especializado no abate de capivaras.",
            "attr":         "max_actions",
            "dice":         0,
            "dice_amount":   0,
            "modifier":     1,
        },
        {
            "id":           "rare_actions",
            "name":         "Pergaminho de Ataque Maior",
            "description":  "Um pergaminho capaz de aumentar a quantidade de AÇÕES neste turno. Tem uma foto de uma capivara com um alvo desenhado. Você entende a mensagem.",
            "attr":         "actions",
            "dice":         0,
            "dice_amount":   0,
            "modifier":     3,
        }
    ]

    legendary_items = [
        {
            "id":           "legendary_healing",
            "name":         "Poção de Cura Lendária",
            "description":  "Um frasco enorme com um líquido vermelho. Aqui deve ter poção suficiente pra erguer uns 20 defuntos.",
            "attr":         "cur_hp",
            "dice":         4,
            "dice_amount":  10,
            "modifier":     20,
        },
        {
            "id":           "legendary_max_hp",
            "name":         "Elixir da Vitalidade Lendário",
            "description":  "Um elixir capaz de aumentar a VIDA MÁXIMA. É um frasco realmente muito grande, tomar isso deve te deixar verde também.",
            "attr":         "max_hp",
            "dice":         0,
            "dice_amount":   0,
            "modifier":     25,
        },
        {
            "id":           "legendary_strength",
            "name":         "Elixir da Força Lendária",
            "description":  "Um elixir capaz de aumentar a FORÇA. O líquido azul parece ter vida própria, as vezes ele fica se 'batendo' dentro do seu frasco.",
            "attr":         "strength",
            "dice":         0,
            "dice_amount":   0,
            "modifier":     3,
        },
        {
            "id":           "legendary_dexterity",
            "name":         "Elixir da Velocidade Lendária",
            "description":  "Um elixir capaz de aumentar a VELOCIDADE. Esse frasco parece incrívelmente leve para a quantidade de líquido amarelo que tem dentro.",
            "attr":         "dexterity",
            "dice":         0,
            "dice_amount":   0,
            "modifier":     3,
        },
        {
            "id":           "legendary_max_actions",
            "name":         "Pergaminho de Combate Lendário",
            "description":  "Um pergaminho capaz de aumentar a quantidade de AÇÕES MÁXIMAS. Repeleto de técnicas avançadas e táticas de combate especializado no abate de capivaras.",
            "attr":         "max_actions",
            "dice":         0,
            "dice_amount":   0,
            "modifier":     2,
        }
    ]

    return [
        commom_items,
        uncommom_items,
        rare_items,
        legendary_items
    ]