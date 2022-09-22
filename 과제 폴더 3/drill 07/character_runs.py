from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('run_character.png')


frame =0
for x in range(0,800,10):
    clear_canvas()
    grass.draw(400,30)
    character.clip_draw(frame*60 ,370,45,70,x,85 )
    update_canvas()
    frame = (frame+1)%9
    delay(0.05)
    get_events()


close_canvas()

