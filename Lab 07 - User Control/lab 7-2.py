import arcade

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
MOVEMENT_SPEED = 3

#theme_music = arcade.load_sound("TS(MK).mp3")


def draw_hazards(center_x, center_y, radius,
                 left, right, top, bottom, left2, right2, top2, bottom2,
                 left3, right3, top3, bottom3, left4, right4, top4, bottom4,):
    #Fire
    arcade.draw_circle_filled(center_x, center_y, radius, arcade.csscolor.ORANGE_RED)
    arcade.draw_circle_outline(center_x, center_y, radius, arcade.csscolor.BLACK, 1)
    #Back Boarder/ WALL
    arcade.draw_lrtb_rectangle_filled(left, right, top, bottom, arcade.csscolor.BROWN)
    arcade.draw_lrtb_rectangle_filled(left2, right2, top2, bottom2, arcade.csscolor.BROWN)
    arcade.draw_lrtb_rectangle_filled(left3, right3, top3, bottom3, arcade.csscolor.BROWN)
    arcade.draw_lrtb_rectangle_filled(left4, right4, top4, bottom4, arcade.csscolor.BROWN)


def draw_spike1(x1, y1, x2, y2, x3, y3):
    #Spikes
    arcade.draw_triangle_filled(x1, y1, x2, y2, x3, y3, arcade.csscolor.RED)
    arcade.draw_triangle_outline(x1, y1, x2, y2, x3, y3, arcade.csscolor.IVORY, 2)


def draw_spike2(x1, y1, x2, y2, x3, y3):

    # Draws a point through passing x and y and making sure it is centered
    #Spikes
    arcade.draw_triangle_filled(x1, y1, x2, y2, x3, y3, arcade.csscolor.RED,)
    arcade.draw_triangle_outline(x1, y1, x2, y2, x3, y3, arcade.csscolor.IVORY, 1)

    # Loops the diagonal/tilted lines
    x_end = x1
    x_start = x2
    y_end = y1
    y_start = y2
    while x_end != 130:
        arcade.draw_line(x_start, y_start, x_end, y_end, arcade.csscolor.WHITE, 2)
        if x_end == 130:
            break
        x_end = x_end-4
        x_start = x_start+2
        y_end = y_end + 20
        y_start = y_start + 20
    arcade.draw_line(145, 445, 220, 445, arcade.csscolor.WHITE, 2)

# Mouse controlled
class Left_fighter:
    def __init__(self, position_x2, position_y2, change_x2, change_y2, texture2, scale2):
        self.position_x2 = position_x2
        self.position_y2 = position_y2
        self.change_x2 = change_x2
        self.change_y2 = change_y2
        self.texture2 = texture2
        self.scale2 = scale2

    def drawLF(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_scaled_texture_rectangle(self.position_x2,
                                             self.position_y2,
                                             self.texture2,
                                             self.scale2)
    def updateLF(self):
        self.position_x2 += self.change_x2
        self.position_y2 += self.change_y2

# Keyboard controlled
class Right_fighter
    def __init__(self, position_x, position_y, change_y, change_x, texture, scale):
        self.position_x = position_x
        self.position_y = position_y
        self.change_y = change_y
        self.change_x = change_x
        self.texture = texture
        self.scale = scale


    def drawRF(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_scaled_texture_rectangle(self.position_x,
                                             self.position_y,
                                             self.texture,
                                             self.scale)

    def updateRF(self):
        self.position_x += self.change_x
        self.position_y += self.change_y

class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        self.set_mouse_visible()

        # Create our ball
        self.left_fighter = Left_fighter(50, 50, 0, 0, arcade.load_texture('BIHAN-removebg-preview.png'), .7)
        self.right_fighter = Right_fighter(100, 50, 0, 0, arcade.load_texture('NOOB-removebg-preview.png'), .7)

    #def updateLF(self):
        #self.left_fighter.update()

    #def updateRF(self):
        #self.right_fighter.update()


    def on_mouse_press(self, x, y, button, modifiers):
        """ Called when the user presses a mouse button. """

        if button == arcade.MOUSE_BUTTON_LEFT:
            print("Left mouse button pressed at", x, y)
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            print("Right mouse button pressed at", x, y)



    def on_mouse_motion(self, x, y, dx, dy):
        """ Called to update our objects.
        Happens approximately 60 times per second."""
        self.left_fighter.position_x = x
        self.left_fighter.position_y = y

    #def update(self, delta_time):
        #self.left_fighter.update()

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.right_fighter.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.right_fighter.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.right_fighter.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.right_fighter.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.right_fighter.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.right_fighter.change_y = 0
    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        arcade.set_background_color(arcade.csscolor.DIM_GRAY)
        self.left_fighter.drawLF()
        self.right_fighter.drawRF()
        #Row 1- circle
        #Rows 2-4 spike
        #row 5-6 border
        draw_hazards(600, 350, 200,
                     0, 10, 700, 0, 0, 1200, 700, 690,
                     0, 1200, 10, 0, 1190, 1200, 700, 0)
        draw_spike1(1200, 350, 0, 250, 50, 300)
        draw_spike2(1200, 350, 0, 250, 50, 300)


def main():
    window = MyGame(1200, 700, "MORTAL KOMBAT")
    arcade.run()


main()