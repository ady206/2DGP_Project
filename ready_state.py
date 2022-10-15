from pico2d import *
import game_framework
import stage_state

image = None
def enter():
    global image
    image = load_image('map/ready.png')
    pass

def exit():
    global image
    del image
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
                game_framework.change_state(stage_state)
    delay(0.01)

def draw():
    clear_canvas()
    image.draw(390, 350)
    update_canvas()

def update():
    handle_events()

def pause():
    pass

def resume():
    pass
