from pico2d import *

class Palm:
    def __init__(self):
        self.image = load_image('map/palmtree.png')
        self.image_floor = load_image('map/palmtree floor.png')

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(0, 600, 1000, 600, 400, 300)
        for i in range(0, 30):
            self.image_floor.clip_draw(0, 0, 100, 40, i * 30 + 50, 100)

class Lake:
    def __init__(self):
        self.image = load_image('map/lake.png')

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(0, 0, 800, 600, 400, 300)

class Space:
    def __init__(self):
        self.image = load_image('map/space.png')
        self.image_floor = load_image('map/space floor.png')

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(0, 0, 800, 600, 400, 300)
        for i in range(28):
            self.image_floor.clip_draw(33, 0, 30, 30, i * 30, 100)