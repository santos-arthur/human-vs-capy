
import modules.core.save as save_module
import modules.core.utils as utils_module


LEADERBOARD_DATA_FILE = 'saves/leaderboardData.json'

def save_status(leaderboard_data: dict):
    save_module.save_status(leaderboard_data, LEADERBOARD_DATA_FILE)

def load_status():
    return save_module.load_status(LEADERBOARD_DATA_FILE)

def wipe_status():
    save_module.wipe_status(LEADERBOARD_DATA_FILE)

def add_to_leaderboard(game_data: dict, player_data: dict):
    leaderboard_data = load_status()
    save_data = {
                'game_data': game_data,
                'player_data': player_data
            }
    if leaderboard_data is None:
        leaderboard_data = [save_data]
    else:
        leaderboard_data.append(save_data)

    save_status(leaderboard_data)

def show_leaderboard():
    utils_module.clear()
    utils_module.centered_print('Placar de Líderes')
    leaderboard_data = load_status()
    if leaderboard_data is None:
        print()
        utils_module.centered_print('Nenhuma partida encontrada!')
    else:
        leaderboard_order = []
        for position in leaderboard_data:
            if leaderboard_order == []:
                leaderboard_order.append(position)
            else:
                for index, ordered_position in enumerate(leaderboard_order, 0):
                    if (position['player_data']['points'] > ordered_position['player_data']['points']) or (position['player_data']['points'] == ordered_position['player_data']['points'] and position['game_data']['level'] > ordered_position['game_data']['level']):
                        leaderboard_order.insert(index, position)
                        break
                else:
                    leaderboard_order.append(position)

        print("╔" + "═" * 5 + "╦" + "═" * 28 + "╦" + "═" * 5 + "╦" + "═" * 5 + "╗")
        print("║ Pos ║ Nome" + " " * 23 + "║ Lvl ║ Pts ║")
        print("╠" + "═" * 5 + "╬" + "═" * 28 + "╬" + "═" * 5 + "╬" + "═" * 5 + "╣")
        for index, item in enumerate(leaderboard_order, 1):
            pos = str(index)
            name = item['player_data']['name']
            name = name if len(name) < 27 else name[:27]

            level = str(item['game_data']['level'])
            points = str(item['player_data']['points'])
            print("║ " + pos + " " * (4 - len(pos)) + "║ " + name + " " * (27 - len(name)) + "║ " + level + " " * (4 - len(level)) + "║ " + points + " " * (4 - len(points)) + "║")
        
        print("╚" + "═" * 5 + "╩" + "═" * 28 + "╩" + "═" * 5 + "╩" + "═" * 5 + "╝")

    print()
    utils_module.press_any_key()