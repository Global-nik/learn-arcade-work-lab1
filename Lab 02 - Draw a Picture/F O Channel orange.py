import arcade
arcade.open_window(650,650, "Channel Orange")
arcade.set_background_color((255, 115, 3))
arcade.start_render()
#
arcade.draw_text('channe1', 110,400, bold=70, font_size=40)
# cooper black font for (channel) and sans serif uppercase for (orange)
arcade.draw_text('O', 340,400, font_size=40)
arcade.draw_text('R', 380,400, font_size=40)
arcade.draw_text('A', 420,400, font_size=40)
arcade.draw_text('N', 460,400, font_size=40)
arcade.draw_text('G', 500,400, font_size=40)
arcade.draw_text('E', 540,400, font_size=40)

# convert to hexidecimal 66,ff,66= 66,255,66 as an example
#arcade.draw is going to be used for project 2
arcade.finish_render()
arcade.run()
