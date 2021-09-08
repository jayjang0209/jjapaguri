import io
from unittest import TestCase
from unittest.mock import patch
from game import display_location
from game import make_board


class TestDisplayLocation(TestCase):
    @patch('random.choice', return_value='Dark room')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_location_character_at_start_point_level_1_region(self, mock_stdout, random_descriptions_generator):
        board_width = 25
        board_height = 25
        x_coord = 0
        y_coord = 0
        character = {'name': 'test', 'x': x_coord, 'y': y_coord}
        game_board = make_board(board_width, board_height)
        display_location(game_board, character)
        expected = "############ current area ###########\n" \
                   "------------ Level 1 area -----------\n" \
                   "Dark room\n" \
                   "your current coordinates: X- 0,  Y- 0\n" \
                   "[@][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "#####################################\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)

    @patch('random.choice', return_value='Dark room')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_location_character_lev1_region_x_upper_bound_when_y_is_zero(self, mock_stdout,
                                                                                 random_descriptions_generator):
        board_width = 25
        board_height = 25
        x_coord = 9
        y_coord = 0
        character = {'name': 'test', 'x': x_coord, 'y': y_coord}
        game_board = make_board(board_width, board_height)
        display_location(game_board, character)
        expected = "############ current area ###########\n" \
                   "------------ Level 1 area -----------\n" \
                   "Dark room\n" \
                   "your current coordinates: X- 9,  Y- 0\n" \
                   "[ ][ ][ ][ ][@]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "#####################################\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)

    @patch('random.choice', return_value='Dark room')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_location_character_lev1_region_y_upper_bound_when_x_is_zero(self, mock_stdout,
                                                                                 random_descriptions_generator):
        board_width = 25
        board_height = 25
        x_coord = 0
        y_coord = 9
        character = {'name': 'test', 'x': x_coord, 'y': y_coord}
        game_board = make_board(board_width, board_height)
        display_location(game_board, character)
        expected = "############ current area ###########\n" \
                   "------------ Level 1 area -----------\n" \
                   "Dark room\n" \
                   "your current coordinates: X- 0,  Y- 9\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[@][ ][ ][ ][ ]\n" \
                   "#####################################\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)

    @patch('random.choice', return_value='Dark room')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_location_character_lev1_region_x_and_y_upper_bound(self, mock_stdout,
                                                                        random_descriptions_generator):
        board_width = 25
        board_height = 25
        x_coord = 9
        y_coord = 9
        character = {'name': 'test', 'x': x_coord, 'y': y_coord}
        game_board = make_board(board_width, board_height)
        display_location(game_board, character)
        expected = "############ current area ###########\n" \
                   "------------ Level 1 area -----------\n" \
                   "Dark room\n" \
                   "your current coordinates: X- 9,  Y- 9\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][@]\n" \
                   "#####################################\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)

    @patch('random.choice', return_value='room of curse')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_location_character_lev2_region_x_lower_bound_when_y_is_zero(self, mock_stdout,
                                                                                 random_descriptions_generator):
        board_width = 25
        board_height = 25
        x_coord = 10
        y_coord = 0
        character = {'name': 'test', 'x': x_coord, 'y': y_coord}
        game_board = make_board(board_width, board_height)
        display_location(game_board, character)
        expected = "############ current area ###########\n" \
                   "------------ Level 2 area -----------\n" \
                   "room of curse\n" \
                   "your current coordinates: X- 10,  Y- 0\n" \
                   "[@][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "#####################################\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)

    @patch('random.choice', return_value='room of curse')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_location_character_lev2_region_x_upper_bound_when_y_is_zero(self, mock_stdout,
                                                                                 random_descriptions_generator):
        board_width = 25
        board_height = 25
        x_coord = 19
        y_coord = 0
        character = {'name': 'test', 'x': x_coord, 'y': y_coord}
        game_board = make_board(board_width, board_height)
        display_location(game_board, character)
        expected = "############ current area ###########\n" \
                   "------------ Level 2 area -----------\n" \
                   "room of curse\n" \
                   "your current coordinates: X- 19,  Y- 0\n" \
                   "[ ][ ][ ][ ][@]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "#####################################\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)

    @patch('random.choice', return_value='room of curse')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_location_character_lev2_region_y_lower_bound_when_x_is_zero(self, mock_stdout,
                                                                                 random_descriptions_generator):
        board_width = 25
        board_height = 25
        x_coord = 0
        y_coord = 10
        character = {'name': 'test', 'x': x_coord, 'y': y_coord}
        game_board = make_board(board_width, board_height)
        display_location(game_board, character)
        expected = "############ current area ###########\n" \
                   "------------ Level 2 area -----------\n" \
                   "room of curse\n" \
                   "your current coordinates: X- 0,  Y- 10\n" \
                   "[@][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "#####################################\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)

    @patch('random.choice', return_value='room of curse')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_location_character_lev2_region_y_upper_bound_when_x_is_zero(self, mock_stdout,
                                                                                 random_descriptions_generator):
        board_width = 25
        board_height = 25
        x_coord = 0
        y_coord = 19
        character = {'name': 'test', 'x': x_coord, 'y': y_coord}
        game_board = make_board(board_width, board_height)
        display_location(game_board, character)
        expected = "############ current area ###########\n" \
                   "------------ Level 2 area -----------\n" \
                   "room of curse\n" \
                   "your current coordinates: X- 0,  Y- 19\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[@][ ][ ][ ][ ]\n" \
                   "#####################################\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)

    @patch('random.choice', return_value='room of curse')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_location_character_lev2_region_x_and_y_upper_bound(self, mock_stdout,
                                                                        random_descriptions_generator):
        board_width = 25
        board_height = 25
        x_coord = 19
        y_coord = 19
        character = {'name': 'test', 'x': x_coord, 'y': y_coord}
        game_board = make_board(board_width, board_height)
        display_location(game_board, character)
        expected = "############ current area ###########\n" \
                   "------------ Level 2 area -----------\n" \
                   "room of curse\n" \
                   "your current coordinates: X- 19,  Y- 19\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][@]\n" \
                   "#####################################\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)

    @patch('random.choice', return_value='Deathbed')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_location_character_lev3_region_x_lower_bound_when_y_is_zero(self, mock_stdout,
                                                                                 random_descriptions_generator):
        board_width = 25
        board_height = 25
        x_coord = 20
        y_coord = 0
        character = {'name': 'test', 'x': x_coord, 'y': y_coord}
        game_board = make_board(board_width, board_height)
        display_location(game_board, character)
        expected = "############ current area ###########\n" \
                   "------------ Level 3 area -----------\n" \
                   "Deathbed\n" \
                   "your current coordinates: X- 20,  Y- 0\n" \
                   "[@][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "#####################################\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)

    @patch('random.choice', return_value='Deathbed')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_location_character_lev3_region_x_upper_bound_when_y_is_zero(self, mock_stdout,
                                                                                 random_descriptions_generator):
        board_width = 25
        board_height = 25
        x_coord = 24
        y_coord = 0
        character = {'name': 'test', 'x': x_coord, 'y': y_coord}
        game_board = make_board(board_width, board_height)
        display_location(game_board, character)
        expected = "############ current area ###########\n" \
                   "------------ Level 3 area -----------\n" \
                   "Deathbed\n" \
                   "your current coordinates: X- 24,  Y- 0\n" \
                   "[ ][ ][ ][ ][@]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "#####################################\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)

    @patch('random.choice', return_value='Deathbed')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_location_character_lev3_region_y_lower_bound_when_x_is_zero(self, mock_stdout,
                                                                                 random_descriptions_generator):
        board_width = 25
        board_height = 25
        x_coord = 0
        y_coord = 20
        character = {'name': 'test', 'x': x_coord, 'y': y_coord}
        game_board = make_board(board_width, board_height)
        display_location(game_board, character)
        expected = "############ current area ###########\n" \
                   "------------ Level 3 area -----------\n" \
                   "Deathbed\n" \
                   "your current coordinates: X- 0,  Y- 20\n" \
                   "[@][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "#####################################\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)

    @patch('random.choice', return_value='Deathbed')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_location_character_lev3_region_y_upper_bound_when_x_is_zero(self, mock_stdout,
                                                                                 random_descriptions_generator):
        board_width = 25
        board_height = 25
        x_coord = 0
        y_coord = 24
        character = {'name': 'test', 'x': x_coord, 'y': y_coord}
        game_board = make_board(board_width, board_height)
        display_location(game_board, character)
        expected = "############ current area ###########\n" \
                   "------------ Level 3 area -----------\n" \
                   "Deathbed\n" \
                   "your current coordinates: X- 0,  Y- 24\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[@][ ][ ][ ][ ]\n" \
                   "#####################################\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)

    @patch('random.choice', return_value='Deathbed')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_location_character_lev3_region_boss_area_area_top_left_corner(self, mock_stdout,
                                                                                   random_descriptions_generator):
        board_width = 25
        board_height = 25
        x_coord = 20
        y_coord = 20
        character = {'name': 'test', 'x': x_coord, 'y': y_coord}
        game_board = make_board(board_width, board_height)
        display_location(game_board, character)
        expected = "############ current area ###########\n" \
                   "------------ Level 3 area -----------\n" \
                   "Deathbed\n" \
                   "your current coordinates: X- 20,  Y- 20\n" \
                   "[@][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][B]\n" \
                   "#####################################\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)

    @patch('random.choice', return_value='Deathbed')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_location_character_lev3_region_boss_area_bottom_left_corner(self, mock_stdout,
                                                                                 random_descriptions_generator):
        board_width = 25
        board_height = 25
        x_coord = 20
        y_coord = 24
        character = {'name': 'test', 'x': x_coord, 'y': y_coord}
        game_board = make_board(board_width, board_height)
        display_location(game_board, character)
        expected = "############ current area ###########\n" \
                   "------------ Level 3 area -----------\n" \
                   "Deathbed\n" \
                   "your current coordinates: X- 20,  Y- 24\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[@][ ][ ][ ][B]\n" \
                   "#####################################\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)

    @patch('random.choice', return_value='Deathbed')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_location_character_lev3_region_boss_area_top_right_corner(self, mock_stdout,
                                                                               random_descriptions_generator):
        board_width = 25
        board_height = 25
        x_coord = 24
        y_coord = 20
        character = {'name': 'test', 'x': x_coord, 'y': y_coord}
        game_board = make_board(board_width, board_height)
        display_location(game_board, character)
        expected = "############ current area ###########\n" \
                   "------------ Level 3 area -----------\n" \
                   "Deathbed\n" \
                   "your current coordinates: X- 24,  Y- 20\n" \
                   "[ ][ ][ ][ ][@]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][B]\n" \
                   "#####################################\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)

    @patch('random.choice', return_value='Deathbed')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_location_character_at_boss_position(self, mock_stdout, random_descriptions_generator):
        board_width = 25
        board_height = 25
        x_coord = 24
        y_coord = 24
        character = {'name': 'test', 'x': x_coord, 'y': y_coord}
        game_board = make_board(board_width, board_height)
        display_location(game_board, character)
        expected = "############ current area ###########\n" \
                   "------------ Level 3 area -----------\n" \
                   "Deathbed\n" \
                   "your current coordinates: X- 24,  Y- 24\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][ ]\n" \
                   "[ ][ ][ ][ ][@]\n" \
                   "#####################################\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)
