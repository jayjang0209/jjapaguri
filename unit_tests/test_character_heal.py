import io
from unittest import TestCase
from unittest.mock import patch
from game import character_heal


class TestCharacterHeal(TestCase):
    def test_character_heal_hp_is_already_full_hp_unchanged(self):  # hp is unchanged when hp is already full
        hp = 20
        max_hp = 20
        game_character = {'name': 'player', 'hp': hp, 'max_hp': max_hp, 'level': 1, 'class_name': ('S1', 'S2', 'S3')}
        expected = game_character['hp']
        character_heal(game_character)
        actual = game_character['hp']
        self.assertEqual(expected, actual)

    def test_character_heal_hp_is_greater_than_max_hp_minus_hp_increment(self):
        #  hp is greater than max hp - hp heal increment and less than max hp. hp_increment = 4.
        hp = 18
        max_hp = 20
        game_character = {'name': 'player', 'hp': hp, 'max_hp': max_hp, 'level': 1, 'class_name': ('S1', 'S2', 'S3')}
        expected = max_hp
        character_heal(game_character)
        actual = game_character['hp']
        self.assertEqual(expected, actual)

    def test_character_heal_hp_is_equal_to_max_hp_minus_hp_increment(self):
        #  hp is max_hp - hp_heal_increment. hp_increment = 4.
        hp = 16
        max_hp = 20
        hp_increment = 4
        game_character = {'name': 'player', 'hp': hp, 'max_hp': max_hp, 'level': 1, 'class_name': ('S1', 'S2', 'S3')}
        expected = hp + hp_increment
        character_heal(game_character)
        actual = game_character['hp']
        self.assertEqual(expected, actual)

    def test_character_heal_hp_is_less_than_max_hp_minus_hp_increment(self):
        #  hp is less than max_hp - hp_heal_increment. #  hp_increment = 4.
        hp = 10
        max_hp = 20
        hp_increment = 4
        game_character = {'name': 'player', 'hp': hp, 'max_hp': max_hp, 'level': 1, 'class_name': ('S1', 'S2', 'S3')}
        expected = hp + hp_increment
        character_heal(game_character)
        actual = game_character['hp']
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_character_heal_test_output_hp_is_already_full_hp_unchanged(self, mock_stdout):
        # hp is already full.
        hp = 20
        max_hp = 20
        game_character = {'name': 'player', 'hp': hp, 'max_hp': max_hp, 'level': 1, 'class_name': ('S1', 'S2', 'S3')}
        character_heal(game_character)
        expected = "S1 player's HP : 20 | \033[32m++++++++++++++++++++\033[0m\033[31m\033[0m\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_character_heal_Test_output_hp_is_greater_than_max_hp_minus_hp_increment(self, mock_stdout):
        #  hp is greater than max hp - hp heal increment and less than max hp. #  hp_increment = 4.
        hp = 18
        max_hp = 20
        game_character = {'name': 'player', 'hp': hp, 'max_hp': max_hp, 'level': 1, 'class_name': ('S1', 'S2', 'S3')}
        character_heal(game_character)
        expected = "Character healed\n" \
                   "S1 player's HP : 20 | \033[32m++++++++++++++++++++\033[0m\033[31m\033[0m\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_character_heal_check_output_hp_is_equal_to_max_hp_minus_hp_increment(self, mock_stdout):
        #  when hp ==  max_hp - hp_heal_increment. #  hp_increment = 4.
        hp = 16
        max_hp = 20
        game_character = {'name': 'player', 'hp': hp, 'max_hp': max_hp, 'level': 1, 'class_name': ('S1', 'S2', 'S3')}
        character_heal(game_character)
        expected = "Character healed\n" \
                   "S1 player's HP : 20 | \033[32m++++++++++++++++++++\033[0m\033[31m\033[0m\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_character_heal_test_output_hp_is_less_than_max_hp_minus_hp_increment(self, mock_stdout):
        #  hp is less than max_hp - hp_heal_increment. hp_increment = 4.
        hp = 10
        max_hp = 20
        game_character = {'name': 'player', 'hp': hp, 'max_hp': max_hp, 'level': 1, 'class_name': ('S1', 'S2', 'S3')}
        character_heal(game_character)
        expected = "Character healed\n" \
                   "S1 player's HP : 14 | \033[32m++++++++++++++\033[0m\033[31m++++++\033[0m\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)
