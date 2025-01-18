from settings import *



def about(win):
    print('here')
    title = Text(Point(WINDOW_WIDTH / 4, WINDOW_HEIGHT / 4), f"Group members")
    title.setTextColor("white")
    title.setFace('Press Start 2P')
    title.setSize(18)
    title.draw(win)


    description = Text(Point(WINDOW_WIDTH / 3 + 30, WINDOW_HEIGHT / 3 + 30),
'''1, Ahmed Jabir           863/13
2, Akrem Mohammed        866/13
3, Akrem Ibrahim         865/13
4, Dagim Solomon         880/13
5, Sebri Shehab          908/13''')

    description.setTextColor("darkgray")
    description.setFace('Press Start 2P')
    description.setSize(12)
    description.draw(win)


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