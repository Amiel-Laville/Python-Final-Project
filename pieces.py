"""
Piece definitions and movement logic for chess
"""

class Piece:
    """Base class for chess pieces"""
    def __init__(self, color, position):
        self.color = color  # 'white' or 'black'
        self.position = position  # (row, col)
        self.symbol = '?'
        
    def get_valid_moves(self, board):
        """Override in subclasses to return list of valid moves"""
        return []
    
    def __repr__(self):
        return f"{self.color[0].upper()}{self.symbol}"


class Pawn(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.symbol = 'P'
        self.has_moved = False
        
    def get_valid_moves(self, board):
        moves = []
        row, col = self.position
        direction = -1 if self.color == 'white' else 1
        start_row = 6 if self.color == 'white' else 1
        
        # Forward move
        new_row = row + direction
        if 0 <= new_row < 8:
            if board.is_empty(new_row, col):
                moves.append((new_row, col))
                # Double move from start
                if row == start_row and board.is_empty(row + 2*direction, col):
                    moves.append((row + 2*direction, col))
        
        # Captures
        for col_offset in [-1, 1]:
            new_col = col + col_offset
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                target = board.get_piece(new_row, new_col)
                if target and target.color != self.color:
                    moves.append((new_row, new_col))
        
        return moves


class Rook(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.symbol = 'R'
        
    def get_valid_moves(self, board):
        moves = []
        row, col = self.position
        
        # Horizontal and vertical directions
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            for i in range(1, 8):
                new_row, new_col = row + dr*i, col + dc*i
                if not (0 <= new_row < 8 and 0 <= new_col < 8):
                    break
                
                target = board.get_piece(new_row, new_col)
                if target is None:
                    moves.append((new_row, new_col))
                elif target.color != self.color:
                    moves.append((new_row, new_col))
                    break
                else:
                    break
        
        return moves


class Knight(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.symbol = 'N'
        
    def get_valid_moves(self, board):
        moves = []
        row, col = self.position
        
        for dr, dc in [(2, 1), (2, -1), (-2, 1), (-2, -1),
                       (1, 2), (1, -2), (-1, 2), (-1, -2)]:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                target = board.get_piece(new_row, new_col)
                if target is None or target.color != self.color:
                    moves.append((new_row, new_col))
        
        return moves


class Bishop(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.symbol = 'B'
        
    def get_valid_moves(self, board):
        moves = []
        row, col = self.position
        
        # Diagonal directions
        for dr, dc in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
            for i in range(1, 8):
                new_row, new_col = row + dr*i, col + dc*i
                if not (0 <= new_row < 8 and 0 <= new_col < 8):
                    break
                
                target = board.get_piece(new_row, new_col)
                if target is None:
                    moves.append((new_row, new_col))
                elif target.color != self.color:
                    moves.append((new_row, new_col))
                    break
                else:
                    break
        
        return moves


class Queen(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.symbol = 'Q'
        
    def get_valid_moves(self, board):
        moves = []
        row, col = self.position
        
        # All 8 directions
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0),
                       (1, 1), (1, -1), (-1, 1), (-1, -1)]:
            for i in range(1, 8):
                new_row, new_col = row + dr*i, col + dc*i
                if not (0 <= new_row < 8 and 0 <= new_col < 8):
                    break
                
                target = board.get_piece(new_row, new_col)
                if target is None:
                    moves.append((new_row, new_col))
                elif target.color != self.color:
                    moves.append((new_row, new_col))
                    break
                else:
                    break
        
        return moves


class King(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.symbol = 'K'
        
    def get_valid_moves(self, board):
        moves = []
        row, col = self.position
        
        # One square in any direction
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < 8 and 0 <= new_col < 8:
                    target = board.get_piece(new_row, new_col)
                    if target is None or target.color != self.color:
                        moves.append((new_row, new_col))
        
        return moves
