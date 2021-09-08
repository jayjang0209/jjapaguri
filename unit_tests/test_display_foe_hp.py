import io
from unittest import TestCase
from unittest.mock import patch
from game import display_foe_hp


class TestDisplayFoeHp(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_foe_hp_max_hp(self, mock_stdout):
        foe = {'name': 'monster', 'hp': 20, 'max_hp': 20}
        display_foe_hp(foe)
        expected = f"{foe['name']}'s HP : 20 | \033[32m++++++++++++++++++++\033[0m\033[31m\033[0m\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_foe_hp_greater_than_zero_and_less_than_max_hp(self, mock_stdout):
        foe = {'name': 'monster', 'hp': 12, 'max_hp': 20}
        display_foe_hp(foe)
        expected = f"{foe['name']}'s HP : 12 | \033[32m++++++++++++\033[0m\033[31m++++++++\033[0m\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_foe_hp_zero_hp(self, mock_stdout):
        foe = {'name': 'monster', 'hp': 0, 'max_hp': 20}
        display_foe_hp(foe)
        expected = f"{foe['name']}'s HP : 0 | \033[32m\033[0m\033[31m++++++++++++++++++++\033[0m\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_foe_hp_less_than_zero(self, mock_stdout):
        foe = {'name': 'monster', 'hp': -5, 'max_hp': 20}
        display_foe_hp(foe)
        expected = f"{foe['name']}'s HP : -5 | \033[32m\033[0m\033[31m++++++++++++++++++++\033[0m\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)
