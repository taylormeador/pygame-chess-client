import globals

def click_col_row(location):
    col = location[0] // globals.SQ_SIZE
    row = location[1] // globals.SQ_SIZE
    if not globals.WHITE_POV:
        col = 7 - col
        row = 7 - row
    return col, row
