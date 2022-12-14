from pico2d import *
import game_framework

image = None
sound = None
win = False

# 927 618
def handle_events():
    global stack
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE or event.key == SDLK_RETURN:
                game_framework.quit()
        elif event.type == SDL_MOUSEBUTTONDOWN:
            game_framework.quit()

def enter():
    global image, sound
    if win == False:
        image = load_image('map/middle defeat.png')
    else:
        image = load_image('map/middle win.png')
        sound = load_wav('sound/SE_Cheer.wav')
        sound.set_volume(20)
        sound.play()
    pass

def exit():
    global image, sound
    del image, sound
    pass

def draw():
    clear_canvas()
    image.draw(450, 300)
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