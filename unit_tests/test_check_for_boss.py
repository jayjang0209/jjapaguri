from unittest import TestCase
from game import check_for_boss


class TestCheckForBoss(TestCase):
    def test_check_for_boss_return_boolean(self):
        x_coord = 24
        y_coord = 24
        character = {'x': x_coord, 'y': y_coord}
        actual = check_for_boss(character)
        self.assertIsInstance(actual, bool)

    def test_check_for_boss_character_reached_boss_position(self):
        x_coord = 24
        y_coord = 24
        character = {'x': x_coord, 'y': y_coord}
        actual = check_for_boss(character)
        self.assertTrue(actual)

    def test_check_for_boss_character_not_reached_boss_position(self):
        x_coord = 15
        y_coord = 15
        character = {'x': x_coord, 'y': y_coord}
        actual = check_for_boss(character)
        self.assertFalse(actual)

    def test_check_for_boss_character_not_reached_boss_position_x_boundary(self):
        x_coord = 23
        y_coord = 24
        character = {'x': x_coord, 'y': y_coord}
        actual = check_for_boss(character)
        self.assertFalse(actual)

    def test_check_for_boss_character_not_reached_boss_position_y_boundary(self):
        x_coord = 24
        y_coord = 23
        character = {'x': x_coord, 'y': y_coord}
        actual = check_for_boss(character)
        self.assertFalse(actual)
