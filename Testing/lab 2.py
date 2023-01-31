import arcade

arcade.open_window(650,650, "Channel Orange")
arcade.set_background_color((255, 115, 3))
arcade.start_render()
#
arcade.draw_circle_filled(325,325,100,arcade.csscolor.BLACK)
#center
arcade.draw_circle_filled(145,145,100,arcade.csscolor.BLACK)
#bottom left
arcade.draw_circle_filled(500,145,100,arcade.csscolor.BLACK)
#bottom right
arcade.draw_circle_filled(145,500,100,arcade.csscolor.BLACK)
#top left
arcade.draw_circle_filled(503,503,100,arcade.csscolor.BLACK)
#top right
#
#
arcade.draw_text('channe1', 110,400, bold=70, font_size=40)
arcade.draw_text('O', 340,400, font_size=40)
arcade.draw_text('R', 380,400, font_size=40)
arcade.draw_text('A', 420,400, font_size=40)
arcade.draw_text('N', 460,400, font_size=40)
arcade.draw_text('G', 500,400, font_size=40)
arcade.draw_text('E', 540,400, font_size=40)
#
arcade.draw_circle_outline(325,325,150,arcade.csscolor.WHITE)
arcade.draw_rectangle_outline(325,100,200,100,arcade.csscolor.WHITE)
arcade.draw_rectangle_outline(325,100,300,100,arcade.csscolor.BLUE)
arcade.draw_rectangle_outline(325,100,400,100,arcade.csscolor.WHITE)
arcade.draw_rectangle_outline(325,100,500,100,arcade.csscolor.BLUE)
arcade.draw_rectangle_outline(325,100,600,100,arcade.csscolor.WHITE)
arcade.draw_rectangle_outline(325,100,100,100,arcade.csscolor.BLUE)
#
arcade.draw_rectangle_outline(325,550,200,100,arcade.csscolor.WHITE)
arcade.draw_rectangle_outline(325,550,300,100,arcade.csscolor.BLUE)
arcade.draw_rectangle_outline(325,550,400,100,arcade.csscolor.WHITE)
arcade.draw_rectangle_outline(325,550,500,100,arcade.csscolor.BLUE)
arcade.draw_rectangle_outline(325,550,600,100,arcade.csscolor.WHITE)
arcade.draw_rectangle_outline(325,550,100,100,arcade.csscolor.BLUE)
#
arcade.draw_text('Has spiraled into this', 110,250, bold=10, font_size=25)
#arcade.draw_text('channe1', 110,400, bold=70, font_size=40)
arcade.finish_render()
arcade.run ()