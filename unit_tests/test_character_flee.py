import io
from unittest import TestCase
from unittest.mock import patch
from game import character_flee


@patch('random.choices', return_value=[False])
@patch('sys.stdout', new_callable=io.StringIO)
class TestCharacterFlee(TestCase):
    def test_character_flee_character_run_away_successfully(self, mock_stdout, random_bool_generator):
        character = {'name': 'player', 'hp': 20, 'max_hp': 20, 'level': 1, 'class_name': ('S1', 'S2', 'S3')}
        character_flee(character)
        expected = "S1 player's HP : 20 | \033[32m++++++++++++++++++++\033[0m\033[31m\033[0m\n"\
                   "player ran away successfully\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)


@patch('random.choices', return_value=[True])
@patch('random.randint', side_effect=[3])
@patch('sys.stdout', new_callable=io.StringIO)
class TestCharacterFlee(TestCase):
    def test_character_flee_foe_stab_back_character(self, mock_stdout, random_number_generator, random_bool_generator):
        character = {'name': 'player', 'hp': 20, 'max_hp': 20, 'level': 1, 'class_name': ('S1', 'S2', 'S3')}
        character_flee(character)
        expected = "player just got stabbed in the back and got - 3 damage\n" \
                   "S1 player's HP : 17 | \033[32m+++++++++++++++++\033[0m\033[31m+++\033[0m\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)
