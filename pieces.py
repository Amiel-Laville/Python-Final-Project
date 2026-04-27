class Piece:
    def __init__(self, color, position):
        self.color = color
        self.position = position
        self.symbol = "?"

    def __str__(self):
        return (self.symbol.upper() if self.color == "white"
                else self.symbol.lower())


class Pawn(Piece):
    def __init__(self, color, pos):
        super().__init__(color, pos)
        self.symbol = "P"

    def get_valid_moves(self, board):
        moves = []
        r, c = self.position

        direction = -1 if self.color == "white" else 1
        start_row = 6 if self.color == "white" else 1

        # forward
        if board.is_valid_position(r + direction, c):
            if board.board[r + direction][c] is None:
                moves.append((r + direction, c))

                if r == start_row and board.board[r + 2*direction][c] is None:
                    moves.append((r + 2*direction, c))

        # capture
        for dc in [-1, 1]:
            nr, nc = r + direction, c + dc
            if board.is_valid_position(nr, nc):
                t = board.board[nr][nc]
                if t and t.color != self.color:
                    moves.append((nr, nc))

        return moves


class Rook(Piece):
    def __init__(self, color, pos):
        super().__init__(color, pos)
        self.symbol = "R"

    def get_valid_moves(self, board):
        moves = []
        r, c = self.position

        for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            for i in range(1,8):
                nr, nc = r + dr*i, c + dc*i
                if not board.is_valid_position(nr,nc):
                    break

                t = board.board[nr][nc]
                if t is None:
                    moves.append((nr,nc))
                else:
                    if t.color != self.color:
                        moves.append((nr,nc))
                    break

        return moves


class Knight(Piece):
    def __init__(self, color, pos):
        super().__init__(color, pos)
        self.symbol = "N"

    def get_valid_moves(self, board):
        moves = []
        r, c = self.position

        for dr, dc in [(2,1),(2,-1),(-2,1),(-2,-1),
                       (1,2),(1,-2),(-1,2),(-1,-2)]:
            nr, nc = r+dr, c+dc
            if board.is_valid_position(nr,nc):
                t = board.board[nr][nc]
                if not t or t.color != self.color:
                    moves.append((nr,nc))

        return moves


class Bishop(Piece):
    def __init__(self, color, pos):
        super().__init__(color, pos)
        self.symbol = "B"

    def get_valid_moves(self, board):
        moves = []
        r, c = self.position

        for dr, dc in [(1,1),(1,-1),(-1,1),(-1,-1)]:
            for i in range(1,8):
                nr, nc = r + dr*i, c + dc*i
                if not board.is_valid_position(nr,nc):
                    break

                t = board.board[nr][nc]
                if t is None:
                    moves.append((nr,nc))
                else:
                    if t.color != self.color:
                        moves.append((nr,nc))
                    break

        return moves


class Queen(Piece):
    def __init__(self, color, pos):
        super().__init__(color, pos)
        self.symbol = "Q"

    def get_valid_moves(self, board):
        return Rook(self.color, self.position).get_valid_moves(board) + \
               Bishop(self.color, self.position).get_valid_moves(board)


class King(Piece):
    def __init__(self, color, pos):
        super().__init__(color, pos)
        self.symbol = "K"

    def get_valid_moves(self, board):
        moves = []
        r, c = self.position

        for dr in [-1,0,1]:
            for dc in [-1,0,1]:
                if dr == 0 and dc == 0:
                    continue

                nr, nc = r+dr, c+dc
                if board.is_valid_position(nr,nc):
                    t = board.board[nr][nc]
                    if not t or t.color != self.color:
                        moves.append((nr,nc))

        return moves
