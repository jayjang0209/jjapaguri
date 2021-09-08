import unittest.mock
import io
from unittest import TestCase
from game import display_character_stats


class TestDisplayCharacterStats(TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_display_character_stats_sorcerer_lv1(self, mock_stdout):
        level = 1
        exp = 0
        max_hp = 15
        character_class = 'Sorcerer'
        class_names = ('Sorcerer', 'Cleric', 'Bishop')
        character = {'level': level, 'exp': exp, 'max_hp': max_hp, 'class': character_class, 'class_name': class_names}
        display_character_stats(character)
        expected = "Character's stats\n" \
                   "Level : 1\n" \
                   "Class name : Sorcerer\n" \
                   "Max HP: 15\n" \
                   "Min DP: 1, Max DP: 25\n" \
                   "Experience Point: 0\n" \
                   "Character's skills ['fire ball', 'ice beam', 'water ball']\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_display_character_stats_sorcerer_lv2(self, mock_stdout):
        level = 2
        exp = 600
        max_hp = 25
        character_class = 'Sorcerer'
        class_names = ('Sorcerer', 'Cleric', 'Bishop')
        character = {'level': level, 'exp': exp, 'max_hp': max_hp, 'class': character_class, 'class_name': class_names}
        display_character_stats(character)
        expected = "Character's stats\n" \
                   "Level : 2\n" \
                   "Class name : Cleric\n" \
                   "Max HP: 25\n" \
                   "Min DP: 1, Max DP: 30\n" \
                   "Experience Point: 600\n" \
                   "Character's skills ['magic claw', 'blizzard', 'holy beam']\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_display_character_stats_sorcerer_lv3(self, mock_stdout):
        level = 3
        exp = 1900
        max_hp = 40
        character_class = 'Sorcerer'
        class_names = ('Sorcerer', 'Cleric', 'Bishop')
        character = {'level': level, 'exp': exp, 'max_hp': max_hp, 'class': character_class, 'class_name': class_names}
        display_character_stats(character)
        expected = "Character's stats\n" \
                   "Level : 3\n" \
                   "Class name : Bishop\n" \
                   "Max HP: 40\n" \
                   "Min DP: 1, Max DP: 35\n" \
                   "Experience Point: 1900\n" \
                   "Character's skills ['meteor', 'god bless', 'thunder storm']\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_display_character_stats_thief_lv1(self, mock_stdout):
        level = 1
        exp = 0
        max_hp = 20
        character_class = 'Thief'
        class_names = ('Thief', 'Assassin', 'Night lord')
        character = {'level': level, 'exp': exp, 'max_hp': max_hp, 'class': character_class, 'class_name': class_names}
        display_character_stats(character)
        expected = "Character's stats\n" \
                   "Level : 1\n" \
                   "Class name : Thief\n" \
                   "Max HP: 20\n" \
                   "Min DP: 6, Max DP: 12\n" \
                   "Experience Point: 0\n" \
                   "Character's skills ['fire in the hole', 'stabbing', 'nut cracking']\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_display_character_stats_thief_lv2(self, mock_stdout):
        level = 2
        exp = 600
        max_hp = 30
        character_class = 'Thief'
        class_names = ('Thief', 'Assassin', 'Night lord')
        character = {'level': level, 'exp': exp, 'max_hp': max_hp, 'class': character_class, 'class_name': class_names}
        display_character_stats(character)
        expected = "Character's stats\n" \
                   "Level : 2\n" \
                   "Class name : Assassin\n" \
                   "Max HP: 30\n" \
                   "Min DP: 8, Max DP: 16\n" \
                   "Experience Point: 600\n" \
                   "Character's skills ['double attack', 'shadow punch', 'shuriken burst']\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_display_character_stats_thief_lv3(self, mock_stdout):
        level = 3
        exp = 1900
        max_hp = 45
        character_class = 'Thief'
        class_names = ('Thief', 'Assassin', 'Night lord')
        character = {'level': level, 'exp': exp, 'max_hp': max_hp, 'class': character_class, 'class_name': class_names}
        display_character_stats(character)
        expected = "Character's stats\n" \
                   "Level : 3\n" \
                   "Class name : Night lord\n" \
                   "Max HP: 45\n" \
                   "Min DP: 10, Max DP: 20\n" \
                   "Experience Point: 1900\n" \
                   "Character's skills ['triple throw', 'dark flare', 'shadow knife']\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_display_character_stats_bowman_lv1(self, mock_stdout):
        level = 1
        exp = 0
        max_hp = 20
        character_class = 'Bowman'
        class_names = ('Bowman', 'Hunter', 'Bow master')
        character = {'level': level, 'exp': exp, 'max_hp': max_hp, 'class': character_class, 'class_name': class_names}
        display_character_stats(character)
        expected = "Character's stats\n" \
                   "Level : 1\n" \
                   "Class name : Bowman\n" \
                   "Max HP: 20\n" \
                   "Min DP: 10, Max DP: 10\n" \
                   "Experience Point: 0\n" \
                   "Character's skills ['double shot', 'bomb arrow', 'sling shot']\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_display_character_stats_bowman_lv2(self, mock_stdout):
        level = 2
        exp = 600
        max_hp = 30
        character_class = 'Bowman'
        class_names = ('Bowman', 'Hunter', 'Bow master')
        character = {'level': level, 'exp': exp, 'max_hp': max_hp, 'class': character_class, 'class_name': class_names}
        display_character_stats(character)
        expected = "Character's stats\n" \
                   "Level : 2\n" \
                   "Class name : Hunter\n" \
                   "Max HP: 30\n" \
                   "Min DP: 12, Max DP: 12\n" \
                   "Experience Point: 600\n" \
                   "Character's skills ['fire arrow', 'lightning arrow', 'crossbow shot']\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_display_character_stats_bowman_lv3(self, mock_stdout):
        level = 3
        exp = 1900
        max_hp = 45
        character_class = 'Bowman'
        class_names = ('Bowman', 'Hunter', 'Bow master')
        character = {'level': level, 'exp': exp, 'max_hp': max_hp, 'class': character_class, 'class_name': class_names}
        display_character_stats(character)
        expected = "Character's stats\n" \
                   "Level : 3\n" \
                   "Class name : Bow master\n" \
                   "Max HP: 45\n" \
                   "Min DP: 14, Max DP: 14\n" \
                   "Experience Point: 1900\n" \
                   "Character\'s skills ['Dragon breath', 'bullseye shot', 'terra ray']\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_display_character_stats_fighter_lv1(self, mock_stdout):
        level = 1
        exp = 0
        max_hp = 25
        character_class = 'Fighter'
        class_names = ('Fighter', 'Warrior', 'Paladin')
        character = {'level': level, 'exp': exp, 'max_hp': max_hp, 'class': character_class,
                     'class_name': class_names}
        display_character_stats(character)
        expected = "Character's stats\n" \
                   "Level : 1\n" \
                   "Class name : Fighter\n" \
                   "Max HP: 25\n" \
                   "Min DP: 3, Max DP: 20\n" \
                   "Experience Point: 0\n" \
                   "Character's skills ['dirty boxing', 'low sweep', 'bat swing']\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_display_character_stats_fighter_lv2(self, mock_stdout):
        level = 2
        exp = 600
        max_hp = 35
        character_class = 'Fighter'
        class_names = ('Fighter', 'Warrior', 'Paladin')
        character = {'level': level, 'exp': exp, 'max_hp': max_hp, 'class': character_class,
                     'class_name': class_names}
        display_character_stats(character)
        expected = "Character's stats\n" \
                   "Level : 2\n" \
                   "Class name : Warrior\n" \
                   "Max HP: 35\n" \
                   "Min DP: 5, Max DP: 22\n" \
                   "Experience Point: 600\n" \
                   "Character's skills ['kendo slash', 'tornado kick', 'dragon sword']\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_display_character_stats_fighter_lv3(self, mock_stdout):
        level = 3
        exp = 1900
        max_hp = 50
        character_class = 'Fighter'
        class_names = ('Fighter', 'Warrior', 'Paladin')
        character = {'level': level, 'exp': exp, 'max_hp': max_hp, 'class': character_class,
                     'class_name': class_names}
        display_character_stats(character)
        expected = "Character's stats\n" \
                   "Level : 3\n" \
                   "Class name : Paladin\n" \
                   "Max HP: 50\n" \
                   "Min DP: 7, Max DP: 24\n" \
                   "Experience Point: 1900\n" \
                   "Character's skills ['sword dance', 'divine crash', 'critical hammer shot']\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)
