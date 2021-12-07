import unittest

from yearsinpixels_business.Entity.Mood import Mood
from yearsinpixels_business.Entity.Entity import Entity

class MoodTest(unittest.TestCase):
    def test_is_there(self):
        self.assertIsNotNone(Mood)

    def test_is_entity(self):
        self.assertTrue(issubclass(Mood, Entity))

    def test_meta(self):
        mood = Mood()
        self.assertIsNotNone(mood.id)
        self.assertIsNotNone(mood.title)
        self.assertIsNotNone(mood.color)

        self.assertTrue(isinstance(mood.id, int))
        self.assertTrue(isinstance(mood.title, str))
        self.assertTrue(isinstance(mood.color, int))
