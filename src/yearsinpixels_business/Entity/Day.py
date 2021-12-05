from datetime import date

from yearsinpixels_business.Entity.Entity import Entity


class Day(Entity):
    def __init__(self):
        self.date = date.today()
        self.title = ""
        self.notes = ""
