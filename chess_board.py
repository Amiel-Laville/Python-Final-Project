class ChessBoard:
    def __init__(self):
        self.board = self.create_board()

    def create_board(self):
        # Initialize a chess board with pieces
        board = [[None for _ in range(8)] for _ in range(8)]
        # Place pieces on the board (for simplicity, only the first row)
        board[0] = ["r", "n", "b", "q", "k", "b", "n", "r"]  # Black pieces
        board[1] = ["p", "p", "p", "p", "p", "p", "p", "p"]  # Black pawns
        board[7] = ["R", "N", "B", "Q", "K", "B", "N", "R"]  # White pieces
        board[6] = ["P", "P", "P", "P", "P", "P", "P", "P"]  # White pawns
        return board

    def display_board(self):
        # Display the chess board
        for row in self.board:
            print(" ".join(piece if piece is not None else '.' for piece in row))

    def get_all_pieces(self):
        pieces = []
        for row in self.board:
            for piece in row:
                if piece is not None:
                    pieces.append(piece)
        return pieces

    # Additional chess methods would be defined here

# Example usage:
board = ChessBoard()
board.display_board()
