import arcade
import math
arcade.open_window(600,600, "My Drawing")
arcade.set_background_color((255, 255, 255))
arcade.start_render()
# convert to hexidecimal 66,ff,66= 66,255,66 as an example
#arcade.draw is going to be used for project 2
arcade.draw_circle_filled(300,300,100,arcade.csscolor.BLACK)
arcade.draw_circle_filled(110,110,100,arcade.csscolor.BLACK)
arcade.draw_circle_filled(490,110,100,arcade.csscolor.BLACK)
arcade.draw_circle_filled(110,490,100,arcade.csscolor.BLACK)
arcade.draw_circle_filled(490,490,100,arcade.csscolor.BLACK)
arcade.finish_render()
arcade.run ()