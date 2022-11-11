import game_framework
import game_world
import middle_state
import result_state
from time import *

import character
from map import *

##############################################################################################################

def handle_events():
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
            if sound_on == True:
                sound.repeat_play()
            else: sound.stop()
        else:
            character.player_character.handle_event(event)

##############################################################################################################

set_stage_time = 0
cur_stage_time = 0
timer = 0
stage_time = 600

stage = None
sound = None
sound_on = True
font = None

stage_count = 0

def enter():
    global stage, stage_count, sound, set_stage_time, font
    set_stage_time = time()
    font = load_font('ENCR10B.TTF', 30)

    stage = Palm()

    character.human = False
    for i in range (3):
        character.RandomCharacter()

    sound = load_music('sound/Tropical.mp3')
    sound.set_volume(20)
    sound.repeat_play()

    game_world.add_object(character.player_character, 1)
    for in_character in character.computer_character:
        game_world.add_object(in_character, 1)
    game_world.add_object(stage, 0)

    character.player_character.x = 300
    character.computer_character[0].x = 100
    character.computer_character[1].x = 500
    character.computer_character[2].x = 700

def exit():
    global stage, sound
    del stage, sound

def update():
    global set_stage_time, cur_stage_time, timer, stage_time
    for game_object in game_world.all_objects():
        game_object.update()

    cur_stage_time = time()
    timer = cur_stage_time - set_stage_time
    stage_time = 600 - timer

    if timer >= 600:
        result_state.win = False
        game_framework.change_state(result_state)

def draw_world():
    global font, stage_time
    for game_object in game_world.all_objects():
        game_object.draw()

    tm = localtime(stage_time)
    font.draw(350, 560, f'{tm.tm_min} : {tm.tm_sec}', (0, 0, 0))

def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def pause():
    global stage_count, sound
    stage_count += 1
    sound.stop()
    game_world.remove_object(stage)

def resume():
    global stage, stage_count, sound_on, sound, set_stage_time
    if stage_count == 1:
        stage = Lake()
        sound = load_music('sound/Tropical.mp3')
        if sound_on == True:
            sound.set_volume(20)
            sound.repeat_play()
        else:
            sound.stop()
    if stage_count == 2:
        stage = Space()
        sound = load_music('sound/Tropical.mp3')
        if sound_on == True:
            sound.set_volume(20)
            sound.repeat_play()
        else:
            sound.stop()

    game_world.add_object(stage, 0)

    character.player_character.x = 300
    character.computer_character[0].x = 100
    character.computer_character[1].x = 500
    character.computer_character[2].x = 700

    set_stage_time = time()
    pass

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

def test_self():
    import sys
    this_module = sys.modules['__main__']
    open_canvas()
    game_framework.run(this_module)
    close_canvas()

if __name__ == '__main__': # 만약 단독 실행 상태이면
    test_self()