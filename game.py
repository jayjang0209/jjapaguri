"""
Your name: Jonghoon Jang, Dongwan Kim
Your student number: A01240621, A01205697

A4
"""

import itertools
import random
import doctest
import time

# Game board constants


def WIDTH():
    """ Return width of the board.

    :return: return 25
    """
    return 25


def HEIGHT():
    """ Return height of the board.

    :return: return 25
    """
    return 25


def MINIMAP_SIDE():
    """ Return the side length of the minimap.

    :return: return 25
    """
    return 5


def X_LOWER_BOUND():
    """ Return x lower bound which is starting point zero.

    :return: return lower bound x zero
    """
    return 0


def Y_LOWER_BOUND():
    """ Return y lower bound which is starting point zero.

    :return: return lower bound y zero
    """
    return 0


def X_UPPER_BOUND():
    """ Return x upper bound which is ending point 24.

    :return: return upper bound 24
    """
    return 24


def Y_UPPER_BOUND():
    """ Return y upper bound which is ending point 24.

    :return: return upper bound 24
    """
    return 24


def LV_1_REGION_DESCRIPTIONS():
    """ Return descriptions for lv 1 region.

    :return: return a tuple of description of lv 1 region
    """
    return 'Devil\'s toilet', 'Dark room', 'Barren land', 'Skeleton market', 'Dangerous kitchen'


def LV_2_REGION_DESCRIPTIONS():
    """ Return descriptions for lv 2 region.

    :return: return a tuple of description of lv 2 region
    """
    return 'room of secret', 'room of death', 'room of devil', 'room of curse', 'room of chaos'


def LV_3_REGION_DESCRIPTIONS():
    """ Return descriptions for lv 3 region.

    :return: return a tuple of description of lv 3 region
    """
    return 'Deathbed', 'Queen\'s nest', 'Blue mouth', 'Lucifer\'s hand', 'Vicious air'


def COORDINATE_INCREMENT():
    """ Return coordinate increment when the character moves.

    :return: return coordinate increment
    """
    return 1


def MAX_COORD_LV_1():
    """ Return maximum coordinate which level 1 monsters appear.

    :return: return an integer 10
    """
    return 10


def MAX_COORD_LV_2():
    """ Return maximum coordinate which level 2 monsters appear.

    :return: return an integer 20
    """
    return 20


# Character constants
def MAX_HP():
    """ Return character's max hp.

    :return: return an integer 20
    """
    return 20


def HP_HEAL_INCREMENT():
    """ Return character's hp increment between encounters of foe.

    :return: return an integer 4
    """
    return 4


def MAX_HP_INCREMENT():
    """ Return character's max_hp increment when the character levels up.

    :return: return an integer 5
    """
    return 5


def HP_DIE():
    """ Return minimum hp when character dies.

    :return: return an integer 0
    """
    return 0


def PLAYER_CHOICES_MOVE():
    """ Return a tuple of character's move choice.

    :return: return a tuple
    """
    return 'North', 'East', 'South', 'West', 'Quit'


def PLAYER_CHOICES_FIGHT_FLEE():
    """ Return a tuple of character's choice fight or flee.

    :return: return a tuple
    """
    return 'Fight', 'Flee'


def PLAYER_CHOICES_CLASS():
    """ Return a tuple of four classes.

    :return: return a tuple
    """
    return 'Sorcerer', 'Thief', 'Bowman', 'Fighter'


def INITIAL_EXPERIENCE():
    """ Return initial experience points of character when start the game.

    :return: return an integer zero
    """
    return 0


def LV_2_EXPERIENCE_REQUIRED():
    """ Return the required experience points to become level two.

    :return: return an integer 600
    """
    return 600  # earn 100 exp when kill level 1 foe , # earn 200 exp when kill level 2 foe


def LV_3_EXPERIENCE_REQUIRED():
    """ Return the required experience points to become level three.

    :return: return an integer 1800
    """
    return 1800  # earn 300 exp when kill level 3 foe


def SORCERER():
    """ Return a dictionary which contains information of class sorcerer.

    :return: return a dictionary
    """
    return {'initial_hp': 15, 'initial_min_dp': 1, 'initial_max_dp': 25, 'class_names': ('Sorcerer', 'Cleric',
                                                                                         'Bishop')}


def SORCERER_SKILL():
    """ Return a dictionary which contains sorcerer's skills.

    :return: return a dictionary
    """
    return {'fire ball': 1, 'ice beam': 1, 'water ball': 1, 'magic claw': 2, 'blizzard': 2, 'holy beam': 2,
            'meteor': 3, 'god bless': 3, 'thunder storm': 3}


def THIEF():
    """ Return a dictionary which contains information of class thief.

    :return: return a dictionary
    """
    return {'initial_hp': 20, 'initial_min_dp': 6, 'initial_max_dp': 12, 'class_names': ('Thief', 'Assassin',
                                                                                         'Night lord')}


def THIEF_SKILL():
    """ Return a dictionary which contains thief's skills.

    :return: return a dictionary
    """
    return {'fire in the hole': 1, 'stabbing': 1, 'nut cracking': 1, 'double attack': 2, 'shadow punch': 2,
            'shuriken burst': 2, 'triple throw': 3, 'dark flare': 3, 'shadow knife': 3}


def BOWMAN():
    """ Return a dictionary which contains information of class bowman.

    :return: return a dictionary
    """
    return {'initial_hp': 20, 'initial_min_dp': 10, 'initial_max_dp': 10, 'class_names': ('Bowman', 'Hunter',
                                                                                          'Bow Master')}


def BOWMAN_SKILL():
    """ Return a dictionary which contains bowman's skills.

    :return: return a dictionary
    """
    return {'double shot': 1, 'bomb arrow': 1, 'sling shot': 1, 'fire arrow': 2, 'lightning arrow': 2,
            'crossbow shot': 2, 'Dragon breath': 3, 'bullseye shot': 3, 'terra ray': 3}


def FIGHTER():
    """ Return a dictionary which contains information of class fighter.

    :return: return a dictionary
    """
    return {'initial_hp': 25, 'initial_min_dp': 3, 'initial_max_dp': 20, 'class_names': ('Fighter', 'Warrior',
                                                                                         'Paladin')}


def FIGHTER_SKILL():
    """ Return a dictionary which contains fighter's skills.

    :return: return a dictionary
    """
    return {'dirty boxing': 1, 'low sweep': 1, 'bat swing': 1, 'kendo slash': 2, 'tornado kick': 2,
            'dragon sword': 2, 'sword dance': 3, 'divine crash': 3, 'critical hammer shot': 3}


def SORCERER_DP_FACTORS_MIN_MAX_INCREMENT_INITIAL():
    """ Return minimum damage point increment, maximum damage point increment, minimum initial damage points, maximum
        initial damage points of Sorcerer class.

    :return: return a tuple
    """
    return 0, 5, 1, 20


def THIEF_DP_FACTORS_MIN_MAX_INCREMENT_INITIAL():
    """ Return minimum damage point increment, maximum damage point increment, minimum initial damage points, maximum
        initial damage points of Thief class.

    :return: return a tuple
    """
    return 2, 4, 4, 8


def BOWMAN_DP_FACTORS_MIN_MAX_INCREMENT_INITIAL():
    """ Return minimum damage point increment, maximum damage point increment, minimum initial damage points, maximum
        initial damage points of Bowman class.

    :return: return a tuple
    """
    return 2, 2, 8, 8


def FIGHTER_DP_FACTORS_MIN_MAX_INCREMENT_INITIAL():
    """ Return minimum damage point increment, maximum damage point increment, minimum initial damage points, maximum
        initial damage points of Fighter class.

    :return: return a tuple
    """
    return 2, 2, 1, 18


# Foe Constatns
def FOE_MAX_HP_LV1():
    """ Return max hp of level one monster.

    :return: return an integer 10
    """
    return 10


def FOE_MAX_HP_LV2():
    """ Return max hp of level two monster.

    :return: return an integer 11
    """
    return 11


def FOE_MAX_HP_LV3():
    """ Return max hp of level three monster.

    :return: return an integer 13
    """
    return 13


def FOE_DP_LV1():
    """ Return minimum and maximum damage point of level one monster.

    :return: return a tuple
    """
    return 1, 7


def FOE_DP_LV2():
    """ Return minimum and maximum damage point of level two monster.

    :return: return a tuple
    """
    return 2, 9


