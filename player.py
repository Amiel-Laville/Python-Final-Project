import random

class Player:
    def __init__(self, color):
        self.color = color

    def convert(self, pos):
        col_map = {
            "a":0,"b":1,"c":2,"d":3,
            "e":4,"f":5,"g":6,"h":7
        }

        col = col_map[pos[0].lower()]
        row = 8 - int(pos[1])

        return (row, col)


class AIPlayer:
    def __init__(self, color):
        self.color = color

    def get_move(self, board):
        moves = []

        for piece in board.get_all_pieces(self.color):
            for m in piece.get_valid_moves(board):
                moves.append((piece, m))

        if not moves:
            return

        piece, move = random.choice(moves)
        board.move_piece(piece.position, move)
