from pico2d import *
import random
import game_framework
import game
import frametime

player_character = None
character = ['Sonic', 'Tales', 'Knuckles', 'AmyRose', 'Tikal', 'Rouge', 'Shadow',
             'Silver', 'Blaze', 'Espio', 'Mighty', 'Super Sonic', 'Super Shadow']
stage_count = None
stage = None

#######################################################
class Sonic:
    def __init__(self):
        self.hp = 100
        self.speed = 2
        self.frame = 0
        self.right = 1
        self.dir_x, self.dir_y = 0, 0
        self.x, self.y = 30, 130
        self.image_left = load_image("character/sonic left.png")
        self.image_right = load_image("character/sonic left.png")

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir_x * self.speed * frametime.FrameTime()
        self.y += self.dir_y * self.speed * frametime.FrameTime()
        InsideWindow(self.x, self.y)

    def draw(self):
        if self.dir_x == 1 or self.right == 1:
            self.image_left.clip_draw(20 + (self.frame * 30), 2320, 30, 40, self.x, self.y)
        if self.dir_x == -1 or self.right == 0:
            self.image_right.clip_draw(20 + self.frame * 30, 3000, 30, 40, self.x, self.y)
        delay(0.05)

class Tales:
    def __init__(self):
        self.hp = 100
        self.speed = 2
        self.frame = 0
        self.right = 1
        self.dir_x, self.dir_y = 0, 0
        self.x, self.y = 30, 130
        self.image_left = load_image("character/tales left.png")
        self.image_right = load_image("character/tales left.png")

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir_x * self.speed * frametime.FrameTime()
        self.y += self.dir_y * self.speed * frametime.FrameTime()
        InsideWindow(self.x, self.y)

    def draw(self):
        if self.dir_x == 1 or self.right == 1:
            self.image_left.clip_draw(self.frame * 55 + 10, 2980, 50, 40, self.x, self.y)
        if self.dir_x == -1 or self.right == 0:
            self.image_right.clip_draw(self.frame, 300, 400, 300, self.x, self.y)
        delay(0.01)

class Knuckles:
    def __init__(self):
        self.hp = 100
        self.speed = 2
        self.frame = 0
        self.right = 1
        self.dir_x, self.dir_y = 0, 0
        self.x, self.y = 30, 130
        self.image_left = load_image("character/knuckles left.png")
        self.image_right = load_image("character/knuckles left.png")

    def update(self):
        self.x += self.dir_x * self.speed * frametime.FrameTime()
        self.y += self.dir_y * self.speed * frametime.FrameTime()
        InsideWindow(self.x, self.y)

    def draw(self):
        if self.dir_x == 1 or self.right == 1:
            self.image_left.clip_draw(self.frame, 300, 400, 300, self.x, self.y)
        if self.dir_x == -1 or self.right == 0:
            self.image_right.clip_draw(self.frame, 300, 400, 300, self.x, self.y)

class AmyRose:
    def __init__(self):
        self.hp = 100
        self.speed = 2
        self.frame = 0
        self.right = 1
        self.dir_x, self.dir_y = 0, 0
        self.x, self.y = 30, 130
        self.image_left = load_image("character/amy rose left.png")
        self.image_right = load_image("character/amy rose left.png")

    def update(self):
        self.x += self.dir_x * self.speed * frametime.FrameTime()
        self.y += self.dir_y * self.speed * frametime.FrameTime()
        InsideWindow(self.x, self.y)

    def draw(self):
        if self.dir_x == 1 or self.right == 1:
            self.image_left.clip_draw(self.frame, 300, 400, 300, self.x, self.y)
        if self.dir_x == -1 or self.right == 0:
            self.image_right.clip_draw(self.frame, 300, 400, 300, self.x, self.y)

class Tikal:
    def __init__(self):
        self.hp = 100
        self.speed = 2
        self.frame = 0
        self.right = 1
        self.dir_x, self.dir_y = 0, 0
        self.x, self.y = 30, 130
        self.image_left = load_image("character/tikal left.png")
        self.image_right = load_image("character/tikal right.png")

    def update(self):
        self.frame = (self.frame + 1) % 6
        self.x += self.dir_x * self.speed * frametime.FrameTime()
        self.y += self.dir_y * self.speed * frametime.FrameTime()
        InsideWindow(self.x, self.y)

    def draw(self):
        if self.dir_x == 1 or self.right == 1:
            self.image_left.clip_draw(self.frame * 30 + 5, 2754, 30, 40, self.x, self.y)
        if self.dir_x == -1 or self.right == 0:
            self.image_right.clip_draw(self.frame, 300, 400, 300, self.x, self.y)
        delay(0.01)

