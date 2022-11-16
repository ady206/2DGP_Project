from pico2d import *
import game_world
import game_framework

from random import *
from time import *

import main_state

player_character = None
computer_character = []

list = ['Sonic', 'Tales', 'Knuckles', 'AmyRose', 'Tikal', 'Rouge', 'Shadow',
             'Silver', 'Blaze', 'Espio', 'Mighty', 'Super Sonic', 'Super Shadow']
human = False

def RandomCharacter():
    global player_character, computer_character, human
    rc = choice(list)
    if human == True:
        if rc == 'Sonic':
            player_character = Sonic()
        elif rc == 'Tales':
            player_character = Tales()
        elif rc == 'Knuckles':
            player_character = Knuckles()
        elif rc == 'AmyRose':
            player_character = AmyRose()
        elif rc == 'Tikal':
            player_character = Tikal()
        elif rc == 'Rouge':
            player_character = Rouge()
        elif rc == 'Shadow':
            player_character = Shadow()
        elif rc == 'Silver':
            player_character = Silver()
        elif rc == 'Blaze':
            player_character = Blaze()
        elif rc == 'Espio':
            player_character = Espio()
        elif rc == 'Mighty':
            player_character = Mighty()
        elif rc == 'Super Sonic':
            player_character = SuperSonic()
        elif rc == 'Super Shadow':
            player_character = SuperShadow()
    else:
        if rc == 'Sonic':
            computer_character.append(Sonic())
        elif rc == 'Tales':
            computer_character.append(Tales())
        elif rc == 'Knuckles':
            computer_character.append(Knuckles())
        elif rc == 'AmyRose':
            computer_character.append(AmyRose())
        elif rc == 'Tikal':
            computer_character.append(Tikal())
        elif rc == 'Rouge':
            computer_character.append(Rouge())
        elif rc == 'Shadow':
            computer_character.append(Shadow())
        elif rc == 'Silver':
            computer_character.append(Silver())
        elif rc == 'Blaze':
            computer_character.append(Blaze())
        elif rc == 'Espio':
            computer_character.append(Espio())
        elif rc == 'Mighty':
            computer_character.append(Mighty())
        elif rc == 'Super Sonic':
            computer_character.append(SuperSonic())
        elif rc == 'Super Shadow':
            computer_character.append(SuperShadow())

##############################################################################################################

NULL, RD, LD, RU, LU, SPACE, JUMP = range(7)
event_name = ['NULL', 'RD', 'LD', 'RU', 'LU', 'SPACE', 'JUMP' ]
key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE,
    (SDL_KEYDOWN, SDLK_UP): JUMP
}

move_dir = [ False, False ]
set_time, cur_time = 0, 0

class IDLE:
    global move_dir
    @staticmethod
    def enter(self, event):
        if event == RU:
            self.dir_x = 0
            move_dir[0] = False
        elif event == LU:
            self.dir_x = 0
            move_dir[1] = False

    @staticmethod
    def exit(self, event):
        pass

    def do(self):
        self.idle_type[0] = self.idle_size

    def draw(self):
        self.image.clip_composite_draw(self.idle_type[0],self.idle_type[1],self.idle_type[2],self.idle_type[3],
                                            self.rotate, self.face_dir,
                                            self.x, self.y, self.idle_type[4], self.idle_type[5])

class RUN:
    global move_dir, RUN_SPEED_PPS
    def enter(self, event):
        if event == RD:
            move_dir[0] = True
        elif event == LD:
            move_dir[1] = True
        if event == RU:
            move_dir[0] = False
        elif event == LU:
            move_dir[1] = False

        if move_dir[0] == True:
            self.dir_x = 1
            self.face_dir = 'None'
        if move_dir[1] == True:
            self.dir_x = -1
            self.face_dir = 'h'
        if move_dir[0] == False and move_dir[1] == False:
            self.dir_x = 0
            self.cur_state.exit(self, NULL)
            try:
                self.cur_state = next_state[IDLE][NULL]
            except KeyError:
                print('Error', self.cur_state.__name__, ' ', "None")
            self.cur_state.enter(self, NULL)

    def exit(self, event):
        pass

    def do(self):
        self.move_type[0] = self.move_size
        self.x += self.dir_x * RUN_SPEED_PPS * game_framework.frame_time
        self.x = 400

    def draw(self):
        self.image.clip_composite_draw(self.move_type[0], self.move_type[1], self.move_type[2], self.move_type[3],
                                            self.rotate, self.face_dir,
                                            self.x, self.y, self.move_type[4], self.move_type[5])

