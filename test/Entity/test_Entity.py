from abc import ABC

import unittest

from src.Entity.Entity import Entity


class EntityTest(unittest.TestCase):
    def test_is_there(self):
        self.assertIsNotNone(Entity)

    def test_is_abstract(self):
        self.assertTrue(issubclass(Entity, ABC))
