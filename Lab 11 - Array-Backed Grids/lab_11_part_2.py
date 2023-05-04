import arcade

'''SCREEN_WIDTH = 500
SCREEN_HEIGHT = 600'''
ROW_COUNT = 10
COLUMN_COUNT = 10
WIDTH = 20
HEIGHT = 20
MARGIN = 5
SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN


class MyGame(arcade.Window):

    def __init__(self, width, height):

        super().__init__(width, height)
        self.grid = []
        self.self_count = 0
        for row in range(ROW_COUNT):
            self.grid.append([])
            for column in range(COLUMN_COUNT):
                self.grid[row].append(0)

        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        """
        Render the screen.
        """
        arcade.start_render()

        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                if self.grid[row][column] == 1:
                    color = arcade.color.DESIRE
                else:
                    color = arcade.color.GLITTER

                x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
                y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2

                arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        column = x // (WIDTH + MARGIN)
        row = y // (HEIGHT + MARGIN)

        print(f"Click coordinates: ({x}, {y}). Grid coordinates: ({row}, {column})")


        if row < ROW_COUNT and column < COLUMN_COUNT:
            if self.grid[row][column] == 0:
                self.grid[row][column] = 1
                self.self_count += 1
            else:
                self.grid[row][column] = 0
                self.self_count -= 1

        print(f"Total of {self.self_count} cells are selected")

        



def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, )
    arcade.run()


if __name__ == "__main__":
    main()