class Player_JUMP:
    global move_dir, JUMP_SPEED_PPS
    @staticmethod
    def enter(self, event):
        global set_time
        if event == JUMP:
            set_time = time()
            self.jump_frame = 0
            self.jump_sound.set_volume(10)
            self.jump_sound.play(1)

        print('ENTER JUMP')
        if event == RD:
            move_dir[0] = True
        elif event == LD:
            move_dir[1] = True
        if event == RU:
            move_dir[0] = False
        elif event == LU:
            move_dir[1] = False

        if move_dir[0] == True:
            self.dir_x = 1
            self.face_dir = 'None'
        if move_dir[1] == True:
            self.dir_x = -1
            self.face_dir = 'h'
        if move_dir[0] == False and move_dir[1] == False:
            self.dir_x = 0

    @staticmethod
    def exit(self, event):
        print('exit JUMP')

    @staticmethod
    def do(self):
        global cur_time, set_time
        self.jump_type[0] = self.jump_size

        cur_time = time()
        if cur_time < set_time + (self.TIMER_PER_ACTION[2] / 2):
            self.dir_y = 1
            self.y += self.dir_y * JUMP_SPEED_PPS * game_framework.frame_time
        elif set_time + (self.TIMER_PER_ACTION[2] / 2) <= cur_time <= set_time + self.TIMER_PER_ACTION[2]:
            self.dir_y = -1
            self.y += self.dir_y * JUMP_SPEED_PPS * game_framework.frame_time
        elif cur_time > set_time + self.TIMER_PER_ACTION[2] :
            self.dir_y = 0
            self.y = 130
            self.cur_state.exit(self, NULL)
            try:
                self.cur_state = next_state[RUN][NULL]
            except KeyError:
                print('Error', self.cur_state.__name__, ' ', "None")
            self.cur_state.enter(self, NULL)

    @staticmethod
    def draw(self):
        self.image.clip_composite_draw(self.jump_type[0], self.jump_type[1], self.jump_type[2], self.jump_type[3],
                                       self.rotate, self.face_dir,
                                       self.x, self.y, self.jump_type[4], self.jump_type[5])

class ATTACK:
    @staticmethod
    def enter(self, event):
        global set_time
        if event == SPACE:
            set_time = time()
            self.attack_frame = 0
            self.attack += 1

            if self.attack % 2 == 0:
                self.kick_sound.set_volume(10)
                self.kick_sound.play(1)
            if self.attack % 2 == 1:
                self.punch_sound.set_volume(10)
                self.punch_sound.play(1)

        if event == RD:
            move_dir[0] = True
        elif event == LD:
            move_dir[1] = True
        if event == RU:
            move_dir[0] = False
        elif event == LU:
            move_dir[1] = False

        if move_dir[0] == True:
            self.dir_x = 1
            self.face_dir = 'None'
        if move_dir[1] == True:
            self.dir_x = -1
            self.face_dir = 'h'
        if move_dir[0] == False and move_dir[1] == False:
            self.dir_x = 0

    @staticmethod
    def exit(self, event):
        pass

    @staticmethod
    def do(self):
        global cur_time, set_time
        self.attack_type[0] = self.attack_size

        cur_time = time()

        if cur_time > set_time + self.TIMER_PER_ACTION[3]:
            if len(computer_character) >= 3:
                Attacked_Character(3)
            else:
                Attacked_Character(len(computer_character))

            self.cur_state.exit(self, NULL)
            try:
                if move_dir[0] == False and move_dir[1] == False:
                    self.cur_state = next_state[IDLE][NULL]
                else:
                    self.cur_state = next_state[RUN][NULL]
            except KeyError:
                print('Error', self.cur_state.__name__, ' ', "None")
            self.cur_state.enter(self, NULL)
    @staticmethod
    def draw(self):
        self.image.clip_composite_draw(self.attack_type[0],self.attack_type[1],self.attack_type[2],self.attack_type[3],
                                       self.rotate, self.face_dir,
                                       self.x, self.y, self.attack_type[4], self.attack_type[5])

