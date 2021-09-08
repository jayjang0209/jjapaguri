import io
from unittest import TestCase
from unittest.mock import patch
from game import create_foe


class TestCreateFoe(TestCase):
    def test_create_foe_create_lev1_foe_names(self):
        lv1_foe_names = ('Mouse', 'Slime', 'Evil fairy', 'Skeleton soldier', 'Baby wyvern', 'Tiny dragon',
                         'Small devil', 'Infested bat')
        x_coord = 1
        y_coord = 1
        character = {'name': 'test', 'x': x_coord, 'y': y_coord}
        foe = create_foe(character)
        actual_name = foe['name']
        self.assertIn(actual_name, lv1_foe_names)

    def test_create_foe_create_lev2_foe_names(self):
        lv2_foe_names = ('White eyed cat', 'Deathly fairy', 'Cursed cockroach', 'Juvenile wyvern',
                         'Middle sized dragon', 'Zombie monkey', 'Intoxicated devil', 'Boogie man')
        x_coord = 15
        y_coord = 15
        character = {'name': 'test', 'x': x_coord, 'y': y_coord}
        foe = create_foe(character)
        actual_name = foe['name']
        self.assertIn(actual_name, lv2_foe_names)

    def test_create_foe_create_lev3_foe_names(self):
        lv3_foe_names = ('General skeleton', 'Devil queen', 'Moth man', 'Cursed elephant', 'Hell dog',
                         'Walking corpse', 'Red dragon', 'Black wyvern')
        x_coord = 21
        y_coord = 21
        character = {'name': 'test', 'x': x_coord, 'y': y_coord}
        foe = create_foe(character)
        actual_name = foe['name']
        self.assertIn(actual_name, lv3_foe_names)

    @patch('random.randint', return_value=1)  # FOE_NAMES_LV1()[1] == 'Slime'
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_create_foe_create_dispaly_current_situation(self, mock_stdout, mock_input):
        x_coord = 5
        y_coord = 5
        character = {'name': 'test', 'x': x_coord, 'y': y_coord}
        create_foe(character)
        expected = "test encounters Slime\n" \
                   "Do you want to fight or run way? \n" \
                   "Enter a number\n"
        actual = mock_stdout.getvalue()
        self.assertMultiLineEqual(actual, expected)

    @patch('random.randint', return_value=1)  # FOE_NAMES_LV1()[1] == 'Slime'
    def test_create_foe_create_lev1_foe(self, random_foe_name_generator):
        x_coord = 1
        y_coord = 1
        character = {'name': 'test', 'x': x_coord, 'y': y_coord}
        expected_name_randomly_generated = 'Slime'
        lev1_foe_max_hp = 10
        lev1_foe_exp = 100
        lev1_foe_min_dp = 1
        lev1_foe_max_dp = 7
        expected = {'name': expected_name_randomly_generated, 'hp': lev1_foe_max_hp, 'max_hp': lev1_foe_max_hp,
                    'exp': lev1_foe_exp, 'min_dp': lev1_foe_min_dp, 'max_dp': lev1_foe_max_dp}
        actual = create_foe(character)
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=1)  # FOE_NAMES_LV1()[1] == 'Slime'
    def test_create_foe_create_lev1_foe_board_x_upper_bound_when_y_is_zero(self, random_foe_name_generator):
        x_coord = 9
        y_coord = 0
        character = {'name': 'test', 'x': x_coord, 'y': y_coord}
        expected_name_randomly_generated = 'Slime'
        lev1_foe_max_hp = 10
        lev1_foe_exp = 100
        lev1_foe_min_dp = 1
        lev1_foe_max_dp = 7
        expected = {'name': expected_name_randomly_generated, 'hp': lev1_foe_max_hp, 'max_hp': lev1_foe_max_hp,
                    'exp': lev1_foe_exp, 'min_dp': lev1_foe_min_dp, 'max_dp': lev1_foe_max_dp}
        actual = create_foe(character)
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=1)  # FOE_NAMES_LV1()[1] == 'Slime'
    def test_create_foe_create_lev1_foe_board_y_upper_bound_when_x_is_zero(self, random_foe_name_generator):
        x_coord = 0
        y_coord = 9
        character = {'name': 'test', 'x': x_coord, 'y': y_coord}
        expected_name_randomly_generated = 'Slime'
        lev1_foe_max_hp = 10
        lev1_foe_exp = 100
        lev1_foe_min_dp = 1
        lev1_foe_max_dp = 7
        expected = {'name': expected_name_randomly_generated, 'hp': lev1_foe_max_hp, 'max_hp': lev1_foe_max_hp,
                    'exp': lev1_foe_exp, 'min_dp': lev1_foe_min_dp, 'max_dp': lev1_foe_max_dp}
        actual = create_foe(character)
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=1)  # FOE_NAMES_LV1()[1] == 'Slime'
    def test_create_foe_create_lev1_foe_board_region_x_and_y_upper_bound(self, random_foe_name_generator):
        x_coord = 9
        y_coord = 9
        character = {'name': 'test', 'x': x_coord, 'y': y_coord}
        expected_name_randomly_generated = 'Slime'
        lev1_foe_max_hp = 10
        lev1_foe_exp = 100
        lev1_foe_min_dp = 1
        lev1_foe_max_dp = 7
        expected = {'name': expected_name_randomly_generated, 'hp': lev1_foe_max_hp, 'max_hp': lev1_foe_max_hp,
                    'exp': lev1_foe_exp, 'min_dp': lev1_foe_min_dp, 'max_dp': lev1_foe_max_dp}
        actual = create_foe(character)
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=0)  # FOE_NAMES_LV2()[0] == 'White eyed cat'
    def test_create_foe_create_lev2_foe_board_x_lower_bound_when_y_is_zero(self, random_foe_name_generator):
        x_coord = 10
        y_coord = 0
        character = {'name': 'test', 'x': x_coord, 'y': y_coord}
        expected_name_randomly_generated = 'White eyed cat'
        lev2_foe_max_hp = 11
        lev2_foe_exp = 200
        lev2_foe_min_dp = 2
        lev2_foe_max_dp = 9
        expected = {'name': expected_name_randomly_generated, 'hp': lev2_foe_max_hp, 'max_hp': lev2_foe_max_hp,
                    'exp': lev2_foe_exp, 'min_dp': lev2_foe_min_dp, 'max_dp': lev2_foe_max_dp}
        actual = create_foe(character)
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=0)  # FOE_NAMES_LV2()[0] == 'White eyed cat'
    def test_create_foe_create_lev2_foe_board_x_upper_bound_when_y_is_zero(self, random_foe_name_generator):
        x_coord = 19
        y_coord = 0
        character = {'name': 'test', 'x': x_coord, 'y': y_coord}
        expected_name_randomly_generated = 'White eyed cat'
        lev2_foe_max_hp = 11
        lev2_foe_exp = 200
        lev2_foe_min_dp = 2
        lev2_foe_max_dp = 9
        expected = {'name': expected_name_randomly_generated, 'hp': lev2_foe_max_hp, 'max_hp': lev2_foe_max_hp,
                    'exp': lev2_foe_exp, 'min_dp': lev2_foe_min_dp, 'max_dp': lev2_foe_max_dp}
        actual = create_foe(character)
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=0)  # FOE_NAMES_LV2()[0] == 'White eyed cat'
    def test_create_foe_create_lev2_foe_y_lower_bound_when_x_is_zero(self, random_foe_name_generator):
        x_coord = 0
        y_coord = 10
        character = {'name': 'test', 'x': x_coord, 'y': y_coord}
        expected_name_randomly_generated = 'White eyed cat'
        lev2_foe_max_hp = 11
        lev2_foe_exp = 200
        lev2_foe_min_dp = 2
        lev2_foe_max_dp = 9
        expected = {'name': expected_name_randomly_generated, 'hp': lev2_foe_max_hp, 'max_hp': lev2_foe_max_hp,
                    'exp': lev2_foe_exp, 'min_dp': lev2_foe_min_dp, 'max_dp': lev2_foe_max_dp}
        actual = create_foe(character)
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=0)  # FOE_NAMES_LV2()[0] == 'White eyed cat'
    def test_create_foe_create_lev2_foe_y_upper_bound_when_x_is_zero(self, random_foe_name_generator):
        x_coord = 0
        y_coord = 19
        character = {'name': 'test', 'x': x_coord, 'y': y_coord}
        expected_name_randomly_generated = 'White eyed cat'
        lev2_foe_max_hp = 11
        lev2_foe_exp = 200
        lev2_foe_min_dp = 2
        lev2_foe_max_dp = 9
        expected = {'name': expected_name_randomly_generated, 'hp': lev2_foe_max_hp, 'max_hp': lev2_foe_max_hp,
                    'exp': lev2_foe_exp, 'min_dp': lev2_foe_min_dp, 'max_dp': lev2_foe_max_dp}
        actual = create_foe(character)
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=0)  # FOE_NAMES_LV2()[0] == 'White eyed cat'
    def test_create_foe_create_lev2_foe_board_x_y_upper_bound(self, random_foe_name_generator):
        x_coord = 19
        y_coord = 19
        character = {'name': 'test', 'x': x_coord, 'y': y_coord}
        expected_name_randomly_generated = 'White eyed cat'
        lev2_foe_max_hp = 11
        lev2_foe_exp = 200
        lev2_foe_min_dp = 2
        lev2_foe_max_dp = 9
        expected = {'name': expected_name_randomly_generated, 'hp': lev2_foe_max_hp, 'max_hp': lev2_foe_max_hp,
                    'exp': lev2_foe_exp, 'min_dp': lev2_foe_min_dp, 'max_dp': lev2_foe_max_dp}
        actual = create_foe(character)
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=3)  # FOE_NAMES_LV3()[3] == 'Cursed elephant'
    def test_create_foe_create_lev3_foe_board_x_lower_bound_when_y_is_zero(self, random_foe_name_generator):
        x_coord = 20
        y_coord = 0
        character = {'name': 'test', 'x': x_coord, 'y': y_coord}
        expected_name_randomly_generated = 'Cursed elephant'
        lev3_foe_max_hp = 13
        lev3_foe_exp = 300
        lev3_foe_min_dp = 3
        lev3_foe_max_dp = 11
        expected = {'name': expected_name_randomly_generated, 'hp': lev3_foe_max_hp, 'max_hp': lev3_foe_max_hp,
                    'exp': lev3_foe_exp, 'min_dp': lev3_foe_min_dp, 'max_dp': lev3_foe_max_dp}
        actual = create_foe(character)
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=3)  # FOE_NAMES_LV3()[3] == 'Cursed elephant'
    def test_create_foe_create_lev3_foe_board_x_upper_bound_when_y_is_zero(self, random_foe_name_generator):
        x_coord = 24
        y_coord = 0
        character = {'name': 'test', 'x': x_coord, 'y': y_coord}
        expected_name_randomly_generated = 'Cursed elephant'
        lev3_foe_max_hp = 13
        lev3_foe_exp = 300
        lev3_foe_min_dp = 3
        lev3_foe_max_dp = 11
        expected = {'name': expected_name_randomly_generated, 'hp': lev3_foe_max_hp, 'max_hp': lev3_foe_max_hp,
                    'exp': lev3_foe_exp, 'min_dp': lev3_foe_min_dp, 'max_dp': lev3_foe_max_dp}
        actual = create_foe(character)
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=3)  # FOE_NAMES_LV3()[3] == 'Cursed elephant'
    def test_create_foe_create_lev3_foe_board_y_lower_bound_when_x_is_zero(self, random_foe_name_generator):
        x_coord = 0
        y_coord = 20
        character = {'name': 'test', 'x': x_coord, 'y': y_coord}
        expected_name_randomly_generated = 'Cursed elephant'
        lev3_foe_max_hp = 13
        lev3_foe_exp = 300
        lev3_foe_min_dp = 3
        lev3_foe_max_dp = 11
        expected = {'name': expected_name_randomly_generated, 'hp': lev3_foe_max_hp, 'max_hp': lev3_foe_max_hp,
                    'exp': lev3_foe_exp, 'min_dp': lev3_foe_min_dp, 'max_dp': lev3_foe_max_dp}
        actual = create_foe(character)
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=3)  # FOE_NAMES_LV3()[3] == 'Cursed elephant'
    def test_create_foe_create_lev3_foe_board_y_upper_bound_when_x_is_zero(self, random_foe_name_generator):
        x_coord = 0
        y_coord = 24
        character = {'name': 'test', 'x': x_coord, 'y': y_coord}
        expected_name_randomly_generated = 'Cursed elephant'
        lev3_foe_max_hp = 13
        lev3_foe_exp = 300
        lev3_foe_min_dp = 3
        lev3_foe_max_dp = 11
        expected = {'name': expected_name_randomly_generated, 'hp': lev3_foe_max_hp, 'max_hp': lev3_foe_max_hp,
                    'exp': lev3_foe_exp, 'min_dp': lev3_foe_min_dp, 'max_dp': lev3_foe_max_dp}
        actual = create_foe(character)
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=3)  # FOE_NAMES_LV3()[3] == 'Cursed elephant'
    def test_create_foe_create_lev3_foe_board_boss_area_area_top_left_corner(self, random_foe_name_generator):
        x_coord = 20
        y_coord = 20
        character = {'name': 'test', 'x': x_coord, 'y': y_coord}
        expected_name_randomly_generated = 'Cursed elephant'
        lev3_foe_max_hp = 13
        lev3_foe_exp = 300
        lev3_foe_min_dp = 3
        lev3_foe_max_dp = 11
        expected = {'name': expected_name_randomly_generated, 'hp': lev3_foe_max_hp, 'max_hp': lev3_foe_max_hp,
                    'exp': lev3_foe_exp, 'min_dp': lev3_foe_min_dp, 'max_dp': lev3_foe_max_dp}
        actual = create_foe(character)
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=3)  # FOE_NAMES_LV3()[3] == 'Cursed elephant'
    def test_create_foe_create_lev3_foe_board_left_of_boss(self, random_foe_name_generator):
        x_coord = 23
        y_coord = 24
        character = {'name': 'test', 'x': x_coord, 'y': y_coord}
        expected_name_randomly_generated = 'Cursed elephant'
        lev3_foe_max_hp = 13
        lev3_foe_exp = 300
        lev3_foe_min_dp = 3
        lev3_foe_max_dp = 11
        expected = {'name': expected_name_randomly_generated, 'hp': lev3_foe_max_hp, 'max_hp': lev3_foe_max_hp,
                    'exp': lev3_foe_exp, 'min_dp': lev3_foe_min_dp, 'max_dp': lev3_foe_max_dp}
        actual = create_foe(character)
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=3)  # FOE_NAMES_LV3()[3] == 'Cursed elephant'
    def test_create_foe_create_lev3_foe_board_above_of_boss(self, random_foe_name_generator):
        x_coord = 24
        y_coord = 23
        character = {'name': 'test', 'x': x_coord, 'y': y_coord}
        expected_name_randomly_generated = 'Cursed elephant'
        lev3_foe_max_hp = 13
        lev3_foe_exp = 300
        lev3_foe_min_dp = 3
        lev3_foe_max_dp = 11
        expected = {'name': expected_name_randomly_generated, 'hp': lev3_foe_max_hp, 'max_hp': lev3_foe_max_hp,
                    'exp': lev3_foe_exp, 'min_dp': lev3_foe_min_dp, 'max_dp': lev3_foe_max_dp}
        actual = create_foe(character)
        self.assertEqual(actual, expected)
