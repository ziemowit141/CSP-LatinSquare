import copy

import numpy as np


def any_duplicate(my_list):
    seen = set()
    for x in my_list:
        if x in seen and x != -1:
            return True
        seen.add(x)
    return False


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
        self.board = np.zeros((size, size), dtype=int)
        self.board[:] = -1
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

    def constraint_checker_v2(self):
        for row in self.board:
            if any_duplicate(row):
                return False

        for col in range(len(self.board)):
            if any_duplicate(self.board[:, col]):
                return False

        return True

    def run_algorithm(self, forward_board, row, col):
        if self.constraint_checker_v2():
            if col >= len(self.board):
                if row + 1 >= len(self.board):
                    return self.board
                else:
                    row += 1
                    col = 0
            for val in range(0, len(self.board)):
                self.board[row, col] = val
                board = self.run_algorithm(self.forward_board, row, col+1)
                if board is not None:
                    return board
                else:
                    self.board[row, col] = -1


        # for value_to_be_inserted in forward_board[row][col]:

        # for value_to_be_inserted in forward_board[row][col]:
        #     if constraint_checker(forward_board, row, col, value_to_be_inserted):
        #         board_copy = board[:]
        #         forward_board_copy = copy.deepcopy(forward_board)
        #         remove_val_from_row(forward_board_copy, row, value_to_be_inserted)
        #         remove_val_from_col(forward_board_copy, col, value_to_be_inserted)
        #         board_copy[row, col] = value_to_be_inserted
        #         if self.check_grid():
        #             return board
        #         self.run_algorithm(board_copy, forward_board_copy, row, col + 1)


board = Board(7)
result = board.run_algorithm([], 0, 0)
print(result)
# board.run_algorithm(board.board, board.forward_board, 0, 0)



# solution = board.run_algorithm(board.board, board.forward_board, 0, 0)
# print(solution)