next_state = {
    IDLE:  {RU: IDLE, RD: RUN,
            LU: IDLE, LD: RUN,
            NULL: IDLE, SPACE: ATTACK, JUMP: Player_JUMP},
    RUN:   {RU: RUN, RD: RUN,
            LU: RUN, LD: RUN,
            NULL: RUN, SPACE: ATTACK, JUMP: Player_JUMP},
    Player_JUMP:   {RU: Player_JUMP, RD: Player_JUMP,
                    LU: Player_JUMP, LD: Player_JUMP,
                    NULL: Player_JUMP, SPACE: Player_JUMP, JUMP: Player_JUMP},
    ATTACK:   {RU: ATTACK, RD: ATTACK,
               LU: ATTACK, LD: ATTACK,
               NULL: ATTACK, SPACE: ATTACK, JUMP: ATTACK},
}

def Attacked_Character(character_count):
    for i in range(character_count):
        if main_state.collide(player_character, computer_character[i]):
            computer_character[i].hp -= player_character.damage
            if computer_character[i].hp <= 0:
                game_world.remove_object(computer_character[i])
                del computer_character[i]

                if len(computer_character) >= 3:
                    game_world.add_object(computer_character[2], 1)
                    computer_character[2].x = main_state.stage.x + randint(-300, 300)

########################################

PIXEL_PER_METER = 10.0 / 0.3
RUN_SPEED_KPH = 20.0 # 마라토너의 평속
RUN_SPEED_MPS = RUN_SPEED_KPH * 1000.0 / 3600.0
RUN_SPEED_PPS = RUN_SPEED_MPS * PIXEL_PER_METER

JUMP_SPEED_MPS = 20.0
PIXEL_PER_JUMP_METER = 10.0 / 0.5
JUMP_SPEED_PPS = JUMP_SPEED_MPS * PIXEL_PER_JUMP_METER

########################################

class Character:
    def __init__(self):
        self.hp = 100
        self.speed = 1.2

        self.idle_frame = 0
        self.move_frame = 0
        self.jump_frame = 0
        self.attack_frame = 0

        self.idle_size = 0
        self.move_size = 0
        self.jump_size = 0
        self.attack_size = 0

        self.FRAMES_PER_ACTION = []
        self.TIMER_PER_ACTION = []

        self.attack = 0
        self.damage = 50
        self.jump_high = 130

        self.face_dir = 'None'  # 이미지 반전
        self.rotate = 0 # 이미지 회전

        self.punch_sound = load_wav('sound/06_attack.wav')
        self.kick_sound = load_wav('sound/05_kickback.wav')
        self.jump_sound = load_wav('sound/00_jump.wav')
        self.dir_x, self.dir_y = 0, 0
        self.x, self.y = 400, 130

        self.event_que = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

    def update(self):
        if self.event_que:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            try:
                self.cur_state = next_state[self.cur_state][event]
            except KeyError:
                print('Error', self.cur_state.__name__, ' ', event)
            self.cur_state.enter(self, event)

        self.idle_frame = (self.idle_frame + self.FRAMES_PER_ACTION[0] / self.TIMER_PER_ACTION[0] * game_framework.frame_time) % self.FRAMES_PER_ACTION[0]
        self.move_frame = (self.move_frame + self.FRAMES_PER_ACTION[1] / self.TIMER_PER_ACTION[1] * game_framework.frame_time) % self.FRAMES_PER_ACTION[1]
        self.jump_frame = (self.jump_frame + self.FRAMES_PER_ACTION[2] / self.TIMER_PER_ACTION[2] * game_framework.frame_time) % self.FRAMES_PER_ACTION[2]
        self.attack_frame = (self.attack_frame + self.FRAMES_PER_ACTION[3] / self.TIMER_PER_ACTION[3] * game_framework.frame_time) % self.FRAMES_PER_ACTION[3]

    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def Index(self):
        global list
        for i in range(13):
            if list[self.index] == list[i]:
                return i

