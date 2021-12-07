from datetime import date

from yearsinpixels_business.Entity.Entity import Entity


class Mood(Entity):
    def __init__(self):
        self.id = 0
        self.title = ""
        self.color = 0
