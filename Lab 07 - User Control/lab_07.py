import arcade

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480


class Left_fighter:
    def __init__(self, position_x, position_y):
        self.position_x = position_x
        self.position_y = position_y


#class Right_fighter:
    #def __init__(self, position_x, position_y):
        # Take the parameters of the init function above,
        # and create instance variables out of them.
        #self.position_x = position_x
        #self.position_y = position_y

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x,
                                  self.position_y,
                                  self.radius,
                                  self.color)


class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        arcade.load_texture('KOM.jpeg')

        # Create our ball
        self.left_fighter = Left_fighter(arcade.load_texture('BIHAN-removebg-preview.png'), 3)
        #self.right_fighter = Right_fighter(arcade.load_texture('NOOB-removebg-preview.png'), .03)


    def on_mouse_press(self, x, y, button, modifiers):
        """ Called when the user presses a mouse button. """

        if button == arcade.MOUSE_BUTTON_LEFT:
            print("Left mouse button pressed at", x, y)
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            print("Right mouse button pressed at", x, y)

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        self.ball.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        """ Called to update our objects.
        Happens approximately 60 times per second."""
        self.ball.position_x = x
        self.ball.position_y = y

    #def update(self, delta_time):
        #self.left_fighter.update()

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.ball.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.ball.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.ball.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.ball.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.ball.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.ball.change_y = 0


def main():
    window = MyGame(640, 480, "Drawing Example")
    arcade.run()


main()