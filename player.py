import random

class Player:
    def __init__(self, color):
        self.color = color

    def get_move(self, board):
        while True:
            try:
                move = input("Move (r c r c): ")
                r1, c1, r2, c2 = map(int, move.split())

                if board.move_piece((r1,c1),(r2,c2)):
                    return
                print("Invalid move")
            except:
                print("Bad input")


class AIPlayer:
    def __init__(self, color):
        self.color = color

    def get_move(self, board):
        pieces = board.get_all_pieces(self.color)

        moves = []
        for p in pieces:
            for m in p.get_valid_moves(board):
                moves.append((p, m))

        if not moves:
            return

        piece, move = random.choice(moves)
        board.move_piece(piece.position, move)
