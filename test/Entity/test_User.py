import unittest

from yearsinpixels_business.Entity.Entity import Entity
from yearsinpixels_business.Entity.User import User


class MyTestCase(unittest.TestCase):
    def test_is_there(self):
        self.assertIsNotNone(User)

    def test_is_entity(self):
        self.assertTrue(issubclass(User, Entity))

    def test_meta(self):
        user = User()
        self.assertIsNotNone(user.guid)
        self.assertIsNotNone(user.email)
        self.assertIsNotNone(user.email_verified)
        self.assertIsNotNone(user.name_first)
        self.assertIsNotNone(user.name_last)
        self.assertIsNotNone(user.gender)
        self.assertIsNotNone(user.password)
        self.assertIsNotNone(user.password_last_update)
        self.assertIsNotNone(user.enabled)
        self.assertIsNotNone(user.twofatoken)
        self.assertIsNotNone(user.login_last)
        self.assertIsNotNone(user.modified)
        self.assertIsNotNone(user.created)
