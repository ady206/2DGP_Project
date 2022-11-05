from pico2d import *
import game_framework
import middle_state

image = None
character_image = None

choose = False
x, y = 0, 0

def handle_events():
    global character_image, choose, x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
            elif event.key == SDLK_RETURN:
                middle_state.image = load_image('map/stage1.png')
                game_framework.change_state(middle_state)
        elif event.type == SDL_MOUSEBUTTONDOWN:
            x, y = event.x, 600 - 1 - event.y
            #  y 280 < 390 < 500 x 25 < 130 < 240 < 345 < 450 < 560 < 665 < 770
            if 280 <= y <= 500 and 25 <= x <= 770:
                choose = True


def enter():
    global image
    image = load_image('map/ready.png')
    pass

def exit():
    global image
    del image
    pass

def draw():
    global choose, x, y
    clear_canvas()
    image.draw(390, 300)

    #  y 280 < 390 < 500 x 25 < 130 < 240 < 345 < 450 < 560 < 665 < 770
    if choose == True:
        character_image = load_image('map/choose.png')
        if 390 <= y < 500:
            if 25 <= x < 130:
                character_image.clip_draw(0, 0, 150, 120, 410, 140)
            if 130 <= x < 240:
                character_image.clip_draw(150, 0, 150, 120, 405, 140)
            if 240 <= x < 345:
                character_image.clip_draw(320, 0, 150, 120, 410, 140)
            if 345 <= x < 450:
                character_image.clip_draw(470, 0, 150, 120, 410, 140)
            if 450 <= x < 560:
                character_image.clip_draw(620, 0, 150, 120, 405, 140)
            if 560 <= x < 665:
                character_image.clip_draw(0, 125, 150, 120, 410, 140)
            if 665 <= x < 770:
                character_image.clip_draw(170, 125, 150, 120, 410, 140)
        elif 280 <= y <= 390:
            if 25 <= x < 130:
                character_image.clip_draw(320, 125, 150, 120, 410, 140)
            if 130 <= x < 240:
                character_image.clip_draw(470, 125, 150, 120, 405, 140)
            if 240 <= x < 345:
                character_image.clip_draw(620, 125, 150, 120, 410, 140)
            if 345 <= x < 450:
                character_image.clip_draw(0, 250, 150, 120, 410, 140)
            if 450 <= x < 560:
                character_image.clip_draw(160, 250, 150, 120, 405, 140)
            if 560 <= x < 665:
                character_image.clip_draw(310, 250, 150, 120, 410, 140)
            if 665 <= x < 770:
                character_image.clip_draw(470, 250, 150, 120, 410, 140)

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