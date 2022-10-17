from pico2d import *
from random import *
from math import *
import time
import game_framework
import game

player_character = None
character = ['Sonic', 'Tales', 'Knuckles', 'AmyRose', 'Tikal', 'Rouge', 'Shadow',
             'Silver', 'Blaze', 'Espio', 'Mighty', 'Super Sonic', 'Super Shadow']
stage_count = None
stage = None

g = -9.81
t = 0
radian = 0 * pi / 180

#######################################################
class Sonic:
    def __init__(self):
        self.hp = 100
        self.speed = 5
        self.frame = 0
        self.time = 0
        self.right = 1
        self.dir_x, self.dir_y = 0, 0
        self.x, self.y = 225, 130
        self.vector = (0, 0, 0)
        self.image_left = load_image("character/sonic left.png")
        self.image_right = load_image("character/sonic right.png")

    def update(self):
        self.time += 1
        if self.time % 3 == 0:
            self.frame = (self.frame + 1) % 8
        self.x += self.dir_x * self.speed * cos(radian)
        self.y += self.speed * sin(radian) - (g * t / 2)

        if self.x > game.window_size_x:
            self.x = game.window_size_x
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
        self.speed = 2
        self.frame = 0
        self.time = 0
        self.right = 1
        self.dir_x, self.dir_y = 0, 0
        self.x, self.y = 30, 130
        self.image_left = load_image("character/tales left.png")
        self.image_right = load_image("character/tales right.png")

    def update(self):
        self.time += 1
        if self.time % 3 == 0:
            self.frame = (self.frame + 1) % 8
        self.x += self.dir_x * self.speed
        self.y += self.dir_y * self.speed
        if self.x > game.window_size_x:
            self.x = game.window_size_x
        if self.x < 0:
            self.x = 0

    def draw(self):
        if self.dir_x == 1 or self.right == 1:
            self.image_left.clip_draw(self.frame * 55 + 10, 2980, 50, 40, self.x, self.y)
        if self.dir_x == -1 or self.right == 0:
            self.image_right.clip_draw(3972 - self.frame * 55, 2980, 50, 40, self.x, self.y)

class Knuckles:
    def __init__(self):
        self.hp = 100
        self.speed = 2
        self.frame = 0
        self.time = 0
        self.right = 1
        self.dir_x, self.dir_y = 0, 0
        self.x, self.y = 30, 130
        self.image_left = load_image("character/knuckles left.png")
        self.image_right = load_image("character/knuckles right.png")

    def update(self):
        self.time += 1
        if self.time % 3 == 0:
            self.frame = (self.frame + 1) % 3
        self.x += self.dir_x * self.speed
        self.y += self.dir_y * self.speed
        if self.x > game.window_size_x:
            self.x = game.window_size_x
        if self.x < 0:
            self.x = 0

    def draw(self):
        if self.dir_x == 1 or self.right == 1:
            self.image_left.clip_draw(self.frame * 35 + 410, 2980, 35, 40, self.x, self.y)
        if self.dir_x == -1 or self.right == 0:
            self.image_right.clip_draw(4032 - 410 - 35 - self.frame * 35, 2980, 35, 40, self.x, self.y)

class AmyRose:
    def __init__(self):
        self.hp = 100
        self.speed = 2
        self.frame = 0
        self.time = 0
        self.right = 1
        self.dir_x, self.dir_y = 0, 0
        self.x, self.y = 30, 130
        self.image_left = load_image("character/amy rose left.png")
        self.image_right = load_image("character/amy rose right.png")

    def update(self):
        self.time += 1
        if self.time % 3 == 0:
            self.frame = (self.frame + 1) % 8
        self.x += self.dir_x * self.speed
        self.y += self.dir_y * self.speed
        if self.x > game.window_size_x:
            self.x = game.window_size_x
        if self.x < 0:
            self.x = 0

    def draw(self):
        # if self.dir_x == 1 or self.right == 1:
            self.image_left.clip_draw(self.frame * 28 + 2, 2750, 30, 40, self.x, self.y)
        # if self.dir_x == -1 or self.right == 0:
        #     self.image_right.clip_draw(self.frame, 300, 400, 300, self.x, self.y)

