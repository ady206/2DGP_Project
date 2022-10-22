from pico2d import *
from math import *
from random import *
import game_framework
import middle_state
import result_state

player_character = None
character = ['Sonic', 'Tales', 'Knuckles', 'AmyRose', 'Tikal', 'Rouge', 'Shadow',
             'Silver', 'Blaze', 'Espio', 'Mighty', 'Super Sonic', 'Super Shadow']
stage_count = 0
stage = None
sound = None
sound_on = True

##############################################################################################################

class Sonic:
    def __init__(self):
        self.hp = 100
        self.speed = 3
        self.frame = 0
        self.attack = True
        self.damage = 6
        self.time = 0
        self.right = 1
        self.radian = 0
        self.jump = False
        self.jump_sound = load_wav('sound/00_jump.wav')
        self.dir_x, self.dir_y = 0, 0
        self.x, self.y = randrange(100, 700), 130
        self.vector = (0, 0, 0)
        self.image_left = load_image("character/sonic left.png")
        self.image_right = load_image("character/sonic right.png")

    def update(self):
        self.time += 1
        if self.time % 5 == 0:
            self.frame = (self.frame + 1) % 8
        self.x += self.dir_x * self.speed
        if self.jump == True:
            if self.radian <= pi * 3 / 2:
                self.radian += (pi / 8)
                self.y += sin(self.radian) * 6
            else:
                self.y = 130
                self.jump = False
                self.radian = 0
        if self.x > 800:
            self.x = 800
        if self.x < 0:
            self.x = 0

    def draw(self):
        if self.dir_x == 1 or self.right == 1:
            self.image_left.clip_draw(20 + (self.frame * 30), 2320, 30, 40, self.x, self.y)
        if self.dir_x == -1 or self.right == 0:
            self.image_right.clip_draw(3982 - (self.frame * 30), 2320, 30, 40, self.x, self.y)

class Tales:
    def __init__(self):
        self.hp = 100
        self.speed = 1.2
        self.idle_frame = 0
        self.move_frame = 0
        self.jump_frame = 0
        self.attack = True
        self.damage = 6
        self.time = 0
        self.right = 1
        self.radian = 0
        self.jump = False
        self.jump_sound = load_wav('sound/00_jump.wav')
        self.dir_x, self.dir_y = 0, 0
        self.x, self.y = randrange(100, 700), 130
        self.image_left = load_image("character/tales left.png")
        self.image_right = load_image("character/tales right.png")

    def update(self):
        self.time += 1
        if self.time % 5 == 0:
            self.idle_frame = (self.idle_frame + 1) % 8
            self.move_frame = (self.move_frame + 1) % 8
            self.jump_frame = (self.jump_frame + 1) % 8
        self.x += self.dir_x * self.speed
        if self.jump == True:
            if self.radian <= pi * 3 / 2:
                if self.time % 7 == 0:
                    self.radian += (pi / 12)
                    self.y += sin(self.radian) * 10
            else:
                self.y = 130
                self.jump = False
                self.radian = 0
        if self.x > 800:
            self.x = 800
        if self.x < 0:
            self.x = 0

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
            if self.right == 1:
                self.image_left.clip_draw(self.idle_frame * 52 + 20, 2650, 50, 40, self.x, self.y)
            elif self.right == 0:
                self.image_right.clip_draw(4032 - 20 - 50 - self.idle_frame * 52, 2650, 50, 40, self.x, self.y)

