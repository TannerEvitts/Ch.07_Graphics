import arcade
import random
'''
PYCASSO PROJECT
---------------
Your job is to make a cool picture.
You must use multiple colors.
You must have a coherent picture. No abstract art with random shapes.
You must use multiple types of graphic functions (e.g. circles, rectangles, lines, etc.)
Somewhere you must include a WHILE or FOR loop to create a repeating pattern.
Do not just redraw the same thing in the same location 10 times. 
You can contain multiple drawing commands in a loop, so you can draw multiple train cars for example.
Please use comments and blank lines to make it easy to follow your program. 
If you have 5 lines that draw a robot, group them together with blank lines above and below. 
Then add a comment at the top telling the reader what you are drawing.
IN THE WINDOW TITLE PLEASE PUT YOUR NAME.
When you are finished Pull Request your file to your instructor.
'''
arcade.open_window(400,550,"Tanner Evitts")
arcade.set_background_color(arcade.color.BLACK)
arcade.start_render()
# outer maze
arcade.draw_line(10,60,10,160,arcade.color.DARK_BLUE,4)
arcade.draw_line(10,160,55,160,arcade.color.DARK_BLUE,4)
arcade.draw_line(55,160,55,175,arcade.color.DARK_BLUE,4)
arcade.draw_line(55,175,10,175,arcade.color.DARK_BLUE,4)
arcade.draw_line(10,175,10,265,arcade.color.DARK_BLUE,4)
arcade.draw_line(10,265,100,265,arcade.color.DARK_BLUE,4)
arcade.draw_line(100,265,100,300,arcade.color.DARK_BLUE,4)
arcade.draw_line(100,300,0,300,arcade.color.DARK_BLUE,4)
arcade.draw_line(0,330,100,330,arcade.color.DARK_BLUE,4)
arcade.draw_line(100,330,100,365,arcade.color.DARK_BLUE,4)
arcade.draw_line(100,365,10,365,arcade.color.DARK_BLUE,4)
arcade.draw_line(10,365,10,515,arcade.color.DARK_BLUE,4)
arcade.draw_line(10,515,195,515,arcade.color.DARK_BLUE,4)
arcade.draw_line(195,515,195,465,arcade.color.DARK_BLUE,4)
arcade.draw_line(195,465,205,465,arcade.color.DARK_BLUE,4)
arcade.draw_line(205,465,205,515,arcade.color.DARK_BLUE,4)
arcade.draw_line(205,515,390,515,arcade.color.DARK_BLUE,4)
arcade.draw_line(390,515,390,365,arcade.color.DARK_BLUE,4)
arcade.draw_line(390,365,300,365,arcade.color.DARK_BLUE,4)
arcade.draw_line(300,365,300,330,arcade.color.DARK_BLUE,4)
arcade.draw_line(300,330,400,330,arcade.color.DARK_BLUE,4)
arcade.draw_line(400,300,300,300,arcade.color.DARK_BLUE,4)
arcade.draw_line(300,300,300,265,arcade.color.DARK_BLUE,4)
arcade.draw_line(300,265,390,265,arcade.color.DARK_BLUE,4)
arcade.draw_line(390,265,390,175,arcade.color.DARK_BLUE,4)
arcade.draw_line(390,175,345,175,arcade.color.DARK_BLUE,4)
arcade.draw_line(345,175,345,160,arcade.color.DARK_BLUE,4)
arcade.draw_line(345,160,390,160,arcade.color.DARK_BLUE,4)
arcade.draw_line(390,160,390,60,arcade.color.DARK_BLUE,4)
arcade.draw_line(10,60,390,60,arcade.color.DARK_BLUE,4)
#PAC-MAN
arcade.draw_text("PAC-MAN",125,302,arcade.color.YELLOW,25)
arcade.draw_arc_filled(200,180,100,100,arcade.color.YELLOW,0,300,30)
#Lives
l=0
while l <= 110:
    arcade.draw_arc_filled(l+40,30,20,20,arcade.color.RED,0,300,30,)
    l+=40
arcade.finish_render()
arcade.run()
