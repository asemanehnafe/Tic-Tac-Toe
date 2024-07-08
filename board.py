class Board:
    def __init__(self):
        self.board = [[" "] * 3 for _ in range(3)]

    def print_board(self):
        print("\n")
        for row in self.board:
            print(" | ".join(row))
            print("---------")
        print("\n")

    def check_win(self, player, current_row, current_col):
        # Check rows
        if all(cell == player for cell in self.board[current_row][:]):
            return 1
        # Check columns
        if all(self.board[row][current_col] == player for row in range(3)):
            return 1
        # Check diagonals
        if all(self.board[i][i] == player for i in range(3)) or \
                all(self.board[i][2 - i] == player for i in range(3)):
            return 1
        if all(all(cell != " " for cell in row) for row in self.board):
            return 0
        return -1

    def set_player(self, row, col, player):
        self.board[row][col] = player

    def is_empty(self, row, col):
        return self.board[row][col] == " "
