import arcade
############################################# This is Fin but I want to add different animations or more to "OHIO"
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def draw_grass():
    """ Draw the ground """
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.AIR_SUPERIORITY_BLUE)


def draw_snow_person(x, y):
    """ Draw a snow person """

    # Draw a point at x, y for reference
    arcade.draw_point(x, y, arcade.color.RED, 5)

    # Snow
    arcade.draw_circle_filled(x,  60 + y, 60, arcade.color.WHITE)
    arcade.draw_circle_filled(x, 140 + y, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(x, 200 + y, 40, arcade.color.WHITE)

    # Eyes
    arcade.draw_circle_filled(x - 15, 210 + y, 5, arcade.color.BLACK)
    arcade.draw_circle_filled(x + 15, 210 + y, 5, arcade.color.BLACK)
    # mouth
    arcade.draw_ellipse_filled(300, 325, 20, 10, arcade.color.BLACK)

    # nose
    arcade.draw_triangle_filled(300, 335, 300, 350, 260, 310, arcade.color.ORANGE)

    # Buttons
    arcade.draw_circle_filled(300, 215, 7, arcade.color.BLACK)
    arcade.draw_circle_filled(300, 250, 7, arcade.color.BLACK)
    arcade.draw_circle_filled(300, 280, 7, arcade.color.BLACK)

def draw_cloud(x, y):
    """Draw a mf cloud"""
    arcade.draw_circle_filled(x + 10, 550 + y, 90, arcade.color.GRAY)
    arcade.draw_circle_filled(x + 100, 560 + y, 90, arcade.color.GRAY)
    arcade.draw_circle_filled(x + 150, 570 + y, 90, arcade.color.GRAY)
    arcade.draw_circle_filled(x + 200, 570 + y, 90, arcade.color.GRAY)
    arcade.draw_circle_filled(x + 250, 560 + y, 90, arcade.color.GRAY)
    arcade.draw_circle_filled(x + 300, 550 + y, 90, arcade.color.GRAY)

def draw_sun(x, y):
    arcade.draw_circle_filled(x + 600, 600 + y, 120, arcade.color.SUNGLOW)

def draw_moon(x, y):
    arcade.draw_ellipse_filled(x + 5, 700 + y, 200, 300, arcade.color.WHITE)


def draw_anti_stuff():
    """Draw all anti stuff"""

    # Anti-Background
    arcade.draw_lrtb_rectangle_filled(400, 800, 800, 200, [254, 255, 109])

    # Anti-Ground
    arcade.draw_lrtb_rectangle_filled(400, 800, SCREEN_HEIGHT / 3, 0, [156, 93, 59])

    # Anti- snow person
    arcade.draw_circle_filled(550, 200, 60, arcade.color.BLACK)
    arcade.draw_circle_filled(550, 280, 50, arcade.color.BLACK)
    arcade.draw_circle_filled(550, 340, 40, arcade.color.BLACK)

    # Anti-Buttons
    arcade.draw_circle_filled(550, 215, 7, arcade.color.WHITE)
    arcade.draw_circle_filled(550, 250, 7, arcade.color.WHITE)
    arcade.draw_circle_filled(550, 280, 7, arcade.color.WHITE)

    # Anti-eyes
    arcade.draw_circle_filled(535, 350, 7, arcade.color.WHITE)
    arcade.draw_circle_filled(565, 350, 7, arcade.color.WHITE)

    # Anti-Wall
    arcade.draw_line(400, 0, 400, 600, arcade.color.WHITE, 10)

    #400 is where I need to start the other stuff

def draw_ohio():
    arcade.draw_rectangle_filled(695, 145, 20, 250, arcade.color.GRAY)
    arcade.draw_rectangle_filled(695,175,190,100,arcade.color.GRAY)
    arcade.draw_text("Ohio", 600, 150, arcade.color.AIR_SUPERIORITY_BLUE, 65)



def on_draw(delta_time):
    """ Draw everything """
    arcade.start_render()

    draw_grass()
    draw_sun(on_draw.sun, 20)
    draw_cloud(on_draw.cloud, 20)
    draw_moon(on_draw.moon, 20)
    draw_moon(150,600)
    draw_anti_stuff()
    draw_ohio()
    draw_cloud(150,600)
    draw_snow_person(300, 140)



    # Add one to the x value, making the snow person move right
    # Negative numbers move left. Larger numbers move faster.
    on_draw.snow_person1_x += 1
    on_draw.cloud += 2
    on_draw.sun += -0.5
    on_draw.moon += 1.5



# Create a value that our on_draw.snow_person1_x will start at.
on_draw.snow_person1_x = 0
on_draw.cloud = 0
on_draw.sun = 0
on_draw.moon = 0



def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.DARK_BLUE)

    # Call on_draw every 60th of a second.
    arcade.schedule(on_draw, 1/60)
    arcade.run()


# Call the main function to get the program started.
main()
