from pico2d import *
import game_framework
import game_world

from grass import Grass
from boy import Boy
from grass1 import Grass1


boy = None
grass = None
grass1 = None

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        else:
            boy.handle_event(event)


# 초기화
def enter():
    global boy, grass, grass1
    boy = Boy()
    grass = Grass()
    grass1 = Grass1()
    game_world.add_object(boy, 1)
    game_world.add_object(grass, 1)
    game_world.add_object(grass1, 0)

# 종료
def exit():
    global boy, grass, grass1
    del boy
    del grass
    del grass1

def update():
    for game_object in game_world.all_objects():
        game_object.update()

def draw_world():
    for game_object in game_world.all_objects():
        game_object.draw()

def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def pause():
    pass

def resume():
    pass




def test_self():
    import play_state

    pico2d.open_canvas()
    game_framework.run(play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()
