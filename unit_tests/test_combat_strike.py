import io
from unittest import TestCase
from unittest.mock import patch
from game import combat_strike


class TestCombatStrike(TestCase):
    @patch('random.randint', side_effect=[0, 5])  # 0: character attack description index, 5: character dp
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_strike_character_high_roller(self, mock_stdout, random_number_generator):
        character = {'name': 'player', 'hp': 20, 'max_hp': 20, 'class': 'Bowman', 'level': 1, 'class_name': ('Bowman',
                     'Hunter', 'Bow Master')}
        foe = {'name': 'monster', 'hp': 10, 'max_hp': 10}
        high_roller = 'character'
        combat_strike(high_roller, character, foe)
        expected = "player used double shot to monster\n" \
                   "monster got -5 damage\n" \
                   "monster's HP : 5 | \033[32m+++++\033[0m\033[31m+++++\033[0m\n" \
                   "Bowman player's HP : 20 | \033[32m++++++++++++++++++++\033[0m\033[31m\033[0m\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)

    @patch('random.randint', side_effect=[0, 5])  # 0: foe attack description index, 5: foe dp
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_strike_foe_high_roller(self, mock_stdout, random_number_generator):
        character = {'name': 'player', 'hp': 20, 'max_hp': 20, 'class': 'Bowman', 'level': 1, 'class_name': ('Bowman',
                     'Hunter', 'Bow Master')}
        foe = {'name': 'monster', 'hp': 10, 'max_hp': 10, 'min_dp': 3, 'max_dp': 5}
        high_roller = 'foe'
        combat_strike(high_roller, character, foe)
        expected = "monster used acid spray to player\n" \
                   "player got -5 damage\n" \
                   "Bowman player's HP : 15 | \033[32m+++++++++++++++\033[0m\033[31m+++++\033[0m\n" \
                   "monster's HP : 10 | \033[32m++++++++++\033[0m\033[31m\033[0m\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)
