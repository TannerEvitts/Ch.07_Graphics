import arcade
#Sign your name: Tanner Evitts

'''
Recreate, exactly the Test Picture from the website. The arcade colors used in this picture in no particular order are:
BLACK, ALMOND, PHLOX, BLUSH, RED, BLUE, WISTERIA, AMBER, BRICK_RED and YELLOW.
The picture is 500px wide and 400px tall. Look up ARC in the documentation to do the PAC-MAN.
'''

arcade.open_window(500,400,"Tanner Evitts")
arcade.set_background_color(arcade.color.ALMOND)

arcade.start_render()

#grid

for x_offset in range(0,410,20):
    arcade.draw_line(0,x_offset,500,x_offset,arcade.color.BLACK)
for y_offset in range(0,510,20):
    arcade.draw_line(y_offset,0,y_offset,400,arcade.color.BLACK)

#Pink Rectangle

arcade.draw_rectangle_filled(50,370,60,20,arcade.color.PHLOX)

#diagonal rectangle

arcade.draw_rectangle_filled(200,260,40,20, arcade.color.BLUSH,135)

#Circle

arcade.draw_circle_filled(250,200,40,arcade.color.WISTERIA)

#Text

arcade.draw_text("I love you. I know.",22,160,arcade.color.BRICK_RED,20)

#Line

arcade.draw_line(80,20,120,60,arcade.color.BLUE)

#point

arcade.draw_point(460,10,arcade.color.RED,5)

#oval

arcade.draw_ellipse_filled(100,100,120,40,arcade.color.AMBER)

#PAC-MAN

arcade.draw_arc_filled(400,320,120,120,arcade.color.YELLOW,0,300,30)

arcade.finish_render()

arcade.run()