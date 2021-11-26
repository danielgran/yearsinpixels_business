import time

import uuid

from yearsinpixels_business.Entity.Entity import Entity


class User(Entity):

    def __init__(self):
        self.guid = str(uuid.uuid4())
        self.email = ""
        self.email_verified = True
        self.name_first = ""
        self.name_last = ""
        self.gender = 0
        self.password = ""
        self.last_update_password = time.time()
        self.enabled = True
        self.last_login = ""
        self.modified = time.time()
        self.created = time.time()
