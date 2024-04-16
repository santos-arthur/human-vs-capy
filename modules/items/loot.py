import random
import modules.items.weapon as weapon_module
import modules.items.armor as armor_module
import modules.items.item as item_module
import modules.core.save as save_module

LOOT_DATA_FILE = 'saves/lootData.json'

def save_status(loot_data: dict):
    save_module.save_status(loot_data, LOOT_DATA_FILE)

def load_status():
    return save_module.load_status(LOOT_DATA_FILE)

def wipe_status():
    save_module.wipe_status(LOOT_DATA_FILE)

def get_rarity(game_data: dict) -> int:
    roll = random.randint(0, 100) 
    match game_data['difficulty']:
        case 0:
            roll += int(game_data['level'] * 2)
        case 1:
            roll += int(game_data['level'] * 1)
        case 2:
            roll += int(game_data['level'] * 0.5)
    if roll <= 50:
        rarity = 0 # Comum
    elif roll <= 75:
        rarity = 1 # Incomum
    elif roll <= 100:
        rarity = 2 # Raro
    else:
        rarity = 3 # Lendário

    return rarity

def get_loot_weights(game_data: dict) -> list:
    weights = []

    match game_data['difficulty']:
        case 0:
            weights = [0.2] * 5
        case 1:
            match game_data['level']:
                case 1 | 2:
                    weights = [0.60, 0.30, 0.10, 0.00, 0.00]
                case 3 | 4:
                    weights = [0.30, 0.50, 0.15, 0.05, 0.00]
                case 5 | 6:
                    weights = [0.10, 0.20, 0.50, 0.15, 0.05]
                case 7 | 8:
                    weights = [0.00, 0.10, 0.30, 0.50, 0.10]
                case 9 | 10:
                    weights = [0.00, 0.00, 0.10, 0.70, 0.20]
        case 2:
            match game_data['level']:
                case 1 | 2:
                    weights = [0.60, 0.30, 0.10, 0.00, 0.00]
                case 3 | 4:
                    weights = [0.30, 0.50, 0.15, 0.05, 0.00]
                case 5 | 6:
                    weights = [0.20, 0.20, 0.40, 0.15, 0.05]
                case 7 | 8:
                    weights = [0.20, 0.20, 0.30, 0.25, 0.05]
                case 9 | 10:
                    weights = [0.20, 0.20, 0.20, 0.35, 0.05]

    return weights

def get_random_loot(game_data: dict) -> dict:
    loot_ratiry = get_rarity(game_data)
    roll = random.randint(0, 100) 

    if roll <= 40:
        return{
            'type': 'armor',
            'item': armor_module.get_random_armor(game_data)
        }
    elif roll <= 80:
        return{
            'type': 'weapon',
            'item': weapon_module.get_random_weapon(game_data, loot_ratiry)
        }
    else:
        return{
            'type': 'item',
            'item': item_module.get_random_item(loot_ratiry)
        }
