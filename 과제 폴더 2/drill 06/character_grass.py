from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

while(1):
    x=0
    y=90
    while(x<800):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,90)
        x=x+2
        delay(0.0001)
    while(y<600):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(799,y)
        y=y+2
        delay(0.0001)
    while(x>0):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,599)
        x=x-2
        delay(0.0001)
    while(y>90):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(0,y)
        y=y-2
        delay(0.0001)

close_canvas()
