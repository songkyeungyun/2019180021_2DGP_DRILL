from pico2d import *
import random
import game_world
import server

class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x = random.randint(0, 1800)
        self.y = random.randint(0, 1000)

    def draw(self):
        sx, sy = self.x - server.background.window_left, self.y - server.background.window_bottom
        self.image.draw(sx, sy)

    def update(self):
        pass

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def handle_collision(self, other, group):
        print('ball disappear')
        if group == 'boy:ball':
            game_world.remove_object(self)