import arcade
'''
FLAG PROJECT
---------------
Make your flag 260 pixels tall
Use the scaling image on the website to determine other dimensions
The hexadecimal colors for the official flag are red: #BF0A30 and blue: #002868
Title the window, "The Stars and Stripes"
You can use a draw_text command and used 20 pt. asterisks for the stars.
We will have a competition to see who can make this flag in the least lines of code.
The record is 16! You will have to use some loops to achieve this.
CHALLENGE: Can you make the entire flag parametrically? This means if I change the hoist to 520px the flag will resize accordingly.
'''

arcade.open_window(494,260,"The Stars and Stripes")
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()
for y_offset in range(-30,347,40):
    arcade.draw_rectangle_filled(247,y_offset,494,20,color=(191,10,48))
arcade.draw_rectangle_filled(98.8,189.995,197.6,140.01,color=(0,40,104))
star_y = 229.96
while star_y > 120:
    star_x = 12.38
    while  star_x < 189:
        arcade.draw_text("*",star_x,star_y,arcade.color.WHITE,20)
        star_x+=32.76
    star_y-=14.04
    star_x = 32.76
    while star_x < 189:
        arcade.draw_text("*",star_x,star_y,arcade.color.WHITE,20)
        star_x+=32.76
    star_y-=14.04
star_x = 16.38
while star_x < 189:
    arcade.draw_text("*",star_x,star_y,arcade.color.WHITE,20)
    star_x+=32.76
arcade.finish_render()
arcade.run()