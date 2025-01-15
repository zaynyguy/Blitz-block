from graphics import *
import time
import math
import random


WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600


# Used to clear the window from any graphical items
def clear_window(win):
    for item in win.items[:]:  
        item.undraw()          
    win.update()               

 


# Used to create a rectangular button
class Button:
    def __init__(self, win, center, width, height, label):

        self.win = win
        self.center = center
        self.width = width
        self.height = height
        self.label = label
        
        # Calculate corners of the rectangle
        x, y = center.getX(), center.getY()
        self.rect = Rectangle(Point(x - width / 2, y - height / 2),
                              Point(x + width / 2, y + height / 2))
        self.rect.setFill("white")  # Default background color
        self.rect.setOutline("gold")
        self.rect.draw(win)

        # Add text to the button
        self.text = Text(center, label)
        self.text.setSize(12)
        self.text.draw(win)

    def is_clicked(self, point):

        x1, y1 = self.rect.getP1().getX(), self.rect.getP1().getY()
        x2, y2 = self.rect.getP2().getX(), self.rect.getP2().getY()
        return x1 <= point.getX() <= x2 and y1 <= point.getY() <= y2

    def set_color(self, color):
        self.rect.setFill(color)

    def set_label(self, new_label):
        self.text.setText(new_label)

    def undraw(self):
        self.rect.undraw()
        self.text.undraw()
    


# Used to create titles in the middle of the screen 
def message_menu(message, win):
    win_message = Text(Point(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2), f"{message}")
    win_message.setTextColor("white")
    win_message.setFace('Press Start 2P')
    win_message.setSize(30)
    win_message.draw(win)

    time.sleep(1)

    menu_button = Button(win, Point(300,400), 100, 50, 'Main menu')
    quit_button = Button(win, Point(500,400), 50, 50, 'Quit!')

    exit_value = 1

    while True:

        point = win.getMouse()

        if quit_button.is_clicked(point):
            exit_value = 0
            break
        if menu_button.is_clicked(point):
            exit_value = 1
            break

    return exit_value

def game_style_menu(win):
    win_message = Text(Point(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2), f"Choose game")
    win_message.setTextColor("white")
    win_message.setFace('Press Start 2P')
    win_message.setSize(30)
    win_message.draw(win)

    breaker = Button(win, Point(250,400), 100, 30, 'Breaker')
    multi = Button(win, Point(400,400), 100, 30, 'Pong')
    play = Button(win, Point(550,400), 100, 30, 'Blitz')

    point = win.getMouse()

    if breaker.is_clicked(point):
        clear_window(win)
        return 0
    if multi.is_clicked(point):
        clear_window(win)
        return 1
    if play.is_clicked(point):
        clear_window(win)
        return 2



