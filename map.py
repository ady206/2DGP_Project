from pico2d import *

class Map:
    pass

class Palm(Map):
    def __init__(self):
        self.image = load_image('map/palmtree.png')
        self.image_floor = load_image('map/palmtree floor.png')

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(0, 600, 1000, 600, 400, 300)
        for i in range(27):
            self.image_floor.clip_draw(0, 0, 40, 40, i * 30, 100)

        for i in range(5):
            self.image_floor.clip_draw(0, 0, 40, 40, i * 30, 230)
        for i in range(5):
            self.image_floor.clip_draw(0, 0, 40, 40, 810 - i * 30, 230)
        for i in range(5):
            self.image_floor.clip_draw(0, 0, 40, 40, 350 + i * 30, 230)

    def get_bb(self):
        return 0, 0, 1600 - 1, 50

class Lake(Map):

    def __init__(self):
        self.image = load_image('map/lake.png')

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(0, 0, 800, 600, 400, 300)

class Space(Map):
    def __init__(self):
        self.image = load_image('map/space.png')
        self.image_floor = load_image('map/space floor.png')

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(0, 0, 800, 600, 400, 300)
        for i in range(28):
            self.image_floor.clip_draw(33, 0, 30, 30, i * 30, 100)