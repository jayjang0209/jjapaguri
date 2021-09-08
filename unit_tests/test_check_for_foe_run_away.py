from unittest import TestCase
from game import check_for_foe_run_away


class TestCheckForFoeRunAway(TestCase):
    def test_check_for_foe_run_away_random_weight(self):
        roll_number = 1000000
        weight_ture = 0.2
        weight_false = 0.8
        result = [check_for_foe_run_away() for _ in range(roll_number)]
        expected_true_number = weight_ture
        expected_false_number = weight_false
        actual_true_number = result.count(True) / roll_number
        actual_false_number = result.count(False) / roll_number
        self.assertAlmostEqual(expected_true_number, actual_true_number, 2)
        self.assertAlmostEqual(expected_false_number, actual_false_number, 2)

    def test_check_for_foe_run_away_is_boolean(self):
        actual = check_for_foe_run_away()
        self.assertIsInstance(actual, bool)
