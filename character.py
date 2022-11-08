from pico2d import *
import game_world
from math import *
from random import *

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

RD, LD, RU, LU, SPACE, JUMP = range(6)
event_name = [ 'RD', 'LD', 'RU', 'LU', 'SPACE', 'JUMP' ]
key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE,
    (SDL_KEYDOWN, SDLK_UP): JUMP
}

class IDLE:
    @staticmethod
    def enter(self, event):
        print('ENTER IDLE')
        self.dir_x = 0

    @staticmethod
    def exit(self, event):
        print('EXIT IDLE')
        if JUMP == event:
            self.jump = True
            IDLE.do(self)

    def do(self):
        if self.jump == True:
            self.Jump()

class RUN:
    def enter(self, event):
        print('ENTER RUN')
        if event == RD:
            self.dir_x += 1
        elif event == LD:
            self.dir_x -= 1
        elif event == RU:
            self.dir_x -= 1
        elif event == LU:
            self.dir_x += 1

    def exit(self, event):
        print('EXIT RUN')
        self.face_dir = self.dir_x
        if JUMP == event:
            self.jump = True
            RUN.do(self)

    def do(self):
        self.x += self.dir_x * self.speed
        self.x = clamp(0, self.x, 800)
        if self.jump == True:
            self.Jump()

next_state = {
    IDLE:  {RU: RUN,  LU: RUN,  RD: RUN,  LD: RUN,  SPACE: IDLE, JUMP: IDLE},
    RUN:   {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE, SPACE: RUN,  JUMP: RUN}
}

########################################

class Character:
    def __init__(self):
        self.hp = 100
        self.speed = 1.2
        self.idle_frame = 0
        self.move_frame = 0
        self.jump_frame = 0
        self.damage = 6
        self.time = 0
        self.face_dir = 1
        self.radian = 0
        self.jump = False
        self.jump_sound = load_wav('sound/00_jump.wav')
        self.attack = False
        self.dir_x, self.dir_y = 0, 0
        self.x, self.y = 400, 130

        self.event_que = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

    def update(self):
        self.time += 1
        if self.event_que:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            try:
                self.cur_state = next_state[self.cur_state][event]
            except KeyError:
                print('Error', self.cur_state.__name__, ' ', event)
            self.cur_state.enter(self, event)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def Jump(self):
        if self.jump == True:
            if self.time % 8 == 0:
                if self.radian <= pi * 3 / 2:
                    self.radian += (pi / 10)
                    self.y += sin(self.radian) * 10
                else:
                    self.y = 130
                    self.jump = False
                    self.radian = 0

class Sonic(Character):
    def __init__(self):
        super(Sonic, self).__init__()
        self.image_left = load_image("character/sonic left.png")
        self.image_right = load_image("character/sonic right.png")

    def update(self):
        super(Sonic, self).update()
        self.cur_state.do(self)

        if self.time % 15 == 0:
            self.idle_frame = (self.idle_frame + 1) % 8
            self.move_frame = (self.move_frame + 1) % 8
            self.jump_frame = (self.jump_frame + 1) % 3

    def draw(self):
        if self.dir_x == 1:
            if self.jump == True:
                self.image_left.clip_draw(245 + (self.jump_frame * 40), 1250, 35, 40, self.x, self.y)
            else:
                self.image_left.clip_draw(10 + self.move_frame * 40, 1830, 40, 40, self.x, self.y)
        if self.dir_x == -1:
            if self.jump == True:
                self.image_right.clip_draw(4032 - 35 - 245 - (self.jump_frame * 40), 1250, 35, 40, self.x, self.y)
            else:
                self.image_right.clip_draw(4032 - 40 - 10  - (self.move_frame * 40), 1830, 40, 40, self.x, self.y)
        if self.dir_x == 0:
            if self.face_dir == 1:
                if self.jump == True:
                    self.image_left.clip_draw(245 + (self.jump_frame * 40), 1250, 35, 40, self.x, self.y)
                else:
                    self.image_left.clip_draw(7 + self.idle_frame * 30, 2285, 30, 40, self.x, self.y)
            elif self.face_dir == -1:
                if self.jump == True:
                    self.image_right.clip_draw(4032 - 35 - 245 - (self.jump_frame * 40), 1250, 35, 40, self.x, self.y)
                else:
                    self.image_right.clip_draw(4032 - 30 - 7 - (self.idle_frame * 30), 2285, 30, 40, self.x, self.y)

