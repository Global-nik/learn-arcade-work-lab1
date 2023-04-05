import random
import arcade
import math

# --- Constants ---
SPRITE_SCALING_RACOON = 0.5
SPRITE_SCALING_BABY = .25
SPRITE_SCALING_ADULT = 0.07
BABY_COUNT = 50
ADULT_COUNT = 25

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "*NEW* SUPER Racoon ball adventure"


class Baby(arcade.Sprite):
    def __init__(self, file, scale):
        super().__init__(file, scale)

    def update(self):
        self.center_y -= 1
        if self.center_y == 0:
            self.center_y = SCREEN_HEIGHT


class Adult(arcade.Sprite):
    def __init__(self, file, scale):
        super().__init__(file, scale)

        """self.circle_angle = 0
        self.circle_radius = 0
        self.circle_speed = 0.008
        self.circle_center_x = 0
        self.circle_center_y = 0"""
    def update(self):
        self.center_x -= 1
        if self.center_x == 0:
            self.center_x = SCREEN_WIDTH
        """self.center_x = self.circle_radius * math.sin(self.circle_angle) * self.circle_center_x
        self.center_y = self.circle_radius * math.cos(self.circle_angle) * self.circle_center_y
        self.circle_angle += self.circle_speed"""





class MyGame(arcade.Window):

    def __init__(self):
        """ Initializer """
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.adult_sound = arcade.load_sound("3dpunch2.wav")
        #self.adult_sound = arcade.load_sound("/Users/Jxen/Desktop/learn-arcade-work/lab_08 - Sprites/punch.mp3")
        self.baby_sound = arcade.load_sound("babylaugh.wav")

        # Variables that will hold sprite lists
        self.racoon_list = None
        self.baby_list = None
        self.adult_list = None

        # Set up the player info
        self.racoon_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        self.game_over = False
        self.win = False

        arcade.set_background_color(arcade.color.TEAL)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.racoon_list = arcade.SpriteList()
        self.baby_list = arcade.SpriteList()
        self.adult_list = arcade.SpriteList()

        # Score
        self.score = 0

        #characters
        self.racoon_sprite = arcade.Sprite("racoon.png", 0.1)
        self.racoon_sprite.center_x = 50
        self.racoon_sprite.center_y = 50
        self.racoon_list.append(self.racoon_sprite)

        # Create the babies
        for i in range(BABY_COUNT):

            # Create the coin instance
            # Coin image from kenney.nl
            baby = Baby("baby.png", SPRITE_SCALING_BABY)
            #arcade.Sprite(":resources:images/items/coinGold.png", SPRITE_SCALING_COIN)

            # Position the coin
            baby.center_x = random.randrange(SCREEN_WIDTH)
            baby.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the coin to the lists
            self.baby_list.append(baby)

        for i in range(ADULT_COUNT):
            adult = Adult("shotgun carl.png", SPRITE_SCALING_ADULT)
                #arcade.Sprite(":resources:images/items/coinGold.png", SPRITE_SCALING_COIN)

            # Position the coin
            """adult.circle_center_x = random.randrange(SCREEN_WIDTH)
            adult.circle_center_y = random.randrange(SCREEN_HEIGHT)
            adult.circle_radius = random.randrange(10, 200)
            adult.circle_angle = random.random() * 2 * math.pi"""
            adult.center_x = random.randrange(SCREEN_WIDTH)
            adult.center_y = random.randrange(SCREEN_HEIGHT)
            # Add the coin to the lists
            self.adult_list.append(adult)

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        self.baby_list.draw()
        self.adult_list.draw()
        self.racoon_list.draw()

        output = f"Score: {self.score}"
        if self.game_over:
            arcade.set_background_color(arcade.color.BLACK)
            print("BETTER LUCK NEXT TIME", 200, 400, arcade.color.LAVA, 25)
        if self.win:
            arcade.set_background_color(arcade.color.LIGHT_SKY_BLUE)
            print("YOU WIN", 200, 400, arcade.color.YELLOW_ROSE, 25)
        arcade.draw_text(text=output, start_x=10, start_y=20,
                         color=arcade.color.WHITE, font_size=14)


    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """

        # Move the center of the player sprite to match the mouse x, y
        self.racoon_sprite.center_x = x
        self.racoon_sprite.center_y = y

    def on_update(self, delta_time):
        if not self.game_over and not self.win:
            self.baby_list.update()
            baby_hit_list = arcade.check_for_collision_with_list(self.racoon_sprite, self.baby_list)
            self.adult_list.update()
            adult_hit_list = arcade.check_for_collision_with_list(self.racoon_sprite, self.adult_list)
            for baby in baby_hit_list:
                baby.remove_from_sprite_lists()
                self.score += 1
                arcade.play_sound(self.baby_sound)
            for adult in adult_hit_list:
                adult.remove_from_sprite_lists()
                self.score -= 5
                arcade.play_sound(self.adult_sound)
                #arcade.play_sound(self.baby_sound)
        #if len(self.baby_list) <= BABY_COUNT:
            #self.win = True
        #if len(self.adult_list) <= ADULT_COUNT:
            #self.game_over = True


def main():
    """ Main function """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":

    main()
