import copy
import random
import time

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


def max_possible_reversed(inserted):
    count = piramid_checker(inserted)
    if count is 0:
        return 4

    for val in available_values(inserted):
        if val > max(inserted):
            count = 1
        else:
            count += 1

    return count


class Board:
    def __init__(self, size):
        self.size = size
        self.board = np.zeros((size, size), dtype=int)
        self.board[:] = -1
        self.forward_board = create_tab_of_tabs(size + 1)

        # Constraints
        self.assign_constraints()
        # self.top = [-1, 4, -1, 4]
        # self.left = [-1, 4, -1, -1]

    def create_constraint__(self):
        constraint_list = [-1 for _ in range(1, self.size + 1)]
        index_set = set()
        for val in range(1):
            index = random.randint(0, self.size - 1)
            while index in index_set:
                index = random.randint(0, self.size - 1)
            index_set.add(index)
            value = random.randint(1, self.size)
            constraint_list[index] = value

        return constraint_list

    def assign_constraints(self):
        self.top = self.create_constraint__()
        self.left = self.create_constraint__()
        self.bottom = self.create_constraint__()
        self.right = self.create_constraint__()

        self.print_constraints()

    def print_constraints(self):
        print(f"Top constraints: {self.top}")
        print(f"Left constraints: {self.left}")
        print(f"Bottom constraints: {self.bottom}")
        print(f"Right constraints: {self.right}")
        print("=======================")

    def print_forward_board(self):
        for row in self.forward_board:
            print(row)

        print("=======================")

    def constraint_checker(self):
        for row in range(self.size):
            if any_duplicate(self.board[row]):
                return False
            if self.left[row] != -1:
                if max_possible(self.board[row]) < self.left[row]:
                    return False
                if piramid_checker(self.board[row]) > self.left[row]:
                    return False

        for col in range(self.size):
            if any_duplicate(self.board[:, col]):
                return False
            if self.top[col] != -1:
                if max_possible(self.board[:, col]) < self.top[col]:
                    return False
                if piramid_checker(self.board[:, col]) > self.top[col]:
                    return False

        for row in range(self.size):
            if self.right[row] != -1:
                if max_possible_reversed(self.board[row][::-1]) < self.right[row]:
                    return False
                if piramid_checker(self.board[row][::-1]) > self.right[row]:
                    return False

        for col in range(self.size):
            if self.bottom[col] != -1:
                if max_possible_reversed(self.board[:, col][::-1]) < self.bottom[col]:
                    return False
                if piramid_checker(self.board[:, col][::-1]) > self.bottom[col]:
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


board = Board(3)
result = board.run_algorithm(board.forward_board, 0, 0)
times = 0
while result is None:
    board.assign_constraints()
    start = time.time()
    result = board.run_algorithm(board.forward_board, 0, 0)
    end = time.time()
    times = end - start
print(result)
print(times)