class Tales(Character):
    def __init__(self):
        super(Tales, self).__init__()
        self.image_left = load_image("character/tales left.png")
        self.image_right = load_image("character/tales right.png")

    def update(self):
        super(Tales, self).update()
        self.cur_state.do(self)

        if self.time % 5 == 0:
            self.idle_frame = (self.idle_frame + 1) % 8
            self.move_frame = (self.move_frame + 1) % 8
            self.jump_frame = (self.jump_frame + 1) % 8

    def draw(self):
        if self.dir_x == 1:
            if self.jump == True:
                self.image_left.clip_draw(self.jump_frame * 50 + 15, 2740, 40, 45, self.x, self.y)
            else:
                self.image_left.clip_draw(self.move_frame * 55 + 10, 2980, 50, 40, self.x, self.y)
        if self.dir_x == -1:
            if self.jump == True:
                self.image_right.clip_draw(4032 - 15 - 40 - self.jump_frame * 50, 2740, 40, 45, self.x, self.y)
            else:
                self.image_right.clip_draw(3972 - self.move_frame * 55, 2980, 50, 40, self.x, self.y)
        if self.dir_x == 0:
            if self.face_dir == 1:
                if self.jump == True:
                    self.image_left.clip_draw(self.jump_frame * 50 + 15, 2740, 40, 45, self.x, self.y)
                else:
                    self.image_left.clip_draw(self.idle_frame * 52 + 20, 2650, 50, 40, self.x, self.y)
            elif self.face_dir == -1:
                if self.jump == True:
                    self.image_right.clip_draw(4032 - 15 - 40 - self.jump_frame * 50, 2740, 40, 45, self.x, self.y)
                else:
                    self.image_right.clip_draw(4032 - 20 - 50 - self.idle_frame * 52, 2650, 50, 40, self.x, self.y)

class Knuckles(Character):
    def __init__(self):
        super(Knuckles, self).__init__()
        self.image_left = load_image("character/knuckles left.png")
        self.image_right = load_image("character/knuckles right.png")

    def update(self):
        super(Knuckles, self).update()
        self.cur_state.do(self)

        if self.time % 5 == 0:
            self.jump_frame = (self.jump_frame + 1) % 8
        if self.time % 10 == 0:
            self.idle_frame = (self.idle_frame + 1) % 3
        if self.time % 20 == 0:
            self.move_frame = (self.move_frame + 1) % 8

    def draw(self):
        if self.dir_x == 1:
            if self.jump == True:
                self.image_left.clip_draw(self.jump_frame * 51 + 2, 1074, 45, 40, self.x, self.y)
            else:
                self.image_left.clip_draw(self.move_frame * 41 + 2, 2680, 40, 40, self.x, self.y)
        if self.dir_x == -1:
            if self.jump == True:
                self.image_right.clip_draw(4032 - 51 - 2 - self.jump_frame * 51, 1074, 45, 40, self.x, self.y)
            else:
                self.image_right.clip_draw(4032 - 41 - 2 - self.move_frame * 41, 2680, 40, 40, self.x, self.y)
        if self.dir_x == 0:
            if self.face_dir == 1:
                if self.jump == True:
                    self.image_left.clip_draw(self.jump_frame * 51 + 2, 1074, 45, 40, self.x, self.y)
                else:
                    self.image_left.clip_draw(self.idle_frame * 35 + 410, 2980, 35, 40, self.x, self.y)
            elif self.face_dir == -1:
                if self.jump == True:
                    self.image_right.clip_draw(4032 - 51 - 2 - self.jump_frame * 51, 1074, 45, 40, self.x, self.y)
                else:
                    self.image_right.clip_draw(4032 - 410 - 35 - self.idle_frame * 35, 2980, 35, 40, self.x, self.y)

