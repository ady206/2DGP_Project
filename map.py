from pico2d import *
import character
import main_state
from time import *

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
        self.image_floor = load_image('map/palmtree floor.png')
        self.floor_high = 180

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(0, 160, 2500, 640, self.x, self.y - 20)
        for i in range(28):
            self.image_floor.clip_draw(0, 0, 40, 40, self.x - 400 + i * 30, 100)

        for i in range(5):
            self.image_floor.clip_draw(0, 0, 40, 40, self.x - 400 + i * 30, self.floor_high)
        for i in range(5):
            self.image_floor.clip_draw(0, 0, 40, 40, self.x - 400 + 810 - i * 30, self.floor_high)
        for i in range(5):
            self.image_floor.clip_draw(0, 0, 40, 40, self.x - 400 + 350 + i * 30, self.floor_high)

    def get_bb(self):
        return 0, 0, 1600 - 1, 50

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