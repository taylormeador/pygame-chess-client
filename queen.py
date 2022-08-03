class Queen:
    def __init__(self, color, row, col):
        self.color = color
        self.piece_type = 'Q'
        self.name = self.color + self.piece_type
        self.fen_piece = 'Q' if color == "w" else 'q'
        self.row = row
        self.col = col

    def __str__(self):
        return self.name

    def location(self):
        location = (self.row, self.col)
        return location


# initialize queens
d1 = Queen("w", 7, 3)

d8 = Queen("b", 0, 3)
