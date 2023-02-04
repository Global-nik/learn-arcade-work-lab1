import arcade
####################################### THIS IS OG
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.DARK_BLUE)
    arcade.start_render()

    # Draw the ground
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.AIR_SUPERIORITY_BLUE)

    # Draw a snow person

    # Snow
    arcade.draw_circle_filled(300, 200, 60, arcade.color.WHITE)
    arcade.draw_circle_filled(300, 280, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(300, 340, 40, arcade.color.WHITE)

    # Eyes
    arcade.draw_circle_filled(285, 350, 5, arcade.color.BLACK)
    arcade.draw_circle_filled(315, 350, 5, arcade.color.BLACK)

    #mouth
    arcade.draw_ellipse_filled(300,325,20,10,arcade.color.BLACK)

    #nose
    arcade.draw_triangle_filled(300,335,300,350,260,310,arcade.color.ORANGE)

    #MY ADDITIONS BELOW
    #Buttons
    arcade.draw_circle_filled(300,215,7,arcade.color.BLACK)
    arcade.draw_circle_filled(300,250,7,arcade.color.BLACK)
    arcade.draw_circle_filled(300,280,7,arcade.color.BLACK)

    #Anti-Background
    arcade.draw_lrtb_rectangle_filled(400, 800, 800, 200, [254,255,109])

    # Anti-Ground
    arcade.draw_lrtb_rectangle_filled(400, 800, SCREEN_HEIGHT / 3, 0, [156, 93, 59])

    # anti- snow person
    arcade.draw_circle_filled(550, 200, 60, arcade.color.BLACK)
    arcade.draw_circle_filled(550, 280, 50, arcade.color.BLACK)
    arcade.draw_circle_filled(550, 340, 40, arcade.color.BLACK)

    # Anti-Buttons
    arcade.draw_circle_filled(550, 215, 7, arcade.color.WHITE)
    arcade.draw_circle_filled(550, 250, 7, arcade.color.WHITE)
    arcade.draw_circle_filled(550, 280, 7, arcade.color.WHITE)

    #Anti-eyes
    arcade.draw_circle_filled(535, 350, 7, arcade.color.WHITE)
    arcade.draw_circle_filled(565, 350, 7, arcade.color.WHITE)

    #Anti-Wall
    arcade.draw_line(400,0,400,600,arcade.color.WHITE,10)

    def on_draw(delta_time):
        """ Draw everything """
        arcade.start_render()

        draw_grass()
        draw_snow_person(150, 140)
        draw_snow_person(450, 180)

        # Call on_draw every 60th of a second.
        arcade.schedule(on_draw, 1 / 600)
        arcade.run()

    #super sayin hair
    #arcade.draw_triangle_filled(300, 335, 300, 350, 260, 310, arcade.color.YELLOW)
    #arcade.draw_triangle_filled(300, 335, 300, 350, 260, 310, arcade.color.YELLOW_ROSE)
    #arcade.draw_triangle_filled(300, 335, 300, 350, 260, 310, arcade.color.YELLOW)
    #arcade.draw_triangle_filled(300, 335, 300, 350, 260, 310, arcade.color.YELLOW_ROSE)


    # Finish and run
    arcade.finish_render()
    arcade.run()


# Call the main function to get the program started.
main()