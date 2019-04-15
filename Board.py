from numpy import zeros


class Board:
    def __init__(self):
        self.board = zeros((5, 5), dtype=int)

    def row_constraint(self, value_to_be_inserted):
        for value in row:
            if value_to_be_inserted == value:
                break

        return True

    def

board = Board()
print(board.board)
