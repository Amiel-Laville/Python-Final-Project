import random

class Player:
    def __init__(self, color):
        self.color = color

    def get_move(self, board):
        while True:
            try:
                move = input(f"{self.color} move (from_r from_c to_r to_c): ")
                r1, c1, r2, c2 = map(int, move.split())

                if board.move_piece((r1, c1), (r2, c2)):
                    return
                else:
                    print("Invalid move, try again.")

            except:
                print("Invalid input.")


class AIPlayer:
    def __init__(self, color):
        self.color = color

    def get_move(self, board):
        print(f"AI ({self.color}) thinking...")

        pieces = board.get_all_pieces(self.color)
        random.shuffle(pieces)

        for (r, c) in pieces:
            # try simple directions
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue

                    nr, nc = r + dr, c + dc

                    if board.move_piece((r, c), (nr, nc)):
                        return
