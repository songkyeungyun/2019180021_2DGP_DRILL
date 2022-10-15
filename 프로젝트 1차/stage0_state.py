from pico2d import *
import game_framework
import title_state
import stage1_state
import item_state
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
        self.dir_x = 0
        self.dir_y = 0
        self.image = load_image('animation.png')
        self.isaac_image = load_image('isaac.png')
        self.tear_image = load_image('tear.png')
        self.item = None

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir_x*5
        self.y += self.dir_y*5
        if self.x > 700:
            self.x = 700
        if self.x < 100:
            self.x = 100
        if self.y > 400:
            self.y = 400
        if self.y < 100:
            self.y = 100

    def draw(self):
        if self.dir_x == 1:
            self.image.clip_draw(self.frame * 63, 0, 65, 100, self.x, self.y)
        elif self.dir_x == -1:
            self.image.clip_composite_draw(self.frame * 63, 0, 65, 100, 3.141592, 'v', self.x, self.y, 65, 100)
        elif self.dir_y == -1 or self.dir_y == 1:
            self.image.clip_draw(self.frame * 63, 100, 65, 120, self.x, self.y)
        elif self.dir_x == 0:
            self.isaac_image.draw(self.x, self.y-10)
        if self.item == 'tear':
            self.tear_image.draw(self.x + 50, self.y)

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
        if self.x > 400:
            self.dir = -1
            self.x = 400
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
        self.x = 700
        self.y = 350
        self.frame = 0
        self.dir = -1
        self.image = load_image('monster1 animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 6
        self.x += self.dir*2
        if self.x > 700:
            self.dir = -1
            self.x = 700
        elif self.x < 400:
            self.dir = 1
            self.x = 400

    def draw(self):
        if self.dir == 1:
            self.image.clip_draw(self.frame * 30, 30, 25, 60, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 30, 30, 25, 60, self.x, self.y)


def handle_events():
    global running, isaac
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
            if event.key == SDLK_i:
                game_framework.push_state(item_state)
            if event.key == SDLK_SPACE:
                isaac.item = 'tear'
        if event.type == SDL_QUIT:
            running = False
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                isaac.dir_x = 1
                isaac.x += isaac.dir_x
            if event.key == SDLK_LEFT:
                isaac.dir_x = -1
                isaac.x += isaac.dir_x
            if event.key == SDLK_UP:
                isaac.dir_y += 1
                isaac.y += isaac.dir_y
            if event.key == SDLK_DOWN:
                isaac.dir_y -= 1
                isaac.y += isaac.dir_y
            if event.key == SDLK_ESCAPE:
                running = False
        if event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                isaac.dir_x = 0
            if event.key == SDLK_LEFT:
                isaac.dir_x = 0
            if event.key == SDLK_UP:
                isaac.dir_y = 0
            if event.key == SDLK_DOWN:
                isaac.dir_y = 0


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
    global isaac, monster1, monster2
    isaac.update()
    monster1.update()
    monster2.update()
    if isaac.x <= 100 and 250 <= isaac.y <= 260:
        game_framework.change_state(stage1_state)
    delay(0.02)


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