from unittest import TestCase
from unittest.mock import patch
from game import make_character


class TestMakeCharacter(TestCase):
    @patch('builtins.input', side_effect=['Character_name', "0"])
    def test_make_character_is_dictionary(self, mock_input):
        actual = make_character()
        self.assertIsInstance(actual, dict)

    @patch('builtins.input', side_effect=['Character_name', "0"])
    def test_make_character_check_character_name(self, mock_input):
        character = make_character()
        actual = character['name']
        expected = 'Character_name'
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['Character_name', "0"])
    def test_make_character_check_is_initial_level_1(self, mock_input):
        character = make_character()
        actual = character['level']
        expected = 1
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['Character_name', "0"])
    def test_make_character_check_is_initial_exp_0(self, mock_input):
        character = make_character()
        actual = character['exp']
        expected = 0
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['Character_name', "0"])  # user chooses Sorcerer Class
    def test_make_character_check_class_sorcerer(self, mock_input):
        name = 'Character_name'
        actual = make_character()
        expected = {'name': name, 'class': 'Sorcerer', 'class_name': ('Sorcerer', 'Cleric', 'Bishop'), 'hp': 15,
                    'max_hp': 15, 'x': 0, 'y': 0, 'level': 1, 'exp': 0}
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['Character_name', "1"])  # user chooses Thief Class
    def test_make_character_check_class_thief(self, mock_input):
        name = 'Character_name'
        actual = make_character()
        expected = {'name': name, 'class': 'Thief', 'class_name': ('Thief', 'Assassin', 'Night lord'), 'hp': 20,
                    'max_hp': 20, 'x': 0, 'y': 0, 'level': 1, 'exp': 0}
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['Character_name', "2"])  # user chooses Bowman Class
    def test_make_character_check_class_bowman(self, mock_input):
        name = 'Character_name'
        actual = make_character()
        expected = {'name': name, 'class': 'Bowman', 'class_name': ('Bowman', 'Hunter', 'Bow Master'), 'hp': 20,
                    'max_hp': 20, 'x': 0, 'y': 0, 'level': 1, 'exp': 0}
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['Character_name', "3"])
    def test_make_character_check_class_fighter(self, mock_input):  # user chooses Fighter Class
        name = 'Character_name'
        actual = make_character()
        expected = {'name': name, 'class': 'Fighter', 'class_name': ('Fighter', 'Warrior', 'Paladin'), 'hp': 25,
                    'max_hp': 25, 'x': 0, 'y': 0, 'level': 1, 'exp': 0}
        self.assertEqual(actual, expected)
