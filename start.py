from graphics import *
import time

WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600

def start():
    
    win = GraphWin("Center Target Game", WINDOW_WIDTH, WINDOW_HEIGHT)
    win.setBackground("black")

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

        if click or key:
            x = click.getX()
            y = click.getY()

            if 330 < x < 470 and 330 < y < 360: # for play
                print('this is play')
                
            elif 330 < x < 470 and 370 < y < 400: # for multiplayer
                print('this is mulit')
                
            elif 330 < x < 470 and 410 < y < 440: # for about
                print('this is about')
                
            elif 330 < x < 470 and 450 < y < 480 or 'Escape': # for quit
                print('this is quit')
                break
            

        time.sleep(1)

    win.close()

start()