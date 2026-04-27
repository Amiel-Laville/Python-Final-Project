import random

class Player:
    def __init__(self, color):
        self.color = color
    
    def get_move(self, board):
        while True:
            try:
                move_input = input(f"{self.color.capitalize()}'s turn. Enter move (row col row col): ")
                parts = move_input.split()
                if len(parts) != 4:
                    print("Invalid format.")
                    continue

                from_row, from_col, to_row, to_col = map(int, parts)

                if board.move_piece((from_row, from_col), (to_row, to_col)):
                    return
                else:
                    print("Invalid move. Try again.")

            except:
                print("Invalid input.")
                

class AIPlayer:
    def __init__(self, color):
        self.color = color
    
    def get_move(self, board):
        print(f"AI ({self.color}) is making a move...")

        pieces = board.get_all_pieces(self.color)

        random.shuffle(pieces)

        for (r, c) in pieces:
            # try random moves
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    new_r, new_c = r + dr, c + dc
                    if board.move_piece((r, c), (new_r, new_c)):
                        return
