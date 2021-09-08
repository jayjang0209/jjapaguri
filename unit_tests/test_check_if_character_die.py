from unittest import TestCase
from game import check_if_character_die


class TestCheckIfCharacterDie(TestCase):
    def test_check_if_character_die_character_dead_HP_zero(self):  # check when hp is zero
        game_character = {'name': '', 'hp': 0, 'x': 4, 'y': 4}
        expected = 'character_die'
        actual = check_if_character_die(game_character)
        self.assertEqual(actual, expected)

    def test_check_if_character_die_character_dead_less_than_zero(self):  # check when hp is less than zero
        game_character = {'name': '', 'hp': -5, 'x': 4, 'y': 4}
        actual = check_if_character_die(game_character)
        expected = 'character_die'
        self.assertEqual(actual, expected)

    def test_check_if_character_die_character_alive_hp_grater_tan_zero(self):  # check when hp is greater than zero
        game_character = {'name': '', 'hp': 15, 'x': 4, 'y': 4}
        actual = check_if_character_die(game_character)
        expected = 'character_alive'
        self.assertEqual(actual, expected)

    def test_check_if_character_is_string(self):  # check if return values is s string
        game_character = {'name': '', 'hp': 15, 'x': 4, 'y': 4}
        actual = check_if_character_die(game_character)
        self.assertIsInstance(actual, str)
