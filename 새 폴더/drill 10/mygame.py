import game_framework
from pico2d import *
import logo_state
import play_state

open_canvas()
game_framework.run(play_state)
clear_canvas()