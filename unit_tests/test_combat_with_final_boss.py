import io
from unittest import TestCase
from unittest.mock import patch
from game import combat_with_final_boss


class TestCombatWithFinalBoss(TestCase):
    @patch('builtins.input', side_effect=["1"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_with_final_boss_character_runaway_print(self, mock_stdout, mock_input):
        character = {'name': 'Test_name'}
        combat_with_final_boss(character)
        expected = f"{character['name']} encounter Black Magician\n" \
                   "Character level should be three to kill the boss\n" \
                   "Once you start the battle,y ou can't run away. This is a fight to the death.\n" \
                   "Do you want to fight or run way? \n" \
                   "Enter a number\n" \
                   """\033[31m
      |\___/|
     /       \ 
    |    /\__/|
    ||\  <.><.>
    | _     > )
     \   /----
      |   -\ 
     /      \ 
Black magician: Will you dare fight me, you petty bug?\033[0m\n""" \
                   "    \n" \
                   "-------------------------------------------\n" \
                   " MENU \n" \
                   " 0) : Fight\n" \
                   " 1) : Flee\n" \
                   "-------------------------------------------\n" \
                   "\n" \
                   "Your are the only hope. Please come back when you ready to fight\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=["1"])
    def test_combat_with_final_boss_character_runaway_return_game_status(self, mock_input):
        character = {'name': 'Test_name'}
        expected = 'game_ongoing'
        actual = combat_with_final_boss(character)
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=["0"])  # user choose to fight with boss
    @patch('random.randint', side_effect=[30, 90, 0, 20])  # foe strike first and character die
    def test_combat_with_final_boss_character_die(self, random_number_generator, mock_input):
        character = {'name': 'Player', 'class': 'Sorcerer', 'class_name': ('Sorcerer', 'Cleric', 'Bishop'), 'hp': 15,
                     'max_hp': 15, 'x': 0, 'y': 0, 'level': 1, 'exp': 0}
        expected = 'character_die'
        actual = combat_with_final_boss(character)
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=["0"])  # user choose to fight with boss
    @patch('random.randint', side_effect=[90, 30, 0, 50])  # foe strike first and character die
    def test_combat_with_final_boss_character_die(self, random_number_generator, mock_input):
        character = {'name': 'Player', 'class': 'Sorcerer', 'class_name': ('Sorcerer', 'Cleric', 'Bishop'), 'hp': 15,
                     'max_hp': 15, 'x': 0, 'y': 0, 'level': 1, 'exp': 0}
        expected = 'boss_die'
        actual = combat_with_final_boss(character)
        self.assertEqual(actual, expected)
