class Rook:
    def __init__(self, color, row, col):
        self.color = color  # 'w' or 'b'
        self.piece_type = 'R'
        self.name = self.color + self.piece_type  # e.g. 'wR'
        self.row = row  # 0-7
        self.col = col  # 0-7
        self.is_attacking = []  # list of square location a piece attacks [(0, 1), (1, 0), etc]
        self.first_move = True  # helps determine castling rights

    def __str__(self):
        return self.name  # 'wR' or 'bR'

    def location(self):
        location = (self.row, self.col)
        return location  # (3, 4)


# initialize rooks
a1 = Rook("w", 7, 0)
h1 = Rook("w", 7, 7)

a8 = Rook("b", 0, 0)
h8 = Rook("b", 0, 7)
