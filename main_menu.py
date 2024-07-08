from game_controller import GameController


class MainMenu:
    @staticmethod
    def show_history():
        try:
            with open('game_results.txt', 'r') as file:
                game_results_content = file.read()
                print("\nhistory:")
                print(game_results_content)
        except FileNotFoundError:
            print("game_results file not found.")

    @staticmethod
    def print_guide():
        print('press start to run a new game')
        print('press exit to quit')
        print('press history to show the history')

    @staticmethod
    def run():
        while True:
            MainMenu.print_guide()
            command = input()
            match command:
                case 'start':
                    GameController.run()
                case 'history':
                    MainMenu.show_history()
                case 'exit':
                    return
                case _:
                    print('Invalid command')
