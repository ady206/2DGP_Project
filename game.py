from pico2d import *
import game_framework
import ready_state
import character_state

window_size_x = 800
window_size_y = 600
open_canvas(window_size_x, window_size_y)
game_framework.run(character_state)
clear_canvas()