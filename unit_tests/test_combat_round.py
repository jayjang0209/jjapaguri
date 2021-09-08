import io
from unittest import TestCase
from unittest.mock import patch
from game import combat_round


class TestCombatRound(TestCase):
    @patch('random.randint', side_effect=[90, 30, 0, 11])
    def test_combat_round_is_tuple(self, random_number_generator):
        character = {'name': 'Player', 'class': 'Sorcerer', 'class_name': ('Sorcerer', 'Cleric', 'Bishop'), 'hp': 15,
                     'max_hp': 15, 'x': 0, 'y': 0, 'level': 1, 'exp': 0}
        foe = {'name': 'White eyed cat', 'hp': 11, 'max_hp': 11, 'exp': 200, 'min_dp': 2, 'max_dp': 9}
        actual = combat_round(character, foe)
        self.assertIsInstance(actual, tuple)

    @patch('random.randint', side_effect=[90, 30, 0, 11])
    def test_combat_round_is_element_bool(self, random_number_generator):
        character = {'name': 'Player', 'class': 'Sorcerer', 'class_name': ('Sorcerer', 'Cleric', 'Bishop'), 'hp': 15,
                     'max_hp': 15, 'x': 0, 'y': 0, 'level': 1, 'exp': 0}
        foe = {'name': 'White eyed cat', 'hp': 11, 'max_hp': 11, 'exp': 200, 'min_dp': 2, 'max_dp': 9}
        actual = combat_round(character, foe)
        for element in actual:
            self.assertIsInstance(element, bool)

    @patch('random.randint', side_effect=[90, 30, 0, 11])
    def test_combat_round_has_three_elements(self, random_number_generator):
        character = {'name': 'Player', 'class': 'Sorcerer', 'class_name': ('Sorcerer', 'Cleric', 'Bishop'), 'hp': 15,
                     'max_hp': 15, 'x': 0, 'y': 0, 'level': 1, 'exp': 0}
        foe = {'name': 'White eyed cat', 'hp': 11, 'max_hp': 11, 'exp': 200, 'min_dp': 2, 'max_dp': 9}
        actual = combat_round(character, foe)
        actual = len([element for element in actual])
        self.assertEqual(actual, 3)

    # character roll = 90, foe roll = 30, character attack description index = 0, character dp = 11
    @patch('random.randint', side_effect=[90, 30, 0, 11])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_round_killed_foe(self, mock_stdout, random_number_generator):
        character = {'name': 'Player', 'class': 'Sorcerer', 'class_name': ('Sorcerer', 'Cleric', 'Bishop'), 'hp': 15,
                     'max_hp': 15, 'x': 0, 'y': 0, 'level': 1, 'exp': 0}
        foe = {'name': 'White eyed cat', 'hp': 11, 'max_hp': 11, 'exp': 200, 'min_dp': 2, 'max_dp': 9}
        combat_round(character, foe)
        expected = "Player used fire ball to White eyed cat\n" \
                   "White eyed cat got -11 damage\n" \
                   "White eyed cat's HP : 0 | \033[32m\033[0m\033[31m+++++++++++\033[0m\n" \
                   "Sorcerer Player's HP : 15 | \033[32m+++++++++++++++\033[0m\033[31m\033[0m\n" \
                   "Foe is dead\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)

    # character roll = 30, foe roll = 90, foe attack description index = 0, fo2 dp = 15
    @patch('random.randint', side_effect=[30, 90, 0, 15])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_round_character_dead(self, mock_stdout, random_number_generator):
        character = {'name': 'Player', 'class': 'Sorcerer', 'class_name': ('Sorcerer', 'Cleric', 'Bishop'), 'hp': 15,
                     'max_hp': 15, 'x': 0, 'y': 0, 'level': 1, 'exp': 0}
        foe = {'name': 'White eyed cat', 'hp': 11, 'max_hp': 11, 'exp': 200, 'min_dp': 2, 'max_dp': 15}
        combat_round(character, foe)
        expected = "White eyed cat used acid spray to Player\n" \
                   "Player got -15 damage\n" \
                   "Sorcerer Player's HP : 0 | \033[32m\033[0m\033[31m+++++++++++++++\033[0m\n" \
                   "White eyed cat's HP : 11 | \033[32m+++++++++++\033[0m\033[31m\033[0m\n" \
                   "Character collapsed...\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)

    @patch('random.randint', side_effect=[30, 30])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_round_roll_draw(self, mock_stdout, random_number_generator):
        character = {'name': 'Player', 'class': 'Sorcerer', 'class_name': ('Sorcerer', 'Cleric', 'Bishop'), 'hp': 15,
                     'max_hp': 15, 'x': 0, 'y': 0, 'level': 1, 'exp': 0}
        foe = {'name': 'White eyed cat', 'hp': 11, 'max_hp': 11, 'exp': 200, 'min_dp': 2, 'max_dp': 15}
        combat_round(character, foe)
        expected = "Nobody successfully strikes anyone!!\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)

    # character roll = 90, foe roll = 30, character attack description index = 0, character dp = 11
    @patch('random.randint', side_effect=[90, 30, 0, 11])
    def test_combat_round_foe_die_true(self, random_number_generator):
        character = {'name': 'Player', 'class': 'Sorcerer', 'class_name': ('Sorcerer', 'Cleric', 'Bishop'), 'hp': 15,
                     'max_hp': 15, 'x': 0, 'y': 0, 'level': 1, 'exp': 0}
        foe = {'name': 'White eyed cat', 'hp': 11, 'max_hp': 11, 'exp': 200, 'min_dp': 2, 'max_dp': 9}

        expected = True, False, False  # foe_die, character_die, foe_runaway
        actual = combat_round(character, foe)
        self.assertEqual(actual, expected)

    # character roll = 30, foe roll = 90, foe attack description index = 0, fo2 dp = 15
    @patch('random.randint', side_effect=[30, 90, 0, 15])
    def test_combat_round_character_die_true(self, random_number_generator):
        character = {'name': 'Player', 'class': 'Sorcerer', 'class_name': ('Sorcerer', 'Cleric', 'Bishop'), 'hp': 15,
                     'max_hp': 15, 'x': 0, 'y': 0, 'level': 1, 'exp': 0}
        foe = {'name': 'White eyed cat', 'hp': 11, 'max_hp': 11, 'exp': 200, 'min_dp': 2, 'max_dp': 9}
        expected = False, True, False  # foe_die, character_die, foe_runaway
        actual = combat_round(character, foe)
        self.assertEqual(actual, expected)

    # character roll = 90, foe roll = 30, character attack description index = 0, character dp = 6
    # foe attack description index = 1, fo2 dp = 3
    @patch('random.randint', side_effect=[90, 30, 0, 6, 1, 3])
    @patch('random.choices', return_value=[True])
    def test_combat_round_foe_run_away_true(self, random_bool_generator, random_number_generator):
        character = {'name': 'Player', 'class': 'Sorcerer', 'class_name': ('Sorcerer', 'Cleric', 'Bishop'), 'hp': 15,
                     'max_hp': 15, 'x': 0, 'y': 0, 'level': 1, 'exp': 0}
        foe = {'name': 'White eyed cat', 'hp': 11, 'max_hp': 11, 'exp': 200, 'min_dp': 2, 'max_dp': 9}
        expected = False, False, True  # foe_die, character_die, foe_runaway
        actual = combat_round(character, foe)
        self.assertEqual(actual, expected)