class AmyRose(Character):
    def __init__(self):
        super(AmyRose, self).__init__()
        self.image_left = load_image("character/amy rose left.png")
        self.image_right = load_image("character/amy rose right.png")

    def update(self):
        super(AmyRose, self).update()
        self.cur_state.do(self)

        if self.time % 30 == 0:
            self.idle_frame = (self.idle_frame + 1) % 8
        if self.time % 10 == 0:
            self.move_frame = (self.move_frame + 1) % 8
            self.jump_frame = (self.jump_frame + 1) % 7

    def draw(self):
        if self.dir_x == 1:
            if self.jump == True:
                self.image_left.clip_draw(self.jump_frame * 51 + 2, 1855, 50, 44, self.x, self.y)
            else:
                self.image_left.clip_draw(self.move_frame * 41 + 2, 2563, 38, 40, self.x, self.y)
        if self.dir_x == -1:
            if self.jump == True:
                self.image_right.clip_draw(4032 - 51 - 2 - self.jump_frame * 51, 1855, 50, 44, self.x, self.y)
            else:
                self.image_right.clip_draw(4032 - 41 - 2 - self.move_frame * 41,  2563, 38, 40, self.x, self.y)
        if self.dir_x == 0:
            if self.face_dir == 1:
                if self.jump == True:
                    self.image_left.clip_draw(self.jump_frame * 51 + 2, 1855, 50, 44, self.x, self.y)
                else:
                    self.image_left.clip_draw(self.idle_frame * 28 + 2, 2750, 30, 40, self.x, self.y)
            elif self.face_dir == -1:
                if self.jump == True:
                    self.image_right.clip_draw(4032 - 51 - 2 - self.jump_frame * 51, 1855, 50, 44, self.x, self.y)
                else:
                    self.image_right.clip_draw(4032 - 30 - 2 - self.idle_frame * 28, 2750, 30, 40, self.x, self.y)

class Tikal(Character):
    def __init__(self):
        super(Tikal, self).__init__()
        self.image_left = load_image("character/tikal left.png")
        self.image_right = load_image("character/tikal right.png")

    def update(self):
        super(Tikal, self).update()
        self.cur_state.do(self)

        if self.time % 10 == 0:
            self.move_frame = (self.move_frame + 1) % 8
        if self.time % 30 == 0:
            self.jump_frame = (self.jump_frame + 1) % 8
            self.idle_frame = (self.idle_frame + 1) % 6

    def draw(self):
        if self.dir_x == 1:
            if self.jump == True:
                self.image_left.clip_draw(self.jump_frame * 39 + 5, 2570, 38, 43, self.x, self.y)
            else:
                self.image_left.clip_draw(self.move_frame * 41 + 5, 2640, 40, 40, self.x, self.y)
        if self.dir_x == -1:
            if self.jump == True:
                self.image_right.clip_draw(4032 - 39 - 5 - self.jump_frame * 39, 2570, 38, 43, self.x, self.y)
            else:
                self.image_right.clip_draw(4032 - 41 - 5 - self.move_frame * 41, 2640, 40, 40, self.x, self.y)
        if self.dir_x == 0:
            if self.face_dir == 1:
                if self.jump == True:
                    self.image_left.clip_draw(self.jump_frame * 39 + 5, 2570, 38, 43, self.x, self.y)
                else:
                    self.image_left.clip_draw(self.idle_frame * 36 + 5, 2700, 38, 40, self.x, self.y)
            elif self.face_dir == -1:
                if self.jump == True:
                    self.image_right.clip_draw(4032 - 39 - 5 - self.jump_frame * 39, 2570, 38, 43, self.x, self.y)
                else:
                    self.image_right.clip_draw(4032 - 36 - 5 - self.idle_frame * 36, 2700, 38, 40, self.x, self.y)

class Rouge(Character):
    def __init__(self):
        super(Rouge, self).__init__()
        self.image_left = load_image("character/rouge left.png")
        self.image_right = load_image("character/rouge right.png")

    def update(self):
        super(Rouge, self).update()
        if self.time % 5 == 0:
            self.idle_frame = (self.idle_frame + 1) % 6
        if self.jump == True:
            if self.radian <= pi * 3 / 2:
                self.radian += (pi / 8)
                self.y += sin(self.radian) * 6
            else:
                self.y = 130
                self.jump = False
                self.radian = 0

    def draw(self):
        if self.dir_x == 1:
            if self.jump == True:
                self.image_left.clip_draw(self.idle_frame * 28, 2984, 28, 40, self.x, self.y)
            else:
                self.image_left.clip_draw(self.idle_frame * 28, 2984, 28, 40, self.x, self.y)
        if self.dir_x == -1:
            if self.jump == True:
                self.image_right.clip_draw(4032 - 28 - self.idle_frame * 28, 2984, 28, 40, self.x, self.y)
            else:
                self.image_right.clip_draw(4032 - 28 - self.idle_frame * 28, 2984, 28, 40, self.x, self.y)
        if self.dir_x == 0:
            if self.face_dir == 1:
                self.image_left.clip_draw(self.idle_frame * 28, 2984, 28, 40, self.x, self.y)
            elif self.face_dir == -1:
                self.image_right.clip_draw(4032 - 28 - self.idle_frame * 28, 2984, 28, 40, self.x, self.y)

