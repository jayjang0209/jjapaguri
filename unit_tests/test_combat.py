import io
from unittest import TestCase
from unittest.mock import patch
from game import combat


class TestCombat(TestCase):
    @patch('random.randint', side_effect=[90, 30, 0, 11])
    # character_roll = 90, foe_roll = 30, character_attack_description_randomly = 0, character_strike_damage_point = 11
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_character_killed_foe(self, mock_stdout, random_number_generator):
        character = {'name': 'Player', 'class': 'Sorcerer', 'class_name': ('Sorcerer', 'Cleric', 'Bishop'), 'hp': 15,
                     'max_hp': 15, 'x': 0, 'y': 0, 'level': 1, 'exp': 0}
        foe = {'name': 'White eyed cat', 'hp': 11, 'max_hp': 11, 'exp': 200, 'min_dp': 2, 'max_dp': 9}
        combat(character, foe)
        expected = "Player used fire ball to White eyed cat\n" \
                   "White eyed cat got -11 damage\n" \
                   "White eyed cat's HP : 0 | \033[32m\033[0m\033[31m+++++++++++\033[0m\n" \
                   "Sorcerer Player's HP : 15 | \033[32m+++++++++++++++\033[0m\033[31m\033[0m\n" \
                   "Foe is dead\n" \
                   "Player killed White eyed cat successfully\n" \
                   "character earned exp:200. current exp:200\n" \
                   "Combat is over\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)

    @patch('random.randint', side_effect=[30, 90, 0, 15])
    # character_roll = 30, foe_roll = 90, foe_attack_description_randomly = 0, character_strike_damage_point = 15
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_character_character_dead(self, mock_stdout, random_number_generator):
        character = {'name': 'Player', 'class': 'Sorcerer', 'class_name': ('Sorcerer', 'Cleric', 'Bishop'), 'hp': 15,
                     'max_hp': 15, 'x': 0, 'y': 0, 'level': 1, 'exp': 0}
        foe = {'name': 'White eyed cat', 'hp': 11, 'max_hp': 11, 'exp': 200, 'min_dp': 2, 'max_dp': 15}
        combat(character, foe)
        expected = "White eyed cat used acid spray to Player\n" \
                   "Player got -15 damage\n" \
                   "Sorcerer Player's HP : 0 | \033[32m\033[0m\033[31m+++++++++++++++\033[0m\n" \
                   "White eyed cat's HP : 11 | \033[32m+++++++++++\033[0m\033[31m\033[0m\n" \
                   "Character collapsed...\n" \
                   "Player is dead\n" \
                   "Combat is over\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)

    @patch('random.randint', side_effect=[30, 30])
    @patch('random.choices', return_value=[True])
    # character_roll = 30, foe_roll = 90, foe_attack_description_randomly = 0, character_strike_damage_point = 15
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_character_roll_draw(self, mock_stdout, random_bool_generator, random_number_generator):
        character = {'name': 'Player', 'class': 'Sorcerer', 'class_name': ('Sorcerer', 'Cleric', 'Bishop'), 'hp': 15,
                     'max_hp': 15, 'x': 0, 'y': 0, 'level': 1, 'exp': 0}
        foe = {'name': 'White eyed cat', 'hp': 11, 'max_hp': 11, 'exp': 200, 'min_dp': 2, 'max_dp': 15}
        combat(character, foe)
        expected = "Nobody successfully strikes anyone!!\n" \
                   "oops!~, Foe ran away~~~~~~~~~~~~~~~~~~~\n" \
                   "Combat is over\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)

    @patch('random.randint', side_effect=[90, 30, 0, 5, 0, 3])
    @patch('random.choices', return_value=[True])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_character_foe_run_away(self, mock_stdout, random_bool_generator, random_number_generator):
        character = {'name': 'Player', 'class': 'Sorcerer', 'class_name': ('Sorcerer', 'Cleric', 'Bishop'), 'hp': 15,
                     'max_hp': 15, 'x': 0, 'y': 0, 'level': 1, 'exp': 0}
        foe = {'name': 'White eyed cat', 'hp': 11, 'max_hp': 11, 'exp': 200, 'min_dp': 2, 'max_dp': 9}
        combat(character, foe)
        expected = "Player used fire ball to White eyed cat\n" \
                   "White eyed cat got -5 damage\n" \
                   "White eyed cat's HP : 6 | \033[32m++++++\033[0m\033[31m+++++\033[0m\n" \
                   "Sorcerer Player's HP : 15 | \033[32m+++++++++++++++\033[0m\033[31m\033[0m\n" \
                   "White eyed cat used acid spray to Player\n" \
                   "Player got -3 damage\n" \
                   "Sorcerer Player's HP : 12 | \033[32m++++++++++++\033[0m\033[31m+++\033[0m\n" \
                   "White eyed cat's HP : 6 | \033[32m++++++\033[0m\033[31m+++++\033[0m\n" \
                   "oops!~, Foe ran away~~~~~~~~~~~~~~~~~~~\n" \
                   "Combat is over\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)