class Knuckles:
    def __init__(self):
        self.hp = 100
        self.speed = 1.2
        self.idle_frame = 0
        self.move_frame = 0
        self.jump_frame = 0
        self.attack = True
        self.damage = 6
        self.time = 0
        self.right = 1
        self.radian = 0
        self.jump = False
        self.jump_sound = load_wav('sound/00_jump.wav')
        self.dir_x, self.dir_y = 0, 0
        self.x, self.y = randrange(100, 700), 130
        self.image_left = load_image("character/knuckles left.png")
        self.image_right = load_image("character/knuckles right.png")

    def update(self):
        self.time += 1
        if self.time % 5 == 0:
            self.jump_frame = (self.jump_frame + 1) % 8
        if self.time % 10 == 0:
            self.idle_frame = (self.idle_frame + 1) % 3
        if self.time % 20 == 0:
            self.move_frame = (self.move_frame + 1) % 8
        self.x += self.dir_x * self.speed
        if self.jump == True:
            if self.radian <= pi * 3 / 2:
                if self.time % 7 == 0:
                    self.radian += (pi / 12)
                    self.y += sin(self.radian) * 10
            else:
                self.y = 130
                self.jump = False
                self.radian = 0
        if self.x > 800:
            self.x = 800
        if self.x < 0:
            self.x = 0

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
            if self.right == 1:
                self.image_left.clip_draw(self.idle_frame * 35 + 410, 2980, 35, 40, self.x, self.y)
            elif self.right == 0:
                self.image_right.clip_draw(4032 - 410 - 35 - self.idle_frame * 35, 2980, 35, 40, self.x, self.y)

class AmyRose:
    def __init__(self):
        self.hp = 100
        self.speed = 1.2
        self.idle_frame = 0
        self.move_frame = 0
        self.jump_frame = 0
        self.attack = True
        self.damage = 6
        self.time = 0
        self.right = 1
        self.radian = 0
        self.jump = False
        self.jump_sound = load_wav('sound/00_jump.wav')
        self.dir_x, self.dir_y = 0, 0
        self.x, self.y = randrange(100, 700), 130
        self.image_left = load_image("character/amy rose left.png")
        self.image_right = load_image("character/amy rose right.png")

    def update(self):
        self.time += 1
        if self.time % 30 == 0:
            self.idle_frame = (self.idle_frame + 1) % 8
        if self.time % 10 == 0:
            self.move_frame = (self.move_frame + 1) % 8
            self.jump_frame = (self.jump_frame + 1) % 7
        self.x += self.dir_x * self.speed
        if self.jump == True:
            if self.radian <= pi * 3 / 2:
                if self.time % 7 == 0:
                    self.radian += (pi / 12)
                    self.y += sin(self.radian) * 10
            else:
                self.y = 130
                self.jump = False
                self.radian = 0
        if self.x > 800:
            self.x = 800
        if self.x < 0:
            self.x = 0

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
            if self.right == 1:
                self.image_left.clip_draw(self.idle_frame * 28 + 2, 2750, 30, 40, self.x, self.y)
            elif self.right == 0:
                self.image_right.clip_draw(4032 - 30 - 2 - self.idle_frame * 28, 2750, 30, 40, self.x, self.y)

class Tikal:
    def __init__(self):
        self.hp = 100
        self.speed = 3
        self.frame = 0
        self.attack = True
        self.damage = 6
        self.time = 0
        self.right = 1
        self.radian = 0
        self.jump = False
        self.jump_sound = load_wav('sound/00_jump.wav')
        self.dir_x, self.dir_y = 0, 0
        self.x, self.y = randrange(100, 700), 130
        self.image_left = load_image("character/tikal left.png")
        self.image_right = load_image("character/tikal right.png")

    def update(self):
        self.time += 1
        if self.time % 5 == 0:
            self.frame = (self.frame + 1) % 6
        self.x += self.dir_x * self.speed
        if self.jump == True:
            if self.radian <= pi * 3 / 2:
                self.radian += (pi / 8)
                self.y += sin(self.radian) * 6
            else:
                self.y = 130
                self.jump = False
                self.radian = 0
        if self.x > 800:
            self.x = 800
        if self.x < 0:
            self.x = 0

    def draw(self):
        if self.dir_x == 1 or self.right == 1:
            self.image_left.clip_draw(self.frame * 30 + 5, 2754, 30, 40, self.x, self.y)
        if self.dir_x == -1 or self.right == 0:
            self.image_right.clip_draw(4032 - 5 - 30 - self.frame * 30, 2754, 30, 40, self.x, self.y)

