from pico2d import *

palm = None
running = True

class Palm:
    def __init__(self):
        self.image = load_image('map/palmtree.png')

    def draw(self):
        self.image.clip_draw(0, 600, 1000, 600, 400, 300)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    delay(0.01)

def enter():
    global palm, running
    palm = Palm()
    running = True
    pass

def exit():
    global palm
    del palm

def draw():
    clear_canvas()
    palm.draw()
    update_canvas()

open_canvas()

enter()

while running:
    handle_events()
    draw()
exit()
# finalization code
close_canvas()
