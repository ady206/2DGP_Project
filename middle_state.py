from pico2d import *
import game_framework
import main_state

image = None

# 927 618
def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
            elif event.key == SDLK_RETURN:
                if main_state.stage_count == 0:
                    game_framework.change_state(main_state)
                else:
                    game_framework.pop_state()


def enter():
    pass

def exit():
    pass

def draw():
    clear_canvas()
    image.draw(420, 300)
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