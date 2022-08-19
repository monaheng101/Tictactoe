import time
from player import HumanPlayer, RandomComputerPlayer
class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # a 3x3 board
        self.current_winner = None 

    def print_board(self):
        # for every row or group of three from the 9 board spaces
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
             print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # prints out which numbers correspond to which spot
        # 0 | 1 | 2 etc
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)] # sub arrays of rows of numbers
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')
    
    # returns a list of available moves after making a move
    def available_moves(self):
        # ['x', 'x', '0'] --> [(0, 'x'), (1, 'o')]
        return [i for i, spot in enumerate(self.board) if spot == ' ']
        # list comprehension for:
        # moves = []
        # for (i, spot) in enumerate(self.board):
        #     if spot == ' ':
        #         moves.append(i)
        # return moves

    # checks if the game has empty sqaures
    def empty_squares(self):
        return ' ' in self.board # boolean

    # counts the number of empty spaces
    def mun_empty_squares(self):
        return self.board.count(' ')

    # making a move with sqaure the user wants the move
    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            # check if winner
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # winner is 3 in row anywhere. (row, cloumn, diognal)
        # check the row
        row_ind = square // 3 # divide by 3 and round down
        row = self.board[row_ind * 3 : (row_ind + 1) * 3 ]
        if all([spot == letter for spot in row]):
            return True

        # check the column 
        col_ind = square % 3
        column = [self.board[col_ind + i * 3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # check the diagonals
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True

            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True

        # if all checks fail
        return False

def play(game, x_player, o_player, print_game=True):
    # returns the winner of the game(the letter) or None for a tie.
    if print_game:
        game.print_board_nums()
    
    letter = 'X' # starting letter

    while game.empty_squares():
        # get the move from the right player
        if letter == '0':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        
        # making the move
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to qaure {square}')
                game.print_board()
                print('')

            # when there is a winner
            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter

            # alternating letters after making a move (switch players)
            letter = '0' if letter == 'X' else 'X'

            time.sleep(1)
    
    # when to one wins <-- 
    if print_game:
        print('It\' a tie.')

    

if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('0')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)