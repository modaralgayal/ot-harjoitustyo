from main import main
from menu_main import menu_main
from values import values

# Run everything here form a function
# Call the function in the if __name__ == "__main__":
# Use the grid value to initialize all needed lists (game_situation, game_board; jne...)
# in a seperate module, after that give them to the the main module for initializing.
# All this for going back and forth in between the game and the menu,


# In the gameloop, make a seperate funciton for winning conditoins, (if "winning_condition"): return True(?)
# Add winning animation and make the game stop.


def run():

    grid = menu_main()
    display, grid, height, width, game_board, game_situation, places_on_board, click_ranges = values(
        grid)

    main(display, grid, height, width, game_board,
         game_situation, places_on_board, click_ranges)


if __name__ == "__main__":
    run()
