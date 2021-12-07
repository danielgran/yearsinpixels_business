from datetime import date
import unittest

from yearsinpixels_business.Entity.Day import Day
from yearsinpixels_business.Entity.Entity import Entity

class DayTest(unittest.TestCase):
    def test_is_there(self):
        self.assertIsNotNone(Day)

    def test_is_entity(self):
        self.assertTrue(issubclass(Day, Entity))

    def test_meta(self):
        day = Day()
        self.assertIsNotNone(day.id_user)
        self.assertIsNotNone(day.date)
        self.assertIsNotNone(day.title)
        self.assertIsNotNone(day.notes)

        self.assertTrue(isinstance(day.id_user, int))
        self.assertTrue(isinstance(day.date, date))
        self.assertTrue(isinstance(day.title, str))
        self.assertTrue(isinstance(day.notes, str))
