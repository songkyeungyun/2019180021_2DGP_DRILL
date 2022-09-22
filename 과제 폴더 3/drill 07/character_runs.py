from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('run_character.png')

frame =0
while True:
    for x in range(0,800,7):
        clear_canvas()
        grass.draw(400,30)
        if frame<3:
            character.clip_draw(frame*67 ,270,70,80,x,85 )
            update_canvas()
            frame = (frame+1)%4
        else:
            character.clip_draw(frame*100 ,270,90,80,x,85 )
            update_canvas()
            frame = (frame+1)%7
        
        delay(0.05)
    for x in range(0,800,7):
        clear_canvas()
        grass.draw(400,30)
        character.clip_draw(frame*67 ,90,63,70,x,85 )
        update_canvas()
        frame = (frame+1)%5
        delay(0.05)
        get_events() 
    for x in range(0,800,10):
        clear_canvas()
        grass.draw(400,30)
        character.clip_draw(frame*67 ,0,63,70,x,85 )
        update_canvas()
        frame = (frame+1)%8
        delay(0.05)
        get_events() 
    for x in range(0,800,10):
        clear_canvas()
        grass.draw(400,30)
        character.clip_draw(frame*70 ,180,60,70,x,85)
        update_canvas()
        frame = (frame+1)%9
        delay(0.05)
        get_events()

    for x in range(0,800,10):
        clear_canvas()
        grass.draw(400,30)
        character.clip_draw(frame*60 ,370,50,70,x,85 )
        update_canvas()
        frame = (frame+1)%10
        delay(0.05)
        get_events() 


close_canvas()

