from settings import *
from multi import *
from single import *


def game():

    # Set up the game window
    win = GraphWin("Center Target Game", WINDOW_WIDTH, WINDOW_HEIGHT)
    win.setBackground("black")
    single(win, True)

    # Wait before closing the window
    time.sleep(1)
    win.close()


game()
