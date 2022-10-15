from pico2d import *
import game_framework
import game

player_character = None
character = ['Sonic', 'Tales', 'Knuckles', 'AmyRose', 'Tikal', 'Rouge', 'Shadow',
             'Silver', 'Blaze', 'Espio', 'Mighty', 'Super Sonic', 'Super Shadow']

class Sonic:
    def __init__(self):
        self.hp = 100
        self.speed = 1.5
        self.frame = 0
        self.dir_x, self.dir_y = 0, 0
        self.x, self.y = 400, 300
        self.image_left = load_image("character/sonic left.png")
        self.image_right = load_image("character/sonic left.png")

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir_x * self.speed * 10
        self.y += self.dir_y * 1
        InsideWindow(self.x, self.y)

    def draw(self):
        self.image_left.clip_draw(20 + (self.frame * 30), 2320, 30, 40, self.x, self.y)
        self.image_right.clip_draw(20 + self.frame * 30, 3000, 30, 40, self.x, self.y)

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
        self.x += self.dir_x * 1
        self.y += self.dir_y * 1
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
        self.x += self.dir_x * 1
        self.y += self.dir_y * 1
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
        self.x += self.dir_x * 1
        self.y += self.dir_y * 1
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
        self.x += self.dir_x * 1
        self.y += self.dir_y * 1
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
        self.x += self.dir_x * 1
        self.y += self.dir_y * 1
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
        self.x += self.dir_x * 1
        self.y += self.dir_y * 1
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
        self.x += self.dir_x * 1
        self.y += self.dir_y * 1
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
        self.x += self.dir_x * 1
        self.y += self.dir_y * 1
        InsideWindow(self.x, self.y)

    def draw(self):
        self.image_left.clip_draw(0, 0, 0, 0, 400, 300)
        self.image_right.clip_draw(0, 0, 0, 0, 400, 300)

class Espio:
    def __init__(self):
        self.hp = 100
        self.speed = 5
        self.frame = 0
        self.dir_x, self.dir_y = 0, 0
        self.x, self.y = 400, 300
        self.image_left = load_image("character/espio left.png")
        self.image_right = load_image("character/espio right.png")

    def update(self):
        self.x += self.dir_x * 1
        self.y += self.dir_y * 1
        InsideWindow(self.x, self.y)

    def draw(self):
        self.image_left.clip_draw(self.frame, 300, 400, 300, self.x, self.y)
        self.image_right.clip_draw(self.frame, 300, 400, 300, self.x, self.y)

class Mighty:
    def __init__(self):
        self.hp = 100
        self.speed = 5
        self.frame = 0
        self.dir_x, self.dir_y = 0, 0
        self.x, self.y = 400, 300
        self.image_left = load_image("character/mighty left.png")
        self.image_right = load_image("character/mighty right.png")

    def update(self):
        self.x += self.dir_x * 1
        self.y += self.dir_y * 1
        InsideWindow(self.x, self.y)

    def draw(self):
        self.image_left.clip_draw(self.frame, 300, 400, 300, self.x, self.y)
        self.image_right.clip_draw(self.frame, 300, 400, 300, self.x, self.y)

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
        self.x += self.dir_x * 1
        self.y += self.dir_y * 1
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
        self.x += self.dir_x * 1
        self.y += self.dir_y * 1
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
    global player_character
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
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_UP:
                player_character.dir_y = 0
            elif event.key == SDLK_LEFT:
                player_character.dir_x = 0
            elif event.key == SDLK_DOWN:
                player_character.dir_y = 0
            elif event.key == SDLK_RIGHT:
                player_character.dir_x = 0
def enter():
    global player_character
    player_character = Sonic()

def exit():
    global player_character
    del player_character

def update():
    player_character.update()
    handle_events()

def draw():
    clear_canvas()
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

if __name__ == '__main__':
    test_self()