class Rouge:
    def __init__(self):
        self.hp = 100
        self.speed = 3
        self.frame = 0
        self.attack = True
        self.damage = 6
        self.time = 0
        self.right = 1
        self.radian = 0
        self.jump = False
        self.jump_sound = load_wav('sound/00_jump.wav')
        self.dir_x, self.dir_y = 0, 0
        self.x, self.y = randrange(100, 700), 130
        self.image_left = load_image("character/rouge left.png")
        self.image_right = load_image("character/rouge right.png")

    def update(self):
        self.time += 1
        if self.time % 5 == 0:
            self.frame = (self.frame + 1) % 6
        self.x += self.dir_x * self.speed
        if self.jump == True:
            if self.radian <= pi * 3 / 2:
                self.radian += (pi / 8)
                self.y += sin(self.radian) * 6
            else:
                self.y = 130
                self.jump = False
                self.radian = 0
        if self.x > 800:
            self.x = 800
        if self.x < 0:
            self.x = 0

    def draw(self):
        if self.dir_x == 1 or self.right == 1:
            self.image_left.clip_draw(self.frame * 28, 2984, 28, 40, self.x, self.y)
        if self.dir_x == -1 or self.right == 0:
            self.image_right.clip_draw(4032 - 28 - self.frame * 28, 2984, 28, 40, self.x, self.y)

class Shadow:
    def __init__(self):
        self.hp = 100
        self.speed = 1.2
        self.idle_frame = 0
        self.move_frame = 0
        self.jump_frame = 0
        self.attack = True
        self.damage = 6
        self.time = 0
        self.right = 1
        self.radian = 0
        self.jump = False
        self.jump_sound = load_wav('sound/00_jump.wav')
        self.dir_x, self.dir_y = 0, 0
        self.x, self.y = randrange(100, 700), 130
        self.image_left = load_image("character/shadow left.png")
        self.image_right = load_image("character/shadow right.png")

    def update(self):
        self.time += 1
        if self.time % 5 == 0:
            self.move_frame = (self.move_frame + 1) % 8
        if self.time % 10 == 0:
            self.idle_frame = (self.idle_frame + 1) % 4
        self.jump_frame = (self.jump_frame + 1) % 4

        self.x += self.dir_x * self.speed
        if self.jump == True:
            if self.radian <= pi * 3 / 2:
                if self.time % 7 == 0:
                    self.radian += (pi / 12)
                    self.y += sin(self.radian) * 10
            else:
                self.y = 130
                self.jump = False
                self.radian = 0
        if self.x > 800:
            self.x = 800
        if self.x < 0:
            self.x = 0

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
            if self.right == 1:
                self.image_left.clip_draw(self.idle_frame * 35 + 202, 2958, 37, 40, self.x, self.y)
            elif self.right == 0:
                self.image_right.clip_draw(4032 - 202 - 37 - self.idle_frame * 35, 2958, 37, 40, self.x, self.y)

##############################################################################################################

class Silver:
    def __init__(self):
        self.hp = 100
        self.speed = 3
        self.frame = 0
        self.attack = True
        self.damage = 6
        self.time = 0
        self.right = 1
        self.radian = 0
        self.jump = False
        self.jump_sound = load_wav('sound/00_jump.wav')
        self.dir_x, self.dir_y = 0, 0
        self.x, self.y = randrange(100, 700), 130
        self.image_left = load_image("character/silver right.png")
        self.image_right = load_image("character/silver left.png")

    def update(self):
        self.time += 1
        if self.time % 5 == 0:
            self.frame = (self.frame + 1) % 7
        self.x += self.dir_x * self.speed
        if self.jump == True:
            if self.radian <= pi * 3 / 2:
                self.radian += (pi / 8)
                self.y += sin(self.radian) * 6
            else:
                self.y = 130
                self.jump = False
                self.radian = 0
        if self.x > 800:
            self.x = 800
        if self.x < 0:
            self.x = 0

    def draw(self):
        if self.dir_x == 1 or self.right == 1:
            self.image_left.clip_draw(4032 - 40 - self.frame * 50, 2984, 40, 40, self.x, self.y)
        if self.dir_x == -1 or self.right == 0:
            self.image_right.clip_draw(self.frame * 50, 2984, 40, 40, self.x, self.y)

