class Piece:
    def __init__(self, color, position):
        self.color = color
        self.position = position
        self.symbol = "?"

    def __str__(self):
        return self.symbol.upper() if self.color == "white" else self.symbol.lower()


class Pawn(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.symbol = "P"

    def get_valid_moves(self, board):
        moves = []
        r, c = self.position

        direction = -1 if self.color == "white" else 1
        start_row = 6 if self.color == "white" else 1

        if board.is_valid_position(r+direction, c):
            if board.board[r+direction][c] is None:
                moves.append((r+direction,c))

                if r == start_row and board.board[r+2*direction][c] is None:
                    moves.append((r+2*direction,c))

        for dc in [-1,1]:
            nr, nc = r+direction, c+dc
            if board.is_valid_position(nr,nc):
                t = board.board[nr][nc]
                if t and t.color != self.color:
                    moves.append((nr,nc))

        return moves
