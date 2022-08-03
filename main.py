import pygame as p
import sys
from game_state import GameState

# init pygame and constants
p.init()
BOARD_WIDTH = BOARD_HEIGHT = 512
DIMENSION = 8
SQ_SIZE = BOARD_HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}

def load_images(piece_set):
    pieces = ['wP', 'wN', 'wB', 'wR', 'wQ', 'wK', 'bP', 'bN', 'bB', 'bR', 'bQ', 'bK']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load('images/' + piece_set + '/' + piece + '.png'), (SQ_SIZE, SQ_SIZE))


# main function contains setup and game loop
def main():
    p.display.set_caption('Chess 9000')
    screen = p.display.set_mode((BOARD_WIDTH, BOARD_HEIGHT))
    clock = p.time.Clock()
    gs = GameState()
    load_images('standard')

    # game loop
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False

        gs.draw_board(screen)

        p.display.flip()
        clock.tick(MAX_FPS)

    p.quit()  # quits pygame
    sys.exit()


main()
