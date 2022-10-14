from pico2d import *
import game_framework
import title_state
isaac = None
stage = None
monster1 = None
monster2 = None
running = True
class Stage:
    def __init__(self):
        self.image = load_image('stage0.png')

    def draw(self):
        self.image.draw(400, 300)

class Isaac:
    def __init__(self):
        self.x = 400
        self.y = 250
        self.frame = 0
        self.dir = 1
        self.image = load_image('animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir*2
        if self.x > 700:
            self.dir = -1
            self.x = 700
        elif self.x < 100:
            self.dir = 1
            self.x = 100

    def draw(self):
        if self.dir == 1:
            self.image.clip_draw(self.frame * 63, 0, 65, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 63, 100, 65, 120, self.x, self.y)

class Monster_1():
    def __init__(self):
        self.x = 100
        self.y = 100
        self.frame = 0
        self.dir = 1
        self.image = load_image('monster2 animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 4
        self.x += self.dir*2
        if self.x > 700:
            self.dir = -1
            self.x = 700
        elif self.x < 100:
            self.dir = 1
            self.x = 100

    def draw(self):
        if self.dir == 1:
            self.image.clip_draw(self.frame * 33, 30, 25, 35, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 33, 30, 25, 35, self.x, self.y)

class Monster_2():
    def __init__(self):
        self.x = 100
        self.y = 350
        self.frame = 0
        self.dir = 1
        self.image = load_image('monster1 animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 6
        self.x += self.dir*2
        if self.x > 700:
            self.dir = -1
            self.x = 700
        elif self.x < 100:
            self.dir = 1
            self.x = 100

    def draw(self):
        if self.dir == 1:
            self.image.clip_draw(self.frame * 30, 30, 25, 60, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 30, 30, 25, 60, self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()


def enter():
    global isaac, stage, running, monster1, monster2
    isaac = Isaac()
    stage = Stage()
    monster1 = Monster_1()
    monster2 = Monster_2()
    running = True
    pass

# 게임 종료 - 객체를 소멸
def exit():
    global isaac, stage, monster1, monster2
    del isaac, stage, monster1, monster2

# 게임 월드 객체를 업데이트 - 게임 로직
def update():
    isaac.update()
    monster1.update()
    monster2.update()
    delay(0.03)


def draw_world():
    stage.draw()
    isaac.draw()
    monster1.draw()
    monster2.draw()

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




