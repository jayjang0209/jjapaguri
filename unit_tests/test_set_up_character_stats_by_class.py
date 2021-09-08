import io
from unittest import TestCase
from unittest.mock import patch
from game import set_up_character_stats_by_class


class TestSetUpCharacterStatusByClass(TestCase):
    @patch('builtins.input', side_effect=["0"])
    def test_set_up_character_stats_by_class_sorcerer(self, mock_input):
        initial_hp_sorcerer = 15
        initial_hp_max_sorcerer = 15
        character_class = 'Sorcerer'
        class_name = ('Sorcerer', 'Cleric', 'Bishop')
        character = {'name': 'ABC_sor', 'class': None, 'class_name': None, 'hp': None, 'max_hp': None, 'x': 0, 'y': 0,
                     'level': 1, 'exp': 0}
        set_up_character_stats_by_class(character)
        actual = character
        expected = {'name': 'ABC_sor', 'class': character_class, 'class_name': class_name, 'hp': initial_hp_sorcerer,
                    'max_hp': initial_hp_max_sorcerer, 'x': 0, 'y': 0, 'level': 1, 'exp': 0}
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=["1"])
    def test_set_up_character_stats_by_class_thief(self, mock_input):
        initial_hp_thief = 20
        initial_hp_max_thief = 20
        character_class = 'Thief'
        class_name = ('Thief', 'Assassin', 'Night lord')
        character = {'name': 'ABC_thief', 'class': None, 'class_name': None, 'hp': None, 'max_hp': None, 'x': 0, 'y': 0,
                     'level': 1, 'exp': 0}
        set_up_character_stats_by_class(character)
        actual = character
        expected = {'name': 'ABC_thief', 'class': character_class, 'class_name': class_name, 'hp': initial_hp_thief,
                    'max_hp': initial_hp_max_thief, 'x': 0, 'y': 0, 'level': 1, 'exp': 0}
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=["2"])
    def test_set_up_character_stats_by_class_bowman(self, mock_input):
        initial_hp_bowman = 20
        initial_hp_max_bowman = 20
        character_class = 'Bowman'
        class_name = ('Bowman', 'Hunter', 'Bow Master')
        character = {'name': 'ABC_bow', 'class': None, 'class_name': None, 'hp': None, 'max_hp': None, 'x': 0, 'y': 0,
                     'level': 1, 'exp': 0}
        set_up_character_stats_by_class(character)
        actual = character
        expected = {'name': 'ABC_bow', 'class': character_class, 'class_name': class_name, 'hp': initial_hp_bowman,
                    'max_hp': initial_hp_max_bowman, 'x': 0, 'y': 0, 'level': 1, 'exp': 0}
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=["3"])
    def test_set_up_character_stats_by_class_fighter(self, mock_input):
        initial_hp_fighter = 25
        initial_hp_max_fighter = 25
        character_class = 'Fighter'
        class_name = ('Fighter', 'Warrior', 'Paladin')
        character = {'name': 'ABC_fig', 'class': None, 'class_name': None, 'hp': None, 'max_hp': None, 'x': 0, 'y': 0,
                     'level': 1, 'exp': 0}
        set_up_character_stats_by_class(character)
        actual = character
        expected = {'name': 'ABC_fig', 'class': character_class, 'class_name': class_name, 'hp': initial_hp_fighter,
                    'max_hp': initial_hp_max_fighter, 'x': 0, 'y': 0, 'level': 1, 'exp': 0}
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=["0"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_set_up_character_stats_by_class_fighter_display_user_options(self, mock_stdout, mock_input):
        character = {'name': 'ABC_fig', 'class': None, 'class_name': None, 'hp': None, 'max_hp': None, 'x': 0, 'y': 0,
                     'level': 1, 'exp': 0}
        set_up_character_stats_by_class(character)
        expected = "-------------------------------------------\n" \
                   " MENU \n" \
                   " 0) : Sorcerer\n" \
                   " 1) : Thief\n" \
                   " 2) : Bowman\n" \
                   " 3) : Fighter\n" \
                   "-------------------------------------------\n\n"
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('builtins.input', side_effect=["0"])
    def test_set_up_character_stats_by_class_original_dictionary_changed(self, mock_input):
        character = {'name': 'ABC_sor', 'class': None, 'class_name': None, 'hp': None, 'max_hp': None, 'x': 0, 'y': 0,
                     'level': 1, 'exp': 0}
        expected = character.copy()
        set_up_character_stats_by_class(character)
        actual = character
        self.assertNotEqual(actual, expected)
