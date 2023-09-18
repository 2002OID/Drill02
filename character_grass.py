from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x=400
y=90
while (True):
 clear_canvas_now()
 grass.draw_now(400, 30)
 character.draw_now(x, y)
 if y == 90:
     if x < 800:
         x = x+2
 if x == 800:
     if y < 600:
         y = y + 2
 if y == 600:
     if x > 0:
         x = x - 2
 if x == 0:
     if y > 90:
         y = y - 2
 delay(0.01)

close_canvas()
