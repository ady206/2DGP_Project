from pico2d import *
import game_framework
import middle_state
import character
from random import *

image = None
character_image = None
character_name = None

choose = False
x, y = 0, 0

go = False
def handle_events():
    global choose, human, go, x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
            elif event.key == SDLK_RETURN:
                middle_state.image = load_image('map/stage1.png')
                if go == True:
                    game_framework.change_state(middle_state)
        elif event.type == SDL_MOUSEBUTTONDOWN:
            x, y = event.x, 600 - 1 - event.y
            if 280 <= y <= 500 and 25 <= x <= 770:
                choose = True
                go = True
                if 390 <= y < 500:
                    if 25 <= x < 130:
                        character.player_character = character.Sonic()
                    if 130 <= x < 240:
                        character.player_character = character.Tales()
                    if 240 <= x < 345:
                        character.player_character = character.Knuckles()
                    if 345 <= x < 450:
                        character.player_character = character.AmyRose()
                    if 450 <= x < 560:
                        character.player_character = character.Tikal()
                    if 560 <= x < 665:
                        character.player_character = character.Rouge()
                    if 665 <= x < 770:
                        character.player_character = character.Shadow()
                elif 280 <= y <= 390:
                    if 25 <= x < 130:
                        character.player_character = character.Silver()
                    if 130 <= x < 240:
                        character.player_character = character.Blaze()
                    if 240 <= x < 345:
                        character.player_character = character.Espio()
                    if 345 <= x < 450:
                        character.player_character = character.Mighty()
                    if 450 <= x < 560:
                        character.player_character = character.SuperSonic()
                    if 560 <= x < 665:
                        character.player_character = character.SuperShadow()
                    if 665 <= x < 770:
                        human = True
                        character.RandomCharacter()


def enter():
    global image
    image = load_image('map/ready.png')
    pass

def exit():
    global image
    del image
    pass

def draw():
    global choose, character_image, character_name, stage_go, x, y
    clear_canvas()
    image.draw(390, 300)

    #  y 280 < 390 < 500 x 25 < 130 < 240 < 345 < 450 < 560 < 665 < 770
    if choose == True:
        character_image = load_image('map/choose.png')
        character_name = load_image('map/names.png')
        # stage_go = load_image('map/go.png')

        # stage_go.clip_draw(0, 0, 230, 115, 685, 50)
        if 390 <= y < 500:
            if 25 <= x < 130:
                character_image.clip_draw(0, 0, 150, 120, 410, 140)
                character_name.clip_draw(0, 0, 100, 23, 410, 47)
            if 130 <= x < 240:
                character_image.clip_draw(150, 0, 150, 120, 405, 140)
                character_name.clip_draw(0, 23, 100, 23, 410, 47)
            if 240 <= x < 345:
                character_image.clip_draw(320, 0, 150, 120, 410, 140)
                character_name.clip_draw(0, 46, 100, 23, 410, 47)
            if 345 <= x < 450:
                character_image.clip_draw(470, 0, 150, 120, 410, 140)
                character_name.clip_draw(0, 69, 100, 23, 410, 47)
            if 450 <= x < 560:
                character_image.clip_draw(620, 0, 150, 120, 405, 140)
                character_name.clip_draw(0, 92, 100, 23, 410, 47)
            if 560 <= x < 665:
                character_image.clip_draw(0, 125, 150, 120, 410, 140)
                character_name.clip_draw(0, 115, 100, 23, 410, 47)
            if 665 <= x < 770:
                character_image.clip_draw(170, 125, 150, 120, 410, 140)
                character_name.clip_draw(0, 138, 100, 23, 410, 47)
        elif 280 <= y <= 390:
            if 25 <= x < 130:
                character_image.clip_draw(320, 125, 150, 120, 410, 140)
                character_name.clip_draw(0, 161, 100, 23, 410, 47)
            if 130 <= x < 240:
                character_image.clip_draw(470, 125, 150, 120, 405, 140)
                character_name.clip_draw(0, 186, 100, 23, 410, 47)
            if 240 <= x < 345:
                character_image.clip_draw(620, 125, 150, 120, 410, 140)
                character_name.clip_draw(0, 211, 100, 23, 410, 47)
            if 345 <= x < 450:
                character_image.clip_draw(0, 250, 150, 120, 410, 140)
                character_name.clip_draw(0, 236, 100, 23, 410, 47)
            if 450 <= x < 560:
                character_image.clip_draw(160, 250, 150, 120, 405, 140)
                character_name.clip_draw(0, 261, 100, 23, 410, 47)
            if 560 <= x < 665:
                character_image.clip_draw(310, 250, 150, 120, 410, 140)
                character_name.clip_draw(0, 286, 100, 23, 410, 47)
            if 665 <= x < 770:
                character_image.clip_draw(470, 250, 150, 120, 410, 140)
                character_name.clip_draw(0, 311, 100, 23, 405, 47)

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