import io
from unittest import TestCase
from unittest.mock import patch
from game import display_mini_map


class TestDisplayMiniMap(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_mini_map_staring_point(self, mock_stdout):
        x_coord = 0
        y_coord = 0
        character = {'x': x_coord, 'y': y_coord}
        display_mini_map(character)
        expected = "[@][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_mini_map_x_upper_bound_when_y_is_zero(self, mock_stdout):
        x_coord = 24
        y_coord = 0
        character = {'x': x_coord, 'y': y_coord}
        display_mini_map(character)
        expected = "[ ][ ][ ][ ][@]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_mini_map_y_upper_bound_when_x_is_zero(self, mock_stdout):
        x_coord = 0
        y_coord = 24
        character = {'x': x_coord, 'y': y_coord}
        display_mini_map(character)
        expected = "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[@][ ][ ][ ][ ]\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_mini_map_region_no_boss(self, mock_stdout):
        x_coord = 19
        y_coord = 19
        character = {'x': x_coord, 'y': y_coord}
        display_mini_map(character)
        expected = "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][@]\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_mini_map_region_no_boss_right_bottom_boundary(self, mock_stdout):
        x_coord = 24
        y_coord = 19
        character = {'x': x_coord, 'y': y_coord}
        display_mini_map(character)
        expected = "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][@]\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_mini_map_region_no_boss_bottom_right_boundary(self, mock_stdout):
        x_coord = 19
        y_coord = 24
        character = {'x': x_coord, 'y': y_coord}
        display_mini_map(character)
        expected = "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][@]\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_mini_map_boss_region_top_left_corner(self, mock_stdout):
        x_coord = 20
        y_coord = 20
        character = {'x': x_coord, 'y': y_coord}
        display_mini_map(character)
        expected = "[@][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][B]\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_mini_map_boss_region_top_right_corner(self, mock_stdout):
        x_coord = 24
        y_coord = 20
        character = {'x': x_coord, 'y': y_coord}
        display_mini_map(character)
        expected = "[ ][ ][ ][ ][@]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][B]\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_mini_map_boss_region_bottom_left_corner(self, mock_stdout):
        x_coord = 20
        y_coord = 24
        character = {'x': x_coord, 'y': y_coord}
        display_mini_map(character)
        expected = "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[@][ ][ ][ ][B]\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_mini_map_character_at_boss_location(self, mock_stdout):
        x_coord = 24
        y_coord = 24
        character = {'x': x_coord, 'y': y_coord}
        display_mini_map(character)
        expected = "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][@]\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)
