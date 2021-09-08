from unittest import TestCase
from unittest.mock import patch
from game import validate_move


class TestValidateMove(TestCase):
    @patch('builtins.input', side_effect=["0"])
    def test_validate_move_valid_move_north(self, mock_input):
        # board_x_lower_bound = 0
        # board_y_lower_bound = 0
        # board_x_upper_bound = 24
        # board_y_upper_bound = 24
        x_coord = 5
        y_coord = 5
        character = {'x': x_coord, 'y': y_coord}
        user_choices = ('North', 'East', 'South', 'West')
        user_choose = 'North'
        choice_number = user_choices.index(user_choose)
        actual = validate_move(choice_number, character)
        self.assertTrue(actual)

    @patch('builtins.input', side_effect=["1"])
    def test_validate_move_valid_move_east(self, mock_input):
        # board_x_lower_bound = 0
        # board_y_lower_bound = 0
        # board_x_upper_bound = 24
        # board_y_upper_bound = 24
        x_coord = 5
        y_coord = 5
        character = {'x': x_coord, 'y': y_coord}
        user_choices = ('North', 'East', 'South', 'West')
        user_choose = 'East'
        choice_number = user_choices.index(user_choose)
        actual = validate_move(choice_number, character)
        self.assertTrue(actual)

    @patch('builtins.input', side_effect=["2"])
    def test_validate_move_valid_move_south(self, mock_input):
        # board_x_lower_bound = 0
        # board_y_lower_bound = 0
        # board_x_upper_bound = 24
        # board_y_upper_bound = 24
        x_coord = 5
        y_coord = 5
        character = {'x': x_coord, 'y': y_coord}
        user_choices = ('North', 'East', 'South', 'West')
        user_choose = 'South'
        choice_number = user_choices.index(user_choose)
        actual = validate_move(choice_number, character)
        self.assertTrue(actual)

    @patch('builtins.input', side_effect=["2"])
    def test_validate_move_valid_move_west(self, mock_input):
        # board_x_lower_bound = 0
        # board_y_lower_bound = 0
        # board_x_upper_bound = 24
        # board_y_upper_bound = 24
        x_coord = 5
        y_coord = 5
        character = {'x': x_coord, 'y': y_coord}
        user_choices = ('North', 'East', 'South', 'West')
        user_choose = 'West'
        choice_number = user_choices.index(user_choose)
        actual = validate_move(choice_number, character)
        self.assertTrue(actual)

    @patch('builtins.input', side_effect=["0"])
    def test_validate_move_invalid_move_north_reached_y_lower_bound(self, mock_input):
        # board_x_lower_bound = 0
        # board_y_lower_bound = 0
        # board_x_upper_bound = 24
        # board_y_upper_bound = 24
        x_coord = 5
        y_coord = 0
        character = {'x': x_coord, 'y': y_coord}
        user_choices = ('North', 'East', 'South', 'West')
        user_choose = 'North'
        choice_number = user_choices.index(user_choose)
        actual = validate_move(choice_number, character)
        self.assertFalse(actual)

    @patch('builtins.input', side_effect=["1"])
    def test_validate_move_invalid_move_east_reached_x_upper_bound(self, mock_input):
        # board_x_lower_bound = 0
        # board_y_lower_bound = 0
        # board_x_upper_bound = 24
        # board_y_upper_bound = 24
        x_coord = 24
        y_coord = 5
        character = {'x': x_coord, 'y': y_coord}
        user_choices = ('North', 'East', 'South', 'West')
        user_choose = 'East'
        choice_number = user_choices.index(user_choose)
        actual = validate_move(choice_number, character)
        self.assertFalse(actual)

    @patch('builtins.input', side_effect=["2"])
    def test_validate_move_invalid_move_south_reached_y_upper_bound(self, mock_input):
        # board_x_lower_bound = 0
        # board_y_lower_bound = 0
        # board_x_upper_bound = 24
        # board_y_upper_bound = 24
        x_coord = 5
        y_coord = 24
        character = {'x': x_coord, 'y': y_coord}
        user_choices = ('North', 'East', 'South', 'West')
        user_choose = 'South'
        choice_number = user_choices.index(user_choose)
        actual = validate_move(choice_number, character)
        self.assertFalse(actual)

    @patch('builtins.input', side_effect=["2"])
    def test_validate_move_invalid_move_south_reached_x_lower_bound(self, mock_input):
        # board_x_lower_bound = 0
        # board_y_lower_bound = 0
        # board_x_upper_bound = 24
        # board_y_upper_bound = 24
        x_coord = 0
        y_coord = 5
        character = {'x': x_coord, 'y': y_coord}
        user_choices = ('North', 'East', 'South', 'West')
        user_choose = 'West'
        choice_number = user_choices.index(user_choose)
        actual = validate_move(choice_number, character)
        self.assertFalse(actual)

    def test_validate_move_return_boolean(self):
        x_coord = 4
        y_coord = 5
        character = {'x': x_coord, 'y': y_coord}
        user_choices = ('North', 'East', 'South', 'West')
        user_choose = 'West'
        choice_number = user_choices.index(user_choose)
        actual = validate_move(choice_number, character)
        self.assertIsInstance(actual, bool)