class Sonic(Character):
    image = None
    icon_image = None
    def __init__(self):
        super(Sonic, self).__init__()
        if Sonic.image == None:
            self.image = load_image("character/sonic.png")
        if Sonic.icon_image == None:
            self.icon_image = load_image("map/icons.png")
        self.index = 0

        self.FRAMES_PER_ACTION = [8, 8, 8, 3]
        self.TIMER_PER_ACTION = [1, 1, 0.5, 0.4]

        self.idle_type = [0, 2285, 30, 40, 30, 40]
        self.move_type = [0, 1830, 40, 40, 40, 40]
        self.jump_type = [0, 1250, 35, 40, 35, 40]
        self.attack_type = [0, 950, 45, 40, 45, 40]

    def update(self):
        super(Sonic, self).update()
        self.cur_state.do(self)

        self.idle_size = int(self.idle_frame) * 30 + 7
        self.move_size = int(self.move_frame) * 40 + 10
        self.jump_size = int(self.jump_frame) * 50 + 15
        self.attack_size = int(self.attack_frame) * 45

    def draw(self):
        self.cur_state.draw(self)

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def handle_collision(self, other, group):
        pass

class Tales(Character):
    image = None
    icon_image = None
    def __init__(self):
        super(Tales, self).__init__()
        if Tales.image == None:
            self.image = load_image("character/tales.png")
        if Tales.icon_image == None:
            self.icon_image = load_image("map/icons.png")
        self.index = 1

        self.FRAMES_PER_ACTION = [8, 8, 8, 8]
        self.TIMER_PER_ACTION = [1, 1, 0.5, 0.5]

        self.idle_type = [0, 2650, 50, 40, 50, 40]
        self.move_type = [0, 2980, 50, 40, 50, 40]
        self.jump_type = [0, 2740, 40, 45, 40, 45]
        self.attack_type = [0, 2600, 52, 40, 52, 40]

    def update(self):
        super(Tales, self).update()
        self.cur_state.do(self)

        self.idle_size = int(self.idle_frame) * 52 + 20
        self.move_size = int(self.move_frame) * 55 + 10
        self.jump_size = int(self.jump_frame) * 50 + 15
        self.attack_size = int(self.attack_frame) * 55

    def draw(self):
        self.cur_state.draw(self)

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def handle_collision(self, other, group):
        pass

class Knuckles(Character):
    image = None
    icon_image = None
    def __init__(self):
        super(Knuckles, self).__init__()
        if Knuckles.image == None:
            self.image = load_image("character/knuckles.png")
        if Knuckles.icon_image == None:
            self.icon_image = load_image("map/icons.png")
        self.index = 2

        self.FRAMES_PER_ACTION = [3, 8, 8, 9]
        self.TIMER_PER_ACTION = [0.5, 1, 0.5, 0.5]

        self.idle_type = [0, 2980, 35, 40, 35, 40]
        self.move_type = [0, 2680, 40, 40, 40, 40]
        self.jump_type = [0, 1074, 45, 40, 40, 36]
        self.attack_type = [0, 1990, 50, 50, 50, 50]

    def update(self):
        super(Knuckles, self).update()
        self.cur_state.do(self)

        self.idle_size = int(self.idle_frame) * 35 + 410
        self.move_size = int(self.move_frame) * 41 + 2
        self.jump_size = int(self.jump_frame) * 51 + 2
        self.attack_size = int(self.attack_frame) * 55

    def draw(self):
        self.cur_state.draw(self)

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def handle_collision(self, other, group):
        pass

