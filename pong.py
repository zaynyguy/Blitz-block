from graphics import *
import time

WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600

# Set up the game window
win = GraphWin("Pong", WINDOW_WIDTH, WINDOW_HEIGHT)
win.setBackground("black")

# Draw paddles
paddle1 = Rectangle(Point(20, 250), Point(30, 350))  # Left paddle
paddle1.setFill("white")
paddle1.draw(win)

paddle2 = Rectangle(Point(770, 250), Point(780, 350))  # Right paddle
paddle2.setFill("white")
paddle2.draw(win)

# Draw ball
ball = Circle(Point(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2), 10)
ball.setFill("white")
ball.draw(win)

# Initialize scores
score1 = 0
score2 = 0
score_display = Text(Point(WINDOW_WIDTH / 2, 50), f"{score1} - {score2}")
score_display.setTextColor("white")
score_display.setSize(20)
score_display.draw(win)

# Ball velocity
dx, dy = 5, 5

# Game loop
while True:
    # Move the ball
    ball.move(dx, dy)
    ball_center = ball.getCenter()

    # Check for wall collisions (top and bottom)
    if ball_center.getY() <= 10 or ball_center.getY() >= 590:
        dy = -dy

    # Check for paddle collisions
    if (20 <= ball_center.getX() - 5 <= 30 and 
        paddle1.getP1().getY() <= ball_center.getY() <= paddle1.getP2().getY()):
        dx = -dx
        ball.move(10, 0)  # Move ball slightly away to prevent sticking
    if (770 <= ball_center.getX() + 5 <= 780 and 
        paddle2.getP1().getY() <= ball_center.getY() <= paddle2.getP2().getY()):
        dx = -dx
        ball.move(-10, 0)  # Move ball slightly away to prevent sticking

    # Check for scoring
    if ball_center.getX() < 0:  # Right player scores
        score2 += 1
        score_display.setText(f"{score1} - {score2}")
        dx, dy = 5, 5  # Reset velocity
        ball.move(400 - ball_center.getX(), 300 - ball_center.getY())
    elif ball_center.getX() > 800:  # Left player scores
        score1 += 1
        score_display.setText(f"{score1} - {score2}")
        dx, dy = -5, 5  # Reset velocity
        ball.move(400 - ball_center.getX(), 300 - ball_center.getY())

    # Check for winning condition
    if score1 >= 10 or score2 >= 10:
        winner = "Left Player" if score1 >= 10 else "Right Player"
        win_message = Text(Point(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2), f"{winner} Wins!")
        win_message.setTextColor("yellow")
        win_message.setSize(30)
        win_message.draw(win)
        break

    # Paddle movement (use key inputs)
    key = win.checkKey()
    if key == "w" and paddle1.getP1().getY() > 0:
        paddle1.move(0, -20)
    elif key == "s" and paddle1.getP2().getY() < 600:
        paddle1.move(0, 20)
    elif key == "Up" and paddle2.getP1().getY() > 0:
        paddle2.move(0, -20)
    elif key == "Down" and paddle2.getP2().getY() < 600:
        paddle2.move(0, 20)

    time.sleep(0.02)  # Slow down the loop

    # Escape sequence
    if key == 'Escape':
        break

# Wait before closing the window
time.sleep(2)
win.close()
