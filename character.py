from pico2d import *
import game_world
from math import *
from random import *
from time import *

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

class IDLE:
    global move_dir
    @staticmethod
    def enter(self, event):
        print('ENTER IDLE')
        if event == RU:
            self.dir_x = 0
            move_dir[0] = False
        elif event == LU:
            self.dir_x = 0
            move_dir[1] = False

    @staticmethod
    def exit(self, event):
        print('EXIT IDLE')

    def do(self):
        self.idle_type[0] = self.idle_size

    def draw(self):
        self.image.clip_composite_draw(self.idle_type[0],self.idle_type[1],self.idle_type[2],self.idle_type[3],
                                            self.rotate, self.face_dir,
                                            self.x, self.y, self.idle_type[4], self.idle_type[5])

move_dir = [ False, False ]
class RUN:
    global move_dir
    def enter(self, event):
        print('ENTER RUN')
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
            self.cur_state.exit(self, NULL)
            try:
                self.cur_state = next_state[IDLE][NULL]
            except KeyError:
                print('Error', self.cur_state.__name__, ' ', "None")
            self.cur_state.enter(self, NULL)

    def exit(self, event):
        print('EXIT RUN')

    def do(self):
        self.move_type[0] = self.move_size

        self.x += self.dir_x * self.speed
        self.x = clamp(0, self.x, 800)

    def draw(self):
        self.image.clip_composite_draw(self.move_type[0], self.move_type[1], self.move_type[2], self.move_type[3],
                                            self.rotate, self.face_dir,
                                            self.x, self.y, self.move_type[4], self.move_type[5])

class Player_JUMP:
    global move_dir
    @staticmethod
    def enter(self, event):
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

    @staticmethod
    def exit(self, event):
        print('exit JUMP')

    @staticmethod
    def do(self):
        self.jump_type[0] = self.jump_size
        if move_dir[0] == True or move_dir[1] == True:
            self.x += self.dir_x * self.speed
            self.x = clamp(0, self.x, 800)

        if self.time % 8 == 0:
            if self.radian <= pi * 3 / 2:
                self.radian += (pi / 10)
                self.y += sin(self.radian) * 10
            else:
                self.y = 130
                self.radian = 0
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

set_time, cur_time = 0, 0
class ATTACK:
    @staticmethod
    def enter(self, event):
        global set_time
        set_time = time()
        print('ENTER ATTACK')
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
        print('EXIT ATTACK')
    @staticmethod
    def do(self):
        global cur_time, set_time
        self.attack_type[0] = self.attack_size
        self.x += self.dir_x * self.speed
        self.x = clamp(0, self.x, 800)

        cur_time = time()
        if cur_time > set_time + 0.3:
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

########################################

class Character:
    def __init__(self):
        self.font = None

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

        self.damage = 6
        self.time = 0
        self.face_dir = 'None'  # 이미지 반전
        self.rotate = 0 # 이미지 회전
        self.radian = 0

        self.jump_sound = load_wav('sound/00_jump.wav')
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

    def draw(self):
        self.cur_state.draw()
        pass

    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def get_bb(self):
        return self.x - 20, self.y - 50, self.x + 20, self.y + 50

    def handle_collision(self, other, group):
        pass

class Sonic(Character):
    image = None
    def __init__(self):
        super(Sonic, self).__init__()
        if Sonic.image == None:
            self.image = load_image("character/sonic.png")
        # self.font = load_font()

        self.idle_type = [0, 2285, 30, 40, 30, 40]
        self.move_type = [0, 1830, 40, 40, 40, 40]
        self.jump_type = [0, 1250, 35, 40, 35, 40]
        self.attack_type = [0, 950, 45, 40, 45, 40]

    def update(self):
        super(Sonic, self).update()
        self.cur_state.do(self)

        self.idle_size = self.idle_frame * 30 + 7
        self.move_size = self.move_frame * 40 + 10
        self.jump_size = self.jump_frame * 50 + 15
        self.attack_size = self.attack_frame * 45

        if self.time % 15 == 0:
            self.idle_frame = (self.idle_frame + 1) % 8
            self.move_frame = (self.move_frame + 1) % 8
            self.jump_frame = (self.jump_frame + 1) % 3
            self.attack_frame = (self.attack_frame + 1) % 6

    def draw(self):
        self.cur_state.draw(self)
        # self.font.draw(self.x - 60, self.y + 50,
        #               '(Time: %3.2f)' % get_time(), (255, 255, 0))

    def get_bb(self):
        return self.x - 20, self.y - 50, self.x + 20, self.y + 50

    def handle_collision(self, other, group):
        pass