class Shadow(Character):
    def __init__(self):
        super(Shadow, self).__init__()
        self.image_left = load_image("character/shadow left.png")
        self.image_right = load_image("character/shadow right.png")

    def update(self):
        super(Shadow, self).update()
        self.cur_state.do(self)

        if self.time % 5 == 0:
            self.move_frame = (self.move_frame + 1) % 8
        if self.time % 10 == 0:
            self.idle_frame = (self.idle_frame + 1) % 4
            self.jump_frame = (self.jump_frame + 1) % 4

    def draw(self):
        if self.dir_x == 1:
            if self.jump == True:
                self.image_left.clip_draw(self.jump_frame * 35 + 620, 2720, 38, 40, self.x, self.y)
            else:
                self.image_left.clip_draw(self.move_frame * 41 + 6, 2864, 42, 40, self.x, self.y)
        if self.dir_x == -1:
            if self.jump == True:
                self.image_right.clip_draw(4032 - 620 - 35 - self.jump_frame * 35, 2720, 38, 40, self.x, self.y)
            else:
                self.image_right.clip_draw(4032 - 6 - 41 - self.move_frame * 41, 2864, 42, 40, self.x, self.y)
        if self.dir_x == 0:
            if self.face_dir == 1:
                if self.jump == True:
                    self.image_left.clip_draw(self.jump_frame * 35 + 620, 2720, 38, 40, self.x, self.y)
                else:
                    self.image_left.clip_draw(self.idle_frame * 35 + 202, 2958, 37, 40, self.x, self.y)
            elif self.face_dir == -1:
                if self.jump == True:
                    self.image_right.clip_draw(4032 - 620 - 35 - self.jump_frame * 35, 2720, 38, 40, self.x, self.y)
                else:
                    self.image_right.clip_draw(4032 - 202 - 37 - self.idle_frame * 35, 2958, 37, 40, self.x, self.y)

##############################################################################################################

class Silver(Character):
    def __init__(self):
        super(Silver, self).__init__()
        self.image_left = load_image("character/silver right.png")
        self.image_right = load_image("character/silver left.png")

    def update(self):
        super(Silver, self).update()
        if self.time % 5 == 0:
            self.idle_frame = (self.idle_frame + 1) % 7
        if self.jump == True:
            if self.radian <= pi * 3 / 2:
                self.radian += (pi / 8)
                self.y += sin(self.radian) * 6
            else:
                self.y = 130
                self.jump = False
                self.radian = 0

    def draw(self):
        if self.dir_x == 1:
            if self.jump == True:
                self.image_left.clip_draw(4032 - 40 - self.idle_frame * 50, 2984, 40, 40, self.x, self.y)
            else:
                self.image_left.clip_draw(4032 - 40 - self.idle_frame * 50, 2984, 40, 40, self.x, self.y)
        if self.dir_x == -1:
            if self.jump == True:
                self.image_right.clip_draw(self.idle_frame * 50, 2984, 40, 40, self.x, self.y)
            else:
                self.image_right.clip_draw(self.idle_frame * 50, 2984, 40, 40, self.x, self.y)
        if self.dir_x == 0:
            if self.face_dir == 1:
                self.image_left.clip_draw(4032 - 40 - self.idle_frame * 50, 2984, 40, 40, self.x, self.y)
            elif self.face_dir == -1:
                self.image_right.clip_draw(self.idle_frame * 50, 2984, 40, 40, self.x, self.y)

