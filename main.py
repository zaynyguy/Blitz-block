from settings import *
from multi import *
from single import *


def game():

    # Set up the game window
    win = GraphWin("Center Target Game", WINDOW_WIDTH, WINDOW_HEIGHT)
    win.setBackground("black")
<<<<<<< HEAD
    single(win, True)
    
=======
    single(win, True)

>>>>>>> e243e51a73b8f6d9171d87ca33a4f03f7ec94f6f
    # Wait before closing the window
    time.sleep(1)
    win.close()


game()