class Tales(Character):
    image = None
    def __init__(self):
        super(Tales, self).__init__()
        if Tales.image == None:
            self.image = load_image("character/tales.png")

        self.idle_type = [0, 2650, 50, 40, 50, 40]
        self.move_type = [0, 2980, 50, 40, 50, 40]
        self.jump_type = [0, 2740, 40, 45, 40, 45]
        self.attack_type = [0, 950, 40, 40, 40, 40]

    def update(self):
        super(Tales, self).update()
        self.cur_state.do(self)

        self.idle_size = self.idle_frame * 52 + 20
        self.move_size = self.move_frame * 55 + 10
        self.jump_size = self.jump_frame * 50 + 15
        self.attack_size = self.attack_frame * 40

        if self.time % 5 == 0:
            self.idle_frame = (self.idle_frame + 1) % 8
            self.move_frame = (self.move_frame + 1) % 8
            self.jump_frame = (self.jump_frame + 1) % 8
            self.attack_frame = (self.attack_frame + 1) % 8

    def draw(self):
        self.cur_state.draw(self)

class Knuckles(Character):
    image = None
    def __init__(self):
        super(Knuckles, self).__init__()
        if Knuckles.image == None:
            self.image = load_image("character/knuckles.png")

        self.idle_type = [0, 2980, 35, 40, 35, 40]
        self.move_type = [0, 2680, 40, 40, 40, 40]
        self.jump_type = [0, 1074, 45, 40, 45, 40]
        self.attack_type = [0, 1074, 45, 40, 45, 40]

    def update(self):
        super(Knuckles, self).update()
        self.cur_state.do(self)

        self.idle_size = self.idle_frame * 35 + 410
        self.move_size = self.move_frame * 41 + 2
        self.jump_size = self.jump_frame * 51 + 2
        self.attack_size = self.attack_frame * 40

        if self.time % 5 == 0:
            self.jump_frame = (self.jump_frame + 1) % 8
        if self.time % 10 == 0:
            self.idle_frame = (self.idle_frame + 1) % 3
        if self.time % 20 == 0:
            self.move_frame = (self.move_frame + 1) % 8

    def draw(self):
        self.cur_state.draw(self)

class AmyRose(Character):
    image = None
    def __init__(self):
        super(AmyRose, self).__init__()
        if AmyRose.image == None:
            self.image = load_image("character/amy rose.png")

        self.idle_type = [0, 2750, 30, 40, 30, 40]
        self.move_type = [0, 2563, 38, 40, 38, 40]
        self.jump_type = [0, 1855, 50, 44, 50, 44]
        self.attack_type = [0, 1074, 45, 40, 45, 40]

    def update(self):
        super(AmyRose, self).update()
        self.cur_state.do(self)

        self.idle_size = self.idle_frame * 28 + 2
        self.move_size = self.move_frame * 41 + 2
        self.jump_size = self.jump_frame * 51 + 2
        self.attack_size = self.attack_frame * 51 + 2

        if self.time % 30 == 0:
            self.idle_frame = (self.idle_frame + 1) % 8
        if self.time % 10 == 0:
            self.move_frame = (self.move_frame + 1) % 8
            self.jump_frame = (self.jump_frame + 1) % 7

    def draw(self):
        self.cur_state.draw(self)

class Tikal(Character):
    image = None
    def __init__(self):
        super(Tikal, self).__init__()
        if Tikal.image == None:
            self.image = load_image("character/tikal.png")

        self.idle_type = [0, 2700, 38, 40, 38, 40]
        self.move_type = [0, 2640, 40, 40, 40, 40]
        self.jump_type = [0, 2570, 38, 43, 38, 43]
        self.attack_type = [0, 2570, 38, 43, 38, 43]

    def update(self):
        super(Tikal, self).update()
        self.cur_state.do(self)

        self.idle_size = self.idle_frame * 36 + 5
        self.move_size = self.move_frame * 41 + 5
        self.jump_size = self.jump_frame * 39 + 5
        self.attack_size = self.attack_frame * 51 + 2

        if self.time % 10 == 0:
            self.move_frame = (self.move_frame + 1) % 8
        if self.time % 30 == 0:
            self.jump_frame = (self.jump_frame + 1) % 8
            self.idle_frame = (self.idle_frame + 1) % 6

    def draw(self):
        self.cur_state.draw(self)

