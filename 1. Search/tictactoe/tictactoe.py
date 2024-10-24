"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    
    if x_count <= o_count:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    available_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                available_actions.add((i, j))
    return  available_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j =  action
    
    if  board[i][j] != EMPTY:
        raise ValueError("Invalid action")
    
    new_board = copy.deepcopy(board)
    
    new_board[i][j] = player(board)
    
    return new_board
    


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
        if row[0] == row[1] == row[2] and row [0] is not EMPTY:
            return row[0]
    
    #  Check columns
    for col in range(3):
        if board[0][col] == board[1][col]  == board[2][col] and board[0][col] is not EMPTY:
            return board[0][col]
    
    #  Check diagonals
    if  board[0][0] == board[1][1] == board[2][2]  and board[0][0] is not EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not EMPTY:
        return board[0][2]
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    
    for row in board:
        if EMPTY in row:
            return False
    
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    game_winner = winner(board)
    
    if  game_winner == X:
        return 1
    elif game_winner == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    curr_player = player(board)
    
    if curr_player == X:
        value, move = max_value(board)
    else:
        value, move = min_value(board)
    
    return  move

def max_value(board):
    """
    Maximizing function for X
    """
    if terminal(board):
        return utility(board), None
    
    value = -float('inf')
    best_move = None
    for action in actions(board):
        min_val, _ = min_value(result(board, action))
        if min_val > value:
            value = min_val
            best_move = action
    return value, best_move

def min_value(board):
    """
    Minizing function for O
    """
    if terminal(board):
        return utility(board), None
    
    value = float('inf')
    best_move = None
    for action in actions(board):
        max_val, _ = max_value(result(board, action))
        if max_val < value:
            value = max_val
            best_move = action
    return value, best_move