class Tikal:
    def __init__(self):
        self.hp = 100
        self.speed = 2
        self.frame = 0
        self.time = 0
        self.right = 1
        self.dir_x, self.dir_y = 0, 0
        self.x, self.y = 30, 130
        self.image_left = load_image("character/tikal left.png")
        self.image_right = load_image("character/tikal right.png")

    def update(self):
        self.time += 1
        if self.time % 3 == 0:
            self.frame = (self.frame + 1) % 6
        self.x += self.dir_x * self.speed
        self.y += self.dir_y * self.speed
        if self.x > game.window_size_x:
            self.x = game.window_size_x
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
        self.speed = 2
        self.frame = 0
        self.time = 0
        self.right = 1
        self.dir_x, self.dir_y = 0, 0
        self.x, self.y = 30, 130
        self.image_left = load_image("character/rouge left.png")
        self.image_right = load_image("character/rouge right.png")

    def update(self):
        if self.time % 3 == 0:
            self.frame = (self.frame + 1) % 6
        self.x += self.dir_x * self.speed
        self.y += self.dir_y * self.speed
        if self.x > game.window_size_x:
            self.x = game.window_size_x
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
        self.speed = 2
        self.frame = 0
        self.time = 0
        self.right = 1
        self.dir_x, self.dir_y = 0, 0
        self.x, self.y = 30, 130
        self.image_left = load_image("character/shadow left.png")
        self.image_right = load_image("character/shadow right.png")

    def update(self):
        if self.time % 3 == 0:
            self.frame = (self.frame + 1) % 4
        self.x += self.dir_x * self.speed
        self.y += self.dir_y * self.speed
        if self.x > game.window_size_x:
            self.x = game.window_size_x
        if self.x < 0:
            self.x = 0

    def draw(self):
        if self.dir_x == 1 or self.right == 1:
            self.image_left.clip_draw(self.frame * 35 + 202, 2960, 37, 40, self.x, self.y)
        if self.dir_x == -1 or self.right == 0:
            self.image_right.clip_draw(4032 - 202 - 37 - self.frame * 35, 2960, 37, 40, self.x, self.y)

#######################################################
class Silver:
    def __init__(self):
        self.hp = 100
        self.speed = 2
        self.frame = 0
        self.time = 0
        self.right = 1
        self.dir_x, self.dir_y = 0, 0
        self.x, self.y = 30, 130
        self.image_left = load_image("character/silver left.png")
        self.image_right = load_image("character/silver right.png")

    def update(self):
        if self.time % 3 == 0:
            self.frame = (self.frame + 1) % 7
        self.x += self.dir_x * self.speed
        self.y += self.dir_y * self.speed
        if self.x > game.window_size_x:
            self.x = game.window_size_x
        if self.x < 0:
            self.x = 0

    def draw(self):
        if self.dir_x == 1 or self.right == 1:
            self.image_left.clip_draw(self.frame * 50, 2984, 40, 40, self.x, self.y)
        if self.dir_x == -1 or self.right == 0:
            self.image_right.clip_draw(4032 - 40 - self.frame * 50, 2984, 40, 40, self.x, self.y)

class Blaze:
    def __init__(self):
        self.hp = 100
        self.speed = 2
        self.frame = 0
        self.time = 0
        self.right = 1
        self.dir_x, self.dir_y = 1, 0
        self.x, self.y = 30, 130
        self.image_left = load_image("character/blaze left.png")
        self.image_right = load_image("character/blaze right.png")

    def update(self):
        self.time += 1
        if self.time % 3 == 0:
            self.frame = (self.frame + 1) % 13
        self.x += self.dir_x * self.speed
        self.y += self.dir_y * self.speed
        if self.x > game.window_size_x:
            self.x = game.window_size_x
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
        self.speed = 2
        self.frame = 0
        self.time = 0
        self.right = 1
        self.dir_x, self.dir_y = 0, 0
        self.x, self.y = 30, 130
        self.image_left = load_image("character/espio left.png")
        self.image_right = load_image("character/espio right.png")

    def update(self):
        self.time += 1
        if self.time % 3 == 0:
            self.frame = (self.frame + 1) % 6
        self.x += self.dir_x * self.speed
        self.y += self.dir_y * self.speed
        if self.x > game.window_size_x:
            self.x = game.window_size_x
        if self.x < 0:
            self.x = 0

    def draw(self):
        if self.dir_x == 1 or self.right == 1:
            self.image_left.clip_draw(self.frame * 27 + 5, 1220, 30, 40, self.x, self.y)
        if self.dir_x == -1 or self.right == 0:
            self.image_right.clip_draw(4032 - 30 - self.frame * 27, 1220, 30, 40, self.x, self.y)