class Rouge(Character):
    image = None
    def __init__(self):
        super(Rouge, self).__init__()
        if Rouge.image == None:
            self.image = load_image("character/rouge.png")

        self.idle_type = [0, 2984, 28, 40, 28, 40]
        self.move_type = [0, 2905, 36, 40, 36, 40]
        self.jump_type = [0, 2730, 38, 40, 38, 40]
        self.attack_type = [0, 2730, 38, 40, 38, 40]

    def update(self):
        super(Rouge, self).update()
        self.cur_state.do(self)

        self.idle_size = self.idle_frame * 28
        self.move_size = self.move_frame * 36
        self.jump_size = self.jump_frame * 40
        self.attack_size = self.attack_frame * 40

        if self.time % 5 == 0:
            self.idle_frame = (self.idle_frame + 1) % 6
            self.move_frame = (self.move_frame + 1) % 8
            self.jump_frame = (self.jump_frame + 1) % 6

    def draw(self):
        self.cur_state.draw(self)

class Shadow(Character):
    image = None
    def __init__(self):
        super(Shadow, self).__init__()
        if Shadow.image == None:
            self.image = load_image("character/shadow.png")

        self.idle_type = [0, 2958, 37, 40, 37, 40]
        self.move_type = [0, 2864, 42, 40, 42, 40]
        self.jump_type = [0, 2720, 38, 40, 38, 40]
        self.attack_type = [0, 2720, 38, 40, 38, 40]

    def update(self):
        super(Shadow, self).update()
        self.cur_state.do(self)

        self.idle_size = self.idle_frame * 35 + 202
        self.move_size = self.move_frame * 41 + 6
        self.jump_size = self.jump_frame * 35 + 620
        self.attack_size = self.attack_frame * 35 + 620

        if self.time % 10 == 0:
            self.move_frame = (self.move_frame + 1) % 8
        if self.time % 10 == 0:
            self.idle_frame = (self.idle_frame + 1) % 4
            self.jump_frame = (self.jump_frame + 1) % 4

    def draw(self):
        self.cur_state.draw(self)

##############################################################################################################

class Silver(Character):
    image = None
    def __init__(self):
        super(Silver, self).__init__()
        if Silver.image == None:
            self.image = load_image("character/silver.png")

        self.idle_type = [0, 2984, 40, 40, 40, 40]
        self.move_type = [0, 2864, 42, 40, 42, 40]
        self.jump_type = [0, 2720, 38, 40, 38, 40]
        self.attack_type = [0, 2720, 38, 40, 38, 40]

    def update(self):
        super(Silver, self).update()
        self.cur_state.do(self)

        self.idle_size = self.idle_frame * 35 + 202
        self.move_size = self.move_frame * 41 + 6
        self.jump_size = self.jump_frame * 35 + 620
        self.attack_size = self.attack_frame * 35 + 620

        if self.time % 15 == 0:
            self.idle_frame = (self.idle_frame + 1) % 7
            self.move_frame = (self.move_frame + 1) % 7
            self.jump_frame = (self.jump_frame + 1) % 7

    def draw(self):
        self.cur_state.draw(self)

class Blaze(Character):
    image = None
    def __init__(self):
        super(Blaze, self).__init__()
        if Blaze.image == None:
            self.image = load_image("character/Blaze.png")

        self.idle_type = [0, 2810, 34, 40, 34, 40]
        self.move_type = [0, 2610, 35, 40, 35, 40]
        self.jump_type = [0, 2480, 35, 40, 35, 40]
        self.attack_type = [0, 2480, 35, 40, 35, 40]

    def update(self):
        super(Blaze, self).update()
        self.cur_state.do(self)

        self.idle_size = self.idle_frame * 35 + 24
        self.move_size = self.move_frame * 35 + 24
        self.jump_size = self.jump_frame * 40 + 210
        self.attack_size = self.attack_frame * 40 + 210

        if self.time % 5 == 0:
            self.idle_frame = (self.idle_frame + 1) % 13
            self.move_frame = (self.move_frame + 1) % 8
            self.jump_frame = (self.jump_frame + 1) % 3

    def draw(self):
        self.cur_state.draw(self)

