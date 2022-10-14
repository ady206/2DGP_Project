from pico2d import *
import game_framework

running = True

class Sonic:
    img_left = load_image("character/sonic left.png")
    img_right = load_image("character/sonic right.png")
    def __init__(self):
        self.image_left = Sonic.img_left
        self.image_right = Sonic.img_right

class Tales:
    img_left = load_image("character/tales left.png")
    img_right = load_image("character/tales right.png")
    def __init__(self):
        self.image_left = Tales.img_left
        self.image_right = Tales.img_right

class Knuckles:
    img_left = load_image("character/knuckles left.png")
    img_right = load_image("character/knuckles right.png")
    def __init__(self):
        self.image_left = Knuckles.img_left
        self.image_right = Knuckles.img_right

class AmyRose:
    img_left = load_image("character/amy rose left.png")
    img_right = load_image("character/amy rose right.png")
    def __init__(self):
        self.image_left = AmyRose.img_left
        self.image_right = AmyRose.img_right

class Tikal:
    img_left = load_image("character/tikal left.png")
    img_right = load_image("character/tikal right.png")
    def __init__(self):
        self.image_left = Tikal.img_left
        self.image_right = Tikal.img_right

class Rouge:
    img_left = load_image("character/rouge left.png")
    img_right = load_image("character/rouge right.png")
    def __init__(self):
        self.image_left = Rouge.img_left
        self.image_right = Rouge.img_right

class Shadow:
    img_left = load_image("character/shadow left.png")
    img_right = load_image("character/shadow right.png")
    def __init__(self):
        self.image_left = Shadow.img_left
        self.image_right = Shadow.img_right

class Silver:
    img_left = load_image("character/silver left.png")
    img_right = load_image("character/silver right.png")
    def __init__(self):
        self.image_left = Silver.img_left
        self.image_right = Silver.img_right

class Blaze:
    img_left = load_image("character/blaze left.png")
    img_right = load_image("character/blaze right.png")
    def __init__(self):
        self.image_left = Blaze.img_left
        self.image_right = Blaze.img_right

class Espio:
    img_left = load_image("character/espio left.png")
    img_right = load_image("character/espio right.png")
    def __init__(self):
        self.image_left = Espio.img_left
        self.image_right = Espio.img_right

class Mighty:
    img_left = load_image("character/mighty left.png")
    img_right = load_image("character/mighty right.png")
    def __init__(self):
        self.image_left = Mighty.img_left
        self.image_right = Mighty.img_right

class SuperSonic:
    img_left = load_image("character/super sonic left.png")
    img_right = load_image("character/super sonic right.png")
    def __init__(self):
        self.image_left = SuperSonic.img_left
        self.image_right = SuperSonic.img_right

class SuperShadow:
    img_left = load_image("character/super shadow left.png")
    img_right = load_image("character/super shadow right.png")
    def __init__(self):
        self.image_left = SuperShadow.img_left
        self.image_right = SuperShadow.img_right

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    delay(0.01)

def enter():
    global running
    running = True
    pass

def exit():

def draw():
    clear_canvas()
    update_canvas()

open_canvas()
enter()
while running:
    handle_events()
    draw()
exit()
# finalization code
close_canvas()
