import pygame as p
import globals

algebraic = [["a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8"],
             ["a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7"],
             ["a6", "b6", "c6", "d6", "e6", "f6", "g6", "h6"],
             ["a5", "b5", "c5", "d5", "e5", "f5", "g5", "h5"],
             ["a4", "b4", "c4", "d4", "e4", "f4", "g4", "h4"],
             ["a3", "b3", "c3", "d3", "e3", "f3", "g3", "h3"],
             ["a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2"],
             ["a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1"]]

fen_to_image_name = {"P": "wP", "N": "wN", "B": "wB", "R": "wR", "Q": "wQ", "K": "wK",
                     "p": "bP", "n": "bN", "b": "bB", "r": "bR", "q": "bQ", "k": "bK"}


# square class for composing board layout
class Square:
    def __init__(self, row, col, piece):
        self.row = row  # 0-7
        self.col = col  # 0-7
        self.piece = piece  # fen piece e.g. white pawn = "P", black queen = "q"
        self.color = "l" if (row % 2 == 0) == (col % 2 == 0) else "d"  # light if row/col are both even/odd else dark
        self.visual_row = row if globals.WHITE_POV else 7 - row  # visual row 0-7
        self.visual_col = col if globals.WHITE_POV else 7 - col  # visual col 0-7
        self.x = self.visual_col * globals.SQ_SIZE  # pygame draw x
        self.y = self.visual_row * globals.SQ_SIZE  # pygame draw y

    def __repr__(self):
        return f"{self.get_algebraic()}: Square({self.row}, {self.col}, {self.piece})"

    def get_location(self):
        location = (self.row, self.col)
        return location

    def get_algebraic(self):
        return algebraic[self.row][self.col]

    def draw_square(self, screen):
        color = globals.LIGHT_SQUARE_COLOR if self.color == "l" else globals.DARK_SQUARE_COLOR
        p.draw.rect(screen, color, p.Rect(self.x, self.y, globals.SQ_SIZE, globals.SQ_SIZE))
        if self.piece != "-":
            screen.blit(globals.IMAGES[fen_to_image_name[self.piece]], p.Rect(self.x, self.y, globals.SQ_SIZE, globals.SQ_SIZE))


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

        self.FEN = ""
        self.color_to_move = ""
        self.castling_rights = ""
        self.en_passant_square = ""
        self.half_moves = ""
        self.full_moves = ""

    # iterate through each square on the board and print it
    def draw_board(self, screen):
        for row in range(8):
            for col in range(8):
                self.board[row][col].draw_square(screen)

    # generate FEN string of current game state
    # TODO rest of FEN string
    def generate_FEN(self):
        FEN = ""
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col].piece
                if piece:
                    FEN += piece.fen_piece
                else:
                    FEN += "1"
            if row != 7:
                FEN += "/"

        return FEN

    # this function will read in a string from the engine API and set the pieces on the board accordingly
    # FEN will be normal format e.g. "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1" is the start position
    def parse_FEN(self, FEN):
        self.FEN = FEN
        FEN = FEN.replace("/", "")
        FEN = FEN.split(" ")

        # loop through pieces and empty squares in fen string
        index = -1
        for char in FEN[0]:
            index += 1
            if index < 64:  # place pieces on board
                if char in globals.FEN_PIECES:
                    # print(f"char: {char} index: {index}")  # debug
                    self.set_piece(char, index)
                elif char in ["1", "2", "3", "4", "5", "6", "7", "8"]:
                    index += int(char) - 1

        # set game state vars
        self.color_to_move = FEN[1]
        self.castling_rights = FEN[2]
        self.en_passant_square = FEN[3]
        self.half_moves = FEN[4]
        self.full_moves = FEN[5]

    # takes a piece (fen str) and index (0-63) and puts it on the approrpiate square
    def set_piece(self, piece, index):
        row = index // 8
        col = index % 8
        self.board[row][col].piece = piece
        # print(f"index: {index} row: {row} col: {col}")  # debug