class Blaze:
    def __init__(self):
        self.hp = 100
        self.speed = 3
        self.frame = 0
        self.attack = True
        self.damage = 6
        self.time = 0
        self.right = 1
        self.radian = 0
        self.jump = False
        self.jump_sound = load_wav('sound/00_jump.wav')
        self.dir_x, self.dir_y = 0, 0
        self.x, self.y = randrange(100, 700), 130
        self.image_left = load_image("character/blaze left.png")
        self.image_right = load_image("character/blaze right.png")

    def update(self):
        self.time += 1
        if self.time % 5 == 0:
            self.frame = (self.frame + 1) % 13
        self.x += self.dir_x * self.speed
        if self.jump == True:
            if self.radian <= pi * 3 / 2:
                self.radian += (pi / 8)
                self.y += sin(self.radian) * 6
            else:
                self.y = 130
                self.jump = False
                self.radian = 0
        if self.x > 800:
            self.x = 800
        if self.x < 0:
            self.x = 0

    def draw(self):
        if self.dir_x == 1 or self.right == 1:
            self.image_left.clip_draw(self.frame * 31 + 382, 1710, 30, 40, self.x, self.y)
        if self.dir_x == -1 or self.right == 0:
            self.image_right.clip_draw(4032 - 382 - 30 - self.frame * 31, 1710, 30, 40, self.x, self.y)

class Espio:
    def __init__(self):
        self.hp = 100
        self.speed = 1.2
        self.idle_frame = 0
        self.move_frame = 0
        self.jump_frame = 0
        self.attack = True
        self.damage = 6
        self.time = 0
        self.right = 1
        self.radian = 0
        self.jump = False
        self.jump_sound = load_wav('sound/00_jump.wav')
        self.dir_x, self.dir_y = 0, 0
        self.x, self.y = 400, 130 # randrange(100, 700), 130
        self.image_left = load_image("character/espio left.png")
        self.image_right = load_image("character/espio right.png")

    def update(self):
        self.time += 1
        if self.time % 20 == 0:
            self.idle_frame = (self.idle_frame + 1) % 6
            self.move_frame = (self.move_frame + 1) % 9
        if self.time % 20 == 0:
            self.jump_frame = (self.jump_frame + 1) % 10
        self.x += self.dir_x * self.speed
        if self.jump == True:
            if self.radian <= pi * 3 / 2:
                if self.time % 7 == 0:
                    self.radian += (pi / 12)
                    self.y += sin(self.radian) * 10
            else:
                self.y = 130
                self.jump = False
                self.radian = 0
        if self.x > 800:
            self.x = 800
        if self.x < 0:
            self.x = 0

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
            if self.right == 1:
                self.image_left.clip_draw(self.idle_frame * 27 + 5, 1220, 27, 40, self.x, self.y)
            elif self.right == 0:
                self.image_right.clip_draw(4032 - 27 - 5 - self.idle_frame * 27, 1220, 27, 40, self.x, self.y)

