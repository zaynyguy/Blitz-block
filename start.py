from graphics import *
from settings import *
import time


def start(win):
    
    title = Text(Point(400, WINDOW_HEIGHT/3), 'Biliz Block')
    title.setSize(100)
    title.setStyle('bold')
    title.setTextColor('white')

    play = Rectangle(Point(330, 330), Point(470, 360))
    play.setFill('white')
    play.setOutline('white')
    
    multi = Rectangle(Point(330, 370), Point(470, 400))
    multi.setFill('white')
    multi.setOutline('white')
    
    about = Rectangle(Point(330, 410), Point(470, 440))
    about.setFill('white')
    about.setOutline('white')
   
    quit = Rectangle(Point(330, 450), Point(470, 480))
    quit.setFill('white')
    quit.setOutline('white')

    play_text = Text(Point(400, 345), 'Play')    
    multi_text = Text(Point(400, 385), 'Multiplayer')    
    about_text = Text(Point(400, 425), 'About')    
    quit_text = Text(Point(400, 465), 'Quit')

    play_text.setStyle('bold')    
    multi_text.setStyle('bold') 
    about_text.setStyle('bold')   
    quit_text.setStyle('bold')

    title.draw(win)
    play.draw(win)
    multi.draw(win)
    about.draw(win)
    quit.draw(win)
    play_text.draw(win)
    multi_text.draw(win)   
    about_text.draw(win)
    quit_text.draw(win)

    while True:
        key = win.checkKey()
        click = win.checkMouse()

        if click:
            x = click.getX()
            y = click.getY()

            if 330 < x < 470 and 330 < y < 360: # for play
                clear_window(win)
                return 0
                
            elif 330 < x < 470 and 370 < y < 400: # for multiplayer
                clear_window(win)
                return 1
                
            elif 330 < x < 470 and 410 < y < 440: # for about
                clear_window(win)
                return 2
                
            elif 330 < x < 470 and 450 < y < 480 : # for quit
                clear_window(win)
                return 3
        if key:
            if key == 'Escape':
                clear_window(win)
                return 3
            
        # def undraw_all():
        #     title.undraw()
        #     play.undraw()
        #     multi.undraw()
        #     about.undraw()
        #     quit.undraw()
        #     play_text.undraw()
        #     multi_text.undraw()   
        #     about_text.undraw()
        #     quit_text.undraw()

        time.sleep(1)

    win.close()