# initialize squares
# pawns
a2 = Square(6, 0, "-")
b2 = Square(6, 1, "-")
c2 = Square(6, 2, "-")
d2 = Square(6, 3, "-")
e2 = Square(6, 4, "-")
f2 = Square(6, 5, "-")
g2 = Square(6, 6, "-")
h2 = Square(6, 7, "-")
a7 = Square(1, 0, "-")
b7 = Square(1, 1, "-")
c7 = Square(1, 2, "-")
d7 = Square(1, 3, "-")
e7 = Square(1, 4, "-")
f7 = Square(1, 5, "-")
g7 = Square(1, 6, "-")
h7 = Square(1, 7, "-")

# knights
b1 = Square(7, 1, "-")
g1 = Square(7, 6, "-")
b8 = Square(0, 1, "-")
g8 = Square(0, 6, "-")

# bishops
c1 = Square(7, 2, "-")
f1 = Square(7, 5, "-")
c8 = Square(0, 2, "-")
f8 = Square(0, 5, "-")

# rooks
a1 = Square(7, 0, "-")
h1 = Square(7, 7, "-")
a8 = Square(0, 0, "-")
h8 = Square(0, 7, "-")

# queens
d1 = Square(7, 3, "-")
d8 = Square(0, 3, "-")

# kings
e1 = Square(7, 4, "-")
e8 = Square(0, 4, "-")

# empty squares
a3 = Square(5, 0, "-")
b3 = Square(5, 1, "-")
c3 = Square(5, 2, "-")
d3 = Square(5, 3, "-")
e3 = Square(5, 4, "-")
f3 = Square(5, 5, "-")
g3 = Square(5, 6, "-")
h3 = Square(5, 7, "-")

a4 = Square(4, 0, "-")
b4 = Square(4, 1, "-")
c4 = Square(4, 2, "-")
d4 = Square(4, 3, "-")
e4 = Square(4, 4, "-")
f4 = Square(4, 5, "-")
g4 = Square(4, 6, "-")
h4 = Square(4, 7, "-")

a5 = Square(3, 0, "-")
b5 = Square(3, 1, "-")
c5 = Square(3, 2, "-")
d5 = Square(3, 3, "-")
e5 = Square(3, 4, "-")
f5 = Square(3, 5, "-")
g5 = Square(3, 6, "-")
h5 = Square(3, 7, "-")

a6 = Square(2, 0, "-")
b6 = Square(2, 1, "-")
c6 = Square(2, 2, "-")
d6 = Square(2, 3, "-")
e6 = Square(2, 4, "-")
f6 = Square(2, 5, "-")
g6 = Square(2, 6, "-")
h6 = Square(2, 7, "-")

squares_from_locations = {'a8': a8, 'b8': b8, 'c8': c8, 'd8': d8, 'e8': e8, 'f8': f8, 'g8': g8, 'h8': h8,
                          'a7': a7, 'b7': b7, 'c7': c7, 'd7': d7, 'e7': e7, 'f7': f7, 'g7': g7, 'h7': h7,
                          'a6': a6, 'b6': b6, 'c6': c6, 'd6': d6, 'e6': e6, 'f6': f6, 'g6': g6, 'h6': h6,
                          'a5': a5, 'b5': b5, 'c5': c5, 'd5': d5, 'e5': e5, 'f5': f5, 'g5': g5, 'h5': h5,
                          'a4': a4, 'b4': b4, 'c4': c4, 'd4': d4, 'e4': e4, 'f4': f4, 'g4': g4, 'h4': h4,
                          'a3': a3, 'b3': b3, 'c3': c3, 'd3': d3, 'e3': e3, 'f3': f3, 'g3': g3, 'h3': h3,
                          'a2': a2, 'b2': b2, 'c2': c2, 'd2': d2, 'e2': e2, 'f2': f2, 'g2': g2, 'h2': h2,
                          'a1': a1, 'b1': b1, 'c1': c2, 'd1': d3, 'e1': e4, 'f1': f1, 'g1': g1, 'h1': h1}