class Mighty:
    def __init__(self):
        self.hp = 100
        self.speed = 1.2
        self.idle_frame = 0
        self.move_frame = 0
        self.jump_frame = 0
        self.attack = True
        self.damage = 6
        self.time = 0
        self.right = 1
        self.radian = 0
        self.jump = False
        self.jump_sound = load_wav('sound/00_jump.wav')
        self.dir_x, self.dir_y = 0, 0
        self.x, self.y = randrange(100, 700), 130
        self.image_left = load_image("character/mighty left.png")
        self.image_right = load_image("character/mighty right.png")

    def update(self):
        self.time += 1
        if self.time % 5 == 0:
            self.idle_frame = (self.idle_frame + 1) % 7
            self.move_frame = (self.move_frame + 1) % 8
        if self.time % 20 == 0:
            self.jump_frame = (self.jump_frame + 1) % 7
        self.x += self.dir_x * self.speed
        if self.jump == True:
            if self.radian <= pi * 3 / 2:
                if self.time % 7 == 0:
                    self.radian += (pi / 12)
                    self.y += sin(self.radian) * 10
            else:
                self.y = 130
                self.jump = False
                self.radian = 0
        if self.x > 800:
            self.x = 800
        if self.x < 0:
            self.x = 0

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
            if self.right == 1:
                self.image_left.clip_draw(self.idle_frame * 28 + 5, 2870, 30, 35, self.x, self.y)
            elif self.right == 0:
                self.image_right.clip_draw(4032 - 28 - 5 - self.idle_frame * 28, 2870, 30, 35, self.x, self.y)

class SuperSonic:
    def __init__(self):
        self.hp = 100
        self.speed = 1.2
        self.idle_frame = 0
        self.move_frame = 0
        self.jump_frame = 0
        self.attack = True
        self.damage = 6
        self.time = 0
        self.right = 1
        self.radian = 0
        self.jump = False
        self.jump_sound = load_wav('sound/00_jump.wav')
        self.dir_x, self.dir_y = 0, 0
        self.x, self.y = 400, 130 #randrange(100, 700), 130
        self.image_left = load_image("character/super sonic left.png")
        self.image_right = load_image("character/super sonic right.png")

    def update(self):
        self.time += 1
        if self.time % 20 == 0:
            self.idle_frame = (self.idle_frame + 1) % 6
        if self.time % 10 == 0:
            self.jump_frame = (self.jump_frame + 1) % 4
        self.x += self.dir_x * self.speed
        if self.jump == True:
            if self.radian <= pi * 3 / 2:
                if self.time % 7 == 0:
                    self.radian += (pi / 12)
                    self.y += sin(self.radian) * 10
            else:
                self.y = 130
                self.jump = False
                self.radian = 0
        if self.x > 800:
            self.x = 800
        if self.x < 0:
            self.x = 0

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
            if self.right == 1:
                self.image_left.clip_draw(self.idle_frame * 25 + 2, 2890, 24, 46, self.x, self.y)
            elif self.right == 0:
                self.image_right.clip_draw(4032 - 24 - 2 - self.idle_frame * 25, 2890, 24, 46, self.x, self.y)

class SuperShadow:
    def __init__(self):
        self.hp = 100
        self.speed = 1.2
        self.idle_frame = 0
        self.move_frame = 0
        self.jump_frame = 0
        self.attack = True
        self.damage = 6
        self.time = 0
        self.right = 1
        self.radian = 0
        self.jump = False
        self.jump_sound = load_wav('sound/00_jump.wav')
        self.dir_x, self.dir_y = 0, 0
        self.x, self.y = randrange(100, 700), 130
        self.image_left = load_image("character/super shadow right.png")
        self.image_right = load_image("character/super shadow left.png")

    def update(self):
        self.time += 1
        if self.time % 5 == 0:
            self.idle_frame = (self.idle_frame + 1) % 2
        if self.time % 7 == 0:
            self.move_frame = (self.move_frame + 1) % 5
        self.jump_frame = (self.jump_frame + 1) % 6
        self.x += self.dir_x * self.speed
        if self.jump == True:
            if self.radian <= pi * 3 / 2:
                if self.time % 7 == 0:
                    self.radian += (pi / 12)
                    self.y += sin(self.radian) * 10
            else:
                self.y = 130
                self.jump = False
                self.radian = 0
        if self.x > 800:
            self.x = 800
        if self.x < 0:
            self.x = 0

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
            if self.right == 1:
                self.image_left.clip_draw(4032 - 282 - 25 - self.idle_frame * 26, 2940, 25, 38, self.x, self.y)
            elif self.right == 0:
                self.image_right.clip_draw(self.idle_frame * 25 + 282, 2940, 25, 38, self.x, self.y)

