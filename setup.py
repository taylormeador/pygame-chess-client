import pygame as p
import globals


def load_images(piece_set):
    pieces = ["wP", "wN", "wB", "wR", "wQ", "wK", "bP", "bN", "bB", "bR", "bQ", "bK"]
    for piece in pieces:
        path = "./images/" + piece_set + "/" + piece + ".png"
        globals.IMAGES[piece] = p.transform.scale(p.image.load(path), (globals.SQ_SIZE, globals.SQ_SIZE))
