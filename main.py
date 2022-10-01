import pygame as p
import sys

import api
from game_state import GameState
import setup
import globals
import time

game_config = setup.Config()

# loop that allows player to choose settings before beginning game
def config():
    p.init()
    p.display.set_caption('Chess 9000')
    screen = p.display.set_mode((globals.BOARD_WIDTH, globals.BOARD_HEIGHT))
    start_button_enable = False
    running = True
    while running:
        screen.fill(p.Color("black"))
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False

            # mouse handler
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()  # (x, y) of mouse click position
                for button in setup.buttons:
                    if button.button_rect.collidepoint(location):  # press the button
                        button.selected = not button.selected
                        for time_button in setup.time_buttons:  # deselect other time control buttons
                            if button in setup.time_buttons and button != time_button:
                                time_button.selected = False
                        for color_button in setup.piece_color_buttons:  # deselect other color button
                            if button in setup.piece_color_buttons and button != color_button:
                                color_button.selected = False
                        for light_color_button in setup.light_color_buttons:  # deselect other color button
                            if button in setup.light_color_buttons and button != light_color_button:
                                light_color_button.selected = False
                        for dark_color_button in setup.dark_color_buttons:  # deselect other color button
                            if button in setup.dark_color_buttons and button != dark_color_button:
                                dark_color_button.selected = False
                        if not start_button_enable:  # don't allow game to start until valid choices are made
                            setup.start_button.selected = False

        # draw buttons
        for button in setup.buttons:
            button.draw_button(screen)

        # don't let user start game without setting up
        if (setup.white_select_button.selected or setup.black_select_button.selected) and \
                (setup.time_3_0_button.selected or setup.time_3_2_button.selected or setup.time_5_0_button.selected):
            start_button_enable = True

        # set selected config vars
        game_config.white_is_human = True if setup.white_select_button.selected else False
        game_config.black_is_human = True if setup.black_select_button.selected else False
        game_config.time_control = 300 if setup.time_5_0_button.selected else 180
        game_config.increment = 2 if setup.time_3_2_button.selected else 0
        for button in setup.light_color_buttons:
            if button.selected:
                game_config.light_square_color = p.Color(button.button_text)
        for button in setup.dark_color_buttons:
            if button.selected:
                game_config.dark_square_color = p.Color(button.button_text)

        # call the main game loop once the start button is enabled and pressed
        if setup.start_button.selected:
            game_config.set_config()
            main()

        p.display.flip()
    main()


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
    player_turn = game_config.white_is_human  # True or False depending on if it is the player's turn to move

    # game loop
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False

            # mouse handler
            elif e.type == p.MOUSEBUTTONDOWN:
                if player_turn:
                    location = p.mouse.get_pos()  # (x, y) of mouse click position
                    col = location[0] // globals.SQ_SIZE  # get column number from location
                    row = location[1] // globals.SQ_SIZE  # get row number from location
                    if square_selected == gs.board[row][col]:  # if the player selects the same square twice
                        square_selected = None  # deselect
                        gs.board[row][col].highlight = False  # remove highlight
                        player_clicks = []  # clear player_clicks
                    else:  # if the player clicks on a piece or empty square
                        square_selected = gs.board[row][col]
                        # append second click if it's not player's own piece
                        if len(player_clicks) == 1 and (square_selected.piece not in globals.FEN_PIECES[0:6] and gs.color_to_move == "w") or \
                                (square_selected.piece not in globals.FEN_PIECES[6:12] and gs.color_to_move == "b"):
                            player_clicks.append(square_selected)
                        # only want to count the click if it's on an ally piece
                        if (square_selected.piece in globals.FEN_PIECES[0:6] and gs.color_to_move == "w") or \
                                (square_selected.piece in globals.FEN_PIECES[6:12] and gs.color_to_move == "b"):
                            square_selected.highlight = True
                            player_clicks.append(square_selected)  # only append first click for valid piece
                    if len(player_clicks) == 2:  # after second click
                        move = player_clicks[0].get_algebraic() + player_clicks[1].get_algebraic()
                        FEN = gs.FEN + " moves " + move
                        newFEN = api.is_legal(FEN)
                        gs.parse_FEN(newFEN)
                        player_clicks[0].highlight, player_clicks[1].highlight = False, False
                        square_selected = None  # deselect
                        player_clicks = []  # clear player_clicks

        gs.draw_board(screen)
        p.display.flip()
        clock.tick(globals.MAX_FPS)

        if not player_turn:
            newFEN = api.best_move(gs.FEN)
            time.sleep(1)
            gs.parse_FEN(newFEN)
        player_turn = True if ((gs.color_to_move == "w" and game_config.white_is_human) or (
                    gs.color_to_move == "b" and game_config.black_is_human)) else False

    p.quit()
    sys.exit()


config()
