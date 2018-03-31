import time
import random


class Character:
    items = []

    status_effects = []

    player_name = ""

    player_short_name = ""

    morality = 0


class Warlock(Character):
    class_name = "Warlock"
    name_flavor = [["The Mighty ", "The ", "The Meek ", "The Powerful ", "The Silent ", "The Broken ", "The Holy ",
                    "The Prime ", "The Psychotic ", "The Chaotic ", "The Omniscient ", "The Omnipotent "],
                   [" of Time", " of the Underworld", " from Eternity", " of Infinity", " of Aeiros",
                    " of Middle-Earth", " Who Never Was", " Who Time Forgot", " of the Undead", " of the Future", ""]]
    hp = 100  # Health
    at = 20  # Attack
    block_chance = 10


class Paladin(Character):
    class_name = "Paladin"
    name_flavor = [["The Strong ", "The Great ", "The Divine ", "The Undying ", "The Righteous ", "The Bold ",
                    "The Immortal ", "The Thundering ", "Lord ", "King ", "Holy ", "The Demi-"],
                   [" of Legend", " of Time", " of the Unknown", " of the Iron Hills", " of God", " born of Fire",
                    " born of Iron", ""]]
    hp = 200
    at = 15
    block_chance = 20


class Marksman(Character):
    class_name = "Marksman"
    name_flavor = [["The Precise ", "The Accurate ", "The Deathly ", "The Shadow ", "The Ghostly ", "The Undead ",
                    "The Quick ", "The God-Chosen ", "The Enigmatic ", "The Loyal "],
                   [" of Death", " of Royalty", " of the Unknown", ", Bringer of Death", " of Darkness", " of Blood",
                    " of Silence", " of the Cursed", " of the Occult", ""]]
    hp = 125
    at = 18
    block_chance = 12


class BlackHeart(Character):
    class_name = "Black Heart"
    name_flavor = [["The Deadly ", "The Mysterious ", "The Cursed ", "The Soul-Bound ", "The Eidolic ", "The Killer ",
                    "Sir ", "Lord ", "The Swift ", "The Blessed ", "Blood-bound ", "", "The", "The Soulish "],
                   [" of the Dark World", " of Steel", " of Ink", " of Danger", " of Darkness", " of the Undead",
                    " of Time", " of Eternity", " of Vengeance", " of Flame", ", born of Shadows", ""]]
    hp = 75
    at = 25
    block_chance = 25


class Ravager(Character):
    class_name = "Ravager"
    name_flavor = [["The Blood-Thirsty ", "The Powerful ", "The Blood-Crazed ", "The Immortal", "The Undying ",
                    "The Savage ", "The Crazed ", "The Deadly ", "The Brave ", "The Honor-bound ", "The Undead ", ""],
                   [" of Iron", " of Death", " of Time", " of Glory", " of the Vikings", " of Valhalla", " of Steel",
                    " of the North", " of Strength", " of the Storm"]]
    hp = 150
    at = 20
    block_chance = 10


class Necromancer(Character):
    class_name = "Necromancer"
    name_flavor = [["The Cursed ", "The Dark ", "The Powerful ", "The Deceitful ", "The Shadow ", "The Iron ",
                    "The Avenged ", "The Forgotten ", "The ", ""],
                   [" of the Dark World", " of Steel", " of Ink", " of Death", " of the Underworld", " of the Undead",
                    " of Time", " of Eternity", " of Vengeance", " of Smoke", ", born of Shadows"]]
    hp = 125
    at = 30
    block_chance = 0


class Titan(Character):
    class_name = "Titan"
    name_flavor = [["The Great ", "The ", "", "The Last ", "The Ultimate ", "The Final ", "The Dying ", "The Crazed ",
                    "The Mad ", "The Old ", "The Ancient ", "The Almighty ", "The Undying ", "The Bleeding "],
                   [" of Life", " Guardian", " of Fire", " of Water", " of Iron", " of Stone", " of the Forest",
                    " of Madness", " of Death", " Master", " Lord", " God", " Deity", " of Time"]]
    hp = 250
    at = 20
    block_chance = 0


class Peasant(Character):
    class_name = "Peasant"
    name_flavor = [["The Simple ", "The ", "The Cursed ", "The Weak ", "The Drunk ", "The Meek ", "The God-Fearing ",
                    "The Strong ", "The Vengeful "],
                   ["", "", "", ""]]
    hp = 100
    at = 10
    block_chance = 40


class Trickster(Character):
    class_name = "Trickster"
    name_flavor = [["The Deranged ", "The Insane ", "The Mad ", "The Crazed ", "The Manic ", "The Blood-thirsty",
                    "The Twitchy ", "The Laughing ", "The Cackling ", "The Howling ", "The Grim ", "The Phantom",
                    "The "],
                   [" of the Underworld", " of the Mountains", " of Deceit", " of Sin", " God", " King", "",
                    " of Lies", " of Nightmares", " of the Nightmare Realm", ""]]
    hp = 30
    at = 25
    block_chance = 95


