from settings import *


# Example settings
FRAME_DELAY = 0.01  # Frame delay in seconds
MAX_BALLS = 3  


def shoot_cannonball(win, start, direction, balls, speed=5):
    # Shoots a cannonball from the start point in the direction.
    if len(balls) >= MAX_BALLS:
        print("Cannot shoot, max number of balls reached.")
        return  # Limit the number of active cannonballs
    ball = Circle(Point(start.getX(), start.getY()), 5)  # Radius = 5
    ball.setFill("blue")
    ball.draw(win)
    balls.append((ball, direction, speed))

def move_cannonballs(win, balls, target, chances, game_over_text):
    """Moves all cannonballs and checks for collisions."""
    for ball, direction, speed in balls[:]:
        dx, dy = direction
        ball.move(dx * speed, dy * speed)  # Only move the ball by dx and dy
        center = ball.getCenter()
        x, y = center.getX(), center.getY()

        # Check if the ball is out of bounds
        if x < 0 or x > WINDOW_WIDTH or y < 0 or y > WINDOW_HEIGHT:
            ball.undraw()  # Remove the ball from the window
            balls.remove((ball, direction, speed))  # Remove it from the list
            chances[0] -= 1  # Decrease the remaining chances
            print(f"Chances left: {chances[0]}")
            if chances[0] <= 0:
                game_over_text.setText("Game Over! No more chances.")
                game_over_text.draw(win)
            continue

        # **Collision with target**: Check if the ball's Y position is within the target's vertical bounds
        target_p1 = target.p1  # Top-left corner of target
        target_p2 = target.p2  # Bottom-right corner of target

        # Check if the ball's Y position intersects with the target's Y position
        if target_p1.getY() <= y <= target_p2.getY() and target_p1.getX() <= x <= target_p2.getX():
            print("Hit!")
            ball.undraw()
            balls.remove((ball, direction, speed))

            # Adjust target size and undraw part of it
            adjust_target_size(target, 1, win)  # Shrink the target by 1

            chances[0] = 3  # Reset chances after a hit (optional, if you want to reset the count)
            return True  # Return True to indicate that the target was hit

    return False  # Return False if no collision was detected


def move_target(target, speed):
    """Move the target vertically along the Y-axis with collision detection."""
    # Get the current position of the target's top-left and bottom-right corners
    p1 = target.p1
    p2 = target.p2

    # Check if the target's top edge has reached the top of the window or bottom of the window
    if p1.getY() <= 0 or p2.getY() >= WINDOW_HEIGHT:
        # Reverse the direction if it hits the top or bottom
        speed = -speed  # Reverse direction when hitting top or bottom

    # Move the target vertically by the speed value
    target.move(0, speed)

    return speed  # Return the updated speed (possibly reversed)

def adjust_target_speed(target_speed, increase_factor, increase_count):
    """Increase target speed by a given factor (20%) for a total of 5 times."""
    if increase_count >= 5:  # If the speed has increased 5 times, stop increasing
        return target_speed, increase_count

    # Increase the speed by the increase factor (20% increase)
    target_speed *= increase_factor
    increase_count += 1  # Increment the speed increase count

    return target_speed, increase_count  # Return the updated speed and increase count

def adjust_target_size(target, size_multiplier, win):
    """Decrease target size by the given multiplier each time it's hit."""
    # Get the current position of the target's top-left and bottom-right corners
    p1 = target.p1
    p2 = target.p2
    target_width = p2.getX() - p1.getX()
    target_height = p2.getY() - p1.getY()

    # Decrease the target's size by the specified multiplier
    target_width *= size_multiplier
    target_height *= size_multiplier

    # Ensure the target doesn't get too small (minimum size, e.g., 20)
    if target_width < 20:
        target_width = 20
    if target_height < 20:
        target_height = 20

    # Undraw the old target
    target.undraw()

    # Create a new target with the updated size
    target.p2 = Point(p1.getX() + target_width, p1.getY() + target_height)
    
    # Redraw the updated target
    target.draw(win)



