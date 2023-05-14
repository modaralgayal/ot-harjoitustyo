import sys
from main import main
from menu_main import menu_main
from values import values


# Run everything here form a function (Done)
# Call the function in the if __name__ == "__main__": (DOne)
# Use the grid value to initialize all needed lists (game_situation, game_board; jne...) (Done)
# in a seperate module, after that give them to the the main module for initializing.
# All this for going back and forth in between the game and the menu. (Done)


# In the gameloop, make a seperate funciton for winning conditoins,
#  (if "winning_condition"): return True(?) (Done)
# Add winning animation and make the game stop.

def run():
    grid = menu_main()
    if grid is None:
        sys.exit()
    grid, places_on_board, click_ranges = values(grid)

    main_result = main(grid, places_on_board, click_ranges)
    if main_result == "GoBack":
        return "Restart"

    return None


if __name__ == "__main__":
    while run() == "Restart":
        run()
