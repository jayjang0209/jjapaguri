from unittest import TestCase
from game import make_board


class TestMakeBoard(TestCase):
    def test_make_board_dimensions(self):
        actual = make_board(25, 25)
        self.assertTrue(len(actual.items()) == 625)

    def test_make_board_is_dictionary(self):
        actual = make_board(25, 25)
        self.assertIsInstance(actual, dict)

    def test_make_board_is_key_tuple(self):
        actual = make_board(25, 25)
        for key in actual.keys():
            self.assertIsInstance(key, tuple)

    def test_make_board_key_has_only_two_elements(self):
        actual = make_board(25, 25)
        for key in actual.keys():
            self.assertTrue(len(key) == 2)

    def test_make_board_coordinate_is_integer(self):
        actual = make_board(25, 25)
        for key in actual.keys():
            self.assertIs(type(key[0]), int)
            self.assertIs(type(key[1]), int)

    def test_make_board_coordinate_is_less_than_width_and_height(self):
        width = 25
        height = 25
        actual = make_board(width, height)
        for key in actual.keys():
            self.assertLess(key[0], width)
            self.assertLess(key[1], height)

    def test_make_board_descriptions_lv1_region(self):
        lv1_descriptions = ('Devil\'s toilet', 'Dark room', 'Barren land', 'Skeleton market', 'Dangerous kitchen')
        lv1_x_lower_bound = 0
        lv1_x_upper_bound = 10
        lv1_y_lower_bound = 0
        lv1_y_upper_bound = 10
        actual = make_board(25, 25)
        for row in range(lv1_y_lower_bound, lv1_y_upper_bound):
            for column in range(lv1_x_lower_bound, lv1_x_upper_bound):
                self.assertIn(actual[(column, row)], lv1_descriptions)

    def test_make_board_descriptions_lv2_region(self):
        lv2_descriptions = ('room of secret', 'room of death', 'room of devil', 'room of curse', 'room of chaos')
        lv2_x_lower_bound = 10
        lv2_x_upper_bound = 20
        lv2_y_lower_bound = 10
        lv2_y_upper_bound = 20
        actual = make_board(25, 25)
        for row in range(lv2_y_lower_bound, lv2_y_upper_bound):
            for column in range(lv2_x_lower_bound, lv2_x_upper_bound):
                self.assertIn(actual[(column, row)], lv2_descriptions)

    def test_make_board_descriptions_lv3_region(self):
        lv3_descriptions = ('Deathbed', 'Queen\'s nest', 'Blue mouth', 'Lucifer\'s hand', 'Vicious air')
        lv3_x_lower_bound = 20
        lv3_x_upper_bound = 25
        lv3_y_lower_bound = 20
        lv3_y_upper_bound = 25
        actual = make_board(25, 25)
        for row in range(lv3_y_lower_bound, lv3_y_upper_bound):
            for column in range(lv3_x_lower_bound, lv3_x_upper_bound):
                self.assertIn(actual[(column, row)], lv3_descriptions)