def FOE_DP_LV3():
    """ Return minimum and maximum damage point of level three monster.

    :return: return a tuple
    """
    return 3, 11


def FOE_LV1_EXP():
    """ Return experience points of level one monster.

    :return: return an integer 100
    """
    return 100


def FOE_LV2_EXP():
    """ Return experience points of level two monster.

    :return: return an integer 200
    """
    return 200


def FOE_LV3_EXP():
    """ Return experience points of level three monster.

    :return: return an integer 300
    """
    return 300


def FOE_NAMES_LV1():
    """ Return names of level one monsters.

    :return: return a tuple
    """
    return (
        'Mouse', 'Slime', 'Evil fairy', 'Skeleton soldier', 'Baby wyvern', 'Tiny dragon', 'Small devil',
        'Infested bat')


def FOE_NAMES_LV2():
    """ Return names of level two monsters.

    :return: return a tuple
    """
    return (
        'White eyed cat', 'Deathly fairy', 'Cursed cockroach', 'Juvenile wyvern', 'Middle sized dragon',
        'Zombie monkey', 'Intoxicated devil', 'Boogie man')


def FOE_NAMES_LV3():
    """ Return names of level three monsters.

    :return: return a tuple
    """
    return (
        'General skeleton', 'Devil queen', 'Moth man', 'Cursed elephant', 'Hell dog', 'Walking corpse', 'Red dragon',
        'Black wyvern')


def FOE_ATTACK_DESCRIPTIONS():
    """ Return the types of attack which are used by foe.

    :return: return a tuple
    """
    return 'acid spray', 'fire ball', 'water blast', 'poison needle'


# Boss constants
def FOE_BOSS_NAME():
    """ Return a name of boss monster.

    :return: return a string
    """
    return 'Black Magician'


def FOE_BOSS_MAX_HP():
    """ Return a maximum hp of boss monster.
    :return: return an integer
    """
    return 40


def BOSS_MIN_MAX_DP():
    """ Return minimum and maximum damage points of boss monster.

    :return: return a tuple
    """
    return 5, 15


def BOSS_LOCATION():
    """ Return the location(x coordinate and y coordinate) of boss monster.

    :return: return a tuple
    """
    return 24, 24


# fight and flee
def COMBAT_ROLL_LOWER():
    """ Return minimum roll number which is one.

    :return: return minimum dice number one
    """
    return 1


def COMBAT_ROLL_UPPER():
    """ Return maximum roll number which is one hundred.

    :return: return maximum dice number one hundred
    """
    return 100


def CHANCE_ENCOUNTER_FOE():
    """ Return 20 which is the chance to encounter an enemy.

    :return: return 20
    """
    return 20


def CHANCE_FOE_STAB_BACK():
    """ Return 20 which is the chance to be attacked in the back by an enemy.

    :return: return 20
    """
    return 20


def CHANCE_FOE_RUNAWAY():
    """ Return the chance of foe running away.

    :return: return an integer
    """
    return 20


def FOE_STAB_BACK_MINIMUM_DAMAGE():
    """ Return the minimum damage when foe stab back.

    :return: return an integer
    """
    return 1


def FOE_STAB_BACK_MAXIMUM_DAMAGE():
    """ Return the maximum damage when foe stab back.

    :return: return an integer
    """
    return 4


def display_game_intro():
    """Display game intro.

    A simple function that print an introduction of the game
    """
    print('\t\t\t\t\t\t\t\t', end='')
    for word in map(str.strip, str.upper("welcome to Busania")):
        time.sleep(0.01)
        print('\033[1;33m'+word+'\033[0m', end=' ')
    print()
    print('\n\t\t\t\t\t\t\t\t\t ', "\033[1;30;43m✨Single User Dungeon✨\033[0m")
    print()
    time.sleep(0.5)
    print("\033[1;30;43m---------------------------------------------INTRO"
          "-------------------------------------------------\033[0m")
    print("\033[1;33mIn the BCIT dimension, there is a great kingdom whose name is Busania\033[0m")
    print("\033[1;33mLocated in the southern part of Korean peninsula, Busania was very beautiful and "
          "peaceful kingdom\033[0m")
    print("\033[1;33mOne day, a bad black magician staged a coup to take over the kingdom\033[0m")
    print("\033[1;33mHe summoned a dungeon from hell on the central part of the kingdom\033[0m")
    print("\033[1;33mVicious monsters from dungeon are killing innocent citizens in Busania\033[0m")
    print("\033[1;33mYou are the only hope to kill the black magician and save Busania\033[0m")
    print("\033[1;33m⚔️Are you ready to go into the dungeon? 🏹\033[0m")
    print("\033[1;30;43m---------------------------------------------------------------------------"
          "------------------------\033[0m")


def game_ending_message(status: str):
    """Display game ending message.

    A simple function that print an ending of the game

    :param status: an string
    :precondition: status must be one of string of 'user_choose_quit', 'achieved_goal'
    :postcondition: display ending message based on character's status

    >>> game_status = 'user_choose_quit'
    >>> game_ending_message(game_status)
    \033[31mYou quit the game. Your are the only hope. Please come back🙋🏻‍♂️\033[0m
    >>> game_status = 'character_die'
    >>> game_ending_message(game_status)
    \033[31mSorry, Your character is dead🤦🏻‍♂️\033[0m
    """
    if status == 'user_choose_quit':
        print("\033[31mYou quit the game. Your are the only hope. Please come back🙋🏻‍♂️\033[0m")
    elif status == 'boss_die':
        goal_achieved_message()
    else:
        print("\033[31mSorry, Your character is dead🤦🏻‍♂️\033[0m")


def goal_achieved_message():
    """ Print ending message when kill the boss.

    :postcondition: print ending message and ascii art
    """
    print("Congratulation!! You defeated a black magician!!")
    print('You saved Busania! Busania becomes peaceful!')
    time.sleep(2)
    print("""\033[33m
    
                               ____                       ____
                              |####|_   _   _   _   _   _|####|
     _    __    __    _       |####| '-' '-' '-' '-' '-' |####|
    |#|__|##|__|##|__|#|      |====|=====================|====|       O
    |__|__|__[]__|__|__|      `.###|'._.'._.'._.'._.'._.'|###.'      /#\ 
    |_|__|__|__|__|__|_|        `.#|OoOOooOoOOoOoOOooOoOO|#.'       /###\ 
     \================/ _   _   _ \=======================/ _   _  /_####\ 
      \ ._.'.__.'._.'/_| |_| |_| |_|     _               |_| |_| |_| |####\ 
       |    .--.    |==============|   .'|'.       _     |===========/#####\ 
       |    |  |    |OOoOOOooOooOoo|   |-+-|     .'|'.   |OOoOOOOoO||=====|
       |    |__|    |oOoooOoOOOoOoO|   |_|_|     |-+-|   |oOooOooOo|| .-. |
       |    ====    |==============|   =====     |_|_|   |=========|| | | |       
       |            |'._.'.__.'._.'|             =====   |'._.'._.'|| | | |
      [==============]         .--[=======================]--.     || |_| |
       |._.'.__.'._.|      _    `.[=======================].' .-.  || === |
       |            |    .'|'.     ||.-.    _.o._    .-.||    | |  ||     |
       |            |    |-+-|     ||| |  _)  =  (_  | |||    | |  ||======]
       |    .--.    |    |_|_|     ||| |  )  ~@~  (  | |||    |_|  ||####.`
       |    |  |    |    =====     |||_|   \  =  /   |_|||    ===  ||##.'
       |    |__|    |              ||===    '._.'    ===||         ||.'
       |    ====    |==============|| _________________ ||=========||
       |            |'._.'.__.'._.'||[_________________]||'._.'._.'||
      [==============]   _    _    || ]| /    |    \ |[ ||    _    ||
       \============|  .'|'..'|'.  || ]|/     |     \|[ ||  .'|'.  ||
        \___________|  |-+-||-+-|  || ]|      |      |[ ||  |-+-|  ||
           ||          |_|_||_|_|  || ]|      |      |[ ||  |_|_|  ||
           ||          ==========  || ]|     ~|~     |[ ||  =====  ||
       ,,  ||                      || ]|      |      |[ ||         ||  ,,
      ,;;,[======================,,|| ]|      |      |[ ||,,=========],;;,
     ,;;;;,||OooOOOooOoOoooOooOO,;;,|_]|______|______|[_|,;;,OoOoOo||,;;;;,
     .----.||OooOoOooOooOoOoOOo,;;;;,/_________________\,;;;;,OOolc||.----.
     '.__.'====================.----.[_________________].----.======='.__.'
     [_________________________'.__.'/                 \ .__.'____________]
                               [____]                   [____]
    \033[0m""")
    time.sleep(1.5)
    print("""\033[31m
        __  ___          __        __         
       /  |/  /___ _____/ /__     / /_  __  __
      / /|_/ / __ `/ __  / _ \   / __ \/ / / /
     / /  / / /_/ / /_/ /  __/  / /_/ / /_/ / 
    /_/  /_/\__,_/\__,_/\___/  /_.___/\__, /  
                                     /____/   
    """)
    time.sleep(2)
    print("""                             
           __    _____    ____  ___   ________  ______  ____
          / /   / /   |  / __ \/   | / ____/ / / / __ \/  _/
     __  / /_  / / /| | / /_/ / /| |/ / __/ / / / /_/ // /  
    / /_/ / /_/ / ___ |/ ____/ ___ / /_/ / /_/ / _, _// /   
    \____/\____/_/  |_/_/   /_/  |_\____/\____/_/ |_/___/   

    """)