class Rouge:
    def __init__(self):
        self.hp = 100
        self.speed = 2
        self.frame = 0
        self.right = 1
        self.dir_x, self.dir_y = 0, 0
        self.x, self.y = 30, 130
        self.image_left = load_image("character/rouge left.png")
        self.image_right = load_image("character/rouge right.png")

    def update(self):
        self.frame = (self.frame + 1) % 6
        self.x += self.dir_x * self.speed * frametime.FrameTime()
        self.y += self.dir_y * self.speed * frametime.FrameTime()
        InsideWindow(self.x, self.y)

    def draw(self):
        if self.dir_x == 1 or self.right == 1:
            self.image_left.clip_draw(self.frame * 28, 2984, 28, 40, self.x, self.y)
        if self.dir_x == -1 or self.right == 0:
            self.image_right.clip_draw(self.frame, 300, 400, 300, self.x, self.y)
        delay(0.01)

class Shadow:
    def __init__(self):
        self.hp = 100
        self.speed = 2
        self.frame = 0
        self.right = 1
        self.dir_x, self.dir_y = 0, 0
        self.x, self.y = 30, 130
        self.image_left = load_image("character/shadow left.png")
        self.image_right = load_image("character/shadow right.png")

    def update(self):
        self.frame = (self.frame + 1) % 4
        self.x += self.dir_x * self.speed * frametime.FrameTime()
        self.y += self.dir_y * self.speed * frametime.FrameTime()
        InsideWindow(self.x, self.y)

    def draw(self):
        if self.dir_x == 1 or self.right == 1:
            self.image_left.clip_draw(self.frame * 35 + 202, 2960, 37, 40, self.x, self.y)
        if self.dir_x == -1 or self.right == 0:
            self.image_right.clip_draw(self.frame, 300, 400, 300, self.x, self.y)
        delay(0.01)

#######################################################
class Silver:
    def __init__(self):
        self.hp = 100
        self.speed = 2
        self.frame = 0
        self.right = 1
        self.dir_x, self.dir_y = 0, 0
        self.x, self.y = 30, 130
        self.image_left = load_image("character/silver left.png")
        self.image_right = load_image("character/silver right.png")

    def update(self):
        self.frame = (self.frame + 1) % 7
        self.x += self.dir_x * self.speed * frametime.FrameTime()
        self.y += self.dir_y * self.speed * frametime.FrameTime()
        InsideWindow(self.x, self.y)

    def draw(self):
        if self.dir_x == 1 or self.right == 1:
            self.image_left.clip_draw(self.frame * 50, 2984, 40, 40, self.x, self.y)
        if self.dir_x == -1 or self.right == 0:
            self.image_right.clip_draw(self.frame, 300, 400, 300, self.x, self.y)
        delay(0.01)

class Blaze:
    def __init__(self):
        self.hp = 100
        self.speed = 2
        self.frame = 0
        self.right = 1
        self.dir_x, self.dir_y = 1, 0
        self.x, self.y = 30, 130
        self.image_left = load_image("character/blaze left.png")
        self.image_right = load_image("character/blaze right.png")

    def update(self):
        self.frame = (self.frame + 1) % 13
        self.x += self.dir_x * self.speed * frametime.FrameTime()
        self.y += self.dir_y * self.speed * frametime.FrameTime()
        InsideWindow(self.x, self.y)

    def draw(self):
        if self.dir_x == 1 or self.right == 1:
            self.image_left.clip_draw(self.frame * 31 + 382, 1710, 30, 40, 400, 300)
        if self.dir_x == -1 or self.right == 0:
            self.image_right.clip_draw(self.frame, 0, 0, 0, 400, 300)
        delay(0.01)

class Espio:
    def __init__(self):
        self.hp = 100
        self.speed = 2
        self.frame = 0
        self.right = 1
        self.dir_x, self.dir_y = 0, 0
        self.x, self.y = 30, 130
        self.image_left = load_image("character/espio left.png")
        self.image_right = load_image("character/espio right.png")

    def update(self):
        self.frame = (self.frame + 1) % 6
        self.x += self.dir_x * self.speed * frametime.FrameTime()
        self.y += self.dir_y * self.speed * frametime.FrameTime()
        InsideWindow(self.x, self.y)

    def draw(self):
        if self.dir_x == 1 or self.right == 1:
            self.image_left.clip_draw(self.frame * 27 + 5, 1220, 30, 40, self.x, self.y)
        if self.dir_x == -1 or self.right == 0:
            self.image_right.clip_draw(self.frame, 300, 400, 300, self.x, self.y)

