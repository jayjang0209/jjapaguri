import io
from unittest import TestCase
from unittest.mock import patch
from game import character_attack_description


class TestCharacterAttackDescription(TestCase):
    @patch('random.randint', side_effect=[0])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_character_attack_description_sorcerer_lv1(self, mock_stdout, random_number_generator):
        level = 1
        character_class = 'Sorcerer'
        sorcerer_lv1_skill = ['fire ball', 'ice beam', 'water ball']
        character = {'name': 'player', 'hp': 20, 'max_hp': 20, 'level': level, 'class': character_class}
        foe = {'name': 'monster'}
        character_attack_description(character, foe)
        expected = f"{character['name']} used {sorcerer_lv1_skill[0]} to {foe['name']}\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)

    @patch('random.randint', side_effect=[0])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_character_attack_description_sorcerer_lv2(self, mock_stdout, random_number_generator):
        level = 2
        character_class = 'Sorcerer'
        sorcerer_lv2_skill = ['magic claw', 'blizzard', 'holy beam']
        character = {'name': 'player', 'hp': 20, 'max_hp': 20, 'level': level, 'class': character_class}
        foe = {'name': 'monster'}
        character_attack_description(character, foe)
        expected = f"{character['name']} used {sorcerer_lv2_skill[0]} to {foe['name']}\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)

    @patch('random.randint', side_effect=[0])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_character_attack_description_sorcerer_lv3(self, mock_stdout, random_number_generator):
        level = 3
        character_class = 'Sorcerer'
        sorcerer_lv3_skill = ['meteor', 'god bless', 'thunder storm']
        character = {'name': 'player', 'hp': 20, 'max_hp': 20, 'level': level, 'class': character_class}
        foe = {'name': 'monster'}
        character_attack_description(character, foe)
        expected = f"{character['name']} used {sorcerer_lv3_skill[0]} to {foe['name']}\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)

    @patch('random.randint', side_effect=[0])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_character_attack_description_thief_lv1(self, mock_stdout, random_number_generator):
        level = 1
        character_class = 'Thief'
        sorcerer_lv1_skill = ['fire in the hole', 'stabbing', 'nut cracking']
        character = {'name': 'player', 'hp': 20, 'max_hp': 20, 'level': level, 'class': character_class}
        foe = {'name': 'monster'}
        character_attack_description(character, foe)
        expected = f"{character['name']} used {sorcerer_lv1_skill[0]} to {foe['name']}\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)

    @patch('random.randint', side_effect=[0])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_character_attack_description_thief_lv2(self, mock_stdout, random_number_generator):
        level = 2
        character_class = 'Thief'
        sorcerer_lv2_skill = ['double attack', 'shadow punch', 'shuriken burst']
        character = {'name': 'player', 'hp': 20, 'max_hp': 20, 'level': level, 'class': character_class}
        foe = {'name': 'monster'}
        character_attack_description(character, foe)
        expected = f"{character['name']} used {sorcerer_lv2_skill[0]} to {foe['name']}\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)

    @patch('random.randint', side_effect=[0])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_character_attack_description_thief_lv3(self, mock_stdout, random_number_generator):
        level = 3
        character_class = 'Thief'
        sorcerer_lv3_skill = ['triple throw', 'dark flare', 'shadow knife']
        character = {'name': 'player', 'hp': 20, 'max_hp': 20, 'level': level, 'class': character_class}
        foe = {'name': 'monster'}
        character_attack_description(character, foe)
        expected = f"{character['name']} used {sorcerer_lv3_skill[0]} to {foe['name']}\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)

    @patch('random.randint', side_effect=[0])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_character_attack_description_bowman_lv1(self, mock_stdout, random_number_generator):
        level = 1
        character_class = 'Bowman'
        sorcerer_lv1_skill = ['double shot', 'bomb arrow', 'sling shot']
        character = {'name': 'player', 'hp': 20, 'max_hp': 20, 'level': level, 'class': character_class}
        foe = {'name': 'monster'}
        character_attack_description(character, foe)
        expected = f"{character['name']} used {sorcerer_lv1_skill[0]} to {foe['name']}\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)

    @patch('random.randint', side_effect=[0])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_character_attack_description_bowman_lv2(self, mock_stdout, random_number_generator):
        level = 2
        character_class = 'Bowman'
        sorcerer_lv2_skill = ['fire arrow', 'lightning arrow', 'crossbow shot']
        character = {'name': 'player', 'hp': 20, 'max_hp': 20, 'level': level, 'class': character_class}
        foe = {'name': 'monster'}
        character_attack_description(character, foe)
        expected = f"{character['name']} used {sorcerer_lv2_skill[0]} to {foe['name']}\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)

    @patch('random.randint', side_effect=[0])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_character_attack_description_bowman_lv3(self, mock_stdout, random_number_generator):
        level = 3
        character_class = 'Bowman'
        sorcerer_lv3_skill = ["Dragon breath", "bullseye shot", "terra ray"]
        character = {'name': 'player', 'hp': 20, 'max_hp': 20, 'level': level, 'class': character_class}
        foe = {'name': 'monster'}
        character_attack_description(character, foe)
        expected = f"{character['name']} used {sorcerer_lv3_skill[0]} to {foe['name']}\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)

    @patch('random.randint', side_effect=[0])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_character_attack_description_fighter_lv1(self, mock_stdout, random_number_generator):
        level = 1
        character_class = 'Fighter'
        sorcerer_lv1_skill = ['dirty boxing', 'low sweep', 'bat swing']
        character = {'name': 'player', 'hp': 20, 'max_hp': 20, 'level': level, 'class': character_class}
        foe = {'name': 'monster'}
        character_attack_description(character, foe)
        expected = f"{character['name']} used {sorcerer_lv1_skill[0]} to {foe['name']}\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)

    @patch('random.randint', side_effect=[0])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_character_attack_description_fighter_lv2(self, mock_stdout, random_number_generator):
        level = 2
        character_class = 'Fighter'
        sorcerer_lv2_skill = ['kendo slash', 'tornado kick', 'dragon sword']
        character = {'name': 'player', 'hp': 20, 'max_hp': 20, 'level': level, 'class': character_class}
        foe = {'name': 'monster'}
        character_attack_description(character, foe)
        expected = f"{character['name']} used {sorcerer_lv2_skill[0]} to {foe['name']}\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)

    @patch('random.randint', side_effect=[0])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_character_attack_description_fighter_lv3(self, mock_stdout, random_number_generator):
        level = 3
        character_class = 'Fighter'
        sorcerer_lv3_skill = ['sword dance', 'divine crash', 'critical hammer shot']
        character = {'name': 'player', 'hp': 20, 'max_hp': 20, 'level': level, 'class': character_class}
        foe = {'name': 'monster'}
        character_attack_description(character, foe)
        expected = f"{character['name']} used {sorcerer_lv3_skill[0]} to {foe['name']}\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)
