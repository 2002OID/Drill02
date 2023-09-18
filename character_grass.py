from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x=400
y=90
move_ment = 0
setea = 270
while (True):
 clear_canvas_now()
 grass.draw_now(400, 30)
 character.draw_now(x, y)
 if move_ment == 0:
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
  if x == 400:
      if y == 90:
          move_ment = 1
 if move_ment == 1:
     setea = setea - 5
     if setea == 0:
         setea = 360
     x = 210 * math.cos(setea * 2 * math.pi / 180) + 400
     y = 210 * math.sin(setea * 2 * math.pi / 180) + 300
     if setea == 270:
         move_ment = 0
             
 #delay(0.01)

close_canvas()

#fin
