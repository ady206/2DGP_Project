from pico2d import *
import game_framework
import main_state
import middle_state

image = None

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
            elif event.key == SDLK_1:
                main_state.player_character = main_state.Sonic()
            elif event.key == SDLK_2:
                main_state.player_character = main_state.Tales()
            elif event.key == SDLK_3:
                main_state.player_character = main_state.Knuckles()
            elif event.key == SDLK_4:
                main_state.player_character = main_state.Shadow()
        elif event.type == SDL_MOUSEBUTTONDOWN:
            game_framework.change_state(middle_state)

def enter():
    global image
    image = load_image('map/ready.png')
    pass

def exit():
    global image
    del image
    pass

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

def test_self():
    import sys
    this_module = sys.modules['__main__']
    open_canvas()
    game_framework.run(this_module)
    close_canvas()

if __name__ == '__main__': # 만약 단독 실행 상태이면
    test_self()