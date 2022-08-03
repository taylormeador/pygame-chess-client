import pygame as p
import sys
from game_state import GameState
import setup
import globals

# init pygame and constants
p.init()

# main function contains setup and game loop
def main():
    p.display.set_caption('Chess 9000')
    screen = p.display.set_mode((globals.BOARD_WIDTH, globals.BOARD_HEIGHT))
    clock = p.time.Clock()
    gs = GameState()
    setup.load_images('standard')

    # game loop
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False

        gs.draw_board(screen)

        p.display.flip()
        clock.tick(globals.MAX_FPS)

    p.quit()  # quits pygame
    sys.exit()


main()
