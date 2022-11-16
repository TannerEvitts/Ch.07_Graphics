import arcade
arcade.open_window(600,600,"My Drawing")
arcade.set_background_color(arcade.color.STAR_COMMAND_BLUE)

arcade.start_render()

#drawing stuff

#rectangle

arcade.draw_lrtb_rectangle_filled(5, 35, 590, 570, arcade.color.BITTER_LIME)
arcade.draw_rectangle_filled(100, 520, 45, 25, arcade.color.BLUSH)
#fence posts

for x_offset in range(0,610,20):
    arcade.draw_rectangle_filled(0+x_offset,60,10,30,arcade.color.WHITE)

#rails

arcade.draw_rectangle_filled(300, 67, 600, 5, arcade.color.WHITE)
arcade.draw_rectangle_filled(300, 52, 600, 5, arcade.color.WHITE)

#Snowman

radius=50
y=50
for i in range(3):
    arcade.draw_circle_filled(100,y,radius,(255,255,255))
    y=y+1.8*radius
    radius=radius*0.8

arcade.finish_render()


arcade.run()