def boss_ascii():
    """ Print ascii art of boss monster.

    :postcondition: print ascii art
    """
    print("""\033[31m
      |\___/|
     /       \ 
    |    /\__/|
    ||\  <.><.>
    | _     > )
     \   /----
      |   -\ 
     /      \ 
Black magician: Will you dare fight me, you petty bug?\033[0m
    """)


def make_board(width: int, height: int) -> {tuple[int, int]: str}:
    """Create game board with with x coordinate in the range [0, width) and y coordinate in the range [0, height).

    A simple function that returns a dictionary of game board with the width by the height

    :param width: an integer
    :param height: an integer
    :precondition: width and height must be a positive integer
    :postcondition: return a dictionary containing tuples with x coordinate in the range [0, width) and y coordinate
                    in the range [0, height) as a key, and location descriptions as a value
    :postcondition: assign location descriptions randomly from the Constant LV_1_REGION_DESCRIPTIONS if
                    x coordinate and y coordinate are less than 10
    :postcondition: assign location descriptions randomly from the Constant LV_2_REGION_DESCRIPTIONS if
                    x coordinate and y coordinate are greater than 10 and less than 20
    :postcondition: assign location descriptions randomly from the Constant LV_3_REGION_DESCRIPTIONS if
                    x coordinate and y coordinate are greater than 20
    :return: dictionary of game board with x in the range [0, width) y in the range [0, height)
    """
    board_coordinates = {(row, column): "description" for row in range(width) for column in range(height)}
    for key in board_coordinates.keys():
        if key[0] < MAX_COORD_LV_1() and key[1] < MAX_COORD_LV_1():  # level 1 region: 0 <= x < 10, 0 <= y < 10.
            board_coordinates[key] = random.choice(LV_1_REGION_DESCRIPTIONS())
        elif key[0] < MAX_COORD_LV_2() and key[1] < MAX_COORD_LV_2():  # level 2:   10 <= x < 20, 10 <= y < 20.
            board_coordinates[key] = random.choice(LV_2_REGION_DESCRIPTIONS())
        else:  # level 3 region in the range 20 <= x < 25, 20 <= y < 25.
            board_coordinates[key] = random.choice(LV_3_REGION_DESCRIPTIONS())
    return board_coordinates


def dispaly_character_class_information():
    """ Display information of four classes.

    :postcondition: print class information

    >>> dispaly_character_class_information() #doctest: +NORMALIZE_WHITESPACE
    You can choose one class out of these options
    '\033[31mSorcerer\033[0m' info: class-evolution-root: ('Sorcerer', 'Cleric', 'Bishop'), initial_hp: 15, Damage Point
     range: lv.1[1,25] lv.2[1,30] lv.3[1,35]
    Sorcerer class skill list:  ['fire ball', 'ice beam', 'water ball', 'magic claw', 'blizzard', 'holy beam', 'meteor',
     'god bless', 'thunder storm']
    '\033[31mThief\033[0m' info: class-evolution-root: ('Thief', 'Assassin', 'Night lord'), initial_hp: 20, Damage Point
     range: lv.1[6,12] lv.2[8,16] lv.3[10,20]
    Thief class skill list:  ['fire in the hole', 'stabbing', 'nut cracking', 'double attack', 'shadow punch', 'shuriken
     burst', 'triple throw', 'dark flare', 'shadow knife']
    '\033[31mBowman\033[0m' info: class-evolution-root: ('Bowman', 'Hunter', 'Bow Master'), initial_hp: 20, Damage Point
     range: lv.1[10,10] lv.2[12,12] lv.3[14,14]
    Bowman class skill list:  ['double shot', 'bomb arrow', 'sling shot', 'fire arrow', 'lightning arrow', 'crossbow
    shot', 'Dragon breath', 'bullseye shot', 'terra ray']
    '\033[31mFighter\033[0m' info: class-evolution-root: ('Fighter', 'Warrior', 'Paladin'), initial_hp: 25, Damage Point
     range: lv.1[3,20] lv.2[5,22] lv.3[7,24]
    Fighter class skill list:  ['dirty boxing', 'low sweep', 'bat swing', 'kendo slash', 'tornado kick', 'dragon sword',
     'sword dance', 'divine crash', 'critical hammer shot']
    """
    print('You can choose one class out of these options')
    print(f"'\033[31mSorcerer\033[0m' info: class-evolution-root: {SORCERER().get('class_names')}"
          f", initial_hp: {SORCERER().get('initial_hp')}, Damage Point range: lv.1[1,25] lv.2[1,30] lv.3[1,35]")
    print("Sorcerer class skill list: ", list(SORCERER_SKILL().keys()))
    print(f"'\033[31mThief\033[0m' info: class-evolution-root: {THIEF().get('class_names')}"
          f", initial_hp: {THIEF().get('initial_hp')}, Damage Point range: lv.1[6,12] lv.2[8,16] lv.3[10,20]")
    print("Thief class skill list: ", list(THIEF_SKILL().keys()))
    print(f"'\033[31mBowman\033[0m' info: class-evolution-root: {BOWMAN().get('class_names')}"
          f", initial_hp: {BOWMAN().get('initial_hp')}, Damage Point range: lv.1[10,10] lv.2[12,12] lv.3[14,14]")
    print("Bowman class skill list: ", list(BOWMAN_SKILL().keys()))
    print(f"'\033[31mFighter\033[0m' info: class-evolution-root: {FIGHTER().get('class_names')}"
          f", initial_hp: {FIGHTER().get('initial_hp')}, Damage Point range: lv.1[3,20] lv.2[5,22] lv.3[7,24]")
    print("Fighter class skill list: ", list(FIGHTER_SKILL().keys()))


def make_character() -> dict:
    """Creat a new character for user to play the game.

    A simple function that returns a dictionary of character information after accepting user input as character's name

    :precondition: prompt the user to input name
    :postcondition: return a dictionary containing character's info
    :return: dictionary containing character's information of name, class, class name, hp, max hp, x-coordinate
                                                                                     , y-coordinate, level and exp
    """
    print("\033[1;33m--------------------------------It is time to create your character-------------------------------"
          "-")
    character = {'name': input("Enter your character name "), 'class': None, 'class_name': None, 'hp': None,
                 'max_hp': None, 'x': X_LOWER_BOUND(), 'y': Y_LOWER_BOUND(), 'level': 1, 'exp': INITIAL_EXPERIENCE()}
    dispaly_character_class_information()
    set_up_character_stats_by_class(character)
    print(f"\033[1;33mCharacter created successfully. Class: \033[1;30;45m{character['class']}\033[0m\033[1;33m, "
          f"Name: \033[1;30;45m{character['name']}\033[0m")
    print()
    return character


