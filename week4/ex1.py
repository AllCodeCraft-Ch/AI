import copy
import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("---------")
    print()

def is_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def minimax(board, depth, maximizing_player):
    if is_winner(board, 'x'):
        return -1
    elif is_winner(board, 'o'):
        return 1
    elif is_full(board):
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for i, j in get_empty_cells(board):
            board_copy = copy.deepcopy(board)
            board_copy[i][j] = 'o'
            eval = minimax(board_copy, depth + 1, False)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i, j in get_empty_cells(board):
            board_copy = copy.deepcopy(board)
            board_copy[i][j] = 'x'
            eval = minimax(board_copy, depth + 1, True)
            min_eval = min(min_eval, eval)
        return min_eval

def find_best_move(board):
    best_val = float('-inf')
    best_move = (-1, -1)
    for i, j in get_empty_cells(board):
        board_copy = copy.deepcopy(board)
        board_copy[i][j] = 'o'
        move_val = minimax(board_copy, 0, False)
        if move_val > best_val:
            best_move = (i, j)
            best_val = move_val
    return best_move

def end_game(board):
    if is_winner(board, 'x'):
        print("Congratulations! You won!")
        return True
    elif is_winner(board, 'o'):
        print("AI 'o' wins! Better luck next time.")
        return True
    elif is_full(board):
        print("It's a draw!")
        return True
    return False

def play_tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    for s in range(9):
        if s % 2 == 0:
            while True:
                try:
                    row, col = map(int, input("Enter your move (row space column): ").split())
                    if board[row][col] != ' ':
                        print("Cell already taken. Try again.")
                    else:
                        break
                except ValueError:
                    print("Invalid input. Please enter two numbers separated by a space.")
                except IndexError:
                    print("Invalid input. Please enter numbers between 0 and 2.")
            board[row][col] = 'x'
        else:
            print("AI 'o' is thinking...")
            row, col = find_best_move(board)
            board[row][col] = 'o'
        print_board(board)
        if end_game(board):
            break

if __name__ == "__main__":
    play_tic_tac_toe()
