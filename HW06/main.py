# Create a Python class TicTacToe representing the Tic-Tac-Toe game.
# Implement basic functionalities: initializing the board, making moves, checking for a
# win/draw, and displaying the board.
class TicTacToe:
    def __init__(self):
        # Initialize the Tic-Tac-Toe game state
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def display_board(self):
        for row in self.board:
            print('|'.join(row))
            print('---------')

    def make_move(self, row, col):

        # check that we aren't placing on top of something
        if self.board[row][col] != "X" and self.board[row][col] != "O" :
            self.board[row][col] = self.current_player
        # Make a move and update the Tic-Tac-Toe board
        pass

    def unmake_move(self, row, col):
        self.board[row][col] = ""
        pass

    def check_winner(self):
        # columns check
        for i in range(0, 3):
            if ((self.board[i][0] == "X" or self.board[i][0] == "O") and self.board[i][0] == self.board[i][1] ==
                    self.board[i][2]):
                return True

        # rows check
        for i in range(0, 3):
            if ((self.board[0][i] == "X" or self.board[0][i] == "O") and self.board[0][i] == self.board[1][i] ==
                    self.board[2][i]):
                return True

        # diagonals
        if ((self.board[0][0] == "X" or self.board[0][0] == "O") and self.board[0][0] == self.board[1][1] ==
                self.board[2][2]):
            return True
        if ((self.board[2][0] == "X" or self.board[2][0] == "O") and self.board[2][0] == self.board[1][1] ==
                self.board[0][2]):
            return True

        return False

        # Check if there is a winner
        pass

    def get_winner(self):
        # columns check
        for i in range(0, 3):
            if ((self.board[i][0] == "X" or self.board[i][0] == "O") and self.board[i][0] == self.board[i][1] ==
                    self.board[i][2]):
                return self.board[i][0]

        # rows check
        for i in range(0, 3):
            if ((self.board[0][i] == "X" or self.board[0][i] == "O") and self.board[0][i] == self.board[1][i] ==
                    self.board[2][i]):
                return self.board[0][i]

        # diagonals
        if ((self.board[0][0] == "X" or self.board[0][0] == "O") and self.board[0][0] == self.board[1][1] ==
                self.board[2][2]):
            return self.board[0][0]
        if ((self.board[2][0] == "X" or self.board[2][0] == "O") and self.board[2][0] == self.board[1][1] ==
                self.board[0][2]):
            return self.board[2][0]

        return False

        # Check if there is a winner
        pass

    def is_draw(self):

        temp = 0
        for i in range(0, 3):
            for j in range(0, 3):
                if self.board[i][j] == "X" or self.board[i][j] == "O":
                    temp += 1
        if temp == 9:
            return True
        return False
        # Check if the game is a draw
        pass

    def available_moves(self):
        moves = []
        for i in range(0, 3):
            for j in range(0, 3):
                if self.board[i][j] != "X" and self.board[i][j] != "O":
                    moves.append((i, j))
        return moves
        # Return a list of available moves (empty cells)
        pass

    # you did not tell us what to use depth for so I shall ignore it.
    def minimax(state, depth, maximizing_player):

        # get available moves,
        # then call minimax on them for the player that goes
        # after this player.

        # minimax(state, depth, maximizing_player):
        # Base Cases:

        # Check if the game is in a terminal state (someone has won or it's
        # a draw).

        # If terminal, return the utility value (-1, 0, or 1) based on the
        # winner or draw.

        # 1 if the AI wins,
        # 0 if a draw,
        # -1 if the player wins.

        # Maximizing Player (AI Player):
        # Initialize max_eval to negative infinity.
        # Iterate through available moves (empty cells).
        # Make the move, recursively call minimax for the next state with
        # the opponent as the maximizing player.
        # Undo the move.
        # Update max_eval with the maximum of the current evaluation
        # and the result of the recursive call.
        # Return max_eval.

        if state.check_winner():
            if state.current_player == maximizing_player:
                return 1
            else:
                return -1
        if state.is_draw():
            return 0
        #I decided on a depth of 7 as it was
        # the highest I could go without encountering
        # any visual slow downs in the console output.
        if depth >= 7:
            return 0

        curDepth = depth + 1

        if maximizing_player == "O":
            max_eval = float('-inf')
            for m in state.available_moves():
                state.make_move(m[0], m[1])
                if state.check_winner():
                    if state.current_player == "O":
                        state.unmake_move(m[0], m[1])
                        return 1
                    else:
                        state.unmake_move(m[0], m[1])
                        return -1
                if state.is_draw():
                    state.unmake_move(m[0], m[1])
                    return 0
                max_eval = max(max_eval, state.minimax(curDepth, "X"))
                state.unmake_move(m[0], m[1])
            return max_eval
        elif maximizing_player == "X":
            min_eval = float('inf')
            for m in state.available_moves():
                state.make_move(m[0], m[1])
                if state.check_winner():
                    if state.current_player == "O":
                        state.unmake_move(m[0], m[1])
                        return 1
                    else:
                        state.unmake_move(m[0], m[1])
                        return -1
                if state.is_draw():
                    state.unmake_move(m[0], m[1])
                    return 0
                min_eval = min(min_eval, state.minimax(curDepth, "O"))
                state.unmake_move(m[0], m[1])
            return min_eval

        # Minimizing Player (Human Player):
        # Similar to the maximizing player, but update min_eval with the
        # minimum of the current evaluation and the result of the
        # recursive call.
        # Return min_eval.

        # Implement the minimax algorithm for Tic-Tac-Toe
        pass

    # Implement the Alpha-Beta Pruning algorithm for adversarial search in the Tic-Tac-Toe
    # game.

    # Create functions minimax and alpha_beta_pruning.
    # minimax should provide the utility value of the current state using the minimax
    # algorithm.

    # alpha_beta_pruning should enhance minimax with Alpha-Beta Pruning for efficiency.
    def alpha_beta_pruning(state, depth, alpha, beta, maximizing_player):
        if state.check_winner():
            if state.current_player == maximizing_player:
                return 1
            else:
                return -1
        if state.is_draw():
            return 0
        if depth >= 7:
            return 0

        curDepth = depth + 1
        if maximizing_player == "O":
            max_eval = float('-inf')
            for m in state.available_moves():
                state.make_move(m[0], m[1])
                if state.check_winner():
                    if state.current_player == "O":
                        state.unmake_move(m[0], m[1])
                        return 1
                    else:
                        state.unmake_move(m[0], m[1])
                        return -1
                if state.is_draw():
                    state.unmake_move(m[0], m[1])
                    return 0
                max_eval = max(max_eval, state.alpha_beta_pruning(curDepth, alpha, beta,"X"))
                state.unmake_move(m[0], m[1])
                # Update alpha with the maximum of alpha and max_eval.
                alpha = max(alpha, max_eval)
                # Pruning.
                if beta <= alpha:
                    break
            return max_eval
        elif maximizing_player == "X":
            min_eval = float('inf')
            for m in state.available_moves():
                state.make_move(m[0], m[1])
                if state.is_draw():
                    state.unmake_move(m[0], m[1])
                    return 0
                if state.check_winner():
                    if state.current_player == "O":
                        state.unmake_move(m[0], m[1])
                        return 1
                    else:
                        state.unmake_move(m[0], m[1])
                        return -1
                min_eval = min(min_eval, state.alpha_beta_pruning(curDepth, alpha, beta, "O"))
                state.unmake_move(m[0], m[1])
                # update beta with minimum of beta and min_eval
                beta = min(beta, min_eval)
                # check for pruning.
                if beta <= alpha:
                    break
            return min_eval

        # Implement the Alpha-Beta Pruning algorithm for Tic-Tac-Toe
        pass

    # Implement a function suggest_next_play that uses the Alpha-Beta Pruning algorithm
    # to suggest the optimal move for the AI player.
    def suggest_next_play(tic_tac_toe):
        best_move = None
        best_eval = float('-inf')
        # iterate through available moves.
        for m in tic_tac_toe.available_moves():
            tic_tac_toe.make_move(m[0], m[1])
            curEval = tic_tac_toe.alpha_beta_pruning(1, float('-inf'), float('inf'), tic_tac_toe.current_player)
            tic_tac_toe.unmake_move(m[0], m[1])
            # update best move if our
            # current evaluation is better
            # than our best evaluation.
            if curEval > best_eval:
                best_eval = curEval
                best_move = m

        return best_move
        # Suggest the next play for the AI player using Alpha-Beta Pruning
        pass


