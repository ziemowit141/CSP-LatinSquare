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
    tab = [[[x for x in range(1, value)] for _ in range(1, value)] for _ in range(1, value)]
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


#########################################
# Piramids Part

def piramid_checker(values):
    prev = [0]
    seen = 0
    for val in values:
        if val > max(prev):
            seen += 1
        prev.append(val)

    return seen


def available_values(values):
    available_values = [x for x in range(1, len(values) + 1)]
    for val in values:
        try:
            available_values.remove(val)
        except ValueError:
            pass

    return available_values


def max_possible(inserted):
    count = 0
    for val in available_values(inserted):
        if val > max(inserted):
            count += 1

    return piramid_checker(inserted) + count


class Board:
    def __init__(self, size):
        self.size = size
        self.board = np.zeros((size, size), dtype=int)
        self.board[:] = -1
        self.forward_board = create_tab_of_tabs(size+1)
        self.columns = [-1, 4, -1, 2]
        self.rows = [-1, 4, -1, -1]

    def create_constraint__(self):
        pass

    def print_forward_board(self):
        for row in self.forward_board:
            print(row)

        print("=======================")

    def constraint_checker(self):
        for row in range(self.size):
            if any_duplicate(self.board[row]):
                return False
            if self.rows[row] != -1:
                if max_possible(self.board[row]) < self.rows[row]:
                    return False
                if piramid_checker(self.board[row]) > self.rows[row]:
                    return False

        for col in range(self.size):
            if any_duplicate(self.board[:, col]):
                return False
            if self.columns[col] != -1:
                if max_possible(self.board[:, col]) < self.columns[col]:
                    return False
                if piramid_checker(self.board[:, col]) > self.columns[col]:
                    return False

        return True

    def run_algorithm(self, forward_board, row, col):
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


board = Board(4)
result = board.run_algorithm(board.forward_board, 0, 0)
print(result)

# print(board.forward_board)
# print(max_possible([1, -1, -1, -1]))
# print(available_values([0, 0, 1, 2]))
# print(piramid_checker([2, 3, 1, 4]))
