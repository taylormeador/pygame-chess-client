class Bishop:
    def __init__(self, color, row, col):
        self.color = color  # 'w' or 'b'
        self.piece_type = 'B'  # bishop
        self.name = self.color + self.piece_type  # e.g.'wB'
        self.fen_piece = 'B' if color == "w" else 'b'
        self.row = row  # 0-7
        self.col = col  # 0-7

    def __str__(self):
        return self.name

    def location(self):
        location = (self.row, self.col)
        return location


# initialize bishops
c1 = Bishop("w", 7, 2)
f1 = Bishop("w", 7, 5)

c8 = Bishop("b", 0, 2)
f8 = Bishop("b", 0, 5)
