from unittest import TestCase
from unittest.mock import patch
from game import character_explore


class TestCharacterExplore(TestCase):
    @patch('random.choices', side_effect=[[True], [False]])  # foe encounter: True, foe stab back: False
    @patch('builtins.input', side_effect=["1"])  # moves south
    def test_character_explore_run_away_after_encounter_foe(self, mock_input, random_bool_generator):
        user_choice = 2  # move south
        board = {(0, 1): 'test room'}
        character = {'name': 'Player', 'class': 'Sorcerer', 'class_name': ('Sorcerer', 'Cleric', 'Bishop'), 'hp': 15,
                     'max_hp': 15, 'x': 0, 'y': 0, 'level': 1, 'exp': 0}
        actual = character_explore(user_choice, character, board)
        expected = "character_alive"
        self.assertEqual(actual, expected)

    @patch('random.choices', side_effect=[[True], [True]])  # foe encounter: True, foe stab back: True
    @patch('builtins.input', side_effect=["1"])  # moves south
    @patch('random.randint', return_value=4)  # foe stab back damage
    def test_character_explore_run_away_stab_back(self, random_number_generator, mock_input, random_bool_generator):
        user_choice = 2  # move south
        board = {(0, 1): 'test room'}
        character = {'name': 'Player', 'class': 'Sorcerer', 'class_name': ('Sorcerer', 'Cleric', 'Bishop'), 'hp': 15,
                     'max_hp': 15, 'x': 0, 'y': 0, 'level': 1, 'exp': 0}
        character_explore(user_choice, character, board)
        expected = 11
        actual = character['hp']
        self.assertEqual(actual, expected)

    @patch('random.choices', return_value=[False])  # for encounter: False
    @patch('builtins.input', side_effect=["1"])  # moves south
    def test_character_explore_character_heal_after_move(self, mock_input, random_bool_generator):
        user_choice = 2  # move south
        board = {(0, 1): 'test room'}
        hp = 11
        character = {'name': 'Player', 'class': 'Sorcerer', 'class_name': ('Sorcerer', 'Cleric', 'Bishop'), 'hp': hp,
                     'max_hp': 15, 'x': 0, 'y': 0, 'level': 1, 'exp': 0}
        character_explore(user_choice, character, board)
        expected = 15
        actual = character['hp']
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=["0"])  # moves south
    @patch('random.randint', side_effect=[30, 90, 0, 16])  # boss strikes and character dies
    def test_character_explore_combat_with_boss_character_die(self, random_number_generator, mock_input):
        user_choice = 2  # move south
        board = {(24, 24): 'Boss room'}
        hp = 15
        character = {'name': 'Player', 'class': 'Sorcerer', 'class_name': ('Sorcerer', 'Cleric', 'Bishop'), 'hp': hp,
                     'max_hp': 15, 'x': 24, 'y': 23, 'level': 1, 'exp': 0}
        expected = "character_die"
        actual = character_explore(user_choice, character, board)
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=["0"])  # moves south
    @patch('random.randint', side_effect=[90, 30, 0, 50])  # character strikes and boss dies
    def test_character_explore_combat_with_boss_boss_die(self, random_number_generator, mock_input):
        user_choice = 2  # move south
        board = {(24, 24): 'Boss room'}
        character = {'name': 'Player', 'class': 'Sorcerer', 'class_name': ('Sorcerer', 'Cleric', 'Bishop'), 'hp': 15,
                     'max_hp': 15, 'x': 24, 'y': 23, 'level': 1, 'exp': 0}
        expected = "boss_die"
        actual = character_explore(user_choice, character, board)
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=["0"])  # moves south
    @patch('random.randint', side_effect=[90, 30, 0, 50])  # character strikes and boss dies
    def test_character_explore_combat_with_boss_boss_die(self, random_number_generator, mock_input):
        user_choice = 2  # move south
        board = {(24, 24): 'Boss room'}
        character = {'name': 'Player', 'class': 'Sorcerer', 'class_name': ('Sorcerer', 'Cleric', 'Bishop'), 'hp': 15,
                     'max_hp': 15, 'x': 24, 'y': 23, 'level': 1, 'exp': 0}
        expected = "boss_die"
        actual = character_explore(user_choice, character, board)
        self.assertEqual(actual, expected)

    @patch('random.choices', return_value=[True])  # foe encounter: True, foe stab back: True
    @patch('builtins.input', return_value="0")  # moves south
    @patch('random.randint', side_effect=[0, 30, 90, 0, 30, 0])  # foe strikes and character die
    def test_character_explore_combat_with_foe_character_die(self, random_number_generator, mock_input,
                                                             random_bool_generator):
        user_choice = 2  # move south
        board = {(0, 1): 'test room'}
        character = {'name': 'Player', 'class': 'Sorcerer', 'class_name': ('Sorcerer', 'Cleric', 'Bishop'), 'hp': 15,
                     'max_hp': 15, 'x': 0, 'y': 0, 'level': 1, 'exp': 0}
        expected = "character_die"
        actual = character_explore(user_choice, character, board)
        self.assertEqual(actual, expected)

    @patch('random.choices', return_value=[True])  # foe encounter: True
    @patch('builtins.input', return_value="0")  # moves south
    @patch('random.randint', side_effect=[0, 90, 30, 0, 30])  # character strikes and foe die
    def test_character_explore_combat_with_foe_foe_die(self, random_number_generator, mock_input,
                                                       random_bool_generator):
        user_choice = 2  # move south
        board = {(0, 1): 'test room'}
        character = {'name': 'Player', 'class': 'Sorcerer', 'class_name': ('Sorcerer', 'Cleric', 'Bishop'), 'hp': 15,
                     'max_hp': 15, 'x': 0, 'y': 0, 'level': 1, 'exp': 0}
        expected = "character_alive"
        actual = character_explore(user_choice, character, board)
        self.assertEqual(actual, expected)
