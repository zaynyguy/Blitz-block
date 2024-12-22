from settings import *
from multi import *
from single import *
from start import *


def game():

    # Set up the game window
    win = GraphWin("Center Target Game", WINDOW_WIDTH, WINDOW_HEIGHT)
    win.setBackground("black")
    menus = {0: single, 1: multi}
    #start screen
    load = start(win)

    #load menus
    menus[load](win)

    # Wait before closing the window
    time.sleep(1)
    win.close()


game()
