from pico2d import *
import game_framework
import character_state

stage_count = 0
stage = None
class Palm:
    def __init__(self):
        self.image = load_image('map/palmtree.png')

    def draw(self):
        self.image.clip_draw(0, 600, 1000, 600, 400, 300)

class Snow:
    def __init__(self):
        self.image = load_image('map/snow.png')

    def draw(self):
        self.image.clip_draw(0, 600, 700, 300, 400, 300)

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
def enter():
    global stage, stage_count
    if stage_count == 0:
        stage = Palm()
        stage_count = 1
    elif stage_count == 1:
        stage = Snow()
        stage_count = 2
    elif stage_count == 2:
        stage = 0
        stage_count = 100
    pass

def exit():
    global stage, stage_count
    del stage, stage_count
    pass

def draw():
    clear_canvas()
    stage.draw()
    update_canvas()

def update():
    handle_events()

def pause():
    pass

def resume():
    pass

def test_self():
    import sys
    this_module = sys.modules['__main__']
    open_canvas()
    game_framework.run(this_module)
    close_canvas()

if __name__ == '__main__':
    test_self()