import random
import arcade
import math

# --- Constants ---
SPRITE_SCALING_RACOON = 0.5
SPRITE_SCALING_BABY = .25
SPRITE_SCALING_ADULT = 0.07
BABY_COUNT = 25
ADULT_COUNT = 25
ADULT_CHECK = ADULT_COUNT - 5
BABY_CHECK = 25
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "*NEW* SUPER Racoon ball adventure"


class Baby(arcade.Sprite):
    def __init__(self, file, scale):
        super().__init__(file, scale)

    def reset_pos(self):
        self.center_y = random.randrange(SCREEN_HEIGHT + 20, SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):
        self.center_y -= 1
        if self.top < 0:
            self.reset_pos()


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
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.adult_sound = arcade.load_sound("3dpunch2.wav")
        self.baby_sound = arcade.load_sound("babylaugh.wav")
        #self.go_sound = arcade.load_sound("TS-fix.wav")
        self.racoon_list = None
        self.baby_list = None
        self.adult_list = None
        self.racoon_sprite = None
        #~~~
        self.score = 0
        self.baby_check = 0
        self.adult_score = 0
        #~~~
        self.set_mouse_visible(False)
        self.game_over = False
        self.win = False
        arcade.set_background_color(arcade.color.DIRT)

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
            baby = Baby("baby.png", SPRITE_SCALING_BABY)
            baby.center_x = random.randrange(SCREEN_WIDTH)
            baby.center_y = random.randrange(SCREEN_HEIGHT)
            self.baby_list.append(baby)

        for i in range(ADULT_COUNT):
            adult = Adult("shotgun carl.png", SPRITE_SCALING_ADULT)
            """adult.circle_center_x = random.randrange(SCREEN_WIDTH)
            adult.circle_center_y = random.randrange(SCREEN_HEIGHT)
            adult.circle_radius = random.randrange(10, 200)
            adult.circle_angle = random.random() * 2 * math.pi"""
            adult.center_x = random.randrange(SCREEN_WIDTH)
            adult.center_y = random.randrange(SCREEN_HEIGHT)
            self.adult_list.append(adult)

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        self.baby_list.draw()
        self.adult_list.draw()
        self.racoon_list.draw()
        score = f"Score: {self.score}"
        baby_score = f"BABIES SAVED: ({self.baby_check}/25)"
        adult_score = f"00 hits: ({self.adult_score}/5)"
        arcade.draw_text(score, 10, 20, arcade.color.BABY_BLUE_EYES)
        arcade.draw_text(baby_score, 10, 40, arcade.color.GLITTER)
        arcade.draw_text(adult_score, 10, 60, arcade.color.CHROME_YELLOW)
        #~~~
        if self.game_over:
            arcade.set_background_color(arcade.color.BLACK)
            arcade.draw_text("BETTER LUCK NEXT TIME", 200, 400, arcade.color.LAVA, 25)


        if self.win:
            arcade.set_background_color(arcade.color.LIGHT_SKY_BLUE)
            arcade.draw_text("YOU WIN", 200, 400, arcade.color.BLACK, 25)
            arcade.draw_text(score, 10, 20, arcade.color.BLACK)
            #arcade.play_sound(self.go_sound)


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
                baby.reset_pos()
                self.score += 1
                self.baby_check += 1
                arcade.play_sound(self.baby_sound)
            for adult in adult_hit_list:

                adult.remove_from_sprite_lists()
                self.score -= 5
                self.adult_score +=1
                arcade.play_sound(self.adult_sound)
        if len(self.baby_list) <= self.baby_check:
            self.win = True
        if len(self.adult_list) <= ADULT_CHECK:
            self.game_over = True


def main():
    """ Main function """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":

    main()
