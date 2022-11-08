from pico2d import *
from math import *
from random import *

import character
import game_framework
import middle_state
import result_state

from character import *
from map import *

stage = None
sound = None
sound_on = True

stage_count = 0
##############################################################################################################

def handle_events():
    global player_character, computer_character
    global stage, stage_count, sound, sound_on
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RETURN):
            if(stage_count >= 2):
                result_state.win = True
                game_framework.change_state(result_state)
            else:
                game_framework.push_state(middle_state)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_F8):
            sound_on = ~sound_on
            if(sound_on == True): sound.repeat_play()
            else: sound.stop()
        else:
            character.player_character.handle_event(event)

##############################################################################################################

def enter():
    global stage, stage_count, sound
    stage = Palm()

    character.human = False
    # for i in range (3):
    #     character.RandomCharacter()

    sound = load_music('sound/Tropical.mp3')
    sound.set_volume(20)
    sound.repeat_play()

    game_world.add_object(character.player_character, 1)
    for in_character in character.computer_character:
        game_world.add_object(in_character, 1)
    game_world.add_object(stage, 0)

    character.player_character.x = 400
    # character.computer_character[0].x = 200
    # character.computer_character[1].x = 500
    # character.computer_character[2].x = 600

def exit():
    global stage, sound
    del stage, sound

def update():
    for game_object in game_world.all_objects():
        game_object.update()

def draw_world():
    for game_object in game_world.all_objects():
        game_object.draw()

def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def pause():
    global stage_count
    stage_count += 1
    middle_state.image = load_image('map/stage1.png')
    if(stage_count == 1):
        middle_state.image = load_image('map/stage2.png')
    if(stage_count == 2):
        middle_state.image = load_image('map/stage3.png')

def resume():
    # global player_character, stage, stage_count, sound
    # if stage_count == 1:
    #     player_character = Tales()
    #     stage = Lake()
    #     sound = load_music('sound/Tropical.mp3')
    #     sound.set_volume(20)
    #     sound.repeat_play()
    # if stage_count == 2:
    #     player_character = Tikal()
    #     stage = Space()
    #     sound = load_music('sound/Tropical.mp3')
    #     sound.set_volume(20)
    #     sound.repeat_play()
    pass

def test_self():
    import sys
    this_module = sys.modules['__main__']
    open_canvas()
    game_framework.run(this_module)
    close_canvas()

if __name__ == '__main__': # 만약 단독 실행 상태이면
    test_self()