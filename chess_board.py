class ChessBoard:
    def __init__(self):
        self.board = self.create_board()

    def create_board(self):
        board = [[None for _ in range(8)] for _ in range(8)]
        board[0] = ["r", "n", "b", "q", "k", "b", "n", "r"]
        board[1] = ["p", "p", "p", "p", "p", "p", "p", "p"]
        board[7] = ["R", "N", "B", "Q", "K", "B", "N", "R"]
        board[6] = ["P", "P", "P", "P", "P", "P", "P", "P"]
        return board

    def display_board(self):
        for row in self.board:
            print(" ".join(piece if piece else "." for piece in row))
        print()

    def is_valid_position(self, r, c):
        return 0 <= r < 8 and 0 <= c < 8

    def move_piece(self, start, end):
        from_r, from_c = start
        to_r, to_c = end

        if not self.is_valid_position(from_r, from_c) or not self.is_valid_position(to_r, to_c):
            return False

        piece = self.board[from_r][from_c]
        if piece is None:
            return False

        target = self.board[to_r][to_c]

        # ❗ prevents capturing your own pieces (THIS FIXES YOUR BUG)
        if target is not None:
            if piece.isupper() == target.isupper():
                return False

        self.board[to_r][to_c] = piece
        self.board[from_r][from_c] = None
        return True

    def get_all_pieces(self, color):
        pieces = []
        for r in range(8):
            for c in range(8):
                piece = self.board[r][c]
                if piece:
                    if color == "white" and piece.isupper():
                        pieces.append((r, c))
                    if color == "black" and piece.islower():
                        pieces.append((r, c))
        return pieces
