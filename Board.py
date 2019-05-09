import time
import matplotlib.pyplot as plt
import copy

import numpy as np


def any_duplicate(my_list):
    seen = set()
    for x in my_list:
        if x in seen and x != -1:
            return True
        seen.add(x)
    return False


def create_tab_of_tabs(value):
    """Creates a list of lists with all possible values to be put in certain position"""
    tab = [[[x for x in range(0, value)] for _ in range(0, value)] for _ in range(0, value)]
    return tab


def remove_val_from_row(tab, row_number, value):
    """Exception to handle situation when value was already removed"""
    for list_ in tab[row_number]:
        try:
            list_.remove(value)
        except ValueError:
            pass


def remove_val_from_col(tab, col_number, value):
    """Exception to handle situation when value was already removed"""
    for list_ in tab:
        try:
            list_[col_number].remove(value)
        except ValueError:
            pass


class Board:
    def __init__(self, size):
        self.size = size
        self.board = np.zeros((size, size), dtype=int)
        self.board[:] = -1
        self.forward_board = create_tab_of_tabs(size)

    def print_forward_board(self, forward_board):
        for row in forward_board:
            print(row)

        print("=======================")

    def constraint_checker(self):
        for row in self.board:
            if any_duplicate(row):
                return False

        for col in range(len(self.board)):
            if any_duplicate(self.board[:, col]):
                return False

        return True

    def run_algorithm(self, forward_board, row, col):
        self.print_forward_board(forward_board)
        if self.constraint_checker():
            if col >= self.size:
                if row + 1 >= self.size:
                    return self.board
                else:
                    row += 1
                    col = 0

            for val in forward_board[row][col]:
                self.board[row, col] = val
                forward_board_copy = copy.deepcopy(forward_board)
                remove_val_from_row(forward_board_copy, row, val)
                remove_val_from_col(forward_board_copy, col, val)
                board = self.run_algorithm(forward_board_copy, row, col + 1)
                if board is not None:
                    return board
                else:
                    self.board[row, col] = -1


board = Board(5)
result = board.run_algorithm(board.forward_board, 0, 0)
print(result)
# times = []
# for x in range(11, 14):
#     board = Board(x)
#     start = time.time()
#     result = board.run_algorithm(board.forward_board, 0, 0)
#     end = time.time()
#     times.append(end-start)
#
# y_pos = [x for x in range(11, 14)]
#
# plt.bar(y_pos, times)
# plt.xlabel('Board Size')
# plt.ylabel('Time in seconds')
# plt.title('Latin square backtracking only')
# plt.show()
