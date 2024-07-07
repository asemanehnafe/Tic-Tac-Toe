import GameMenu


def show_history():
    print('')


def run():
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
