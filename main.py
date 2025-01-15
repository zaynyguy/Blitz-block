from settings import *
from multi import *
from single import *
from start import *
from about import *
from play import *


def game():

    # Set up the game window
    win = GraphWin("Center Target Game", WINDOW_WIDTH, WINDOW_HEIGHT)
    win.setBackground("light gray")
    menus = {0: single, 1: multi, 2: about}

    exit = 1
    while True:
        if exit:
            #start screen
            load = start(win)
            #load menus
            if load == 3:
                break
            if load == 0:
                mode = game_style_menu(win)
                if mode == 0:
                    exit = single(win)
                elif mode == 1:
                    exit = multi(win)
                elif mode == 2:
                   exit = play(win)
            else:    
                exit = menus[load](win)
            clear_window(win)
        else:
            break


    # Wait before closing the window
    win.close()


game()
