import pygame as p
import pawn
import knight
import bishop
import rook
import queen
import king

SQ_SIZE = 64
white_pov = True
light_square_color = "ivory"  # TODO more colors
dark_square_color = "dark green"

# square class for composing board layout
class Square:
    def __init__(self, row, col, piece):
        self.row = row  # 0-7
        self.col = col  # 0-7
        self.piece = piece  # piece object instance
        self.color = "l" if (row % 2 == 0) == (col % 2 == 0) else "d"  # light if row/col are both even/odd else dark
        self.visual_row = row if white_pov else 7 - row  # visual row 0-7
        self.visual_col = col if white_pov else 7 - row  # visual col 0-7
        self.x = self.visual_col * SQ_SIZE  # pygame draw x
        self.y = self.visual_row * SQ_SIZE  # pygame draw y

    def __repr__(self):
        return f"Square({self.row}, {self.col}, {self.piece}"

    def location(self):
        location = (self.row, self.col)
        return location

    def draw_square(self, screen):
        from main import IMAGES
        color = light_square_color if self.color == "l" else dark_square_color
        p.draw.rect(screen, color, p.Rect(self.x, self.y, SQ_SIZE, SQ_SIZE))
        if self.piece != 0:
            screen.blit(IMAGES[str(self.piece)], p.Rect(self.x, self.y, SQ_SIZE, SQ_SIZE))


class GameState:
    def __init__(self):
        # the board will always be represented internally with white being at the bottom of the board
        self.board = [[a8, b8, c8, d8, e8, f8, g8, h8],
                      [a7, b7, c7, d7, e7, f7, g7, h7],
                      [a6, b6, c6, d6, e6, f6, g6, h6],
                      [a5, b5, c5, d5, e5, f5, g5, h5],
                      [a4, b4, c4, d4, e4, f4, g4, h4],
                      [a3, b3, c3, d3, e3, f3, g3, h3],
                      [a2, b2, c2, d2, e2, f2, g2, h2],
                      [a1, b1, c1, d1, e1, f1, g1, h1]]
        self.ally_color = 'w'  # white
        self.enemy_color = 'b'  # black

    # iterate through each square on the board and print it
    def draw_board(self, screen):
        for row in range(8):
            for col in range(8):
                self.board[row][col].draw_square(screen)


# initialize squares
# pawns
a2 = Square(6, 0, pawn.a2)
b2 = Square(6, 1, pawn.b2)
c2 = Square(6, 2, pawn.c2)
d2 = Square(6, 3, pawn.d2)
e2 = Square(6, 4, pawn.e2)
f2 = Square(6, 5, pawn.f2)
g2 = Square(6, 6, pawn.g2)
h2 = Square(6, 7, pawn.h2)
a7 = Square(1, 0, pawn.a7)
b7 = Square(1, 1, pawn.b7)
c7 = Square(1, 2, pawn.c7)
d7 = Square(1, 3, pawn.d7)
e7 = Square(1, 4, pawn.e7)
f7 = Square(1, 5, pawn.f7)
g7 = Square(1, 6, pawn.g7)
h7 = Square(1, 7, pawn.h7)

# knights
b1 = Square(7, 1, knight.b1)
g1 = Square(7, 6, knight.g1)
b8 = Square(0, 1, knight.b8)
g8 = Square(0, 6, knight.g8)

# bishops
c1 = Square(7, 2, bishop.c1)
f1 = Square(7, 5, bishop.f1)
c8 = Square(0, 2, bishop.c8)
f8 = Square(0, 5, bishop.f8)

# rooks
a1 = Square(7, 0, rook.a1)
h1 = Square(7, 7, rook.h1)
a8 = Square(0, 0, rook.a8)
h8 = Square(0, 7, rook.h8)

# queens
d1 = Square(7, 3, queen.d1)
d8 = Square(0, 3, queen.d8)

# kings
e1 = Square(7, 4, king.e1)
e8 = Square(0, 4, king.e8)

# empty squares
a3 = Square(5, 0, 0)
b3 = Square(5, 1, 0)
c3 = Square(5, 2, 0)
d3 = Square(5, 3, 0)
e3 = Square(5, 4, 0)
f3 = Square(5, 5, 0)
g3 = Square(5, 6, 0)
h3 = Square(5, 7, 0)

a4 = Square(4, 0, 0)
b4 = Square(4, 1, 0)
c4 = Square(4, 2, 0)
d4 = Square(4, 3, 0)
e4 = Square(4, 4, 0)
f4 = Square(4, 5, 0)
g4 = Square(4, 6, 0)
h4 = Square(4, 7, 0)

a5 = Square(3, 0, 0)
b5 = Square(3, 1, 0)
c5 = Square(3, 2, 0)
d5 = Square(3, 3, 0)
e5 = Square(3, 4, 0)
f5 = Square(3, 5, 0)
g5 = Square(3, 6, 0)
h5 = Square(3, 7, 0)

a6 = Square(2, 0, 0)
b6 = Square(2, 1, 0)
c6 = Square(2, 2, 0)
d6 = Square(2, 3, 0)
e6 = Square(2, 4, 0)
f6 = Square(2, 5, 0)
g6 = Square(2, 6, 0)
h6 = Square(2, 7, 0)

squares_from_locations = {'a8': a8, 'b8': b8, 'c8': c8, 'd8': d8, 'e8': e8, 'f8': f8, 'g8': g8, 'h8': h8,
                          'a7': a7, 'b7': b7, 'c7': c7, 'd7': d7, 'e7': e7, 'f7': f7, 'g7': g7, 'h7': h7,
                          'a6': a6, 'b6': b6, 'c6': c6, 'd6': d6, 'e6': e6, 'f6': f6, 'g6': g6, 'h6': h6,
                          'a5': a5, 'b5': b5, 'c5': c5, 'd5': d5, 'e5': e5, 'f5': f5, 'g5': g5, 'h5': h5,
                          'a4': a4, 'b4': b4, 'c4': c4, 'd4': d4, 'e4': e4, 'f4': f4, 'g4': g4, 'h4': h4,
                          'a3': a3, 'b3': b3, 'c3': c3, 'd3': d3, 'e3': e3, 'f3': f3, 'g3': g3, 'h3': h3,
                          'a2': a2, 'b2': b2, 'c2': c2, 'd2': d2, 'e2': e2, 'f2': f2, 'g2': g2, 'h2': h2,
                          'a1': a1, 'b1': b1, 'c1': c2, 'd1': d3, 'e1': e4, 'f1': f1, 'g1': g1, 'h1': h1}
