from pico2d import *
import game_framework
import game
import stage_state

player_character = None
image = None
def enter():
    global image, player_character
    player_character = stage_state.Sonic()
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
            elif event.key == SDLK_1:
                stage_state.player_character = stage_state.Sonic()
            elif event.key == SDLK_2:
                stage_state.player_character = stage_state.Tales()
            elif event.key == SDLK_3:
                stage_state.player_character = stage_state.Knuckles()
            elif event.key == SDLK_4:
                stage_state.player_character = stage_state.Shadow()
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