class Mighty:
    def __init__(self):
        self.hp = 100
        self.speed = 2
        self.frame = 0
        self.time = 0
        self.right = 1
        self.dir_x, self.dir_y = 0, 0
        self.x, self.y = 30, 130
        self.image_left = load_image("character/mighty left.png")
        self.image_right = load_image("character/mighty right.png")

    def update(self):
        self.time += 1
        if self.time % 3 == 0:
            self.frame = (self.frame + 1) % 7
        self.x += self.dir_x * self.speed
        self.y += self.dir_y * self.speed
        if self.x > game.window_size_x:
            self.x = game.window_size_x
        if self.x < 0:
            self.x = 0

    def draw(self):
        if self.dir_x == 1 or self.right == 1:
            self.image_left.clip_draw(self.frame * 25 + 3, 2880, 27, 40, self.x, self.y)
        if self.dir_x == -1 or self.right == 0:
            self.image_right.clip_draw(4032 - 3 - 27 - self.frame * 25, 2880, 27, 40, self.x, self.y)

class SuperSonic:
    def __init__(self):
        self.hp = 100
        self.speed = 2
        self.frame = 0
        self.time = 0
        self.right = 1
        self.dir_x, self.dir_y = 0, 0
        self.x, self.y = 30, 130
        self.image_left = load_image("character/super sonic left.png")
        self.image_right = load_image("character/super sonic right.png")

    def update(self):
        self.time += 1
        if self.time % 3 == 0:
            self.frame = (self.frame + 1) % 6
        self.x += self.dir_x * self.speed
        self.y += self.dir_y * self.speed
        if self.x > game.window_size_x:
            self.x = game.window_size_x
        if self.x < 0:
            self.x = 0

    def draw(self):
        if self.dir_x == 1 or self.right == 1:
            self.image_left.clip_draw(self.frame * 24, 2894, 24, 46, self.x, self.y)
        if self.dir_x == -1 or self.right == 0:
            self.image_right.clip_draw(4032 - 24 - self.frame * 24, 2894, 24, 46, self.x, self.y)

class SuperShadow:
    def __init__(self):
        self.hp = 100
        self.speed = 2
        self.frame = 0
        self.time = 0
        self.right = 1
        self.dir_x, self.dir_y = 0, 0
        self.x, self.y = 30, 130
        self.image_left = load_image("character/super shadow right.png")
        self.image_right = load_image("character/super shadow left.png")

    def update(self):
        self.time += 1
        if self.time % 5 == 0:
            self.frame = (self.frame + 1) % 2
        self.x += self.dir_x * self.speed
        self.y += self.dir_y * self.speed
        if self.x > game.window_size_x:
            self.x = game.window_size_x
        if self.x < 0:
            self.x = 0

    def draw(self):
        if self.dir_x == 1 or self.right == 1:
            self.image_left.clip_draw(4032 - 280 - 26 - self.frame * 26, 2940, 26, 40, self.x, self.y)
        if self.dir_x == -1 or self.right == 0:
            self.image_right.clip_draw(self.frame * 26 + 280, 2940, 26, 40, self.x, self.y)
#######################################################

class Palm:
    image = None
    image_floor = None
    def draw(self):
        self.image = load_image('map/palmtree.png')
        self.image_floor = load_image('map/palmtree floor.png')

        self.image.clip_draw(0, 600, 1000, 600, 400, 300)
        for i in range(0, 7):
            self.image_floor.clip_draw(0, 0, 100, 40, i * 30 + 50, 100)
        for i in range(0, 7):
            self.image_floor.clip_draw(0, 0, 100, 40, i * 30 + 340, 100)
        for i in range(0, 7):
            self.image_floor.clip_draw(0, 0, 100, 40, i * 30 + 630, 100)

#######################################################

#######################################################
def handle_events():
    global player_character, stage, stage_count, g, t, radian

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
            elif event.key == SDLK_UP:
                player_character.y += player_character.speed * sin(radian) - (g * t / 2)
                print(t)
            elif event.key == SDLK_LEFT:
                player_character.right = 0
                player_character.dir_x = -1
            elif event.key == SDLK_RIGHT:
                player_character.right = 1
                player_character.dir_x = 1
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_UP:
                player_character.dir_y = 0
            elif event.key == SDLK_LEFT:
                player_character.dir_x = 0
            elif event.key == SDLK_RIGHT:
                player_character.dir_x = 0
    delay(0.01)

def enter():
    global player_character, stage, stage_count
    player_character = SuperShadow()
    stage = Palm()
    stage_count = 0

def exit():
    global player_character, stage, stage_count
    del player_character, stage, stage_count

def update():
    global g, t, radian

    t += 0.01
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