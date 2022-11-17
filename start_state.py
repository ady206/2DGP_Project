from pico2d import *
import game_framework
import ready_state

image = None
sound = None

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
        elif event.type == SDL_MOUSEBUTTONDOWN:
            game_framework.change_state(ready_state)

def enter():
    global image, sound
    image = load_image('map/start.png')

    sound = load_music('sound/start sound.mp3')
    sound.set_volume(20)
    sound.repeat_play()
    pass

def exit():
    global image, sound
    del image, sound
    pass

def draw():
    clear_canvas()
    image.draw(400, 300)
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