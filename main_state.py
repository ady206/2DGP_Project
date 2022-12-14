import game_framework
import game_world
import middle_state
import result_state

from time import *
from random import *

import character
from map import *
import server

##############################################################################################################

def handle_events():
    global stage, stage_count, sound, sound_on
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_F8):
            sound_on = ~sound_on
            if sound_on == True:
                sound.repeat_play()
            else: sound.stop()
        else:
            server. player_character.handle_event(event)

def Count(a, x, y):
    if 0 <= a % 10 <= 4:
        server.stage.timer_image.clip_composite_draw(39 * (a % 10), 36, 26, 22, 0, ' ', x, y, 30, 30)
    if 5 <= a % 10 <= 9:
        server.stage.timer_image.clip_composite_draw(39 * ((a % 10) - 5), 0, 26, 22, 0, ' ', x, y, 30, 30)

def drawTimer(a, b):
    size = 30
    # minute
    if 0 <= a <= 4:
        server.stage.timer_image.clip_composite_draw(39 * a, 36, 26, 22, 0, ' ', 370, 560, size, size)
    if 5 <= a <= 9:
        server.stage.timer_image.clip_composite_draw(39 * (a - 5), 0, 26, 22, 0, ' ', 370, 560, size, size)
    if a == 10:
        server.stage.timer_image.clip_composite_draw(39, 36, 26, 22, 0, ' ', 345, 560, size, size)
        server.stage.timer_image.clip_composite_draw(0, 36, 26, 22, 0, ' ', 370, 560, size, size)

    # :
    for i in range(2):
        server.stage.timer_image.clip_composite_draw(39 * 5, 0, 26, 22, 0, ' ', 400, 560 + (i * 10), 22, 22)

    # second 10
    if 0 <= b // 10 <= 4:
        server.stage.timer_image.clip_composite_draw(39 * (b // 10), 36, 26, 22, 0, ' ', 430, 560, size, size)
    if b // 10 == 5:
        server.stage.timer_image.clip_composite_draw(0, 0, 26, 22, 0, ' ', 430, 560, size, size)

    # second 1
    if 0 <= b % 10 <= 4:
        server.stage.timer_image.clip_composite_draw(39 * (b % 10), 36, 26, 22, 0, ' ', 465, 560, size, size)
    if 5 <= b % 10 <= 9:
        server.stage.timer_image.clip_composite_draw(39 * ((b % 10) - 5), 0, 26, 22, 0, ' ', 465, 560, size, size)

def drawHp(a, x, y):
    # a // 100
    if a // 100 == 1:
        server.stage.timer_image.clip_composite_draw(39, 36, 26, 22, 0, ' ', x - 44, y, 22, 22)

    # (a % 100 // 10)
    b = (a % 100) // 10
    if 0 <= b <= 4:
        server.stage.timer_image.clip_composite_draw(39 * b, 36, 26, 22, 0, ' ', x - 22, y, 22, 22)
    if 5 <= b <= 9:
        server.stage.timer_image.clip_composite_draw(39 * (b - 5), 0, 26, 22, 0, ' ', x - 22, y, 22, 22)

    # a % 10
    if 0 <= a % 10 <= 4:
        server.stage.timer_image.clip_composite_draw(39 * (a % 10), 36, 26, 22, 0, ' ', x, y, 22, 22)
    if 5 <= a % 10 <= 9:
        server.stage.timer_image.clip_composite_draw(39 * ((a % 10) - 5), 0, 26, 22, 0, ' ', x, y, 22, 22)

def drawIcon(a, x, y):
    a.icon_image.clip_composite_draw(30 * a.Index(), 0, 30, 23, 0, ' ', x, y, 40, 30)

##############################################################################################################

set_stage_time = 0
cur_stage_time = 0
timer = 0
stage_time = 600

hit_time = 0
hit_delay_time = 0

sound = None
sound_on = True

stage_count = 0

def enter():
    global stage_count, sound, set_stage_time
    set_stage_time = time()

    server.stage = Palm()
    AppendPalmFloor()

    character.human = False
    for i in range (3):
        character.RandomCharacter(server.player_character, server.computer_character)
    character.Prepare()

    sound = load_music('sound/Tropical.mp3')
    sound.set_volume(20)
    sound.repeat_play()

    game_world.add_object(server.player_character, 2)
    for i in range(3):
        game_world.add_object(server.computer_character[i], 1)
    game_world.add_object(server.stage, 0)
    for i in server.stage_floor:
        game_world.add_object(i, 0)

    game_world.add_collision_group(server.player_character, server.computer_character, 'player_character:computer_character')
    game_world.add_collision_group(server.player_character, server.stage_floor, 'player_character:stage_floor')
    game_world.add_collision_group(server.player_character, server.stage_floor, 'computer_character:stage_floor')

    server.player_character.x = server.stage.w // 2
    for i in range(3):
        server.computer_character[i].x = randint(server.stage.w // 2 - 300, server.stage.w // 2 + 300)

    for in_character in server.computer_character:
        in_character.build_behavior_tree()

def exit():
    global sound
    del sound

def update():
    global set_stage_time, cur_stage_time, timer, stage_time
    for game_object in game_world.all_objects():
        game_object.update()

    cur_stage_time = time()
    timer = cur_stage_time - set_stage_time
    stage_time = 300 - timer

    global hit_time, hit_delay_time

    for in_character in server.computer_character:
        in_character.x += in_character.speed * math.cos(in_character.dir) * game_framework.frame_time
        in_character.y += in_character.speed * math.sin(in_character.dir) * game_framework.frame_time
        in_character.x = clamp(server.stage.w // 2 - 400, in_character.x, server.stage.w // 2 + 400)

        in_character.damage = 5
        if 0 <= stage_time % 3 <= in_character.TIMER_PER_ACTION[3]:
            in_character.cur_state = character.COMATTACK
            if collide(in_character, server.player_character):
                if server.player_character.hit == False:
                    hit_time = time()
                    server.player_character.hp -= in_character.damage
                    server.player_character.x -= 15
                server.player_character.hit = True
                hit_delay_time = time()

                if hit_delay_time >= hit_time + 2:
                    server.player_character.hit = False
        else:
            in_character.cur_state = character.COMRUN

        in_character.bt.run()

    if stage_time <= 0:
        result_state.win = False
        game_framework.change_state(result_state)
    if server.player_character.y <= 0:
        result_state.win = False
        game_framework.change_state(result_state)
    if server.player_character.hp <= 0:
        result_state.win = False
        game_framework.change_state(result_state)

    if server.cleared >= 10:
        server.cleared = 0
        if (stage_count >= 2):
            result_state.win = True
            game_framework.change_state(result_state)
        else:
            game_framework.push_state(middle_state)

def draw_world():
    global stage_time
    for game_object in game_world.all_objects():
        game_object.draw()

    tm = localtime(stage_time)
    drawTimer(tm.tm_min, tm.tm_sec)
    drawHp(server.player_character.hp, 150, 50)
    drawIcon(server.player_character, 70, 50)
    Count(server.cleared, 750, 560)
    for i in range(3):
        drawHp(server.computer_character[i].hp, 350 + (i * 200), 50)
        drawIcon(server.computer_character[i], 270 + (i * 200), 50)

def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def pause():
    global stage_count, sound
    stage_count += 1
    sound.stop()
    server.player_character.hp = 100
    server.player_character.cur_state.exit(server.player_character, character.NULL)
    server.player_character.cur_state = character.IDLE
    server.player_character.cur_state.enter(server.player_character, character.NULL)
    game_world.clear()
    server.stage = None
    server.computer_character.clear()
    server.stage_floor.clear()
    server.prepare_list.clear()

    character.human = False
    for i in range (3):
        character.RandomCharacter(server.player_character, server.computer_character)
        server.computer_character[i].hp = 100
    character.Prepare()
    game_world.add_object(server.player_character, 2)
    for i in range(3):
        game_world.add_object(server.computer_character[i], 1)

def resume():
    global stage_count, sound_on, sound, set_stage_time
    if stage_count == 1:
        server.stage = Lake()
        AppendLakeFloor()
        sound = load_music('sound/Lake.mp3')
        if sound_on == True:
            sound.set_volume(20)
            sound.repeat_play()
        else:
            sound.stop()
    if stage_count == 2:
        server.stage = Space()
        AppendSpaceFloor()
        sound = load_music('sound/Space.mp3')
        if sound_on ==  True:
            sound.set_volume(20)
            sound.repeat_play()
        else:
            sound.stop()

    game_world.add_object(server.stage, 0)
    for i in server.stage_floor:
        game_world.add_object(i, 0)

    game_world.add_collision_group(server.player_character, server.computer_character,
                                   'player_character:computer_character')
    game_world.add_collision_group(server.player_character, server.stage_floor, 'player_character:stage_floor')
    game_world.add_collision_group(server.player_character, server.stage_floor, 'computer_character:stage_floor')
    server.player_character.x = server.stage.w // 2
    for i in range(3):
        server.computer_character[i].x = randint(server.stage.w // 2 - 300, server.stage.w // 2 + 300)

    for in_character in server.computer_character:
        in_character.build_behavior_tree()

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