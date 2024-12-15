from settings import *
from blitz_block import *

def game():

    # Set up the game window
    win = GraphWin("Center Target Game", WINDOW_WIDTH, WINDOW_HEIGHT)
    win.setBackground("black")
    blitz(win)
    
    # Wait before closing the window
    time.sleep(2)
    win.close()

game()

        

