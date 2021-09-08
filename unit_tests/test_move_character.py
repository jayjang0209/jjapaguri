from unittest import TestCase
from game import move_character


class TestMoveCharacter(TestCase):
    def test_move_character_move_north(self):
        x_coord = 5
        y_coord = 5
        move_increment = 1
        character = {'x': x_coord, 'y': y_coord}
        user_choices = ('North', 'East', 'South', 'West')
        user_choose = 'North'
        choice_number = user_choices.index(user_choose)
        expected = {'x': x_coord, 'y': y_coord - move_increment}
        move_character(choice_number, character)
        actual = character
        self.assertEqual(actual, expected)

    def test_move_character_move_east(self):
        x_coord = 5
        y_coord = 5
        move_increment = 1
        character = {'x': x_coord, 'y': y_coord}
        user_choices = ('North', 'East', 'South', 'West')
        user_choose = 'East'
        choice_number = user_choices.index(user_choose)
        expected = {'x': x_coord + move_increment, 'y': y_coord}
        move_character(choice_number, character)
        actual = character
        self.assertEqual(actual, expected)

    def test_move_character_move_south(self):
        x_coord = 5
        y_coord = 5
        move_increment = 1
        character = {'x': x_coord, 'y': y_coord}
        user_choices = ('North', 'East', 'South', 'West')
        user_choose = 'South'
        choice_number = user_choices.index(user_choose)
        expected = {'x': x_coord, 'y': y_coord + move_increment}
        move_character(choice_number, character)
        actual = character
        self.assertEqual(actual, expected)

    def test_move_character_move_west(self):
        x_coord = 5
        y_coord = 5
        move_increment = 1
        character = {'x': x_coord, 'y': y_coord}
        user_choices = ('North', 'East', 'South', 'West')
        user_choose = 'West'
        choice_number = user_choices.index(user_choose)
        expected = {'x': x_coord - move_increment, 'y': y_coord}
        move_character(choice_number, character)
        actual = character
        self.assertEqual(actual, expected)
