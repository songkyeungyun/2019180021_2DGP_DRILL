from pico2d import *
import game_framework
import title_state
import item_state

boy = None
grass = None
running = True
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x = 0
        self.y = 90
        self.frame = 0
        self.dir = 1
        self.image = load_image('animation_sheet.png')
        self.item = None

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir * 3
        if self.x > 800:
            self.dir = -1
            self.x = 800
        elif self.x < 0:
            self.dir = 1
            self.x = 0

    def draw(self):
        i =50
        if self.item == '+':
            self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x-i, self.y)
            i -= 50
        elif self.item == '-':
            pass
        if self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
            elif event.key == SDLK_b:
                game_framework.push_state(item_state)

    delay(0.01)


def enter():
    global boy, grass, running
    boy = Boy()
    grass = Grass()
    running = True
    pass

# 게임 종료 - 객체를 소멸
def exit():
    global boy, grass
    del boy, grass

# 게임 월드 객체를 업데이트 - 게임 로직
def update():
    boy.update()


def draw_world():
    grass.draw()
    boy.draw()

# 게임 월드 렌더링
def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def pause():
    pass

def resume():
    pass

def test_self():
    import sys
    this_module = sys.modules['__main__']
    pico2d.open_canvas()
    game_framework.run(this_module)
    pico2d.close_canvas()


if __name__ == '__main__':
    test_self()