class Undead(Character):
    class_name = "Undead"
    name_flavor = [["The ", "The Rotting ", "The Feared ", "The Screaming ", "The Bleeding ", "The Agile ", "",
                    "The Immortal ", "The Foreseen ", "The Silent "],
                   [" of the Ground", " of the Past", " of Ashes", "", "", "", "", "", " of Flesh", "of Fright",
                    " of Bondage", " of Bones"]]
    hp = 1
    at = 20
    block_chance = 99


class Revenant(Character):
    class_name = "Revenant"
    name_flavor = [["The ", "The Last ", "The Last Great ", "The First ", "The Final ", "The Faded ", "The Bleeding ",
                    "The Screaming ", "The Gone ", "The Hardened ", "The Iron ", "The Steel ", "The Vengeful ", "The "],
                   ["", "", "", "", "", " of Hope", " of Fear", " of Darkness", " of Hell", " of the Earth", "", "",
                    "", "", "", "", "", " of God", " of Faith", " Sent by Jehovah"]]
    hp = 150
    at = 20
    block_chance = 30


def get_name(player):  # This gets the player's randomized name prefix/suffix.
    player.player_name = random.choice(player.name_flavor[0]) + player.class_name + random.choice(player.name_flavor[1])


def wait(seconds):  # This is my Scratch-ified version of python 'sleep'
    time.sleep(seconds)


def line_stutter(dialogue, placement, times, speed):  # This is purely for aesthetic text stuttering.
    for _ in range(times):
        print(dialogue[placement])
        wait(speed)


def name_display(player):
    print(player.player_name)


def quiz(player):
    get_name(player)
    total_judgment = 0
    for x in range(len(questionnaire[0])):
        print("          " + questionnaire[0][x])
        print("      " + questionnaire[1][x]), print("")
        for i in range(4):
            print("        " + questionnaire[2][x * 4 + i])
        print("")
        while True:
            judgement = input('       ')
            if judgement == "1":
                judgement = -2
                total_judgment += judgement
                break
            if judgement == "2":
                judgement = -1
                total_judgment += judgement
                break
            if judgement == "3":
                judgement = 1
                total_judgment += judgement
                break
            if judgement == "4":
                judgement = 2
                total_judgment += judgement
                break
        wait(0)
    wait(1), print("Tallying score. . ."), wait(2)
    if total_judgment <= -18:
        player = Necromancer
        get_name(player)
    elif -15 >= total_judgment > -18:
        player = Ravager
        get_name(player)
    elif -10 >= total_judgment > -15:
        player = Undead
        get_name(player)
    elif -7 >= total_judgment > -10:
        player = Trickster
        get_name(player)
    elif -4 >= total_judgment > -7:
        player = Titan
        get_name(player)
    elif -1 >= total_judgment > -4:
        player = BlackHeart
        get_name(player)
    elif total_judgment == 0:
        player = Peasant
        get_name(player)
    elif 1 <= total_judgment < 6:
        player = Warlock
        get_name(player)
    elif 6 <= total_judgment < 11:
        player = Marksman
        get_name(player)
    elif 11 <= total_judgment < 16:
        player = Paladin
        get_name(player)
    elif 16 <= total_judgment < 21:
        player = Revenant
        get_name(player)
    player.morality = total_judgment
    print("Congratulations! You are " + player.player_name + "!")
    print("")
    print("Here are your stats:")


def journey(player):
    areas = [[" in their lair", " deep in concentration", " scavenging the wreckage of a ruined village",
             " scaling a volcano", " terrorizing villagers", " waiting for a hero that will never come",
              " in target practice ", " practicing the Dark Arts", " chanting a demonic rune"],
             [" during a thunderstorm", " during the rain", " and leveling up", " and working on their stats",
              " during a snowstorm", " and gathering potion ingredients", "", "", "", "", "", "", "", "", "", ""],
             [" in a tavern", " fixing their house", " looting a dungeon", " leveling up", " crafting an item",
              " in a cutscene", " doing a side-mission", " looking for online walkthroughs", " choosing a skill tree"],
             ["", ""]]

    enemies = [["Villager", "Foot Soldier", "Guard", "Knight", "Militia", "Weak Hero", "Paladin", "Revenant",
                "Mage", "Warlock", "Archer", "Marksman", "King", "Hero", "Spirit", "Max Level Hero"],
               ["Wolf", "Goblin", "Gnome", "Undead", "Orc", "Pyromancer", "Troll", "Ogre", "Chimera", "Trickster",
                "Ghost", "Assassin", "Titan", "Beast", "Mini-Boss", "Final Boss", "Final Boss's True Form"]]

    places = [["Silent Springs", "Peace Meadow", "Ocular Oasis", "Ember Town", "Harbinger Palace"],
              ["Deceit Valley", "Turmoil Towers", "Eidolic Bog", "Ravenous Kingdom", "Boss's Lair"]]
    if player.morality < 0:
        print(player.player_short_name, "starts out" + random.choice(areas[0]) + random.choice(areas[1]))
        wait(3)
        print("They decide to scour the world in search of heroes to defeat, thus begins their journey!")
    else:
        print(player.player_short_name, "begins" + random.choice(areas[2]) + random.choice(areas[3]))
        wait(3)



