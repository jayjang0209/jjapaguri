import io
from unittest import TestCase
from unittest.mock import patch
from game import foe_attack_description


class TestFoeAttackDescription(TestCase):
    @patch('random.randint', return_value=0)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_foe_attack_description_first(self, mock_stdout, random_number_generator):
        foe_attacks = ('acid spray', 'fire ball', 'water blast', 'poison needle')
        foe = {'name': 'monster'}
        character = {'name': 'player', 'hp': 20, 'max_hp': 20}
        foe_attack_description(character, foe)
        expected = "monster used acid spray to player\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=1)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_foe_attack_description_second(self, mock_stdout, random_number_generator):
        foe_attacks = ('acid spray', 'fire ball', 'water blast', 'poison needle')
        foe = {'name': 'monster'}
        character = {'name': 'player', 'hp': 20, 'max_hp': 20}
        foe_attack_description(character, foe)
        expected = "monster used fire ball to player\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=2)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_foe_attack_description_third(self, mock_stdout, random_number_generator):
        foe_attacks = ('acid spray', 'fire ball', 'water blast', 'poison needle')
        foe = {'name': 'monster'}
        character = {'name': 'player', 'hp': 20, 'max_hp': 20}
        foe_attack_description(character, foe)
        expected = "monster used water blast to player\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=3)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_foe_attack_description_forth(self, mock_stdout, random_number_generator):
        foe_attacks = ('acid spray', 'fire ball', 'water blast', 'poison needle')
        foe = {'name': 'monster'}
        character = {'name': 'player', 'hp': 20, 'max_hp': 20}
        foe_attack_description(character, foe)
        expected = "monster used poison needle to player\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)
