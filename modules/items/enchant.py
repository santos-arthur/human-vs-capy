import random

def create_enchant(name: str, description: str, type: int, damage_dice: int, dice_amount: int, chance: int) -> dict:
    return {
        'name':         name,
        'description':  description,
        'type':         type,
        'damage_dice':   damage_dice,
        'dice_amount':   dice_amount,
        'chance':       chance
    }

def enchants() -> list:
    fire = create_enchant(
        name='Fogo',
        description='Cria uma explosão de fogo quando acerta o alvo. Causando mais dano!',
        type=0,
        damage_dice=6,
        dice_amount=1,
        chance=100
    )

    ice = create_enchant(
        name='Gelo',
        description='Tem uma chance de congelar o inimigo pelo próximo turno!',
        type=1,
        damage_dice=0,
        dice_amount=0,
        chance=50
    )
    
    blood = create_enchant(
        name='Sangue',
        description='Sempre que causar dano em um inimigo, cure um pouco de vida!',
        type=2,
        damage_dice=6,
        dice_amount=1,
        chance=100
    )

    return [
        fire,
        ice,
        blood
    ]

def get_random_enchant() -> dict:
    enchant_list = enchants()

    roll = random.randint(0,len(enchant_list) - 1)

    return enchant_list[roll]

def apply_effect(player_data, attack_weapon, enemy_data):
    damage = 0
    heal   = 0
    frozen = False
    match attack_weapon['enchant']['type']:
        case 0:
            values = [random.randint(1, attack_weapon['enchant']['damage_dice']) for _ in range(attack_weapon['enchant']['dice_amount'])]
            damage += sum(values) + attack_weapon['rarity']
        case 1:
            frozen = True if random.randint(1, 100) <= (attack_weapon['enchant']['chance'] + (attack_weapon['rarity'] * 10)) else False
        case 2:
            values = [random.randint(1, attack_weapon['enchant']['damage_dice']) for _ in range(attack_weapon['enchant']['dice_amount'])]
            heal = min(sum(values) + attack_weapon['rarity'], (player_data['max_hp'] - player_data['cur_hp']))
    
    return {
        'damage':   damage,
        'heal':     heal,
        'frozen':   frozen
    }