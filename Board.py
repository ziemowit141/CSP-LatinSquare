import copy

import numpy as np


def constraint_checker(value_array, row, col, value_to_be_inserted):
    if value_to_be_inserted in value_array[row][col] and constraint_checker_after_removal(value_array[:], row, col,
                                                                                          value_to_be_inserted):
        return True

    return False


def constraint_checker_after_removal(value_array, row, col, value_to_be_inserted):
    value_array_copy = copy.deepcopy(value_array)
    remove_val_from_row(value_array_copy, row, value_to_be_inserted)
    remove_val_from_col(value_array_copy, col, value_to_be_inserted)
    list_row = value_array_copy[row]
    list_row = list_row[col + 1:]

    for list_ in list_row:
        if len(list_) == 0:
            return False

    for list_ in value_array_copy[row + 1:]:
        if len(list_[col]) == 0:
            return False

    return True


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
        self.forward_board = create_tab_of_tabs(size)

    def print_forward_board(self):
        for row in self.forward_board:
            print(row)

        print("=======================")

    def check_grid(self):
        for row in self.forward_board:
            if not all(elem in row for elem in [x for x in range(self.size)]):
                return False

        return True

    def run_algorithm(self, board, forward_board, row, col):
        # Check if we are still in bounds
        if col >= len(board):
            if row + 1 >= len(board):
                print(board)
                return False
            else:
                row += 1
                col = 0

        for value_to_be_inserted in forward_board[row][col]:
            print(value_to_be_inserted)
            if constraint_checker(forward_board, row, col, value_to_be_inserted):
                board_copy = board[:]
                forward_board_copy = copy.deepcopy(forward_board)
                remove_val_from_row(forward_board_copy, row, value_to_be_inserted)
                remove_val_from_col(forward_board_copy, col, value_to_be_inserted)
                board_copy[row, col] = value_to_be_inserted
                if self.check_grid():
                    return board
                self.run_algorithm(board_copy, forward_board_copy, row, col+1)

        print(board)


board = Board(4)
# print(len(board.board))
# print(board.check_grid())
board.run_algorithm(board.board, board.forward_board, 0, 0)
# remove_val_from_col(board.forward_board, 1, 2)
# remove_val_from_row(board.forward_board, 0, 2)
# board.print_forward_board()
# asd = board.forward_board[0]
# print(asd[1:])
