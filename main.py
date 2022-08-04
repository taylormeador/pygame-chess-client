import pygame as p
import sys

import api
from game_state import GameState
import setup
import globals


# main function contains setup and game loop
def main():
    p.init()
    p.display.set_caption('Chess 9000')
    screen = p.display.set_mode((globals.BOARD_WIDTH, globals.BOARD_HEIGHT))
    clock = p.time.Clock()
    gs = GameState()
    gs.parse_FEN(globals.START_POSITION)
    square_selected = None
    player_clicks = []
    setup.load_images('standard')  # TODO add config options

    # game loop
    running = True
    while running:
        for e in p.event.get():
            # quit condition
            if e.type == p.QUIT:
                running = False

            # mouse handler
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()  # (x, y) of mouse click position
                col = location[0] // globals.SQ_SIZE  # get column number from location
                row = location[1] // globals.SQ_SIZE  # get row number from location
                if square_selected == gs.board[row][col]:  # if the player selects the same square twice
                    square_selected = None  # deselect
                    player_clicks = []  # clear player_clicks
                else:  # if the player clicks on a piece or empty square
                    square_selected = gs.board[row][col]
                    player_clicks.append(square_selected)  # appends for both 1st or 2nd click
                if len(player_clicks) == 2:  # after second click
                    move = player_clicks[0].get_algebraic() + player_clicks[1].get_algebraic()
                    FEN = gs.FEN + " moves " + move
                    gs.parse_FEN(api.is_legal(FEN))
                    square_selected = None  # deselect
                    player_clicks = []  # clear player_clicks

        gs.draw_board(screen)
        p.display.flip()
        clock.tick(globals.MAX_FPS)

    p.quit()
    sys.exit()


main()
