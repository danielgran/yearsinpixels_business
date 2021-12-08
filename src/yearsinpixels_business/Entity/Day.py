from datetime import date

from yearsinpixels_business.Entity.Entity import Entity


class Day(Entity):
    def __init__(self):
        self.id_user = 0
        self.id_mood1 = 0
        self.id_mood2 = 0
        self.date = date.today()
        self.title = ""
        self.notes = ""
