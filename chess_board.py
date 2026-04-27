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
            print(" ".join(piece if piece else '.' for piece in row))
        print()

    def is_valid_position(self, row, col):
        return 0 <= row < 8 and 0 <= col < 8

    def move_piece(self, start, end):
        from_row, from_col = start
        to_row, to_col = end

        if not (self.is_valid_position(from_row, from_col) and
                self.is_valid_position(to_row, to_col)):
            return False

        piece = self.board[from_row][from_col]
        if piece is None:
            return False

        # Basic move (no real chess rules enforced)
        self.board[to_row][to_col] = piece
        self.board[from_row][from_col] = None
        return True

    def get_all_pieces(self, color):
        pieces = []
        for r in range(8):
            for c in range(8):
                piece = self.board[r][c]
                if piece:
                    if (color == 'white' and piece.isupper()) or \
                       (color == 'black' and piece.islower()):
                        pieces.append((r, c))
        return pieces
