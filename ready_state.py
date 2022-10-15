from pico2d import *
import game_framework
import map_state

class Ready:
    image = None
    def __init__(self):
        self.image = Ready.image

    def draw(self):
        self.image.draw(390, 350)

ready = None

def enter():
    Ready.image = load_image('map/ready.png')
    global ready
    ready = Ready()
    pass

def exit():
    global ready
    del ready
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
            elif event.key == SDLK_SPACE:
                game_framework.change_state(map_state)
    delay(0.01)

def draw():
    clear_canvas()
    ready.draw()
    update_canvas()

def update():
    handle_events()

def pause():
    pass

def resume():
    pass