class Blaze(Character):
    def __init__(self):
        super(Blaze, self).__init__()
        self.image_left = load_image("character/blaze left.png")
        self.image_right = load_image("character/blaze right.png")

    def update(self):
        super(Blaze, self).update()
        if self.time % 5 == 0:
            self.idle_frame = (self.idle_frame + 1) % 13
        if self.jump == True:
            if self.radian <= pi * 3 / 2:
                self.radian += (pi / 8)
                self.y += sin(self.radian) * 6
            else:
                self.y = 130
                self.jump = False
                self.radian = 0

    def draw(self):
        if self.dir_x == 1:
            if self.jump == True:
                self.image_left.clip_draw(self.idle_frame * 31 + 382, 1710, 30, 40, self.x, self.y)
            else:
                self.image_left.clip_draw(self.idle_frame * 31 + 382, 1710, 30, 40, self.x, self.y)
        if self.dir_x == -1:
            if self.jump == True:
                self.image_right.clip_draw(4032 - 382 - 30 - self.idle_frame * 31, 1710, 30, 40, self.x, self.y)
            else:
                self.image_right.clip_draw(4032 - 382 - 30 - self.idle_frame * 31, 1710, 30, 40, self.x, self.y)
        if self.dir_x == 0:
            if self.face_dir == 1:
                self.image_left.clip_draw(self.idle_frame * 31 + 382, 1710, 30, 40, self.x, self.y)
            elif self.face_dir == -1:
                self.image_right.clip_draw(4032 - 382 - 30 - self.idle_frame * 31, 1710, 30, 40, self.x, self.y)

class Espio(Character):
    def __init__(self):
        super(Espio, self).__init__()
        self.image_left = load_image("character/espio left.png")
        self.image_right = load_image("character/espio right.png")

    def update(self):
        super(Espio, self).update()
        self.cur_state.do(self)

        if self.time % 20 == 0:
            self.idle_frame = (self.idle_frame + 1) % 6
            self.move_frame = (self.move_frame + 1) % 9
        if self.time % 20 == 0:
            self.jump_frame = (self.jump_frame + 1) % 10

    def draw(self):
        if self.dir_x == 1:
            if self.jump == True:
                self.image_left.clip_draw(self.jump_frame * 35 + 5, 780, 35, 40, self.x, self.y)
            else:
                self.image_left.clip_draw(self.move_frame * 35 + 5, 1130, 35, 40, self.x, self.y)
        if self.dir_x == -1:
            if self.jump == True:
                self.image_right.clip_draw(4032 - 35 - 5 - self.jump_frame * 35, 780, 35, 40, self.x, self.y)
            else:
                self.image_right.clip_draw(4032 - 35 - 5 - self.move_frame * 35, 1130, 35, 40, self.x, self.y)
        if self.dir_x == 0:
            if self.face_dir == 1:
                if self.jump == True:
                    self.image_left.clip_draw(self.jump_frame * 35 + 5, 780, 35, 40, self.x, self.y)
                else:
                    self.image_left.clip_draw(self.idle_frame * 27 + 5, 1220, 27, 40, self.x, self.y)
            elif self.face_dir == -1:
                if self.jump == True:
                    self.image_right.clip_draw(4032 - 35 - 5 - self.jump_frame * 35, 780, 35, 40, self.x, self.y)
                else:
                    self.image_right.clip_draw(4032 - 27 - 5 - self.idle_frame * 27, 1220, 27, 40, self.x, self.y)

class Mighty(Character):
    def __init__(self):
        super(Mighty, self).__init__()
        self.image_left = load_image("character/mighty left.png")
        self.image_right = load_image("character/mighty right.png")

    def update(self):
        super(Mighty, self).update()
        self.cur_state.do(self)

        if self.time % 5 == 0:
            self.idle_frame = (self.idle_frame + 1) % 7
            self.move_frame = (self.move_frame + 1) % 8
        if self.time % 20 == 0:
            self.jump_frame = (self.jump_frame + 1) % 7

    def draw(self):
        if self.dir_x == 1:
            if self.jump == True:
                self.image_left.clip_draw(self.jump_frame * 40 + 310, 2870, 38, 38, self.x, self.y)
            else:
                self.image_left.clip_draw(self.move_frame * 35 + 137, 2780, 33, 38, self.x, self.y)
        if self.dir_x == -1:
            if self.jump == True:
                self.image_right.clip_draw(4032 - 310 - 40 - self.jump_frame * 40, 2870, 38, 38, self.x, self.y)
            else:
                self.image_right.clip_draw(4032 - 137 - 35 - self.move_frame * 35, 2780, 33, 38, self.x, self.y)
        if self.dir_x == 0:
            if self.face_dir == 1:
                if self.jump == True:
                    self.image_left.clip_draw(self.jump_frame * 40 + 310, 2870, 38, 38, self.x, self.y)
                else:
                    self.image_left.clip_draw(self.idle_frame * 28 + 5, 2870, 30, 35, self.x, self.y)
            elif self.face_dir == -1:
                if self.jump == True:
                    self.image_right.clip_draw(4032 - 310 - 40 - self.jump_frame * 40, 2870, 38, 38, self.x, self.y)
                else:
                    self.image_right.clip_draw(4032 - 28 - 5 - self.idle_frame * 28, 2870, 30, 35, self.x, self.y)