class Espio(Character):
    image = None
    def __init__(self):
        super(Espio, self).__init__()
        if Espio.image == None:
            self.image = load_image("character/espio.png")

        self.idle_type = [0, 1220, 27, 40, 27, 40]
        self.move_type = [0, 1130, 35, 40, 35, 40]
        self.jump_type = [0, 780, 35, 40, 35, 40]
        self.attack_type = [0, 780, 35, 40, 35, 40]

    def update(self):
        super(Espio, self).update()
        self.cur_state.do(self)

        self.idle_size = self.idle_frame * 27 + 5
        self.move_size = self.move_frame * 35 + 5
        self.jump_size = self.jump_frame * 35 + 5
        self.attack_size = self.attack_frame * 35 + 5

        if self.time % 20 == 0:
            self.idle_frame = (self.idle_frame + 1) % 6
            self.move_frame = (self.move_frame + 1) % 9
        if self.time % 20 == 0:
            self.jump_frame = (self.jump_frame + 1) % 10

    def draw(self):
        self.cur_state.draw(self)

class Mighty(Character):
    image = None
    def __init__(self):
        super(Mighty, self).__init__()
        if Mighty.image == None:
            self.image = load_image("character/mighty.png")

        self.idle_type = [0, 2920, 30, 40, 30, 40]
        self.move_type = [0, 2670, 38, 40, 38, 40]
        self.jump_type = [0, 2830, 30, 40, 30, 40]
        self.attack_type = [0, 2830, 30, 40, 30, 40]

    def update(self):
        super(Mighty, self).update()
        self.cur_state.do(self)

        self.idle_size = self.idle_frame * 28
        self.move_size = self.move_frame * 35
        self.jump_size = self.jump_frame * 24
        self.attack_size = self.attack_frame * 24

        if self.time % 5 == 0:
            self.idle_frame = (self.idle_frame + 1) % 5
            self.move_frame = (self.move_frame + 1) % 9
            self.jump_frame = (self.jump_frame + 1) % 6

    def draw(self):
        self.cur_state.draw(self)

class SuperSonic(Character):
    image = None
    def __init__(self):
        super(SuperSonic, self).__init__()
        if SuperSonic.image == None:
            self.image = load_image("character/super sonic.png")

        self.idle_type = [0, 2890, 24, 46, 24, 46]
        self.move_type = [0, 2890, 35, 46, 35, 46]
        self.jump_type = [0, 2410, 38, 40, 38, 40]
        self.attack_type = [0, 2410, 38, 40, 38, 40]

    def update(self):
        super(SuperSonic, self).update()
        self.cur_state.do(self)

        self.idle_size = self.idle_frame * 25 + 2
        self.move_size = self.move_frame + 394
        self.jump_size = self.jump_frame * 36 + 10
        self.attack_size = self.attack_frame * 36 + 10

        if self.time % 20 == 0:
            self.idle_frame = (self.idle_frame + 1) % 6
        if self.time % 10 == 0:
            self.jump_frame = (self.jump_frame + 1) % 4
            self.attack_frame = (self.attack_frame + 1) % 4

    def draw(self):
        self.cur_state.draw(self)

class SuperShadow(Character):
    image = None
    def __init__(self):
        super(SuperShadow, self).__init__()
        if SuperShadow.image == None:
            self.image = load_image("character/super shadow.png")

        self.idle_type = [0, 2940, 25, 38, 25, 38]
        self.move_type = [0, 2842, 34, 36, 34, 36]
        self.jump_type = [0, 2724, 37, 38, 37, 38]
        self.attack_type = [0, 2724, 37, 38, 37, 38]

    def update(self):
        super(SuperShadow, self).update()
        self.cur_state.do(self)

        self.idle_size = 4032 - 282 - 25 - self.idle_frame * 26
        self.move_size = 4032 - 260 - 32 - self.move_frame * 32
        self.jump_size = 4032 - 38 - 23 - self.jump_frame * 38
        self.attack_size = 4032 - 38 - 23 - self.attack_frame * 38

        if self.time % 5 == 0:
            self.idle_frame = (self.idle_frame + 1) % 2
        if self.time % 7 == 0:
            self.move_frame = (self.move_frame + 1) % 5
            self.jump_frame = (self.jump_frame + 1) % 6
            self.attack_frame = (self.attack_frame + 1) % 6

    def draw(self):
        self.cur_state.draw(self)