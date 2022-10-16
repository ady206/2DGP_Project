from pico2d import *
import game_framework
import game
import frametime

player_character = None
character = ['Sonic', 'Tales', 'Knuckles', 'AmyRose', 'Tikal', 'Rouge', 'Shadow',
             'Silver', 'Blaze', 'Espio', 'Mighty', 'Super Sonic', 'Super Shadow']
stage_count = None
stage = None

class Sonic:
    def __init__(self):
        self.hp = 100
        self.speed = 2
        self.frame = 0
        self.dir_x, self.dir_y = 0, 0
        self.x, self.y = 400, 300
        self.image_left = load_image("character/sonic left.png")
        self.image_right = load_image("character/sonic left.png")

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir_x * self.speed * frametime.FrameTime()
        self.y += self.dir_y * self.speed * frametime.FrameTime()
        InsideWindow(self.x, self.y)

    def draw(self):
        self.image_left.clip_draw(20 + (self.frame * 30), 2320, 30, 40, self.x, self.y)
        self.image_right.clip_draw(20 + self.frame * 30, 3000, 30, 40, self.x, self.y)
        delay(0.05)

class Tales:
    def __init__(self):
        self.hp = 100
        self.speed = 5
        self.frame = 0
        self.dir_x, self.dir_y = 0, 0
        self.x, self.y = 400, 300
        self.image_left = load_image("character/tales left.png")
        self.image_right = load_image("character/tales left.png")

    def update(self):
        self.x += self.dir_x * self.speed * frametime.FrameTime()
        self.y += self.dir_y * self.speed * frametime.FrameTime()
        InsideWindow(self.x, self.y)

    def draw(self):
        self.image_left.clip_draw(self.frame, 300, 400, 300, self.x, self.y)
        self.image_right.clip_draw(self.frame, 300, 400, 300, self.x, self.y)

class Knuckles:
    def __init__(self):
        self.hp = 100
        self.speed = 5
        self.frame = 0
        self.dir_x, self.dir_y = 0, 0
        self.x, self.y = 400, 300
        self.image_left = load_image("character/knuckles left.png")
        self.image_right = load_image("character/knuckles left.png")

    def update(self):
        self.x += self.dir_x * self.speed * frametime.FrameTime()
        self.y += self.dir_y * self.speed * frametime.FrameTime()
        InsideWindow(self.x, self.y)

    def draw(self):
        self.image_left.clip_draw(self.frame, 300, 400, 300, self.x, self.y)
        self.image_right.clip_draw(self.frame, 300, 400, 300, self.x, self.y)

class AmyRose:
    def __init__(self):
        self.hp = 100
        self.speed = 5
        self.frame = 0
        self.dir_x, self.dir_y = 0, 0
        self.x, self.y = 400, 300
        self.image_left = load_image("character/amy rose left.png")
        self.image_right = load_image("character/amy rose left.png")

    def update(self):
        self.x += self.dir_x * self.speed * frametime.FrameTime()
        self.y += self.dir_y * self.speed * frametime.FrameTime()
        InsideWindow(self.x, self.y)

    def draw(self):
        self.image_left.clip_draw(self.frame, 300, 400, 300, self.x, self.y)
        self.image_right.clip_draw(self.frame, 300, 400, 300, self.x, self.y)

class Tikal:
    def __init__(self):
        self.hp = 100
        self.speed = 5
        self.frame = 0
        self.dir_x, self.dir_y = 0, 0
        self.x, self.y = 400, 300
        self.image_left = load_image("character/tikal left.png")
        self.image_right = load_image("character/tikal right.png")

    def update(self):
        self.x += self.dir_x * self.speed * frametime.FrameTime()
        self.y += self.dir_y * self.speed * frametime.FrameTime()
        InsideWindow(self.x, self.y)

    def draw(self):
        self.image_left.clip_draw(self.frame, 300, 400, 300, self.x, self.y)
        self.image_right.clip_draw(self.frame, 300, 400, 300, self.x, self.y)

class Rouge:
    def __init__(self):
        self.hp = 100
        self.speed = 5
        self.frame = 0
        self.dir_x, self.dir_y = 0, 0
        self.x, self.y = 400, 300
        self.image_left = load_image("character/rouge left.png")
        self.image_right = load_image("character/rouge right.png")

    def update(self):
        self.x += self.dir_x * self.speed * frametime.FrameTime()
        self.y += self.dir_y * self.speed * frametime.FrameTime()
        InsideWindow(self.x, self.y)

    def draw(self):
        self.image_left.clip_draw(self.frame, 300, 400, 300, self.x, self.y)
        self.image_right.clip_draw(self.frame, 300, 400, 300, self.x, self.y)

class Shadow:
    def __init__(self):
        self.hp = 100
        self.speed = 5
        self.frame = 0
        self.dir_x, self.dir_y = 0, 0
        self.x, self.y = 400, 300
        self.image_left = load_image("character/shadow left.png")
        self.image_right = load_image("character/shadow right.png")

    def update(self):
        self.x += self.dir_x * self.speed * frametime.FrameTime()
        self.y += self.dir_y * self.speed * frametime.FrameTime()
        InsideWindow(self.x, self.y)

    def draw(self):
        self.image_left.clip_draw(self.frame, 300, 400, 300, self.x, self.y)
        self.image_right.clip_draw(self.frame, 300, 400, 300, self.x, self.y)

