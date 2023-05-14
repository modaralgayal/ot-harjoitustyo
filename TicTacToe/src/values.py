def values(grid):

    places_on_board = []
    click_ranges = []
    _x = 60
    _y = 85
    for level in range(grid):
        for column in range(grid):
            click_ranges.append(((column*70+_x, column*70+_x+70),
                                (level*90+_y, level*90+_y+90), (level, column)))
            places_on_board.append((column*70+_x, level*90+_y))

    return grid, places_on_board, click_ranges
