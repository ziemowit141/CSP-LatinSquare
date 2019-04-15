import random

from numpy import zeros


def constraint_checker(row, value_to_be_inserted):
    for value in row:
        if value_to_be_inserted == value:
            break

    return True


class Board:
    def __init__(self):
        self.board = zeros((5, 5), dtype=int)
        self.forward_board = 


    def run_algorithm(self):
        for field in self.board:
            value_to_be_inserted = random.randint(0, 5)
            while not constraint_checker(value_to_be_inserted):
                value_to_be_inserted = random.randint(0, 5)
            field = value_to_be_inserted

board = Board()
print(board.board)