def set_up_character_stats_by_class(character: dict):
    """ set character's stats based on the class chosen by the user

    :param character: a dictionary which contains character's information of name, class, class name, hp, max hp
                                                                     , x-coordinate, y-coordinate, level and exp
    :precondition:  a parameter character should be a dictionary
    :postcondition: set character's stats based on the class chosen by the user
    """
    class_name = get_user_choice(PLAYER_CHOICES_CLASS())
    if class_name == PLAYER_CHOICES_CLASS().index('Sorcerer'):
        character['hp'], character['max_hp'], character['class'], character['class_name'] = \
            SORCERER()['initial_hp'], SORCERER()['initial_hp'], PLAYER_CHOICES_CLASS()[0], SORCERER()['class_names']
    elif class_name == PLAYER_CHOICES_CLASS().index('Thief'):
        character['hp'], character['max_hp'], character['class'], character['class_name'] = \
            THIEF()['initial_hp'], THIEF()['initial_hp'], PLAYER_CHOICES_CLASS()[1], THIEF()['class_names']
    elif class_name == PLAYER_CHOICES_CLASS().index('Bowman'):
        character['hp'], character['max_hp'], character['class'], character['class_name'] = \
            BOWMAN()['initial_hp'], BOWMAN()['initial_hp'], PLAYER_CHOICES_CLASS()[2], BOWMAN()['class_names']
    else:
        character['hp'], character['max_hp'], character['class'], character['class_name'] = \
            FIGHTER()['initial_hp'], FIGHTER()['initial_hp'], PLAYER_CHOICES_CLASS()[3], FIGHTER()['class_names']


def display_character_stats(character: dict):
    """ Show character's stats.

    A simple function which displays characters stats like level, class name, hp, dp, exp and skills

    :param character: a dictionary
    :precondition: character should be a dictionary containing character information
    :postcondition: print character's stats

    >>> char = {'level': 1, 'exp':100,'max_hp': 20,  'class': 'Sorcerer' ,'class_name':('Sorcerer', 'Cleric',\
     'Bishop')}
    >>> display_character_stats(char)
    Character's stats
    Level : 1
    Class name : Sorcerer
    Max HP: 20
    Min DP: 1, Max DP: 25
    Experience Point: 100
    Character's skills ['fire ball', 'ice beam', 'water ball']
    >>> char = {'level': 2, 'exp':800,'max_hp': 20,  'class': 'Thief' ,'class_name':('Thief', 'Assassin',\
     'Night lord')}
    >>> display_character_stats(char)
    Character's stats
    Level : 2
    Class name : Assassin
    Max HP: 20
    Min DP: 8, Max DP: 16
    Experience Point: 800
    Character's skills ['double attack', 'shadow punch', 'shuriken burst']
    >>> char = {'level': 3, 'exp':1900,'max_hp': 20,  'class': 'Bowman' ,'class_name':('Bowman', 'Hunter',\
     'Bow master')}
    >>> display_character_stats(char)
    Character's stats
    Level : 3
    Class name : Bow master
    Max HP: 20
    Min DP: 14, Max DP: 14
    Experience Point: 1900
    Character's skills ['Dragon breath', 'bullseye shot', 'terra ray']
    >>> char = {'level': 1, 'exp':100,'max_hp': 20,  'class': 'Fighter' ,'class_name':('Fighter', 'Warrior',\
     'Paladin')}
    >>> display_character_stats(char)
    Character's stats
    Level : 1
    Class name : Fighter
    Max HP: 20
    Min DP: 3, Max DP: 20
    Experience Point: 100
    Character's skills ['dirty boxing', 'low sweep', 'bat swing']
    """
    print("Character's stats", f"Level : {character['level']}", sep='\n')
    print(f"Class name : {character['class_name'][character['level'] - 1]}")
    print(f"Max HP: {character['max_hp']}")
    print(f"Min DP: {character_damage_points(character)[0]}, Max DP: {character_damage_points(character)[1]}")
    print(f"Experience Point: {character['exp']}")
    print(f"Character's skills", end=' ')
    if character['class'] == PLAYER_CHOICES_CLASS()[0]:
        skills = [pair[0] for pair in SORCERER_SKILL().items() if pair[1] == character['level']]
    elif character['class'] == PLAYER_CHOICES_CLASS()[1]:
        skills = [pair[0] for pair in THIEF_SKILL().items() if pair[1] == character['level']]
    elif character['class'] == PLAYER_CHOICES_CLASS()[2]:
        skills = [pair[0] for pair in BOWMAN_SKILL().items() if pair[1] == character['level']]
    else:
        skills = [pair[0] for pair in FIGHTER_SKILL().items() if pair[1] == character['level']]
    print(skills)


def display_location(board: dict, character: dict):
    """Print location descriptions, x and y coordinates of character's current location.

    :param board: a dictionary
    :param character: a dictionary
    :precondition: board must be a dictionary with a tuple containing x, y coordinates as key and a string of location
                description
    :precondition: character must be a dictionary with 'x', 'y' keys and x, y coordinates as a value
    :postcondition: print correct location descriptions and x, y coordinates of character's current location
    :postcondition: print the map which shows a visualised location of character and region description

    >>> game_board = {(0, 0): 'test0'}
    >>> game_character = {'name': 'test', 'hp': 20, 'x': 0, 'y': 0}
    >>> display_location(game_board, game_character)
    ############ current area ###########
    ------------ Level 1 area -----------
    test0
    your current coordinates: X- 0,  Y- 0
    [@][ ][ ][ ][ ]
    [ ][ ][ ][ ][ ]
    [ ][ ][ ][ ][ ]
    [ ][ ][ ][ ][ ]
    [ ][ ][ ][ ][ ]
    #####################################
    >>> game_board = {(7, 7): 'test1'}
    >>> game_character = {'name': 'test', 'hp': 20, 'x': 7, 'y': 7}
    >>> display_location(game_board, game_character)
    ############ current area ###########
    ------------ Level 1 area -----------
    test1
    your current coordinates: X- 7,  Y- 7
    [ ][ ][ ][ ][ ]
    [ ][ ][ ][ ][ ]
    [ ][ ][@][ ][ ]
    [ ][ ][ ][ ][ ]
    [ ][ ][ ][ ][ ]
    #####################################
    >>> game_board = {(23, 15): 'test2'}
    >>> game_character = {'name': 'test', 'hp': 20, 'x': 23, 'y': 15}
    >>> display_location(game_board, game_character)
    ############ current area ###########
    ------------ Level 3 area -----------
    test2
    your current coordinates: X- 23,  Y- 15
    [ ][ ][ ][@][ ]
    [ ][ ][ ][ ][ ]
    [ ][ ][ ][ ][ ]
    [ ][ ][ ][ ][ ]
    [ ][ ][ ][ ][ ]
    #####################################
    >>> game_board = {(20, 20): 'test3'}
    >>> game_character = {'name': 'test', 'hp': 20, 'x': 20, 'y': 20}
    >>> display_location(game_board, game_character)
    ############ current area ###########
    ------------ Level 3 area -----------
    test3
    your current coordinates: X- 20,  Y- 20
    [@][ ][ ][ ][ ]
    [ ][ ][ ][ ][ ]
    [ ][ ][ ][ ][ ]
    [ ][ ][ ][ ][ ]
    [ ][ ][ ][ ][B]
    #####################################
    """
    if character['x'] < MAX_COORD_LV_1() and character['y'] < MAX_COORD_LV_1():
        region = 'Level 1 area'
    elif character['x'] < MAX_COORD_LV_2() and character['y'] < MAX_COORD_LV_2():
        region = 'Level 2 area'
    else:
        region = 'Level 3 area'
    print('############ current area ###########')
    print(f'------------ {region} -----------')
    print(board[(character['x'], character['y'])])
    print(f"your current coordinates: X- {character['x']},  Y- {character['y']}")
    display_mini_map(character)
    print('#####################################')


