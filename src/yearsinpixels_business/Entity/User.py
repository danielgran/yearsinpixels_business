from datetime import datetime

import uuid

from yearsinpixels_business.Entity.Entity import Entity


class User(Entity):

    def __init__(self):
        self.id = 0
        self.guid = str(uuid.uuid4())
        self.email = ""
        self.email_verified = True
        self.name_first = ""
        self.name_last = ""
        self.password = ""
        self.password_last_update = datetime.now()
        self.enabled = True
        self.twofatoken = ""
        self.login_last = datetime.now()
        self.modified = datetime.now()
        self.created = datetime.now()
