from pico2d import *
import game_framework
import ready_state

from time import *

image = None
sound = None
click_sound = None

clicked = False

set_time = 0
cur_time = 0

def handle_events():
    global clicked, set_time, click_sound
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if clicked == False:
                set_time = time()
            clicked = True
            click_sound.play()

def enter():
    global image, sound, clicked, set_time, click_sound
    image = load_image('map/start.png')

    sound = load_music('sound/start sound.mp3')
    click_sound = load_wav('sound/SE_Window_Open.wav')
    click_sound.set_volume(20)
    sound.set_volume(20)
    sound.repeat_play()

    pass

def exit():
    global image, sound, click_sound
    del image, sound, click_sound
    pass

def draw():
    clear_canvas()
    image.draw(400, 300)
    update_canvas()

def update():
    global clicked, set_time, cur_time
    handle_events()

    cur_time = time()
    if clicked == True and cur_time >= set_time + 2:
        game_framework.change_state(ready_state)

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