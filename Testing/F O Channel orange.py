import arcade
arcade.open_window(650,650, "Channel Orange")
arcade.set_background_color((255, 115, 3))
arcade.start_render()
#
arcade.draw_text('channe1', 110,400, bold=70, font_size=40, font_name= cooper black font, this doesnt work so input the actual font code or download it)
# cooper black font for (channel) and sans serif uppercase for (orange)
arcade.draw_text('0', 340,400, font_size=40)
arcade.draw_text('R', 370,400, font_size=38, font)
#arcade.draw_text('A', 350,400, font_size=30)
#arcade.draw_text('N', 370,400, font_size=30)
#arcade.draw_text('G', 390,400, font_size=30)
#arcade.draw_text('E', 410,400, font_size=30)
# convert to hexidecimal 66,ff,66= 66,255,66 as an example
#arcade.draw is going to be used for project 2
arcade.finish_render()
arcade.run()