class AmyRose(Character):
    image = None
    icon_image = None
    def __init__(self):
        super(AmyRose, self).__init__()
        if AmyRose.image == None:
            self.image = load_image("character/amy rose.png")
        if AmyRose.icon_image == None:
            self.icon_image = load_image("map/icons.png")
        self.index = 3

        self.FRAMES_PER_ACTION = [3, 3, 7, 3]
        self.TIMER_PER_ACTION = [0.7, 0.7, 1, 0.3]

        self.idle_type = [0, 2750, 30, 40, 30, 40]
        self.move_type = [0, 2563, 38, 40, 38, 40]
        self.jump_type = [0, 1855, 50, 44, 50, 44]
        self.attack_type = [0, 1600, 50, 40, 45, 40]

    def update(self):
        super(AmyRose, self).update()
        self.cur_state.do(self)

        self.idle_size = int(self.idle_frame) * 28 + 2
        self.move_size = int(self.move_frame) * 41 + 2
        self.jump_size = int(self.jump_frame) * 51 + 2
        self.attack_size = int(self.attack_frame) * 55

    def draw(self):
        self.cur_state.draw(self)

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def handle_collision(self, other, group):
        pass

class Tikal(Character):
    image = None
    icon_image = None
    def __init__(self):
        super(Tikal, self).__init__()
        if Tikal.image == None:
            self.image = load_image("character/tikal.png")
        if Tikal.icon_image == None:
            self.icon_image = load_image("map/icons.png")
        self.index = 4

        self.FRAMES_PER_ACTION = [6, 8, 6, 8]
        self.TIMER_PER_ACTION = [1, 1, 0.5, 0.5]

        self.idle_type = [0, 2700, 38, 40, 38, 40]
        self.move_type = [0, 2640, 40, 40, 40, 40]
        self.jump_type = [0, 2570, 38, 43, 38, 43]
        self.attack_type = [0, 2570, 38, 43, 38, 43]

    def update(self):
        super(Tikal, self).update()
        self.cur_state.do(self)

        self.idle_size = int(self.idle_frame) * 36 + 5
        self.move_size = int(self.move_frame) * 41 + 5
        self.jump_size = int(self.jump_frame) * 39 + 5
        self.attack_size = int(self.attack_frame) * 51 + 2

    def draw(self):
        self.cur_state.draw(self)

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def handle_collision(self, other, group):
        pass

class Rouge(Character):
    image = None
    icon_image = None
    def __init__(self):
        super(Rouge, self).__init__()
        if Rouge.image == None:
            self.image = load_image("character/rouge.png")
        if Rouge.icon_image == None:
            self.icon_image = load_image("map/icons.png")
        self.index = 5

        self.FRAMES_PER_ACTION = [6, 8, 6, 14]
        self.TIMER_PER_ACTION = [1, 1, 0.5, 1.2]

        self.idle_type = [0, 2984, 28, 40, 30, 40]
        self.move_type = [0, 2905, 36, 40, 40, 40]
        self.jump_type = [0, 2730, 38, 40, 40, 40]
        self.attack_type = [0, 2470, 45, 42, 45, 42]

    def update(self):
        super(Rouge, self).update()
        self.cur_state.do(self)

        self.idle_size = int(self.idle_frame) * 30
        self.move_size = int(self.move_frame) * 36
        self.jump_size = int(self.jump_frame) * 40
        self.attack_size = int(self.attack_frame) * 50

    def draw(self):
        self.cur_state.draw(self)

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def handle_collision(self, other, group):
        pass

