import game_framework
import game_world
import middle_state
import result_state

from time import *
from random import *

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

def drawTimer(a, b):
    size = 30
    # minute
    if 0 <= a <= 4:
        stage.timer_image.clip_composite_draw(39 * a, 36, 26, 22, 0, ' ', 370, 560, size, size)
    if 5 <= a <= 9:
        stage.timer_image.clip_composite_draw(39 * (a - 5), 0, 26, 22, 0, ' ', 370, 560, size, size)
    if a == 10:
        stage.timer_image.clip_composite_draw(39, 36, 26, 22, 0, ' ', 345, 560, size, size)
        stage.timer_image.clip_composite_draw(0, 36, 26, 22, 0, ' ', 370, 560, size, size)

    # :
    for i in range(2):
        stage.timer_image.clip_composite_draw(39 * 5, 0, 26, 22, 0, ' ', 400, 560 + (i * 10), 22, 22)

    # second 10
    if 0 <= b // 10 <= 4:
        stage.timer_image.clip_composite_draw(39 * (b // 10), 36, 26, 22, 0, ' ', 430, 560, size, size)
    if b // 10 == 5:
        stage.timer_image.clip_composite_draw(0, 0, 26, 22, 0, ' ', 430, 560, size, size)

    # second 1
    if 0 <= b % 10 <= 4:
        stage.timer_image.clip_composite_draw(39 * (b % 10), 36, 26, 22, 0, ' ', 465, 560, size, size)
    if 5 <= b % 10 <= 9:
        stage.timer_image.clip_composite_draw(39 * ((b % 10) - 5), 0, 26, 22, 0, ' ', 465, 560, size, size)

def drawHp(a, x, y):
    # a // 100
    if a // 100 == 1:
        stage.timer_image.clip_composite_draw(39, 36, 26, 22, 0, ' ', x - 44, y, 22, 22)

    # (a % 100 // 10)
    b = (a % 100) // 10
    if 0 <= b <= 4:
        stage.timer_image.clip_composite_draw(39 * b, 36, 26, 22, 0, ' ', x - 22, y, 22, 22)
    if 5 <= b <= 9:
        stage.timer_image.clip_composite_draw(39 * (b - 5), 0, 26, 22, 0, ' ', x - 22, y, 22, 22)

    # a % 10
    if 0 <= a % 10 <= 4:
        stage.timer_image.clip_composite_draw(39 * (a % 10), 36, 26, 22, 0, ' ', x, y, 22, 22)
    if 5 <= a % 10 <= 9:
        stage.timer_image.clip_composite_draw(39 * ((a % 10) - 5), 0, 26, 22, 0, ' ', x, y, 22, 22)

def drawIcon(a, x, y):
    a.icon_image.clip_composite_draw(30 * a.Index(), 0, 30, 23, 0, ' ', x, y, 40, 30)

##############################################################################################################

set_stage_time = 0
cur_stage_time = 0
timer = 0
stage_time = 600

stage = None
sound = None
sound_on = True

stage_count = 0

def enter():
    global stage, stage_count, sound, set_stage_time, font
    set_stage_time = time()

    stage = Palm(character.player_character.x, 300)
    character.human = False
    for i in range (3):
        character.RandomCharacter()

    sound = load_music('sound/Tropical.mp3')
    sound.set_volume(20)
    sound.repeat_play()

    game_world.add_object(character.player_character, 2)
    for in_character in character.computer_character:
        game_world.add_object(in_character, 1)
    game_world.add_object(stage, 0)

    character.player_character.x = 400
    character.computer_character[0].x = randint(100, 700)
    character.computer_character[1].x = randint(100, 700)
    character.computer_character[2].x = randint(100, 700)

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
    if character.player_character.hp <= 0:
        result_state.win = False
        game_framework.change_state(result_state)

    distance_x = character.player_character.dir_x * character.RUN_SPEED_PPS * game_framework.frame_time
    stage.x -= distance_x
    for in_character in character.computer_character:
        in_character.x -= distance_x

def draw_world():
    global stage_time
    for game_object in game_world.all_objects():
        game_object.draw()

    number_character = 0
    tm = localtime(stage_time)
    drawTimer(tm.tm_min, tm.tm_sec)
    drawHp(character.player_character.hp, 150, 50)
    drawIcon(character.player_character, 70, 50)

    for in_character in character.computer_character:
        drawHp(in_character.hp, 350 + (number_character * 200), 50)
        drawIcon(in_character, 270 + (number_character * 200), 50)
        number_character += 1

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
        stage = Lake(character.player_character.x, 300)
        sound = load_music('sound/Lake.mp3')
        if sound_on == True:
            sound.set_volume(20)
            sound.repeat_play()
        else:
            sound.stop()
    if stage_count == 2:
        stage = Space(character.player_character.x, 300)
        sound = load_music('sound/Space.mp3')
        if sound_on == True:
            sound.set_volume(20)
            sound.repeat_play()
        else:
            sound.stop()
    game_world.add_object(stage, 0)

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