##############################################################################################################

class Palm:
    image = None
    image_floor = None

    def __init__(self):
        self.image = load_image('map/palmtree.png')
        self.image_floor = load_image('map/palmtree floor.png')

    def draw(self):
        self.image.clip_draw(0, 600, 1000, 600, 400, 300)
        for i in range(0, 30):
            self.image_floor.clip_draw(0, 0, 100, 40, i * 30 + 50, 100)

class Lake:
    image = None
    image_floor = None

    def __init__(self):
        self.image = load_image('map/lake.png')

    def draw(self):
        self.image.clip_draw(0, 0, 800, 600, 400, 300)

##############################################################################################################

def RandomCharacter():
    global player_character
    if choice(character) == 'Sonic':
        player_character = Sonic()
    elif choice(character) == 'Tales':
        player_character = Tales()
    elif choice(character) == 'Knuckles':
        player_character = Knuckles()
    elif choice(character) == 'AmyRose':
        player_character = AmyRose()
    elif choice(character) == 'Tikal':
        player_character = Tikal()
    elif choice(character) == 'Rouge':
        player_character = Rouge()
    elif choice(character) == 'Shadow':
        player_character = Shadow()
    elif choice(character) == 'Silver':
        player_character = Silver()
    elif choice(character) == 'Blaze':
        player_character = Blaze()
    elif choice(character) == 'Espio':
        player_character = Espio()
    elif choice(character) == 'Mighty':
        player_character = Mighty()
    elif choice(character) == 'Super Sonic':
        player_character = SuperSonic()
    elif choice(character) == 'Super Shadow':
        player_character = SuperShadow()

def handle_events():
    global player_character, stage, stage_count, sound, sound_on
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
            elif event.key == SDLK_SPACE:
                stage_count += 1
                if(stage_count >= 3):
                    stage_count = 0
                    result_state.win = True
                    game_framework.change_state(result_state)
                else:
                    game_framework.push_state(middle_state)
            elif event.key == SDLK_UP:
                if player_character.y == 130:
                    player_character.jump = True
                    player_character.jump_sound.play()
                    player_character.jump_sound.set_volume(10)
            elif event.key == SDLK_LEFT:
                player_character.right = 0
                player_character.dir_x = -1
            elif event.key == SDLK_RIGHT:
                player_character.right = 1
                player_character.dir_x = 1
            elif event.key == SDLK_1:
                RandomCharacter()
            elif event.key == SDLK_F8:
                sound_on = ~sound_on
                if(sound_on == True):
                    sound.repeat_play()
                else:
                    sound.stop()
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_UP:
                pass
            elif event.key == SDLK_LEFT:
                if player_character.right == 1:
                    player_character.dir_x = 1
                else:
                    player_character.dir_x = 0
            elif event.key == SDLK_RIGHT:
                if player_character.right == 0:
                    player_character.dir_x = -1
                else:
                    player_character.dir_x = 0

##############################################################################################################

def enter():
    global player_character, stage, stage_count, sound
    if stage_count == 0:
        player_character = Tikal()
        stage = Palm()
        sound = load_music('sound/Tropical.mp3')
        sound.set_volume(20)
        sound.repeat_play()
    stage_count = 0

def exit():
    global player_character, stage, sound
    del player_character, stage, sound

def update():
    player_character.update()
    handle_events()

def draw():
    clear_canvas()
    stage.draw()
    player_character.draw()
    update_canvas()

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