class Shadow(Character):
    image = None
    icon_image = None
    def __init__(self):
        super(Shadow, self).__init__()
        if Shadow.image == None:
            self.image = load_image("character/shadow.png")
        if Shadow.icon_image == None:
            self.icon_image = load_image("map/icons.png")
        self.index = 6

        self.FRAMES_PER_ACTION = [4, 8, 4, 8]
        self.TIMER_PER_ACTION = [0.9, 1, 0.5, 0.5]

        self.idle_type = [0, 2958, 37, 40, 37, 40]
        self.move_type = [0, 2864, 42, 40, 42, 40]
        self.jump_type = [0, 2720, 38, 40, 38, 40]
        self.attack_type = [0, 100, 45, 44, 45, 44]

    def update(self):
        super(Shadow, self).update()
        self.cur_state.do(self)

        self.idle_size = int(self.idle_frame) * 35 + 202
        self.move_size = int(self.move_frame) * 41 + 6
        self.jump_size = int(self.jump_frame) * 35 + 620
        self.attack_size = int(self.attack_frame) * 45

    def draw(self):
        self.cur_state.draw(self)

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def handle_collision(self, other, group):
        pass

##############################################################################################################

class Silver(Character):
    image = None
    icon_image = None
    def __init__(self):
        super(Silver, self).__init__()
        if Silver.image == None:
            self.image = load_image("character/silver.png")
        if Silver.icon_image == None:
            self.icon_image = load_image("map/icons.png")
        self.index = 7

        self.FRAMES_PER_ACTION = [7, 7, 7, 7]
        self.TIMER_PER_ACTION = [1, 1, 0.5, 0.5]

        self.idle_type = [0, 2984, 40, 40, 40, 40]
        self.move_type = [0, 2864, 42, 40, 42, 40]
        self.jump_type = [0, 2720, 38, 40, 38, 40]
        self.attack_type = [0, 2720, 38, 40, 38, 40]

    def update(self):
        super(Silver, self).update()
        self.cur_state.do(self)

        self.idle_size = int(self.idle_frame) * 50
        self.move_size = int(self.move_frame) * 41 + 6
        self.jump_size = int(self.jump_frame) * 35 + 620
        self.attack_size = int(self.attack_frame) * 35 + 620

    def draw(self):
        self.cur_state.draw(self)

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def handle_collision(self, other, group):
        pass

class Blaze(Character):
    image = None
    icon_image = None
    def __init__(self):
        super(Blaze, self).__init__()
        if Blaze.image == None:
            self.image = load_image("character/Blaze.png")
        if Blaze.icon_image == None:
            self.icon_image = load_image("map/icons.png")
        self.index = 8

        self.FRAMES_PER_ACTION = [13, 8, 3, 2]
        self.TIMER_PER_ACTION = [2, 1, 0.5, 0.3]

        self.idle_type = [0, 2810, 34, 40, 34, 40]
        self.move_type = [0, 2610, 35, 40, 35, 40]
        self.jump_type = [0, 2480, 35, 40, 35, 40]
        self.attack_type = [0, 1930, 45, 45, 40, 40]

    def update(self):
        super(Blaze, self).update()
        self.cur_state.do(self)

        self.idle_size = int(self.idle_frame) * 35 + 24
        self.move_size = int(self.move_frame) * 35 + 24
        self.jump_size = int(self.jump_frame) * 40 + 210
        self.attack_size = int(self.attack_frame) * 45 + 25 + (self.attack % 2) * 90

    def draw(self):
        self.cur_state.draw(self)

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def handle_collision(self, other, group):
        pass

class Espio(Character):
    image = None
    icon_image = None
    def __init__(self):
        super(Espio, self).__init__()
        if Espio.image == None:
            self.image = load_image("character/espio.png")
        if Espio.icon_image == None:
            self.icon_image = load_image("map/icons.png")
        self.index = 9

        self.FRAMES_PER_ACTION = [6, 9, 10, 5]
        self.TIMER_PER_ACTION = [1, 1, 0.5, 0.5]

        self.idle_type = [0, 1220, 27, 40, 27, 40]
        self.move_type = [0, 1130, 35, 40, 35, 40]
        self.jump_type = [0, 780, 35, 40, 35, 40]
        self.attack_type = [0, 514, 45, 40, 45, 40]

    def update(self):
        super(Espio, self).update()
        self.cur_state.do(self)

        self.idle_size = int(self.idle_frame) * 27 + 5
        self.move_size = int(self.move_frame) * 35 + 5
        self.jump_size = int(self.jump_frame) * 35 + 5
        self.attack_size = int(self.attack_frame) * 45

    def draw(self):
        self.cur_state.draw(self)

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def handle_collision(self, other, group):
        pass

