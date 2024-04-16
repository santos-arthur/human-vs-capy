import modules.core.menu as menu_module
import modules.core.game as game_module
import modules.core.config as config_module
import modules.core.leaderboard as leaderboard_module

while True:
    option = menu_module.main_menu()

    match option:
        case 'new_game':
            game_module.new_game()
        case 'continue_game':
            game_module.run_game()
        case 'leaderboard':
            leaderboard_module.show_leaderboard()
        case 'configs':
            config_module.configs_menu()
        case 'credits':
            menu_module.show_credtis()
        case 'exit':
            if menu_module.confirm_menu_action('Deseja realmente sair do jogo?'):
                print("Muito obrigado por jogar Humans vs Capy!")
                break