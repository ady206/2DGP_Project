from pico2d import *
import game_framework
import frametime
import stage_state

window_size_x = 800
window_size_y = 600

open_canvas(window_size_x, window_size_y)
frametime.SetStartTime()
game_framework.run(stage_state)
clear_canvas()