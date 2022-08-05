import pygame as p
import globals

# loads images into dict
def load_images(piece_set):
    pieces = ["wP", "wN", "wB", "wR", "wQ", "wK", "bP", "bN", "bB", "bR", "bQ", "bK"]
    for piece in pieces:
        path = "./images/" + piece_set + "/" + piece + ".png"
        globals.IMAGES[piece] = p.transform.scale(p.image.load(path), (globals.SQ_SIZE, globals.SQ_SIZE))

# custom class for storing game config variables
class Config:
    def __init__(self):
        self.white_is_human = None
        self.black_is_human = None
        self.light_square_color = None
        self.dark_square_color = None
        self.time_control = None
        self.increment = None

    def set_config(self):
        globals.WHITE_POV = self.white_is_human
        globals.LIGHT_SQUARE_COLOR = self.light_square_color
        globals.DARK_SQUARE_COLOR = self.dark_square_color
        globals.TIME_CONTROL = self.time_control
        globals.INCREMENT = self.increment


class Button:
    def __init__(self, button_text, button_location, button_width):
        self.button_text = button_text
        self.button_location = button_location
        self.button_width = button_width
        self.button_height = 35
        self.button_rect = p.Rect(self.button_location[0], self.button_location[1], self.button_width, self.button_height)
        self.selected = False
        self.selected_color = p.Color("cyan")

    def draw_button(self, screen):
        # draw the rectangle
        color = self.selected_color if self.selected else p.Color("white")
        p.draw.rect(screen, color, self.button_rect)

        # draw the text
        font = p.font.SysFont("Helvetica", 20, False, False)
        text_object = font.render(self.button_text, 1, p.Color("Black"))
        text_location = (self.button_location[0] + self.button_width//6, self.button_location[1] + self.button_height//6)
        screen.blit(text_object, text_location)


start_button = Button("Start Game", (globals.BOARD_WIDTH - 200, globals.BOARD_HEIGHT - 50), 150)
white_select_button = Button("White", (25, 25), 75)
black_select_button = Button("Black", (25, 75), 75)
time_3_0_button = Button("3+0", (150, 25), 60)
time_3_2_button = Button("3+2", (150, 75), 60)
time_5_0_button = Button("5+0", (150, 125), 60)
white_button = Button("White", (250, 25), 85)
beige_button = Button("Beige", (250, 75), 85)
ivory_button = Button("Ivory", (250, 125), 85)
gray_button = Button("Gray", (350, 25), 85)
dark_gray_button = Button("Dark Gray", (350, 75), 125)
green_button = Button("Dark Green", (350, 125), 150)

buttons = [start_button, white_select_button, black_select_button, time_3_0_button, time_3_2_button, time_5_0_button, white_button, beige_button, ivory_button, gray_button, dark_gray_button, green_button]
time_buttons = [time_3_0_button, time_3_2_button, time_5_0_button]
piece_color_buttons = [white_select_button, black_select_button]
light_color_buttons = [white_button, beige_button, ivory_button]
dark_color_buttons = [gray_button, dark_gray_button, green_button]
