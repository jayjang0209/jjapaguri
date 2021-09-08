from unittest import TestCase
from game import character_damage_points


class TestCharacterDamagePoints(TestCase):
    def test_character_damage_points_is_tuple(self):
        character = {'level': 1, 'class': 'Sorcerer'}
        character_min_max_dp = character_damage_points(character)
        self.assertIsInstance(character_min_max_dp, tuple)

    def test_character_damage_sorcerer_level_1(self):
        character = {'level': 1, 'class': 'Sorcerer'}
        min_dp = 1
        max_dp = 25
        expected = (min_dp, max_dp)
        actual = character_damage_points(character)
        self.assertEqual(expected, actual)

    def test_character_damage_sorcerer_level_2(self):
        character = {'level': 2, 'class': 'Sorcerer'}
        min_dp = 1
        max_dp = 30
        expected = (min_dp, max_dp)
        actual = character_damage_points(character)
        self.assertEqual(expected, actual)

    def test_character_damage_sorcerer_level_3(self):
        character = {'level': 3, 'class': 'Sorcerer'}
        min_dp = 1
        max_dp = 35
        expected = (min_dp, max_dp)
        actual = character_damage_points(character)
        self.assertEqual(expected, actual)

    def test_character_damage_thief_level_1(self):
        character = {'level': 1, 'class': 'Thief'}
        min_dp = 6
        max_dp = 12
        expected = (min_dp, max_dp)
        actual = character_damage_points(character)
        self.assertEqual(expected, actual)

    def test_character_damage_thief_level_2(self):
        character = {'level': 2, 'class': 'Thief'}
        min_dp = 8
        max_dp = 16
        expected = (min_dp, max_dp)
        actual = character_damage_points(character)
        self.assertEqual(expected, actual)

    def test_character_damage_thief_level_3(self):
        character = {'level': 3, 'class': 'Thief'}
        min_dp = 10
        max_dp = 20
        expected = (min_dp, max_dp)
        actual = character_damage_points(character)
        self.assertEqual(expected, actual)

    def test_character_damage_bowmen_level_1(self):
        character = {'level': 1, 'class': 'Bowman'}
        min_dp = 10
        max_dp = 10
        expected = (min_dp, max_dp)
        actual = character_damage_points(character)
        self.assertEqual(expected, actual)

    def test_character_damage_bowmen_level_2(self):
        character = {'level': 2, 'class': 'Bowman'}
        min_dp = 12
        max_dp = 12
        expected = (min_dp, max_dp)
        actual = character_damage_points(character)
        self.assertEqual(expected, actual)

    def test_character_damage_bowmen_level_3(self):
        character = {'level': 3, 'class': 'Bowman'}
        min_dp = 14
        max_dp = 14
        expected = (min_dp, max_dp)
        actual = character_damage_points(character)
        self.assertEqual(expected, actual)

    def test_character_damage_fighter_level_1(self):
        character = {'level': 1, 'class': 'Fighter'}
        min_dp = 3
        max_dp = 20
        expected = (min_dp, max_dp)
        actual = character_damage_points(character)
        self.assertEqual(expected, actual)

    def test_character_damage_fighter_level_2(self):
        character = {'level': 2, 'class': 'Fighter'}
        min_dp = 5
        max_dp = 22
        expected = (min_dp, max_dp)
        actual = character_damage_points(character)
        self.assertEqual(expected, actual)

    def test_character_damage_fighter_level_3(self):
        character = {'level': 3, 'class': 'Fighter'}
        min_dp = 7
        max_dp = 24
        expected = (min_dp, max_dp)
        actual = character_damage_points(character)
        self.assertEqual(expected, actual)