def display_mini_map(character: dict):
    """ Pring minimap which shows character's location.

    :param character: a dictionary
    :precondition: character must be a dictionary containing x, y as key and an integer a value
    :postcondition: print minimap which shows character's current x, y-coordinate and location

    >>> game_character = {'x': 0, 'y': 0}
    >>> display_mini_map(game_character)
    [@][ ][ ][ ][ ]
    [ ][ ][ ][ ][ ]
    [ ][ ][ ][ ][ ]
    [ ][ ][ ][ ][ ]
    [ ][ ][ ][ ][ ]
    >>> game_character = {'x': 7, 'y': 7}
    >>> display_mini_map(game_character)
    [ ][ ][ ][ ][ ]
    [ ][ ][ ][ ][ ]
    [ ][ ][@][ ][ ]
    [ ][ ][ ][ ][ ]
    [ ][ ][ ][ ][ ]
    >>> game_character = {'x': 23, 'y': 15}
    >>> display_mini_map(game_character)
    [ ][ ][ ][@][ ]
    [ ][ ][ ][ ][ ]
    [ ][ ][ ][ ][ ]
    [ ][ ][ ][ ][ ]
    [ ][ ][ ][ ][ ]
    >>> game_character = {'x': 20, 'y': 20}
    >>> display_mini_map(game_character)
    [@][ ][ ][ ][ ]
    [ ][ ][ ][ ][ ]
    [ ][ ][ ][ ][ ]
    [ ][ ][ ][ ][ ]
    [ ][ ][ ][ ][B]
    """
    location = (character['x'], character['y'])
    for column in range(MINIMAP_SIDE()):  # MINIMAP_SIDE() == 5
        for row in range(MINIMAP_SIDE()):
            if location[0] >= MAX_COORD_LV_2() and location[1] >= MAX_COORD_LV_2():  # MAX_COORD_LV_2() = 20
                if row == location[0] % MINIMAP_SIDE() and column == location[1] % MINIMAP_SIDE():
                    print('[@]', end='')
                elif row == MINIMAP_SIDE() - 1 and column == MINIMAP_SIDE() - 1:
                    print('[B]', end='')
                else:
                    print('[ ]', end='')
            else:
                print('[@]', end='') if (row == location[0] % MINIMAP_SIDE() and
                                         column == location[1] % MINIMAP_SIDE()) else print('[ ]', end='')
        print()


def check_for_level_up(character: dict, foe: dict):
    """Show character's stats when the character levels up.

    :param character: a dictionary
    :param foe: a dictionary

    :precondition: character must be a dictionary containing character information
    :precondition: foe must be a dictionary containing foe information
    :precondition: a key 'exp' of dictionary 'character' must be an integer
    :precondition: a key 'exp' of dictionary 'foe' must be an integer
    :postcondition: print earned exp, current exp, new level and character's info if character levels up from 1 to 2
                    and 2 to 3

    >>> foe_level_1 = {'exp': 100}
    >>> player = {'name': 'P','level': 1, 'hp': 20, 'max_hp': 20, 'exp': 100, 'class_name': ('Thief', 'Assassin', \
                                                                              'Night lord'), 'class':'Thief'}
    >>> check_for_level_up(player, foe_level_1)
    character earned exp:100. current exp:100
    >>> foe_level_1 = {'exp': 100}
    >>> player = {'name': 'P','level': 1, 'hp': 20, 'max_hp': 20, 'exp': 600, 'class_name': ('Thief', 'Assassin', \
                                                                              'Night lord'), 'class':'Thief'}
    >>> check_for_level_up(player, foe_level_1)
    character earned exp:100. current exp:600
    P level up to 2, became Assassin
    Character's stats
    Level : 2
    Class name : Assassin
    Max HP: 30
    Min DP: 8, Max DP: 16
    Experience Point: 600
    Character's skills ['double attack', 'shadow punch', 'shuriken burst']
    >>> foe_level_2 = {'exp': 200}
    >>> player = {'name': 'P','level': 2, 'hp': 20, 'max_hp': 20, 'exp': 800, 'class_name': ('Thief', 'Assassin', \
                                                                              'Night lord'), 'class':'Thief'}
    >>> check_for_level_up(player, foe_level_2)
    character earned exp:200. current exp:800
    >>> foe_level_2 = {'exp': 200}
    >>> player = {'name': 'P','level': 2, 'hp': 20, 'max_hp': 20, 'exp': 1800, 'class_name': ('Thief', 'Assassin', \
                                                                               'Night lord'), 'class':'Thief'}
    >>> check_for_level_up(player, foe_level_2)
    character earned exp:200. current exp:1800
    P level up to 3, became Night lord
    Character's stats
    Level : 3
    Class name : Night lord
    Max HP: 35
    Min DP: 10, Max DP: 20
    Experience Point: 1800
    Character's skills ['triple throw', 'dark flare', 'shadow knife']
    >>> foe_level_3 = {'exp': 300}
    >>> player = {'name': 'P','level': 3, 'hp': 20, 'max_hp': 20, 'exp': 2100, 'class_name': ('Thief', 'Assassin', \
                                                                               'Night lord'), 'class':'Thief'}
    >>> check_for_level_up(player, foe_level_3)

    """
    if character['level'] != 3:
        level = character['level']
        print(f"character earned exp:{foe['exp']}. current exp:{character['exp']}")
        if character['level'] == 1 and character['exp'] >= LV_2_EXPERIENCE_REQUIRED():
            character['level'] = 2
            character['max_hp'] += character['level'] * MAX_HP_INCREMENT()
            character['hp'] = character['max_hp']  # reset to max
            print(f"{character['name']} level up to {character['level']}, became {character['class_name'][level]}")
            display_character_stats(character)
        elif character['level'] == 2 and character['exp'] >= LV_3_EXPERIENCE_REQUIRED():
            character['level'] = 3
            character['max_hp'] += character['level'] * MAX_HP_INCREMENT()
            character['hp'] = character['max_hp']
            print(f"{character['name']} level up to {character['level']}, became {character['class_name'][level]}")
            display_character_stats(character)


def get_user_choice(user_options: tuple) -> int:
    """Return an integer of user input.

    A simple function that prints menu choices and asks users for a number of choices and returns the number

    :param user_options: a tuple
    :precondition: choice_options must be a tuple containing options for the user to choose
    :precondition: user must enter a integer as an input
    :postcondition: return correctly a integer of user input
    :return: integer of user input
    """
    number_options = [pair for pair in zip(itertools.count(0), user_options)]
    print('-------------------------------------------')
    print(' MENU ')
    for i in range(len(number_options)):
        print(f" {number_options[i][0]}) : {number_options[i][1]}")
    print('-------------------------------------------')
    user_choice = input('Enter a number ')
    print()
    while not user_choice.isdigit() or int(user_choice) not in range(len(number_options)):
        user_choice = input('Please enter a valid number ')
    return int(user_choice)


def validate_move(user_choice: int, character: dict) -> bool:
    """Return True if and only if user's choice is valid.

    A simple function that returns True if user's choice on moving their character is valid within the game board

    :param user_choice: a integer
    :param character: a dictionary
    :precondition: board must be a dictionary with a tuple containing x, y coordinates as key
    :precondition: user_choice must be a positive integer or equal to zero
    :precondition: character must be a dictionary with 'x', 'y' keys and current x, y coordinates as a value
    :postcondition: returns True if user's choice on moving their character is valid in the range from [0,0]
    :return: True if the user's choice is valid, else False
    """
    valid = False
    if user_choice == PLAYER_CHOICES_MOVE().index('North') and character['y'] != Y_LOWER_BOUND():  # Y_LOWER = 0
        valid = True
    elif user_choice == PLAYER_CHOICES_MOVE().index('East') and character['x'] != X_UPPER_BOUND():  # X_LOWER = 24
        valid = True
    elif user_choice == PLAYER_CHOICES_MOVE().index('South') and character['y'] != Y_UPPER_BOUND():  # Y_LOWER = 24
        valid = True
    elif user_choice == PLAYER_CHOICES_MOVE().index('West') and character['x'] != X_LOWER_BOUND():  # X_LOWER = 0
        valid = True
    return valid


def move_character(user_choice: int, character: dict):
    """Move character in the directions of North, East, South and West.

    :param user_choice: a integer
    :param character: a dictionary
    :precondition: user_choice must be a valid integer
    :precondition: user_choice must be a positive integer or equal to zero
    :precondition: character must be a dictionary with 'x', 'y' keys and current x, y coordinates as a value
    :postcondition: move correctly the character by 1 in the direction based on user choice
    """
    if user_choice == PLAYER_CHOICES_MOVE().index('North'):  # COORDINATE_INCREMENT = 1
        character['y'] -= COORDINATE_INCREMENT()
    elif user_choice == PLAYER_CHOICES_MOVE().index('East'):
        character['x'] += COORDINATE_INCREMENT()
    elif user_choice == PLAYER_CHOICES_MOVE().index('South'):
        character['y'] += COORDINATE_INCREMENT()
    elif user_choice == PLAYER_CHOICES_MOVE().index('West'):
        character['x'] -= COORDINATE_INCREMENT()


