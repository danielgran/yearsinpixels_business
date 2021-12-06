from datetime import datetime
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
        self.assertIsNotNone(user.id)
        self.assertIsNotNone(user.guid)
        self.assertIsNotNone(user.email)
        self.assertIsNotNone(user.email_verified)
        self.assertIsNotNone(user.name_first)
        self.assertIsNotNone(user.name_last)
        self.assertIsNotNone(user.password)
        self.assertIsNotNone(user.password_last_update)
        self.assertIsNotNone(user.enabled)
        self.assertIsNotNone(user.twofatoken)
        self.assertIsNotNone(user.login_last)
        self.assertIsNotNone(user.modified)
        self.assertIsNotNone(user.created)

        self.assertTrue(isinstance(user.id, int))
        self.assertTrue(isinstance(user.guid, str))
        self.assertTrue(isinstance(user.email, str))
        self.assertTrue(isinstance(user.email_verified, bool))
        self.assertTrue(isinstance(user.name_first, str))
        self.assertTrue(isinstance(user.name_last, str))
        self.assertTrue(isinstance(user.password, str))
        self.assertTrue(isinstance(user.password_last_update, datetime))
        self.assertTrue(isinstance(user.enabled, bool))
        self.assertTrue(isinstance(user.twofatoken, str))
        self.assertTrue(isinstance(user.login_last, datetime))
        self.assertTrue(isinstance(user.modified, datetime))
        self.assertTrue(isinstance(user.created, datetime))
