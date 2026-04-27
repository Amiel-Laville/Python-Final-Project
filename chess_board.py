from pieces import Pawn, Rook, Knight, Bishop, Queen, King

class ChessBoard:
    def __init__(self):
        self.board = self.create_board()

    def create_board(self):
        board = [[None for _ in range(8)] for _ in range(8)]

        board[0] = [
            Rook("black",(0,0)), Knight("black",(0,1)),
            Bishop("black",(0,2)), Queen("black",(0,3)),
            King("black",(0,4)), Bishop("black",(0,5)),
            Knight("black",(0,6)), Rook("black",(0,7))
        ]

        board[1] = [Pawn("black",(1,i)) for i in range(8)]
        board[6] = [Pawn("white",(6,i)) for i in range(8)]

        board[7] = [
            Rook("white",(7,0)), Knight("white",(7,1)),
            Bishop("white",(7,2)), Queen("white",(7,3)),
            King("white",(7,4)), Bishop("white",(7,5)),
            Knight("white",(7,6)), Rook("white",(7,7))
        ]

        return board

    def display_board(self):
        print("    a  b  c  d  e  f  g  h")
        print("  +------------------------+")

        for i, row in enumerate(self.board):
            row_num = 8 - i
            print(f"{row_num} |", end=" ")

            for piece in row:
                print(piece if piece else ".", end="  ")

            print(f"| {row_num}")

        print("  +------------------------+")
        print("    a  b  c  d  e  f  g  h\n")

    def is_valid_position(self, r, c):
        return 0 <= r < 8 and 0 <= c < 8

    def move_piece(self, start, end):
        r1, c1 = start
        r2, c2 = end

        if not self.is_valid_position(r1, c1) or not self.is_valid_position(r2, c2):
            return False

        piece = self.board[r1][c1]
        if not piece:
            return False

        if (r2, c2) not in piece.get_valid_moves(self):
            return False

        self.board[r2][c2] = piece
        self.board[r1][c1] = None
        piece.position = (r2, c2)

        return True

    def get_all_pieces(self, color):
        return [
            p for r in self.board for p in r
            if p and p.color == color
        ]
