from pico2d import *
import game_framework

player_character = None
character = ['Sonic', 'Tales', 'Knuckles', 'AmyRose', 'Tikal', 'Rouge', 'Shadow',
             'Silver', 'Blaze', 'Espio', 'Mighty', 'Super Sonic', 'Super Shadow']

class Sonic:
    def __init__(self):
        self.image_left = load_image("character/sonic left.png")
        self.image_right = load_image("character/sonic left.png")

    def draw(self):
        self.image.clip_draw(0, 0, 0, 0, 400, 300)

class Tales:
    def __init__(self):
        self.image_left = load_image("character/tales left.png")
        self.image_right = load_image("character/tales left.png")

    def draw(self):
        self.image.clip_draw(0, 0, 0, 0, 400, 300)

class Knuckles:
    def __init__(self):
        self.image_left = load_image("character/knuckles left.png")
        self.image_right = load_image("character/knuckles left.png")

    def draw(self):
        self.image.clip_draw(0, 0, 0, 0, 400, 300)

class AmyRose:
    def __init__(self):
        self.image_left = load_image("character/amy rose left.png")
        self.image_right = load_image("character/amy rose left.png")

    def draw(self):
        self.image.clip_draw(0, 0, 0, 0, 400, 300)

class Tikal:
    def __init__(self):
        self.image_left = load_image("character/tikal left.png")
        self.image_right = load_image("character/tikal right.png")

    def draw(self):
        self.image.clip_draw(0, 0, 0, 0, 400, 300)

class Rouge:
    def __init__(self):
        self.image_left = load_image("character/rouge left.png")
        self.image_right = load_image("character/rouge right.png")

    def draw(self):
        self.image.clip_draw(0, 0, 0, 0, 400, 300)

class Shadow:
    def __init__(self):
        self.image_left = load_image("character/shadow left.png")
        self.image_right = load_image("character/shadow right.png")

    def draw(self):
        self.image.clip_draw(0, 0, 0, 0, 400, 300)

class Silver:
    def __init__(self):
        self.image_left = load_image("character/silver left.png")
        self.image_right = load_image("character/silver right.png")

    def draw(self):
        self.image.clip_draw(0, 0, 0, 0, 400, 300)

class Blaze:
    def __init__(self):
        self.image_left = load_image("character/blaze left.png")
        self.image_right = load_image("character/blaze right.png")

    def draw(self):
        self.image.clip_draw(0, 0, 0, 0, 400, 300)

class Espio:
    def __init__(self):
        self.image_left = load_image("character/espio left.png")
        self.image_right = load_image("character/espio right.png")

    def draw(self):
        self.image.clip_draw(0, 0, 0, 0, 400, 300)

class Mighty:
    def __init__(self):
        self.image_left = load_image("character/mighty left.png")
        self.image_right = load_image("character/mighty right.png")

    def draw(self):
        self.image.clip_draw(0, 0, 0, 0, 400, 300)

class SuperSonic:
    def __init__(self):
        self.image_left = load_image("character/super sonic left.png")
        self.image_right = load_image("character/super sonic right.png")

    def draw(self):
        self.image.clip_draw(0, 0, 0, 0, 400, 300)

class SuperShadow:
    def __init__(self):
        self.image_left = load_image("character/super shadow left.png")
        self.image_right = load_image("character/super shadow right.png")

    def draw(self):
        self.image.clip_draw(0, 0, 0, 0, 400, 300)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()

def enter():
    global player_character
    player_character = Sonic()

def exit():
    global player_character
    del player_character

def draw():
    clear_canvas()
    player_character.draw()
    update_canvas()

def update():
    handle_events()

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