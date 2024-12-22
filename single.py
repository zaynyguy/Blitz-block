from settings import *


def single(win):

    # Draw the paddle
    paddle = Rectangle(Point(WINDOW_WIDTH / 2 - 50, WINDOW_HEIGHT - 30),
                       Point(WINDOW_WIDTH / 2 + 50, WINDOW_HEIGHT - 20))
    paddle.setFill('white')
    paddle.draw(win)

    # Draw ball
    ball_start_x = WINDOW_WIDTH / 2
    ball_start_y = WINDOW_HEIGHT / 2 + 50
    ball_radius = 10
    ball = Circle(Point(ball_start_x, ball_start_y), ball_radius)
    ball.setFill("white")
    ball.draw(win)

    # Draw a target to hit 
    taget_start_x = WINDOW_WIDTH / 2
    taget_start_y = WINDOW_HEIGHT / 2 - 50
    target_radius = 50
    target = Circle(Point(taget_start_x, taget_start_y), target_radius)
    target.setFill('red')
    target.draw(win)

    score1 = 0
    score_display = Text(Point(WINDOW_WIDTH / 2, 50), f"{score1}")
    score_display.setTextColor("white")
    score_display.setSize(20)
    score_display.draw(win)

    life = 3
    life_display = Text(Point( 30, WINDOW_HEIGHT - 30), f"{life}")
    life_display.setTextColor("white")
    life_display.setSize(20)
    life_display.draw(win)

    # Ball velocity
    dx, dy = random.choice([-5, 5]), -5 # Randomize initial direction

    # Target velocity
    tx = 5

    while True:

        # Move the ball
        ball.move(dx, dy)
        ball_center = ball.getCenter()

        # Move target
        target.move(tx, 0)
        target_center = target.getCenter()

        # Check wall collision
        if target_center.getX() - target_radius <= 0 or target_center.getX() + target_radius >= WINDOW_WIDTH:
            tx = -tx

        # Check ball collision with target
        if (target_center.getX() - target_radius <= ball_center.getX() <= target_center.getX() + target_radius and
                target_center.getY() - target_radius <= ball_center.getY() <= target_center.getY() + target_radius):
            
            score1 += 1
            score_display.setText(f"{score1}")

            # Determine collision side
            dx_diff = abs(ball_center.getX() - target_center.getX())
            dy_diff = abs(ball_center.getY() - target_center.getY())

            if dx_diff > dy_diff:  # Horizontal collision
                dx = -dx
                # Separate the ball to avoid sticking
                if ball_center.getX() < target_center.getX():
                    ball.move(-5, 0)
                else:
                    ball.move(5, 0)
            else:  # Vertical collision
                dy = -dy
                # Separate the ball to avoid sticking
                if ball_center.getY() < target_center.getY():
                    ball.move(0, -5)
                else:
                    ball.move(0, 5)



        # Check for paddle collisions
        if (WINDOW_HEIGHT - 30 <= ball_center.getY() + ball_radius <= WINDOW_HEIGHT - 20 and
                paddle.getP1().getX() <= ball_center.getX() <= paddle.getP2().getX()):
            dy = -dy
            # Move the ball out of the paddle to avoid sticking
            ball.move(0, -(ball_radius + 5))


        # Check for wall collision (bottom)
        if ball_center.getY() + ball_radius >= WINDOW_HEIGHT:
            life -= 1
            life_display.setText(f"{life}")
            ball.move(ball_start_x - ball_center.getX(),
                    ball_start_y - ball_center.getY())
            dx, dy = random.choice([-5, 5]), -5
            if dy > 0:
                dy = -dy  # Ensure ball moves upwards after reset
        
        # Check for wall collision
        if ball_center.getY() - ball_radius <= 0:
            dy = -dy
        if ball_center.getX() - ball_radius <= 0 or ball_center.getX() + ball_radius > WINDOW_WIDTH:
            dx = -dx
            # Separate the ball to avoid sticking
            if ball_center.getX() - ball_radius <= 0:
                ball.move(5, 0)
            elif ball_center.getX() + ball_radius > WINDOW_WIDTH:
                ball.move(-5, 0)

        # End game if no lives left
        if life == 0:
            break

        if score1 >= 5:
        # End the game when a player reaches 5 points
            win_message = Text(Point(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2), f"Congratulation")
            win_message.setTextColor("yellow")
            win_message.setStyle('bold')
            win_message.setSize(36)
            win_message.draw(win)
            time.sleep(1)
            break

        # Paddle movement
        key = win.checkKey()
        if key in ["a", "Left"] and paddle.getP1().getX() > 0:
            paddle.move(-20, 0)
        elif key in ["d", "Right"] and paddle.getP2().getX() < WINDOW_WIDTH:
            paddle.move(20, 0)

        time.sleep(0.02)  # Slow down the loop

        # Escape sequence
        if key == 'Escape':
            break

