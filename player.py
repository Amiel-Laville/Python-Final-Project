"""Player and AI logic for chess"""

class Player:
    def __init__(self, color):
        self.color = color
    
    def get_move(self, board):
        while True:
            try:
                move_input = input(f"{self.color.capitalize()}'s turn. Enter move (row col row col): ")
                parts = move_input.split()
                if len(parts) != 4:
                    print("Invalid format. Use 'from_row from_col to_row to_col'")
                    continue
                from_row, from_col, to_row, to_col = map(int, parts)
                if board.move_piece((from_row, from_col), (to_row, to_col)):
                    return
                else:
                    print("Invalid move. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Use 'from_row from_col to_row to_col'")

class AIPlayer:
    def __init__(self, color):
        self.color = color
    
    def get_move(self, board):
        print(f"AI ({self.color}) is thinking...")
        for piece in board.get_all_pieces(self.color):
            moves = piece.get_valid_moves(board)
            if moves:
                move = moves[0]
                board.move_piece(piece.position, move)
                return