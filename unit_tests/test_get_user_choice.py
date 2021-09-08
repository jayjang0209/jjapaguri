import io
from unittest import TestCase
from unittest.mock import patch
from game import get_user_choice


class TestGetUserChoice(TestCase):
    @patch('builtins.input', side_effect=["0"])
    def test_get_user_choice_return_integer(self, mock_input):
        user_choices = ('North', 'East', 'South', 'West', 'Quit')
        actual = get_user_choice(user_choices)
        self.assertIsInstance(actual, int)

    @patch('builtins.input', side_effect=["3"])
    def test_get_user_choice_return_same_integer_of_user_input(self, mock_input):
        user_choices = ('North', 'East', 'South', 'West', 'Quit')
        expected = 3
        actual = get_user_choice(user_choices)
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=["0"])
    def test_get_user_choice_return_integer_less_than_length_of_user_options_lower_bound(self, mock_input):
        user_choices = ('North', 'East', 'South', 'West', 'Quit')
        index_last_element = len(user_choices)
        actual = get_user_choice(user_choices)
        self.assertLess(actual, index_last_element)

    @patch('builtins.input', side_effect=["4"])
    def test_get_user_choice_return_integer_less_than_length_of_user_options_upper_bound(self, mock_input):
        user_choices = ('North', 'East', 'South', 'West', 'Quit')
        length_of_choices = len(user_choices)
        actual = get_user_choice(user_choices)
        self.assertLess(actual, length_of_choices)

    @patch('builtins.input', side_effect=["1"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice_prompt_user_choices_move(self, mock_stdout, mock_input):
        user_choices = ('North', 'East', 'South', 'West', 'Quit')
        get_user_choice(user_choices)
        expected = "-------------------------------------------\n" \
                   " MENU \n" \
                   " 0) : North\n" \
                   " 1) : East\n" \
                   " 2) : South\n" \
                   " 3) : West\n" \
                   " 4) : Quit\n" \
                   "-------------------------------------------\n" \
                   "\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=["1"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice_prompt_user_choices_fight(self, mock_stdout, mock_input):
        user_choices = ('Fight', 'Flee')
        get_user_choice(user_choices)
        expected = "-------------------------------------------\n" \
                   " MENU \n" \
                   " 0) : Fight\n" \
                   " 1) : Flee\n" \
                   "-------------------------------------------\n" \
                   "\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=["1"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice_prompt_user_choices_fight(self, mock_stdout, mock_input):
        user_choices = ('Sorcerer', 'Thief', 'Bowman', 'Fighter')
        get_user_choice(user_choices)
        expected = "-------------------------------------------\n" \
                   " MENU \n" \
                   " 0) : Sorcerer\n" \
                   " 1) : Thief\n" \
                   " 2) : Bowman\n" \
                   " 3) : Fighter\n" \
                   "-------------------------------------------\n\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)