def input_int(prompt):
    num = 0
    while True:
        try:
            num = int(input(prompt))
        except ValueError:
            print("Please enter an integer.")
            continue
        else:
            # we got an integer so break the loop.
            return num
            # break


# lower and upper lim are inclusive.
def input_in_bounds(lower_lim, upper_lim, prompt):
    num = input_int(prompt)
    while True:
        if num > upper_lim:
            print("Input must be less than or equal to " + str(upper_lim))
            num = input_int(prompt)
            continue
        elif num < lower_lim:
            print("Input must be greater than or equal to " + str(lower_lim))
            num = input_int(prompt)
            continue
        else:
            return num


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Test your implementation
    tic_tac_toe = TicTacToe()
    tic_tac_toe.display_board()
    i = 9
    while i > 0:
        # if it is the player's turn.
        if tic_tac_toe.current_player == "X":
            r = input_in_bounds(0, 2, "Enter row index: ")
            c = input_in_bounds(0, 2, "Enter column index: ")

            print(tic_tac_toe.current_player + "'s turn!")

            while tic_tac_toe.board[r][c] == "X":
                print("Please enter an unoccupied space.")
                r = input_in_bounds(0, 2, "Enter row index: ")
                c = input_in_bounds(0, 2, "Enter column index: ")
                continue
            tic_tac_toe.make_move(r, c)
            tic_tac_toe.display_board()
            tic_tac_toe.current_player = "O"
        elif tic_tac_toe.current_player == "O":
            print(tic_tac_toe.current_player + "'s turn!")
            nextMove = tic_tac_toe.suggest_next_play()
            tic_tac_toe.make_move(nextMove[0], nextMove[1])
            tic_tac_toe.display_board()
            tic_tac_toe.current_player = "X"
        i -= 1
        if tic_tac_toe.check_winner():
            print()
            tic_tac_toe.display_board()
            print(tic_tac_toe.get_winner() + " Won!")
            break
        if tic_tac_toe.is_draw():
            print()
            tic_tac_toe.display_board()
            print("It's a draw!")
            break



    # tic_tac_toe.make_move(0, 0)
    # tic_tac_toe.make_move(0, 1)
    # tic_tac_toe.make_move(0, 2)

    # Make moves and test the minimax and alpha-beta pruning functions
    # Suggest the next play for the AI player and display the board
    # Compare results and analyze efficiency
    # Provide documentation and analysis

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# when it comes to efficiency sometimes minimax can be as efficient as
# alpha-beta pruning simply because there is nothing to prune some times.

# but, that doesn't mean one is better than the other.
# I think that alpha beta is really useful and isn't too far removed
# from minimax so it's worth it.