def check_for_boss(character: dict) -> bool:
    """Return True if the character encounter a boss, else False.

    A simple function checks if the character's location is (24, 24) and encounter a boss

    :param character: a dictionary
    :precondition: character must be a dictionary containing x, y coordinates as key and an integer as a value
    :postcondition: return True if the character encounter a foe, else False
    :return: True if the character encounter a boss, else False

    >>> boss_x_coordinate = 24
    >>> boss_y_coordinate = 24
    >>> game_character = {'x': 24, 'y': 24}
    >>> check_for_boss(game_character)
    True
    >>> boss_x_coordinate = 24
    >>> boss_y_coordinate = 24
    >>> game_character = {'x': 10, 'y': 24}
    >>> check_for_boss(game_character)
    False
    >>> boss_x_coordinate = 24
    >>> boss_y_coordinate = 24
    >>> game_character = {'x': 24, 'y': 8}
    >>> check_for_boss(game_character)
    False
    >>> boss_x_coordinate = 24
    >>> boss_y_coordinate = 24
    >>> game_character = {'x': 0, 'y': 0}
    >>> check_for_boss(game_character)
    False
    """
    return character['x'] == BOSS_LOCATION()[0] and character['y'] == BOSS_LOCATION()[1]  # Boss location (24, 24)


def create_boss(character: dict) -> dict:
    """Create a new boss.

    A simple function that returns a boss information

    :param character: a dictionary
    :precondition: character must be a dictionary containing character information
    :return: a dictionary which contains boss info
    """
    boss = {'name': FOE_BOSS_NAME(), 'hp': FOE_BOSS_MAX_HP(), 'max_hp': FOE_BOSS_MAX_HP(), 'exp': 0,
            'min_dp': BOSS_MIN_MAX_DP()[0], 'max_dp': BOSS_MIN_MAX_DP()[1]}
    print(f"{character['name']} encounter {boss['name']}")
    print("Character level should be three to kill the boss")
    print("Once you start the battle,y ou can't run away. This is a fight to the death.")
    print("Do you want to fight or run way? ")
    print("Enter a number")
    return boss


def combat_with_final_boss(character: dict) -> str:
    """Execute the combat with boss.

    A simple function which prompts user to choose fight or flee and shows character death or boss death
                                                                                   if a user choose fight

    :param character: a dictionary
    :precondition: prompt user to choose fight or flee
    :precondition: character must be a dictionary containing character information
    :postcondition: either character or boss should die if the user choose fight
    :return: return 'game_ongoing' if the user choose flee, else 'character_die' if character is dead, else 'boss_die'
    """
    boss = create_boss(character)
    boss_ascii()
    user_choice = get_user_choice(PLAYER_CHOICES_FIGHT_FLEE())
    if user_choice == PLAYER_CHOICES_FIGHT_FLEE().index("Fight"):
        character_die, boss_die, foe_runaway = False, False, False
        while not boss_die and not character_die:
            boss_die, character_die, foe_runaway = combat_round(character, boss)
        return 'character_die' if character['hp'] <= HP_DIE() else 'boss_die'
    else:
        print('Your are the only hope. Please come back when you ready to fight')
        return 'game_ongoing'


def display_character_hp(character: dict):
    """Display character's current HP and HP status bar.

    :param character: a dictionary
    :precondition: character must be a dictionary with 'hp', 'max_hp', 'class_name' keys and current HP, max HP
                    as their values
    :postcondition: Display character's current HP and HP status bar.

    >>> game_character = {'name': 'character', 'hp': 20, 'max_hp': 20, 'level': 1,'class_name': ('S1', 'S2', 'S3')}
    >>> display_character_hp(game_character)
    S1 character's HP : 20 | \033[32m++++++++++++++++++++\033[0m\033[31m\033[0m
    >>> game_character = {'name': 'character', 'hp': 0, 'max_hp': 20, 'level': 1,'class_name': ('T1', 'T2', 'T3')}
    >>> display_character_hp(game_character)
    T1 character's HP : 0 | \033[32m\033[0m\033[31m++++++++++++++++++++\033[0m
    >>> game_character = {'name': 'character', 'hp': 12, 'max_hp': 20, 'level': 1,'class_name': ('A1', 'A2', 'A3')}
    >>> display_character_hp(game_character)
    A1 character's HP : 12 | \033[32m++++++++++++\033[0m\033[31m++++++++\033[0m
    >>> game_character = {'name': 'character', 'hp': -5, 'max_hp': 20, 'level': 1,'class_name': ('A1', 'A2', 'A3')}
    >>> display_character_hp(game_character)
    A1 character's HP : -5 | \033[32m\033[0m\033[31m++++++++++++++++++++\033[0m
    """
    current_hp = character['hp'] if character['hp'] > HP_DIE() else HP_DIE()
    print(f"{character['class_name'][character['level'] - 1]} {character['name']}'s HP : {character['hp']} | "
          f"\033[32m{'+' * current_hp}\033[0m\033[31m"
          f"{'+' * (character['max_hp'] - current_hp)}\033[0m")


def display_foe_hp(foe: dict):
    """Display foe's current HP and HP status bar.

    :param foe: a dictionary
    :precondition: foe must be a dictionary with 'hp', 'max_hp' keys and current HP, max HP as their values
    :postcondition: Display foe's current HP and HP status bar.

    >>> game_foe = {'name': 'monster', 'hp': 15, 'max_hp': 15}
    >>> display_foe_hp(game_foe)
    monster's HP : 15 | \033[32m+++++++++++++++\033[0m\033[31m\033[0m
    >>> game_foe = {'name': 'monster', 'hp': 8, 'max_hp': 15}
    >>> display_foe_hp(game_foe)
    monster's HP : 8 | \033[32m++++++++\033[0m\033[31m+++++++\033[0m
    >>> game_foe = {'name': 'monster', 'hp': 0, 'max_hp': 15}
    >>> display_foe_hp(game_foe)
    monster's HP : 0 | \033[32m\033[0m\033[31m+++++++++++++++\033[0m
    >>> game_foe = {'name': 'monster', 'hp': -5, 'max_hp': 15}
    >>> display_foe_hp(game_foe)
    monster's HP : -5 | \033[32m\033[0m\033[31m+++++++++++++++\033[0m
    """
    current_hp = foe['hp'] if foe['hp'] > HP_DIE() else HP_DIE()
    print(f"{foe['name']}'s HP : {foe['hp']} | \033[32m{'+' * current_hp}\033[0m\033[31m"
          f"{'+' * (foe['max_hp'] - current_hp)}\033[0m")


def check_for_foe() -> bool:
    """Return True if the character encounter a foe, else False.

    A simple function that returns True if the character encounter with 20% percent chance

    :postcondition: return True if the character encounter a foe, else False
    :return: True if the character encounter a foe, else False
    """
    return random.choices([True, False], weights=(CHANCE_ENCOUNTER_FOE(), 100 - CHANCE_ENCOUNTER_FOE()), k=1)[0]


def check_for_foe_run_away() -> bool:
    """ Return True if a foe runs away.

    A simple function that returns True if a foe runs away with 20% percent chance

    :postcondition: return True if a foe runs away, else False
    :return: True if a foe runs away, else False
    """
    return random.choices([True, False], weights=(CHANCE_FOE_RUNAWAY(), 100 - CHANCE_FOE_RUNAWAY()), k=1)[0]


def create_foe(character: dict) -> dict:
    """Creat a foe in various levels.

    A simple function that returns a dictionary of foe information of name, hp, max hp, exp, min dp and max dp

    :postcondition: create lv 1 foe with the name from FOE_NAMES_LV1 if x coordinate and y coordinate are less than 10
    :postcondition: create lv 2 foe with the name from FOE_NAMES_LV2 if x coordinate and y coordinate are less than 20
    :postcondition: create lv 3 foe with the name from FOE_NAMES_LV3 if x coordinate and y coordinate are more than 20
    :return: dictionary containing foe information of name, hp, max hp, exp, min dp and max dp
    """
    foe_lv1_names = dict((sequence_number, foe) for sequence_number, foe in enumerate(FOE_NAMES_LV1()))
    foe_lv2_names = dict((sequence_number, foe) for sequence_number, foe in enumerate(FOE_NAMES_LV2()))
    foe_lv3_names = dict((sequence_number, foe) for sequence_number, foe in enumerate(FOE_NAMES_LV3()))
    if character['x'] < MAX_COORD_LV_1() and character['y'] < MAX_COORD_LV_1():
        foe = {'name': foe_lv1_names[random.randint(0, len(foe_lv1_names) - 1)], 'hp': FOE_MAX_HP_LV1(),
               'max_hp': FOE_MAX_HP_LV1(), 'exp': FOE_LV1_EXP(), 'min_dp': FOE_DP_LV1()[0], 'max_dp': FOE_DP_LV1()[1]}
    elif character['x'] < MAX_COORD_LV_2() and character['y'] < MAX_COORD_LV_2():
        foe = {'name': foe_lv2_names[random.randint(0, len(foe_lv2_names) - 1)], 'hp': FOE_MAX_HP_LV2(),
               'max_hp': FOE_MAX_HP_LV2(), 'exp': FOE_LV2_EXP(), 'min_dp': FOE_DP_LV2()[0], 'max_dp': FOE_DP_LV2()[1]}
    else:
        foe = {'name': foe_lv3_names[random.randint(0, len(foe_lv3_names) - 1)], 'hp': FOE_MAX_HP_LV3(),
               'max_hp': FOE_MAX_HP_LV3(), 'exp': FOE_LV3_EXP(), 'min_dp': FOE_DP_LV3()[0], 'max_dp': FOE_DP_LV3()[1]}
    print(f"{character['name']} encounters {foe['name']}")
    print("Do you want to fight or run way? ", "Enter a number", sep='\n')
    return foe


