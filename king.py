class King:
    def __init__(self, color, row, col):
        self.color = color
        self.piece_type = 'K'
        self.name = self.color + self.piece_type
        self.fen_piece = 'K' if color == "w" else 'k'
        self.row = row
        self.col = col

    def __str__(self):
        return self.name

    def location(self):
        location = (self.row, self.col)
        return location


# initialize kings
e1 = King("w", 7, 4)

e8 = King("b", 0, 4)