class Mighty(Character):
    image = None
    icon_image = None
    def __init__(self):
        super(Mighty, self).__init__()
        if Mighty.image == None:
            self.image = load_image("character/mighty.png")
        if Mighty.icon_image == None:
            self.icon_image = load_image("map/icons.png")
        self.index = 10

        self.FRAMES_PER_ACTION = [5, 9, 6, 3]
        self.TIMER_PER_ACTION = [1, 1, 0.5, 0.5]

        self.idle_type = [0, 2920, 30, 40, 32, 40]
        self.move_type = [0, 2670, 35, 40, 35, 40]
        self.jump_type = [0, 2830, 30, 40, 30, 40]
        self.attack_type = [0, 2220, 35, 40, 35, 40]

    def update(self):
        super(Mighty, self).update()
        self.cur_state.do(self)

        self.idle_size = int(self.idle_frame) * 28
        self.move_size = int(self.move_frame) * 35
        self.jump_size = int(self.jump_frame) * 24
        self.attack_size = int(self.attack_frame) * 40

    def draw(self):
        self.cur_state.draw(self)

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def handle_collision(self, other, group):
        pass

class SuperSonic(Character):
    image = None
    icon_image = None
    def __init__(self):
        super(SuperSonic, self).__init__()
        if SuperSonic.image == None:
            self.image = load_image("character/super sonic.png")
        if SuperSonic.icon_image == None:
            self.icon_image = load_image("map/icons.png")
        self.index = 11

        self.FRAMES_PER_ACTION = [6, 1, 4, 2]
        self.TIMER_PER_ACTION = [1, 1, 0.5, 0.5]

        self.idle_type = [0, 2890, 24, 46, 24, 46]
        self.move_type = [0, 2890, 35, 46, 35, 46]
        self.jump_type = [0, 2410, 38, 40, 38, 40]
        self.attack_type = [0, 2730, 45, 40, 45, 40]

    def update(self):
        super(SuperSonic, self).update()
        self.cur_state.do(self)

        self.idle_size = int(self.idle_frame) * 25 + 2
        self.move_size = int(self.move_frame) + 394
        self.jump_size = int(self.jump_frame) * 36 + 10
        self.attack_size = int(self.attack_frame) * 45 + (self.attack % 2 * 150)

        if self.attack % 2 == 0:
            self.FRAMES_PER_ACTION[3] = 4
        if self.attack % 2 == 1:
            self.FRAMES_PER_ACTION[3] = 2

    def draw(self):
        self.cur_state.draw(self)

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def handle_collision(self, other, group):
        pass

class SuperShadow(Character):
    image = None
    icon_image = None
    def __init__(self):
        super(SuperShadow, self).__init__()
        if SuperShadow.image == None:
            self.image = load_image("character/super shadow.png")
        if SuperShadow.icon_image == None:
            self.icon_image = load_image("map/icons.png")
        self.index = 12

        self.FRAMES_PER_ACTION = [2, 5, 6, 6]
        self.TIMER_PER_ACTION = [1, 1, 0.5, 0.5]

        self.idle_type = [0, 2940, 25, 38, 25, 38]
        self.move_type = [0, 2842, 34, 36, 34, 36]
        self.jump_type = [0, 2724, 37, 38, 37, 38]
        self.attack_type = [0, 2380, 45, 35, 45, 35]

    def update(self):
        super(SuperShadow, self).update()
        self.cur_state.do(self)

        self.idle_size = 4032 - 282 - 25 - int(self.idle_frame) * 26
        self.move_size = 4032 - 260 - 32 - int(self.move_frame) * 32
        self.jump_size = 4032 - 38 - 23 - int(self.jump_frame) * 38
        self.attack_size = 4032 - 45 - int(self.attack_frame) * 45

    def draw(self):
        self.cur_state.draw(self)

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def handle_collision(self, other, group):
        pass