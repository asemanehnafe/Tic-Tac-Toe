import GameMenu


def show_history():
    try:
        with open('game_results.txt', 'r') as file:
            game_results_content = file.read()
            print("\nhistory:")
            print(game_results_content)
    except FileNotFoundError:
        print("game_results file not found.")


def print_guide():
    print('press start to run a new game')
    print('press exit to quit')
    print('press history to show the history')


def run():
    while True:
        print_guide()
        command = input()
        match command:
            case 'start':
                GameMenu.run()
            case 'history':
                show_history()
            case 'exit':
                return
            case _:
                print('Invalid command')
