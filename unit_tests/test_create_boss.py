import io
from unittest import TestCase
from unittest.mock import patch
from game import create_boss


class TestCreateBoss(TestCase):
    def test_create_boss_is_dictionary(self):
        character = {'name': "test name"}
        actual = create_boss(character)
        self.assertIsInstance(actual, dict)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_create_boss_display_explanation_to_user(self, mock_stdout):
        character = {'name': "test name"}
        create_boss(character)
        expected = f"{character['name']} encounter Black Magician\n" \
                   "Character level should be three to kill the boss\n" \
                   "Once you start the battle,y ou can't run away. This is a fight to the death.\n" \
                   "Do you want to fight or run way? \n" \
                   "Enter a number\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)
