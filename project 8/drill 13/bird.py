from pico2d import *

import game_framework
import game_world


TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 4

class RUN:
    def enter(self, event):
        print('ENTER RUN')
        self.dir += 1


    def exit(self, event):
        print('EXIT RUN')
        self.face_dir = self.dir

    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        self.x = clamp(0, self.x, 1600)
        if self.x > 1600 -20:
            self. dir = -1
        if self. x < 0 +20:
            self. dir = 1

    def draw(self):
        if self.dir == -1:
            self.image.clip_composite_draw(int(self.frame)*185, 0, 175, 140, 3.141592, 'v', self.x, self.y, 175, 140)
        elif self.dir == 1:
            self.image.clip_draw(int(self.frame)*185, 0, 175, 140, self.x, self.y)



PIXEL_PER_METER = 10.0 / 0.3
RUN_SPEED_KPH = 20
RUN_SPEED_MPM = RUN_SPEED_KPH * 1000.0 / 60.0
RUN_SPEED_MPS = RUN_SPEED_MPM / 60.0
RUN_SPEED_PPS = RUN_SPEED_MPS * PIXEL_PER_METER


class Bird:

    def __init__(self):
        self.x, self.y = 100, 300
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('bird_animation.png')
        self.font = load_font('ENCR10B.TTF', 16)

        self.timer = 100

        self.event_que = []
        self.cur_state = RUN
        self.cur_state.enter(self, None)

    def update(self):
        self.cur_state.do(self)

        if self.event_que:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        self.font.draw(self.x - 60, self.y + 50, f'(Time:{get_time():.2f})', (255, 255, 0))

    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_event(self, event):
        pass

