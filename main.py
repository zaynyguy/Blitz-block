from settings import *
from multi import *
from single import *
from start import *
from about import *


def game():

    # Set up the game window
    win = GraphWin("Center Target Game", WINDOW_WIDTH, WINDOW_HEIGHT)
    win.setBackground("black")
    menus = {0: single, 1: multi, 2: about}

    exit = 1
    while True:
        if exit:
            #start screen
            load = start(win)
            #load menus
            if load == 3:
                break
            exit = menus[load](win)
            clear_window(win)
        else:
            break


    # Wait before closing the window
    win.close()


game()