def text_reader(dialogue, speed, amount, placement):
    for x in range(amount):
        print(dialogue[x + placement])
        wait(speed)


def stats(player):
    print("HP:", player.hp)
    print("Attack:", player.at)
    print("Block:", player.block_chance, "%")


# Below is a list of the current possible Characters on a scale of most evil to most heroic.
# Necromancer, Ravager, Undead, Trickster, Titan, Black Heart, Peasant, Warlock, Marksman, Paladin, Revenant

questionnaire = [["╠════════ Question One ════════╣", "╠════════ Question Two ════════╣",
                  "╠════════ Question Three ════════╣", "╠════════ Question Four ════════╣",
                  "╠════════ Question Five ════════╣", "╠════════ Question Six ════════╣",
                  "╠════════ Question Seven ════════╣", "╠════════ Question Eight ════════╣",
                  "╠════════ Question Nine ════════╣", "╠════════ Question Ten ════════╣"],
                 ["What time of day do you prefer?",
                  "Which of the following options do you think the world be better without?",
                  "Choose a tool from the options below.", "Which kind of area in the options below best suits you?",
                  "Choose an attribute which best describes you.", "Choose a weakness which best describes you.",
                  "Which option best describes your height?", "How would you describe your friends?",
                  "Which basic element best suits you?", "What kind of character do you think you got?"],
                 ["1.) Night", "2.) Dusk", "3.) Dawn", "4.) Day",
                  "1.) Weakness", "2.) Differences", "3.) War", "4.) Hate",
                  "1.) Scythe", "2.) Axe", "3.) Hammer", "4.) Wrench",
                  "1.) Mountainous", "2.) Urban", "3.) Forested", "4.) Field",
                  "1.) Strong", "2.) Clever", "3.) Smart", "4.) Determined",
                  "1.) Not Strong Enough", "2.) Uncaring", "3.) Egotistical", "4.) Vain",
                  "1.) Not Tall Enough", "2.) Kind Of Short", "3.) Okay", "4.) Too Tall",
                  "1.) Inferior", "2.) Decent", "3.) Good", "4.) Loyal",
                  "1.) Fire", "2.) Stone", "3.) Water", "4.) Nature",
                  "1.) Evil", "2.) Bad", "3.) Good", "4.) Heroic"]]

text = ["Hello, and welcome to:",
        "         ████████████████████████████████████████████████████████████████",
        " #######  ########  #######  ########  ##    ##     ######  ##     ## ########  ##     ## #### ##     ##    ###    ##       ",
        "##     ##    ##    ##     ## ##     ##  ##  ##     ##    ## ##     ## ##     ## ##     ##  ##  ##     ##   ## ##   ##       ",
        "##           ##    ##     ## ##     ##   ####      ##       ##     ## ##     ## ##     ##  ##  ##     ##  ##   ##  ##       ",
        " ######      ##    ##     ## ########     ##        ######  ##     ## ########  ##     ##  ##  ##     ## ##     ## ##       ",
        "      ##     ##    ##     ## ##   ##      ##             ## ##     ## ##   ##    ##   ##   ##   ##   ##  ######### ##       ",
        "##    ##     ##    ##     ## ##    ##     ##       ##    ## ##     ## ##    ##    ## ##    ##    ## ##   ##     ## ##       ",
        " ######      ##     #######  ##     ##    ##        ######   #######  ##     ##    ###    ####    ###    ##     ## ######## ",
        "Welcome to STORY SURVIVAL", "The text game that decides whether you live or die",
        "In a little bit, you're going to take a little quiz to let the computer judge your soul.",
        "It'll decide which archetype is most like you depending on YOUR choices.",
        "After which, you'll see whether or not your character survives their own story.",
        "So be prepared. . .", ""]

user = Peasant

line_stutter(text, 1, 10, .25)
wait(1)
text_reader(text, 0, 7, 2)
wait(3)
line_stutter(text, 1, 10, .25)
text_reader(text, 2, 5, 11)
wait(1)

quiz(user)
print(user.player_short_name)
quit()
stats(user)
print(""), print("Now your journey begins. . .")
wait(2)
