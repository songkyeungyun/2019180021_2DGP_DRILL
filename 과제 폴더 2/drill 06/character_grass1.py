import math
from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

while(1):
    x=0
    y=90
    z=180
    r=270
    while(x<90):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(400-math.cos(x/180*math.pi)*250,300+math.sin(x/180*math.pi)*250)
        delay(0.01)
        x=x+2
    while(y<180 ):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(400-math.cos(y/180*math.pi)*250,300+math.sin(y/180*math.pi)*250)
        delay(0.01)
        y=y+2
    while(z<270):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(400-math.cos(z/180*math.pi)*250,300+math.sin(z/180*math.pi)*250)
        delay(0.01)
        z=z+2
    while(r<360):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(400-math.cos(r/180*math.pi)*250,300+math.sin(r/180*math.pi)*250)
        delay(0.01)
        r=r+2    
    

close_canvas()
