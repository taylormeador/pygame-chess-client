class Knight:
    def __init__(self, color, row, col):
        self.color = color
        self.piece_type = 'N'
        self.name = self.color + self.piece_type
        self.row = row
        self.col = col
        self.is_attacking = []

    def __str__(self):
        return self.name

    def location(self):
        location = (self.row, self.col)
        return location


# initialize knights
b1 = Knight("w", 7, 1)
g1 = Knight("w", 7, 6)

b8 = Knight("b", 0, 1)
g8 = Knight("b", 0, 6)
