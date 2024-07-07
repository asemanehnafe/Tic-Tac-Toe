from Board import Board
from Player import Player
from Game import Game


def player_move(board, player):
    valid_move = False
    while not valid_move:
        try:
            row = int(input(f"Player {player.name}, enter row (1-3): ")) - 1
            col = int(input(f"Player {player.name}, enter column (1-3): ")) - 1
            if row in range(3) and col in range(3) and board.is_empty(row,col):
                board.set_player(row, col, player.symbol)
                valid_move = True
            else:
                print("Invalid move. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def run():
    first_player_name = input('Enter player 1 name:')
    second_player_name = input('Enter player 2 name:')
    first_player = Player(first_player_name, 'X')
    second_player = Player(second_player_name, 'O')
    board = Board()
    print(first_player.name, first_player.symbol)
    print(second_player.name, second_player.symbol)
    turn = 1
    while True:
        board.print_board()
        current_player = first_player if turn == 1 else second_player
        player_move(board, current_player.symbol)
        win = board.check_win(current_player)
        if win == 1:
            board.print_board()
            print(f"Player {current_player.name} wins!")
            break
        elif win == 0:
            board.print_board()
            print("It's a tie!")
            break
        turn = 0 if turn else 1

