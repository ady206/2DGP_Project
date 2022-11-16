from pico2d import *
import character
import main_state
from time import *


def AppendFloor(c, x, y, limit):
    main_state.stage_floor.append(c(x, y, limit))

def AppendPalmFloor():
    AppendFloor(Palmfloor, character.player_character.x - 380, 100, 20)
    AppendFloor(Palmfloor, character.player_character.x - 380, 200, 5)
    AppendFloor(Palmfloor, character.player_character.x - 20, 200, 5)

class Map:
    def __init__(self, x, y):
        self.timer_image = load_image('map/numbers.png')
        self.x = x
        self.y = y
        pass

class Palm(Map):
    image = None
    def __init__(self, x, y):
        super(Palm, self).__init__(x, y)
        if Palm.image == None:
            self.image = load_image('map/palmtree.png')
        self.x = x
        self.y = y

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(0, 160, 2500, 640, self.x, self.y - 20)

class Palmfloor(Map):
    image = None
    def __init__(self, x, y, draw_limit):
        super(Palmfloor, self).__init__(x, y)
        if Palmfloor.image == None:
            self.image_floor = load_image('map/palmtree floor.png')
        self.x = x
        self.y = y
        self.draw_limit = draw_limit

    def update(self):
        pass

    def draw(self):
        for i in range(self.draw_limit):
            self.image_floor.clip_draw(0, 0, 40, 40, self.x + i * 40, self.y)

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + self.draw_limit * 40 - 20, self.y + 20

class Lake(Map):
    image = None
    def __init__(self, x, y):
        super(Lake, self).__init__(x, y)
        if Lake.image == None:
            self.image = load_image('map/lake.png')

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(0, 160, 2500, 640, self.x, self.y - 20)
class Space(Map):
    image = None
    def __init__(self, x, y):
        super(Space, self).__init__(x, y)
        if Space.image == None:
            self.image = load_image('map/space.png')
        self.image_floor = load_image('map/space floor.png')

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(0, 160, 2500, 640, self.x, self.y - 20)
        for i in range(28):
            self.image_floor.clip_draw(33, 0, 30, 30, self.x - 400 + i * 30, 100)