class Silver:
    def __init__(self):
        self.hp = 100
        self.speed = 5
        self.frame = 0
        self.dir_x, self.dir_y = 0, 0
        self.x, self.y = 400, 300
        self.image_left = load_image("character/silver left.png")
        self.image_right = load_image("character/silver right.png")

    def update(self):
        self.x += self.dir_x * self.speed * frametime.FrameTime()
        self.y += self.dir_y * self.speed * frametime.FrameTime()
        InsideWindow(self.x, self.y)

    def draw(self):
        self.image_left.clip_draw(self.frame, 300, 400, 300, self.x, self.y)
        self.image_right.clip_draw(self.frame, 300, 400, 300, self.x, self.y)

class Blaze:
    def __init__(self):
        self.hp = 100
        self.speed = 5
        self.frame = 0
        self.dir_x, self.dir_y = 0, 0
        self.x, self.y = 400, 300
        self.image_left = load_image("character/blaze left.png")
        self.image_right = load_image("character/blaze right.png")

    def update(self):
        self.x += self.dir_x * self.speed * frametime.FrameTime()
        self.y += self.dir_y * self.speed * frametime.FrameTime()
        InsideWindow(self.x, self.y)

    def draw(self):
        self.image_left.clip_draw(0, 0, 0, 0, 400, 300)
        self.image_right.clip_draw(0, 0, 0, 0, 400, 300)

class Espio:
    def __init__(self):
        self.hp = 100
        self.speed = 2
        self.frame = 0
        self.dir_x, self.dir_y = 0, 0
        self.x, self.y = 400, 300
        self.image_left = load_image("character/espio left.png")
        self.image_right = load_image("character/espio right.png")

    def update(self):
        self.frame = (self.frame + 1) % 6
        self.x += self.dir_x * self.speed * frametime.FrameTime()
        self.y += self.dir_y * self.speed * frametime.FrameTime()
        InsideWindow(self.x, self.y)

    def draw(self):
        self.image_left.clip_draw(self.frame * 27 + 5, 1220, 30, 40, self.x, self.y)
        self.image_right.clip_draw(self.frame, 300, 400, 300, self.x, self.y)

class Mighty:
    def __init__(self):
        self.hp = 100
        self.speed = 2
        self.frame = 0
        self.dir_x, self.dir_y = 0, 0
        self.x, self.y = 400, 300
        self.image_left = load_image("character/mighty left.png")
        self.image_right = load_image("character/mighty right.png")

    def update(self):
        self.frame = (self.frame + 1) % 7
        self.x += self.dir_x * self.speed * frametime.FrameTime()
        self.y += self.dir_y * self.speed * frametime.FrameTime()
        InsideWindow(self.x, self.y)

    def draw(self):
        self.image_left.clip_draw(self.frame * 25 + 3, 2880, 27, 40, self.x, self.y)
        self.image_right.clip_draw(self.frame, 300, 400, 300, self.x, self.y)
        delay(0.03)
class SuperSonic:
    def __init__(self):
        self.hp = 100
        self.speed = 5
        self.frame = 0
        self.dir_x, self.dir_y = 0, 0
        self.x, self.y = 400, 300
        self.image_left = load_image("character/super sonic left.png")
        self.image_right = load_image("character/super sonic right.png")

    def update(self):
        self.x += self.dir_x * self.speed * frametime.FrameTime()
        self.y += self.dir_y * self.speed * frametime.FrameTime()
        InsideWindow(self.x, self.y)

    def draw(self):
        self.image_left.clip_draw(self.frame, 300, 400, 300, self.x, self.y)
        self.image_right.clip_draw(self.frame, 300, 400, 300, self.x, self.y)

class SuperShadow:
    def __init__(self):
        self.hp = 100
        self.speed = 5
        self.frame = 0
        self.dir_x, self.dir_y = 0, 0
        self.x, self.y = 400, 300
        self.image_left = load_image("character/super shadow left.png")
        self.image_right = load_image("character/super shadow right.png")

    def update(self):
        self.x += self.dir_x * self.speed * frametime.FrameTime()
        self.y += self.dir_y * self.speed * frametime.FrameTime()
        InsideWindow(self.x, self.y)

    def draw(self):
        self.image_left.clip_draw(self.frame, 300, 400, 300, self.x, self.y)
        self.image_right.clip_draw(self.frame, 300, 400, 300, self.x, self.y)

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
                player_character.dir_x = -1
                player_character.x += player_character.dir_x * 1
            elif event.key == SDLK_DOWN:
                player_character.dir_y = -1
                player_character.y += player_character.dir_y * 1
            elif event.key == SDLK_RIGHT:
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

two, three, four = None, None, None
def enter():
    global player_character, stage, stage_count, two, three, four
    player_character = Espio()
    stage = load_image('map/palmtree.png')
    two, three, four = 600, 1000, 600
    stage_count = 0

def exit():
    global player_character, stage, stage_count, two, three, four
    del player_character, stage, stage_count, two, three, four

def update():
    player_character.update()
    handle_events()

def draw():
    clear_canvas()
    stage.clip_draw(0, two, three, four, 400, 300)
    player_character.draw()
    update_canvas()

def pause():
    pass

def resume():
    pass