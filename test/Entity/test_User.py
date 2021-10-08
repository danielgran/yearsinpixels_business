import unittest

from src.Entity.User import User


class MyTestCase(unittest.TestCase):
    def test_is_there(self):
        ent = User()

    def test_meta(self):
        ent = User()
        self.assertTrue(ent.guid is not None)
        self.assertTrue(ent.email is not None)
        self.assertTrue(ent.username is not None)