def combat(character: dict, foe: dict):
    """Execute combat between character and foe.

    :param character: a dictionary
    :param foe: a dictionary
    :precondition: character and foe must be a dictionary with 'name' and 'hp' as the key, and their values
    :postcondition: execute combat between character and foe until one combatant dies, foe runs away or the user choose
                    to quit the game
    """
    foe_die, character_die, foe_runaway = False, False, False
    user_choice = 0  # user option 0 = 'Fight'
    while not foe_die and not character_die and not foe_runaway and user_choice == 0:  # user option 0 = 'Fight'
        foe_die, character_die, foe_runaway = combat_round(character, foe)
        if foe_die:
            print(f"{character['name']} killed {foe['name']} successfully")
            character['exp'] += foe['exp']  # character earns the exp when the foe is dead.
            check_for_level_up(character, foe)
        elif character_die:
            print(f"{character['name']} is dead")
        elif foe_runaway:
            print('oops!~, Foe ran away~~~~~~~~~~~~~~~~~~~')
        else:
            user_choice = get_user_choice(PLAYER_CHOICES_FIGHT_FLEE())  # User option: fight and run away.
    character_flee(character) if user_choice == 1 else print('Combat is over')  # user option 1 = 'Flee'


def combat_round(character: dict, foe: dict) -> tuple[bool, bool, bool]:
    """Execute a single combat round between character and foe.

    :param character: a dictionary
    :param foe: a dictionary
    :precondition: character and foe must be a dictionary with 'name' and 'hp' as the key, and their values
    :postcondition: each combatant rolls a dice and high roller strikes first and if it's a draw , then nobody strikes
                    anyone
    :postcondition: executes a single combat round between character and foe
    :postcondition: return True for foe_die if foe's HP is less than or equal to zero, else False
    :postcondition: return True for character_die if character's HP is less than or equal to zero, else False
    :postcondition: return True for foe_runaway if the foe runs away, else False
    :return foe_die: return True if the foe is dead, else False
    :return character_die: return True if the character is dead, else False
    :return foe_runaway: return True if foe runs away, else False
    """
    character_roll_number = random.randint(COMBAT_ROLL_LOWER(), COMBAT_ROLL_UPPER())  # Roll range [1, 100].
    foe_roll_number = random.randint(COMBAT_ROLL_LOWER(), COMBAT_ROLL_UPPER())   # Roll range [1, 100].
    if character_roll_number > foe_roll_number:  # Character strike first.
        combat_strike('character', character, foe)
        combat_strike('foe', character, foe) if foe['hp'] > HP_DIE() else print('Foe is dead')
    elif character_roll_number < foe_roll_number:  # Foe strike first.
        combat_strike('foe', character, foe)
        combat_strike('character', character, foe) if character['hp'] > HP_DIE() else print('Character collapsed...')
    else:
        print("Nobody successfully strikes anyone!!")
    foe_die = True if foe['hp'] <= HP_DIE() else False  # HP_DIE() = 0
    character_die = True if character['hp'] <= HP_DIE() else False
    foe_runaway = check_for_foe_run_away() if foe['name'] != FOE_BOSS_NAME() and foe['hp'] > 0 else False
    return foe_die, character_die, foe_runaway


def combat_strike(high_roller: str, character: dict, foe: dict):
    """Deduct random damage from the defender's health.

    A simple function that rolls to determine inflicted damage and deduct the damage from the defender's health

    :param high_roller: a string
    :param character:  a dictionary
    :param foe: a dictionary
    :precondition: high_roller must be a string representing first striker on a combat round
    :precondition: character and foe must be a dictionary with 'name' and 'hp' as the key, and their values
    :postcondition: rolls to determine inflicted damage and deduct the damage from the defender's health
    :postcondition: displays both character's and foe's HP after a high roller's strike
    """
    if high_roller == 'character':
        character_attack_description(character, foe)
        character_min_max_dp = character_damage_points(character)
        foe_inflicted_damage = random.randint(character_min_max_dp[0], character_min_max_dp[1])
        foe['hp'] -= foe_inflicted_damage
        print(f"{foe['name']} got -{foe_inflicted_damage} damage")
        display_foe_hp(foe)
        display_character_hp(character)
    else:
        foe_attack_description(character, foe)
        character_inflicted_damage = random.randint(foe['min_dp'], foe['max_dp'])
        character['hp'] -= character_inflicted_damage
        print(f"{character['name']} got -{character_inflicted_damage} damage")
        display_character_hp(character)
        display_foe_hp(foe)


def character_damage_points(character: dict) -> tuple[int, int]:
    """ Set character's dp based on the class

    :param character: a dictionary
    :precondition: character must be a dictionary with 'level' and 'class' as the key, and their values
    :precondition: value of key 'level' must be an integer in the rainge [1, 3]
    :precondition: value of key 'class' must be one of string of 'Sorcerer', 'Thief', 'Bowman', 'Fighter'
    :postcondition: return a tuple which conatins minimum and maximum dp based on the level and the class
    :return: return a tuple which conatins minimum and maximum dp based on the level and the class

    >>> game_character = {'level': 1, 'class': 'Sorcerer'}
    >>> character_damage_points(game_character)
    (1, 25)
    >>> game_character = {'level': 2, 'class': 'Sorcerer'}
    >>> character_damage_points(game_character)
    (1, 30)
    >>> game_character = {'level': 3, 'class': 'Sorcerer'}
    >>> character_damage_points(game_character)
    (1, 35)
    >>> game_character = {'level': 1, 'class': 'Thief'}
    >>> character_damage_points(game_character)
    (6, 12)
    >>> game_character = {'level': 2, 'class': 'Thief'}
    >>> character_damage_points(game_character)
    (8, 16)
    >>> game_character = {'level': 3, 'class': 'Thief'}
    >>> character_damage_points(game_character)
    (10, 20)
    >>> game_character = {'level': 1, 'class': 'Bowman'}
    >>> character_damage_points(game_character)
    (10, 10)
    >>> game_character = {'level': 2, 'class': 'Bowman'}
    >>> character_damage_points(game_character)
    (12, 12)
    >>> game_character = {'level': 3, 'class': 'Bowman'}
    >>> character_damage_points(game_character)
    (14, 14)
    >>> game_character = {'level': 1, 'class': 'Fighter'}
    >>> character_damage_points(game_character)
    (3, 20)
    >>> game_character = {'level': 2, 'class': 'Fighter'}
    >>> character_damage_points(game_character)
    (5, 22)
    >>> game_character = {'level': 3, 'class': 'Fighter'}
    >>> character_damage_points(game_character)
    (7, 24)
    """
    if character['class'] == PLAYER_CHOICES_CLASS()[0]:  # Sorcerer
        min_dp_increment, max_dp_increment, min_initial, max_initial = SORCERER_DP_FACTORS_MIN_MAX_INCREMENT_INITIAL()
    elif character['class'] == PLAYER_CHOICES_CLASS()[1]:  # Thief
        min_dp_increment, max_dp_increment, min_initial, max_initial = THIEF_DP_FACTORS_MIN_MAX_INCREMENT_INITIAL()
    elif character['class'] == PLAYER_CHOICES_CLASS()[2]:  # Bowman
        min_dp_increment, max_dp_increment, min_initial, max_initial = BOWMAN_DP_FACTORS_MIN_MAX_INCREMENT_INITIAL()
    else:  # Fighter
        min_dp_increment, max_dp_increment, min_initial, max_initial = FIGHTER_DP_FACTORS_MIN_MAX_INCREMENT_INITIAL()
    return min_dp_increment * character['level'] + min_initial, max_dp_increment * character['level'] + max_initial


