class Pawn:
    def __init__(self, color, row, col):
        self.color = color
        self.piece_type = 'P'
        self.name = self.color + self.piece_type
        self.row = row
        self.col = col

    def __str__(self):
        return self.name

    def location(self):
        location = (self.row, self.col)
        return location


# initialize pawns
a7 = Pawn("b", 1, 0)
b7 = Pawn("b", 1, 1)
c7 = Pawn("b", 1, 2)
d7 = Pawn("b", 1, 3)
e7 = Pawn("b", 1, 4)
f7 = Pawn("b", 1, 5)
g7 = Pawn("b", 1, 6)
h7 = Pawn("b", 1, 7)

a2 = Pawn("w", 6, 0)
b2 = Pawn("w", 6, 1)
c2 = Pawn("w", 6, 2)
d2 = Pawn("w", 6, 3)
e2 = Pawn("w", 6, 4)
f2 = Pawn("w", 6, 5)
g2 = Pawn("w", 6, 6)
h2 = Pawn("w", 6, 7)