class SuperSonic(Character):
    def __init__(self):
        super(SuperSonic, self).__init__()
        self.image_left = load_image("character/super sonic left.png")
        self.image_right = load_image("character/super sonic right.png")

    def update(self):
        super(SuperSonic, self).update()
        self.cur_state.do(self)

        if self.time % 20 == 0:
            self.idle_frame = (self.idle_frame + 1) % 6
        if self.time % 10 == 0:
            self.jump_frame = (self.jump_frame + 1) % 4

    def draw(self):
        if self.dir_x == 1:
            if self.jump == True:
                self.image_left.clip_draw(self.jump_frame * 36 + 10, 2410, 38, 40, self.x, self.y)
            else:
                self.image_left.clip_draw(self.move_frame + 394, 2890, 35, 46, self.x, self.y)
        if self.dir_x == -1:
            if self.jump == True:
                self.image_right.clip_draw(4032 - 36 - 10 - self.jump_frame * 36, 2410, 38, 40, self.x, self.y)
            else:
                self.image_right.clip_draw(4032 - 40 - 394 - self.move_frame, 2890, 35, 46, self.x, self.y)
        if self.dir_x == 0:
            if self.face_dir == 1:
                if self.jump == True:
                    self.image_left.clip_draw(self.jump_frame * 36 + 10, 2410, 38, 40, self.x, self.y)
                else:
                    self.image_left.clip_draw(self.idle_frame * 25 + 2, 2890, 24, 46, self.x, self.y)
            elif self.face_dir == -1:
                if self.jump == True:
                    self.image_right.clip_draw(4032 - 36 - 10 - self.jump_frame * 36, 2410, 38, 40, self.x, self.y)
                else:
                    self.image_right.clip_draw(4032 - 24 - 2 - self.idle_frame * 25, 2890, 24, 46, self.x, self.y)

class SuperShadow(Character):
    def __init__(self):
        super(SuperShadow, self).__init__()
        self.image_left = load_image("character/super shadow right.png")
        self.image_right = load_image("character/super shadow left.png")

    def update(self):
        super(SuperShadow, self).update()
        self.cur_state.do(self)

        if self.time % 5 == 0:
            self.idle_frame = (self.idle_frame + 1) % 2
        if self.time % 7 == 0:
            self.move_frame = (self.move_frame + 1) % 5
            self.jump_frame = (self.jump_frame + 1) % 6

    def draw(self):
        if self.dir_x == 1:
            if self.jump == True:
                self.image_left.clip_draw(4032 - 38 - 23 - self.jump_frame * 38, 2724, 37, 38, self.x, self.y)
            else:
                self.image_left.clip_draw(4032 - 260 - 32 - self.move_frame * 32, 2842, 34, 36, self.x, self.y)
        if self.dir_x == -1:
            if self.jump == True:
                self.image_right.clip_draw(self.jump_frame * 38 + 23, 2724, 37, 38, self.x, self.y)
            else:
                self.image_right.clip_draw(self.move_frame * 32 + 260, 2842, 34, 36, self.x, self.y)
        if self.dir_x == 0:
            if self.face_dir == 1:
                if self.jump == True:
                    self.image_left.clip_draw(4032 - 38 - 23 - self.jump_frame * 38, 2724, 37, 38, self.x, self.y)
                else:
                    self.image_left.clip_draw(4032 - 282 - 25 - self.idle_frame * 26, 2940, 25, 38, self.x, self.y)
            elif self.face_dir == -1:
                if self.jump == True:
                    self.image_right.clip_draw(self.jump_frame * 38 + 23, 2724, 37, 38, self.x, self.y)
                else:
                    self.image_right.clip_draw(self.idle_frame * 25 + 282, 2940, 25, 38, self.x, self.y)