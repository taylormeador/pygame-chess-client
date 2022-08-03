import pygame as p
import sys
import requests

# init pygame and constants
p.init()
BOARD_WIDTH = BOARD_HEIGHT = 512
DIMENSION = 8
SQ_SIZE = BOARD_HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}

# main function contains setup and game loop
def main():
    p.display.set_caption('Chess')
    screen = p.display.set_mode((BOARD_WIDTH, BOARD_HEIGHT))
    clock = p.time.Clock()

    # game loop
    running = False
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False

        p.display.flip()
        clock.tick(MAX_FPS)

    p.quit()  # quits pygame
    sys.exit()


main()