class Mighty:
    def __init__(self):
        self.hp = 100
        self.speed = 2
        self.frame = 0
        self.right = 1
        self.dir_x, self.dir_y = 0, 0
        self.x, self.y = 30, 130
        self.image_left = load_image("character/mighty left.png")
        self.image_right = load_image("character/mighty right.png")

    def update(self):
        self.frame = (self.frame + 1) % 7
        self.x += self.dir_x * self.speed * frametime.FrameTime()
        self.y += self.dir_y * self.speed * frametime.FrameTime()
        InsideWindow(self.x, self.y)

    def draw(self):
        if self.dir_x == 1 or self.right == 1:
            self.image_left.clip_draw(self.frame * 25 + 3, 2880, 27, 40, self.x, self.y)
        if self.dir_x == -1 or self.right == 0:
            self.image_right.clip_draw(self.frame, 300, 400, 300, self.x, self.y)
        delay(0.03)

class SuperSonic:
    def __init__(self):
        self.hp = 100
        self.speed = 2
        self.frame = 0
        self.right = 1
        self.dir_x, self.dir_y = 0, 0
        self.x, self.y = 30, 130
        self.image_left = load_image("character/super sonic left.png")
        self.image_right = load_image("character/super sonic right.png")

    def update(self):
        self.x += self.dir_x * self.speed * frametime.FrameTime()
        self.y += self.dir_y * self.speed * frametime.FrameTime()
        InsideWindow(self.x, self.y)

    def draw(self):
        self.image_left.clip_draw(self.frame, 300, 400, 300, self.x, self.y)
        if self.dir_x == 1 or self.right == 1:
            self.image_left.clip_draw(self.frame, 300, 400, 300, self.x, self.y)
        if self.dir_x == -1 or self.right == 0:
            self.image_right.clip_draw(self.frame, 300, 400, 300, self.x, self.y)

class SuperShadow:
    def __init__(self):
        self.hp = 100
        self.speed = 2
        self.frame = 0
        self.right = 1
        self.dir_x, self.dir_y = 0, 0
        self.x, self.y = 30, 130
        self.image_left = load_image("character/super shadow left.png")
        self.image_right = load_image("character/super shadow right.png")

    def update(self):
        self.x += self.dir_x * self.speed * frametime.FrameTime()
        self.y += self.dir_y * self.speed * frametime.FrameTime()
        InsideWindow(self.x, self.y)

    def draw(self):
        self.image_left.clip_draw(self.frame, 300, 400, 300, self.x, self.y)
        if self.dir_x == 1 or self.right == 1:
            self.image_left.clip_draw(self.frame, 300, 400, 300, self.x, self.y)
        if self.dir_x == -1 or self.right == 0:
            self.image_right.clip_draw(self.frame, 300, 400, 300, self.x, self.y)
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

def InsideWindow(x, y):
    if x > game.window_size_x:
        x = game.window_size_x
    elif x < 0:
        x = 0
    if y > game.window_size_y:
        y = game.window_size_y
    elif y < 0:
        y = 0

def handle_events():
    global player_character, stage, stage_count, two, three, four
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
            elif event.key == SDLK_UP:
                player_character.dir_y = 1
                player_character.y += player_character.dir_y * 1
            elif event.key == SDLK_LEFT:
                player_character.right = 0
                player_character.dir_x = -1
                player_character.x += player_character.dir_x * 1
            elif event.key == SDLK_DOWN:
                player_character.dir_y = -1
                player_character.y += player_character.dir_y * 1
            elif event.key == SDLK_RIGHT:
                player_character.right = 1
                player_character.dir_x = 1
                player_character.x += player_character.dir_x * 1
            elif event.key == SDLK_1:
                stage_count = 1
                stage = load_image('map/snow.png')
                two, three, four = 0, 700, 300
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_UP:
                player_character.dir_y = 0
            elif event.key == SDLK_LEFT:
                player_character.dir_x = 0
            elif event.key == SDLK_DOWN:
                player_character.dir_y = 0
            elif event.key == SDLK_RIGHT:
                player_character.dir_x = 0
    delay(0.01)

def enter():
    global player_character, stage, stage_count
    player_character = Shadow()
    stage = Palm()
    stage_count = 0

def exit():
    global player_character, stage, stage_count
    del player_character, stage, stage_count

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