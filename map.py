from pico2d import *
from time import *

import main_state
import server

def AppendFloor(c, x, y, limit):
    server.stage_floor.append(c(x, y, limit))

def AppendPalmFloor():
    AppendFloor(Palmfloor, 2016 - 380, 80, 20)
    AppendFloor(Palmfloor, 2016 - 380, 180, 5)
    AppendFloor(Palmfloor, 2016 - 20, 180, 5)

def AppendLakeFloor():
    AppendFloor(Lakefloor, 2016 - 380, 80, 21)
    AppendFloor(Lakefloor, 2016 - 380, 180, 5)
    AppendFloor(Lakefloor, 2016 + 260, 180, 5)

def AppendSpaceFloor():
    AppendFloor(Spacefloor, 2016 - 380, 80, 21)
    AppendFloor(Spacefloor, 2016 - 380, 180, 5)
    AppendFloor(Spacefloor, 2016 + 260, 180, 5)

class Map:
    def __init__(self):
        self.timer_image = load_image('map/numbers.png')
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.window_left = 0
        self.window_bottom = 0
        pass

class Palm(Map):
    def __init__(self):
        super(Palm, self).__init__()
        self.image = load_image('map/palmtree.png')
        self.w = self.image.w
        self.h = self.image.h

    def update(self):
        self.window_left = clamp(0, (int)(server.player_character.x) - self.canvas_width // 2, self.w - self.canvas_width - 1)
        self.window_bottom = clamp(0, (int)(server.player_character.x) - self.canvas_height // 2, self.h - self.canvas_height - 1)

    def draw(self):
        self.image.clip_draw_to_origin(self.window_left, self.window_bottom, self.canvas_width, self.canvas_height, 0, 2)

class Palmfloor(Map):
    image = None
    def __init__(self, x, y, draw_limit):
        super(Palmfloor, self).__init__()
        if Palmfloor.image == None:
            self.image_floor = load_image('map/palmtree floor.png')
        self.draw_limit = draw_limit
        self.x, self.y = x, y
        self.w = self.image_floor.w
        self.h = self.image_floor.h

    def update(self):
        pass

    def draw(self):
        sx, sy = self.x - server.stage.window_left - 20, self.y - server.stage.window_bottom
        for i in range(self.draw_limit):
            self.image_floor.clip_draw_to_origin(0, 0, 40, 40, sx + i * 40, sy)

    def get_bb(self):
        sx, sy = self.x - server.stage.window_left - 20, self.y - server.stage.window_bottom
        return sx, sy + 39, sx + self.draw_limit * 40 , sy + 40

class Lake(Map):
    def __init__(self):
        super(Lake, self).__init__()
        self.image = load_image('map/lake.png')
        self.w = self.image.w
        self.h = self.image.h

    def update(self):
        self.window_left = clamp(0, (int)(server.player_character.x) - self.canvas_width // 2, self.w - self.canvas_width - 1)
        self.window_bottom = clamp(0, (int)(server.player_character.x) - self.canvas_height // 2, self.h - self.canvas_height - 1)

    def draw(self):
        self.image.clip_draw_to_origin(self.window_left, self.window_bottom, self.canvas_width, self.canvas_height, 0, 0)

class Lakefloor(Map):
    image = None
    def __init__(self, x, y, draw_limit):
        super(Lakefloor, self).__init__()
        if Lakefloor.image == None:
            self.image_floor = load_image('map/lake floor.png')
        self.draw_limit = draw_limit
        self.x, self.y = x, y
        self.w = self.image_floor.w
        self.h = self.image_floor.h

    def update(self):
        pass

    def draw(self):
        sx, sy = self.x - server.stage.window_left - 20, self.y - server.stage.window_bottom
        for i in range(self.draw_limit):
            self.image_floor.clip_draw_to_origin(0, 0, 40, 40, sx + i * 40, sy)

    def get_bb(self):
        sx, sy = self.x - server.stage.window_left - 20, self.y - server.stage.window_bottom
        return sx, sy + 39, sx + self.draw_limit * 40 , sy + 40

class Space(Map):
    def __init__(self):
        super(Space, self).__init__()
        self.image = load_image('map/space.png')
        self.w = self.image.w
        self.h = self.image.h

    def update(self):
        self.window_left = clamp(0, (int)(server.player_character.x) - self.canvas_width // 2, self.w - self.canvas_width - 1)
        self.window_bottom = clamp(0, (int)(server.player_character.x) - self.canvas_height // 2, self.h - self.canvas_height - 1)

    def draw(self):
        self.image.clip_draw_to_origin(self.window_left, self.window_bottom, self.canvas_width, self.canvas_height, 0, 0)

class Spacefloor(Map):
    image = None
    def __init__(self, x, y, draw_limit):
        super(Spacefloor, self).__init__()
        if Spacefloor.image == None:
            self.image_floor = load_image('map/space floor.png')
        self.draw_limit = draw_limit
        self.x, self.y = x, y
        self.w = self.image_floor.w
        self.h = self.image_floor.h

    def update(self):
        pass

    def draw(self):
        sx, sy = self.x - server.stage.window_left - 20, self.y - server.stage.window_bottom
        for i in range(self.draw_limit):
            self.image_floor.clip_draw_to_origin(0, 0, 40, 40, sx + i * 40, sy)

    def get_bb(self):
        sx, sy = self.x - server.stage.window_left - 20, self.y - server.stage.window_bottom
        return sx, sy + 39, sx + self.draw_limit * 40 , sy + 40