def calculate_direction(p1, p2):
    """Calculates a unit vector direction from p1 to p2."""
    dx = p2.getX() - p1.getX()
    dy = p2.getY() - p1.getY()
    magnitude = math.sqrt(dx**2 + dy**2)
    return dx / magnitude, dy / magnitude

def play(win):
    # Create cannon base and axis
    canon_base = Rectangle(Point(0, WINDOW_HEIGHT - 20), Point(100, WINDOW_HEIGHT))
    canon_axis = Circle(Point(canon_base.getCenter().getX(), WINDOW_HEIGHT - 20), 30)
    aim_line = Line(Point(canon_axis.getCenter().getX(), canon_axis.getCenter().getY()), Point(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
    target = Rectangle(Point(WINDOW_WIDTH - 100, WINDOW_HEIGHT // 2 - 50), Point(WINDOW_WIDTH - 50, WINDOW_HEIGHT // 2 + 50))

    # Set properties
    canon_base.setFill("black")
    canon_axis.setFill("red")
    aim_line.setArrow("last")
    aim_line.setOutline("red")
    target.setFill("blue")

    # Draw on the window
    aim_line.draw(win)
    canon_axis.draw(win)
    canon_base.draw(win)
    target.draw(win)

    # Initial coordinates of the aim line
    p1 = aim_line.getP1()
    p2 = aim_line.getP2()

    balls = []  # List to hold active cannonballs
    chances = [MAX_BALLS]  # Store the number of chances left (using list to allow modification inside functions)

    # Game Over Text (optional to display when out of chances)
    game_over_text = Text(Point(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2), "")
    game_over_text.setSize(20)

    # Winning Text (optional to display when target is shrunk 5 times)
    win_text = Text(Point(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2), "")
    win_text.setSize(20)

    target_speed = 1  # Initial speed of the target (starts at 0)
    size_multiplier = 1.2  # Start with no size increase (no change)
    shrink_count = 0  # Track how many times the target's size has been increased
    speed_increase_count = 0  # Track how many times the target's speed has been increased

    while chances[0] > 0:  # Loop continues as long as there are chances left
        start_time = time.time()  # Start frame timer

        

        key = win.checkKey()
        if key == 'Up' and p2.y > 0:
            aim_line.undraw()
            p2 = Point(p2.getX(), p2.getY() - 5)
            aim_line = Line(p1, p2)
            aim_line.setArrow('last')
            aim_line.setOutline('red')
            aim_line.draw(win)

        elif key == 'Down' and p2.y < WINDOW_HEIGHT - 20:
            aim_line.undraw()
            p2 = Point(p2.getX(), p2.getY() + 5)
            aim_line = Line(p1, p2)
            aim_line.setArrow('last')
            aim_line.setOutline('red')
            aim_line.draw(win)

        elif key == 'space':
            if chances[0] > 0:  # Only allow shooting if there are chances left
                direction = calculate_direction(p1, p2)
                shoot_cannonball(win, canon_axis.getCenter(), direction, balls)

        elif key == 'Escape':
            break  # Exit the loop

        # Move and update cannonballs, check for collisions
        if move_cannonballs(win, balls, target, chances, game_over_text):
            # If the target was hit, adjust its size and speed
            shrink_count += 1
            target_speed, speed_increase_count = adjust_target_speed(target_speed, 1.3, speed_increase_count)
            
            adjust_target_size(target, 0.70, win)

            # If the target has increased its size and speed 5 times, display the winning message
            if shrink_count >= 5:
                clear_window(win)
                time.sleep(1)
                exit = message_menu('Congratulation', win)
                return exit

        # Move the target vertically with collision detection and speed adjustment
        target_speed = move_target(target, target_speed)

        # Enforce frame rate
        elapsed_time = time.time() - start_time
        if elapsed_time < FRAME_DELAY:
            time.sleep(FRAME_DELAY - elapsed_time)

    # Once the player runs out of chances, display "Game Over"
    if chances[0] <= 0:
        clear_window(win)
        time.sleep(1)
        exit = message_menu('Game over', win)
        return exit

