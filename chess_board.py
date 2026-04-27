# chess_board.py

class ChessBoard:
    def __init__(self):
        self.board = self.setup_board()

    def setup_board(self):
        return [['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
                ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
                [' ' for _ in range(8)],
                [' ' for _ in range(8)],
                [' ' for _ in range(8)],
                [' ' for _ in range(8)],
                ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
                ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']]

    def display(self):
        for row in self.board:
            print(' '.join(row))

    def move_piece(self, start, end):
        # Logic to move a piece
        pass
