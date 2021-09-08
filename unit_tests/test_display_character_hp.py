import io
from unittest import TestCase
from unittest.mock import patch
from game import display_character_hp


class TestDisplayCharacterHp(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_character_hp_max_hp(self, mock_stdout):
        character = {'name': 'TestName', 'hp': 20, 'max_hp': 20, 'level': 1, 'class_name': ('S1', 'S2', 'S3')}
        display_character_hp(character)
        expected = f"S1 {character['name']}'s HP : 20 | \033[32m++++++++++++++++++++\033[0m\033[31m\033[0m\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_character_hp_greater_than_zero_and_less_than_max_hp(self, mock_stdout):
        character = {'name': 'TestName', 'hp': 12, 'max_hp': 20, 'level': 1, 'class_name': ('S1', 'S2', 'S3')}
        display_character_hp(character)
        expected = f"S1 {character['name']}'s HP : 12 | \033[32m++++++++++++\033[0m\033[31m++++++++\033[0m\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_character_hp_zero_hp(self, mock_stdout):
        character = {'name': 'TestName', 'hp': 0, 'max_hp': 20, 'level': 1, 'class_name': ('S1', 'S2', 'S3')}
        display_character_hp(character)
        expected = f"S1 {character['name']}'s HP : 0 | \033[32m\033[0m\033[31m++++++++++++++++++++\033[0m\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_character_hp_less_than_zero(self, mock_stdout):
        character = {'name': 'TestName', 'hp': -5, 'max_hp': 20, 'level': 1, 'class_name': ('S1', 'S2', 'S3')}
        display_character_hp(character)
        expected = f"S1 {character['name']}'s HP : -5 | \033[32m\033[0m\033[31m++++++++++++++++++++\033[0m\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)