def character_attack_description(character: dict, foe: dict):
    """Display an explanation of character's attack.

    :param character: a dictionary
    :param foe: a dictionary
    :precondition: foe must be a dictionary with 'name' and 'hp' as the key, and their values
    :precondition: character must be a dictionary with 'name', 'hp', 'class', 'level' as the key, and their values
    :precondition: value of 'class' key must be one of the strings of 'Sorcerer', 'Thief', 'Amazon', 'Fighter'
    :postcondition: Display an explanation of character's attack based on character's level and class
    """
    if character['class'] == 'Sorcerer':
        descriptions = [pair[0] for pair in SORCERER_SKILL().items() if pair[1] == character['level']]
    elif character['class'] == 'Thief':
        descriptions = [pair[0] for pair in THIEF_SKILL().items() if pair[1] == character['level']]
    elif character['class'] == 'Bowman':
        descriptions = [pair[0] for pair in BOWMAN_SKILL().items() if pair[1] == character['level']]
    else:
        descriptions = [pair[0] for pair in FIGHTER_SKILL().items() if pair[1] == character['level']]
    attacks = {i: descriptions[i] for i in range(len(descriptions))}
    attack = attacks[random.randint(0, len(attacks) - 1)]
    print(f"{character['name']} used {attack} to {foe['name']}")


def foe_attack_description(character: dict, foe: dict):
    """Display an explanation of foe's attack.

    :param character: a dictionary
    :param foe: a dictionary
    :precondition: character and foe must be a dictionary with 'name' and 'hp' as the key, and their values
    :postcondition: Display an explanation of foe's attack
    """
    attacks = {i: FOE_ATTACK_DESCRIPTIONS()[i] for i in range(len(FOE_ATTACK_DESCRIPTIONS()))}
    attack = attacks[random.randint(0, len(attacks) - 1)]
    print(f"{foe['name']} used {attack} to {character['name']}")


def character_flee(character: dict):
    """Ran away from a foe.

    A simple function that runs away from a foe when the character encounter a foe

    :param character: a dictionary
    :precondition: character must be a dictionary with 'name' and 'hp' as the key, and their values
    :postcondition: the character run away when the character encounter a foe
    :postcondition: the character can be inflicted damage in the range [1, 4] with 20% chance
    :postcondition: ran away from a foe
    """
    if random.choices([True, False], weights=(CHANCE_FOE_STAB_BACK(), 100 - CHANCE_FOE_STAB_BACK()), k=1)[0]:
        damage_by_foe = random.randint(FOE_STAB_BACK_MINIMUM_DAMAGE(), FOE_STAB_BACK_MAXIMUM_DAMAGE())
        character['hp'] -= damage_by_foe
        print(f"{character['name']} just got stabbed in the back and got - {damage_by_foe} damage")
        display_character_hp(character)
    else:
        display_character_hp(character)
        print(f"{character['name']} ran away successfully")


def character_heal(character: dict):
    """Increase the character's HP.

    A simple function that increases the character's HP each time the character moves and does not encounter a foe

    :param character: a dictionary
    :precondition: character must be a dictionary with 'name' and 'hp' as the key, and their values
    :postcondition: increases correctly the character's HP by 4
    :postcondition: increases character's HP up to maximum HP if HP is greater than or equal to (max_hp - 4)

    >>> game_character = {'name': 'player', 'hp': 10, 'max_hp': 20, 'level': 1,'class_name': ('S1', 'S2', 'S3')}
    >>> character_heal(game_character)
    Character healed
    S1 player's HP : 14 | \033[32m++++++++++++++\033[0m\033[31m++++++\033[0m
    >>> game_character = {'name': 'player', 'hp': 16, 'max_hp': 20, 'level': 1,'class_name': ('S1', 'S2', 'S3')}
    >>> character_heal(game_character)
    Character healed
    S1 player's HP : 20 | \033[32m++++++++++++++++++++\033[0m\033[31m\033[0m
    >>> game_character = {'name': 'player', 'hp': 18, 'max_hp': 20, 'level': 1,'class_name': ('S1', 'S2', 'S3')}
    >>> character_heal(game_character)
    Character healed
    S1 player's HP : 20 | \033[32m++++++++++++++++++++\033[0m\033[31m\033[0m
    >>> game_character = {'name': 'player', 'hp': 20, 'max_hp': 20, 'level': 1,'class_name': ('S1', 'S2', 'S3')}
    >>> character_heal(game_character)
    S1 player's HP : 20 | \033[32m++++++++++++++++++++\033[0m\033[31m\033[0m
    """
    if character['hp'] != character['max_hp']:
        character['hp'] += HP_HEAL_INCREMENT()  # HP_HEAL_INCREMENT() = 4
        if character['hp'] > character['max_hp']:
            character['hp'] = character['max_hp']
        print('Character healed')
    display_character_hp(character)


def check_if_character_die(character: dict) -> str:
    """Return string 'character_die' if and only if the character dies.

    :param character: a dictionary
    :precondition: character must be a dictionary with 'name' and 'hp' as the key, and their values
    :postcondition: returns the string 'character_die' if the character's HP is less than or equal to zero
    :return: returns True if user reaches their goal, else string 'character_alive'

    >>> game_character = {'name': '', 'hp': 0, 'x': 4, 'y': 4}
    >>> check_if_character_die(game_character)
    'character_die'
    >>> game_character = {'name': '', 'hp': -5, 'x': 4, 'y': 4}
    >>> check_if_character_die(game_character)
    'character_die'
    >>> game_character = {'name': '', 'hp': 1, 'x': 4, 'y': 4}
    >>> check_if_character_die(game_character)
    'character_alive'
    """
    return 'character_die' if character['hp'] <= HP_DIE() else 'character_alive'  # HP_DIE() = 0


def character_explore(user_choice: int, character: dict, board: dict) -> str:
    """Return a string of status of the character.

    A simple function that increases the character's current status.

    :param user_choice: a integer
    :param character: a dictionary
    :param board: a dictionary
    :precondition: user_choice must be a positive integer or equal to zero
    :precondition: board must be a dictionary with a tuple containing x, y coordinates as key and a string of location
                description
    :precondition: character must be a dictionary containing character's name, HP, x-coordinate, y-coordinate
    :postcondition: returns 'boss_die' as status if character kills the final boss or 'character_die' as status if
                    character is dead, or 'character_alive' if character is alive after a combat or a flee, else
                    'game_ongoing' as status
    :postcondition: returns status of the character depends on character current HP and x, y coordinate
    :return: a string representing the status of the character
    """
    move_character(user_choice, character)
    display_location(board, character)
    status = 'game_ongoing'
    if check_for_boss(character):
        status = combat_with_final_boss(character)
    elif check_for_foe():
        foe = create_foe(character)
        user_choice = get_user_choice(PLAYER_CHOICES_FIGHT_FLEE())  # PLAYER_CHOICES_FIGHT_FLEE() = 'Fight', 'Flee'
        combat(character, foe) if user_choice == PLAYER_CHOICES_FIGHT_FLEE().index('Fight') else \
            character_flee(character)
        status = check_if_character_die(character)
    else:
        character_heal(character)
    return status


def game():
    """Execute the main game"""
    board = make_board(WIDTH(), HEIGHT())  # WIDTH() = 25, HEIGHT() = 25
    display_game_intro()
    character = make_character()
    display_location(board, character)
    status = 'game_ongoing'
    while status != 'user_choose_quit' and status != 'boss_die' and status != 'character_die':
        user_choice = get_user_choice(PLAYER_CHOICES_MOVE())
        if user_choice == PLAYER_CHOICES_MOVE().index('Quit'):
            status = 'user_choose_quit'
        elif validate_move(user_choice, character):
            status = character_explore(user_choice, character, board)
        else:
            print("you can't move in that direction")
            display_location(board, character)
    game_ending_message(status)


def main():
    """Execute the program."""
    doctest.testmod(verbose=True)
    game()


if __name__ == "__main__":
    main()
