import io
from unittest import TestCase
from unittest.mock import patch
from game import check_for_level_up


class TestCheckForLevelUp(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_for_level_up_exp_kill_first_lev1_foe(self, mock_stdout):
        foe_level_1 = {'exp': 100}
        player = {'name': 'P', 'level': 1, 'hp': 20, 'max_hp': 20, 'exp': 100, 'class_name': ('S1', 'S2', 'S3'),
                  'class': 'Thief'}
        check_for_level_up(player, foe_level_1)
        actual = mock_stdout.getvalue()
        expected = "character earned exp:100. current exp:100\n"
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_for_level_up_exp_kill_first_lev2_foe(self, mock_stdout):
        foe_level_1 = {'exp': 200}
        player = {'name': 'P', 'level': 1, 'hp': 20, 'max_hp': 20, 'exp': 200, 'class_name': ('S1', 'S2', 'S3'),
                  'class': 'Thief'}
        check_for_level_up(player, foe_level_1)
        actual = mock_stdout.getvalue()
        expected = "character earned exp:200. current exp:200\n"
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_for_level_up_exp_kill_first_lev3_foe(self, mock_stdout):
        foe_level_1 = {'exp': 300}
        player = {'name': 'P', 'level': 1, 'hp': 20, 'max_hp': 20, 'exp': 300, 'class_name': ('S1', 'S2', 'S3'),
                  'class': 'Thief'}
        check_for_level_up(player, foe_level_1)
        actual = mock_stdout.getvalue()
        expected = "character earned exp:300. current exp:300\n"
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_for_level_up_lev1_exp_upper_bound(self, mock_stdout):
        foe_level_1 = {'exp': 100}
        player = {'name': 'P', 'level': 1, 'hp': 20, 'max_hp': 20, 'exp': 500, 'class_name': ('S1', 'S2', 'S3'),
                  'class': 'Thief'}
        check_for_level_up(player, foe_level_1)
        actual = mock_stdout.getvalue()
        expected = "character earned exp:100. current exp:500\n"
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_for_level_up_from_lev1_to_lev2(self, mock_stdout):
        foe_level_1 = {'exp': 100}
        player = {'name': 'P', 'level': 1, 'hp': 20, 'max_hp': 20, 'exp': 600, 'class_name': ('S1', 'S2', 'S3'),
                  'class': 'Thief'}
        check_for_level_up(player, foe_level_1)
        actual = mock_stdout.getvalue()
        expected = "character earned exp:100. current exp:600\n" \
                   "P level up to 2, became S2\n" \
                   "Character's stats\n" \
                   "Level : 2\n" \
                   "Class name : S2\n" \
                   "Max HP: 30\n" \
                   "Min DP: 8, Max DP: 16\n" \
                   "Experience Point: 600\n" \
                   "Character's skills ['double attack', 'shadow punch', 'shuriken burst']\n"
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_for_level_up_lev2_exp_lower_bound(self, mock_stdout):
        foe_level_1 = {'exp': 100}
        player = {'name': 'P', 'level': 2, 'hp': 20, 'max_hp': 20, 'exp': 700, 'class_name': ('S1', 'S2', 'S3'),
                  'class': 'Thief'}
        check_for_level_up(player, foe_level_1)
        actual = mock_stdout.getvalue()
        expected = "character earned exp:100. current exp:700\n"
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_for_level_up_lev2_exp_upper_bound(self, mock_stdout):
        foe_level_2 = {'exp': 200}
        player = {'name': 'P', 'level': 2, 'hp': 20, 'max_hp': 20, 'exp': 1700, 'class_name': ('S1', 'S2', 'S3'),
                  'class': 'Thief'}
        check_for_level_up(player, foe_level_2)
        actual = mock_stdout.getvalue()
        expected = "character earned exp:200. current exp:1700\n"
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_for_level_up_from_lev2_to_lev3(self, mock_stdout):
        foe_level_1 = {'exp': 300}
        player = {'name': 'P', 'level': 2, 'hp': 20, 'max_hp': 20, 'exp': 1800, 'class_name': ('S1', 'S2', 'S3'),
                  'class': 'Thief'}
        check_for_level_up(player, foe_level_1)
        actual = mock_stdout.getvalue()
        expected = "character earned exp:300. current exp:1800\n" \
                   "P level up to 3, became S3\n" \
                   "Character's stats\n" \
                   "Level : 3\n" \
                   "Class name : S3\n" \
                   "Max HP: 35\n" \
                   "Min DP: 10, Max DP: 20\n" \
                   "Experience Point: 1800\n" \
                   "Character's skills ['triple throw', 'dark flare', 'shadow knife']\n"
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_for_level_up_reached_max_level(self, mock_stdout):
        foe_level_3 = {'exp': 300}
        player = {'name': 'P', 'level': 3, 'hp': 20, 'max_hp': 20, 'exp': 190, 'class_name': ('S1', 'S2', 'S3'),
                  'class': 'Thief'}
        check_for_level_up(player, foe_level_3)
        actual = mock_stdout.getvalue()
        expected = ""
        self.assertEqual(actual, expected)
