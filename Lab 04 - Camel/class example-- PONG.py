import arcade
import random
from pyglet.window import key
from pyglet.window import Window

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCALE = 0.1

keyboard = None

# Ball Variables
ball_texture = arcade.load_texture("../Week 4/beach-ball.png")
ball_x = random.randint(0,700)
ball_y = random.randint(0,700)
ball_dx = random.randint(-5,5)
ball_dy = random.randint(-8,8)
rotation_dr = random.randint(5,10)
rotation_var = 0

# Paddle Variables
paddle_x = random.randint(50,750)
paddle_y = 50
paddle_size = 100
paddle_llimit = 0
paddle_rlimit = 700
left = False
right = False

def sgn(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

def place_ball():
    global ball_x, ball_y, ball_dx, ball_dy, rotation_dr
    ball_x = random.randint(0, 700)
    ball_y = random.randint(0, 700)
    ball_dx = random.randint(-10, 10)
    ball_dy = random.randint(-8, 8)
    rotation_dr = random.randint(5, 10)

# keboard reader
def read_key():
    global left, right
    left = False
    right = False
    if keyboard[key.S]:
        left = True
    elif keyboard[key.D]:
        right = True

def draw_paddle():
    read_key()
    global paddle_x, paddle_y, paddle_llimit, paddle_rlimit, paddle_size, left, right, keyboard
    # get new paddle position
    if left:
        paddle_x -= 10
        if paddle_x < paddle_llimit:
            paddle_x = paddle_llimit
    elif right:
        paddle_x += 10
        if paddle_x > paddle_rlimit:
            paddle_x = paddle_rlimit
    arcade.draw_rectangle_filled(paddle_x + paddle_size/2, paddle_y, paddle_size, 25, arcade.csscolor.WHITE)

def on_draw(delta_time):
    global ball_x, ball_y, ball_dx, ball_dy, ball_texture, rotation_dr, rotation_var
    """ Draw everything """
    arcade.start_render()
    draw_paddle()

    # Update beach ball
    ball_x += ball_dx
    ball_y += ball_dy
    if ball_x > SCREEN_WIDTH or ball_x < 10:
        ball_dx =  -sgn(ball_x) * random.randint(-10,10)
        ball_dy += sgn(ball_dy)
        rotation_dr = random.randint(-10, 10)

    # check top
    if ball_y > SCREEN_HEIGHT:
        ball_dy = -ball_dy
        rotation_dr = random.randint(-10, 10)

    # check bottom
    if ball_y < 0:
        place_ball()

    # check paddle
    if ball_x >= paddle_x and ball_x <= paddle_x + paddle_size:
        if ball_y <= paddle_y + 25/2 and ball_y >= paddle_y - 25/2:
            #collision
            ball_dx += sgn(ball_dx)
            ball_dy = -ball_dy
            rotation_dr = random.randint(-10, 10)

    # manage rotation
    rotation_var += rotation_dr
    if rotation_var > 360:
        rotation_var = 0  # handle overflows
    elif rotation_var < 0:
        rotation_var = 360

    # draw beach ball
    arcade.draw_scaled_texture_rectangle(ball_x, ball_y, ball_texture, SCALE, rotation_var)

def main():
    global keyboard
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.BLACK)
    window = arcade.get_window()
    keyboard = key.KeyStateHandler()
    window.push_handlers(keyboard)

    # Call on_draw every 60th of a second.
    arcade.schedule(on_draw, 1/60)
    arcade.run()
####CANT RUN MISSING BEACHBALL.PNG!!!!!!!!!!!!!
# Call the main function to get the program started.
main()