import random
import Mechs
import math
import Enemies
import copy
import Magic
import Quests


def tsleep(thyme):
    Mechs.tsleep(thyme)


flv_xp = 0
flv_gold = 0

#--------------------------------------------------------------------------------------
################################################################### MAIN DUNGEON FUNCTION
#--------------------------------------------------------------------------------------


def Dungeon():
    global flv_xp
    global flv_gold
    flv_xp = 0
    flv_gold = 0

    Magic.EE_Used = 0

    floors = random.randint(math.ceil(.2 * Mechs.level),
                            math.ceil(.6 * Mechs.level))
    if floors > 14:
        floors = random.randint(11, 14)
    if floors < 4:
        floors = random.randint(2, 4)

    Mechs.PlayerHasDied = False
    while floors > 0:
        if Mechs.PlayerHasDied or Mechs.PlayerQuit == True:
            break
        currentfloor = random.randint(1, 100)
        if currentfloor < 70:
            random_encounter(1, 100)
            floors = floors - 1
            tsleep(1)
        elif currentfloor <= 84:
            puzzle()
            floors = floors - 1
            tsleep(1)
        elif currentfloor <= 92:
            treasure()
            floors = floors - 1
            tsleep(1)
        elif currentfloor <= 92:
            special_room()
            floors = floors - 1
            tsleep(1)

    if Mechs.PlayerHasDied == True:
        print("You scurry out of the dungeon")
        tsleep(1)
    else:
        print(
            f"You have reached the end of the dungeon! You gained a total of {flv_xp} XP and {flv_gold} gold on this journey!"
        )
        tsleep(1)

    Magic.EE_Used = 0


#--------------------------------------------------------------------------------------
###################################################################### TREASURE ROOM
#--------------------------------------------------------------------------------------


def treasure():

    global flv_xp
    global flv_gold

    chest_opened = False
    chest_trapped = random.randint(1, 5)

    ## Defines coin multiplier if chest is not trapped
    if chest_trapped != 1:
        coinmod = random.randint(10, 30)
        if coinmod >= 29:
            coinmod = random.randint(80, 100)

    print(
        "You stumble into a dark room with a dimly lit chest, the air around you hangs ominously..."
    )
    tsleep(1)
    print(
        "This roleplay lore shit is pretty cringy, but you have a choice to make. Do you open the chest, or continue on to the next room?"
    )
    tsleep(1)

    while chest_opened == False:
        treasureinput = input(
            "Enter 'o' to open the chest, or 'c' to continue to the next room.\n"
        ).lower()
        if treasureinput == "o":
            print("You decide to open the chest, and do so with caution.")
            tsleep(1)
            treasurewait = 0
            while treasurewait < 3:
                print("...")
                tsleep(1)
                treasurewait += 1
            print("")
            if chest_trapped == 1:
                print(
                    "The chest was trapped! A lil goblin boi bites your hand, dealing 3 damage, before running away. Your hand has the hurty hurty, so you cannot run after him."
                )
                Mechs.health -= 3
                tsleep(2)
                print(
                    "You continue on along your way, your hand has the hurty hurt."
                )
                chest_opened = True
            if chest_trapped != 1:
                print(
                    "You open the chest, half expecting a little goblin boi to bite your hand and run away. As time passes, your hand remains unbitten. You notice some goodies in the bottom of the chest."
                )
                tsleep(5)
                if coinmod > 60:
                    print(
                        f"CHA CHING BABY, you found a chest with a whopping {coinmod} gold in it!"
                    )
                    Mechs.gold += coinmod
                    tsleep(1)
                    print(
                        f"You now have {Mechs.gold} gold coins in your pretty pink purse."
                    )
                elif coinmod <= 60:
                    print(
                        f"Much to your delight, you find a nice pile of {coinmod} gold in the chest."
                    )
                    Mechs.gold += coinmod
                    tsleep(1)
                    print(
                        f"You now have {Mechs.gold} gold coins in your pretty pink purse."
                    )
                flv_gold += coinmod
                Quests.fetchquest_check()
                tsleep(1)
                print(
                    "You continue on along your way, your pockets slightly heavier than before."
                )
                tsleep(1)
                chest_opened = True

        elif treasureinput == "c":
            print(
                "You choose to continue on along your way, the thought of a little goblin boi jumping out of the chest to bite your hand was just too much to bear."
            )
            chest_opened = True


#--------------------------------------------------------------------------------------
########################################################### PUZZLE
#--------------------------------------------------------------------------------------


def puzzle():
    global flv_gold

    puzzle_choice = random.randint(1, 2)
    stab = random.randint(1, 4)
    chest_open = random.randint(1, 10)

    if puzzle_choice == 1:
        prize = random.randint(80, 110)
        prize2 = prize
        prize3 = math.floor(prize * .1)
        print(
            'A funny looking fella with a large wizard hat and no pants appears before you. He shows you a greasy paper bag and says "To open this chest you must guess a number between 1 and 10. The more you guess the less you will be rewarded!"'
        )
        guesses = 5
        while guesses > 0:
            player_guess = input()
            print(f'You guess the magical number {player_guess}. ')
            tsleep(1)
            if player_guess == str(chest_open):
                print(
                    f'The funny fella throws the grease bag at you and shuffles awkwardly away giving you the grand prize of {prize} gold.'
                )
                tsleep(1)
                Mechs.gold = prize + Mechs.gold
                flv_gold += prize
                break
            if player_guess != chest_open:
                print(
                    f'You punch in {player_guess} on the "chest". You are incorrect and have lost gold for your mistake.'
                )
                prize = prize2 - prize3
                prize2 = prize
                guesses -= 1
                if guesses == 0:
                    print(
                        'The funny fella runs away from you leaving you with no reward...'
                    )
                    tsleep(1)
                    break
            print('Guess again.')
    elif puzzle_choice == 2:
        prize = random.randint(10, 50)
        print(
            'You come across a naked man shouting profanities! He spots you and yells seemingly with all the force he can "HOW DO YOU SPELL ONOMATOPOEIA???". You suspect he might do something crazy if you get it wrong or ignore him.\n'
        )
        tsleep(1)
        print(
            'What is Your answer? Do you ignore him? [spell onomatopoeia, Ignore or I]'
        )
        answer = input().lower()
        if answer == 'onomatopoeia':
            print(
                f"You confidently spell Onomatopoeia to the crazy individual. Once you finish he screams 'FINALLY, I AM COMPLETE.' He slowly fades from existence leaving behind {prize} gold."
            )
            tsleep(1)
            Mechs.gold += prize
            flv_gold += prize
            print(f'You now have {Mechs.gold} gold!')
            tsleep(1)
        elif answer == 'ignore' or answer == 'i':
            print(
                'You keep walking further into the dungeon past this crazy fool. As you walk by him you hear him begin to cry. The further you get the louder his wails. You hope you never see him again.'
            )
            tsleep(1)
        else:
            print(
                'Your poor spelling or inability to summon the courage to walk away from this man makes him angry. He pulls a shank out from his anus and slashes at you.'
            )
            tsleep(1)
            if stab >= 2:
                print(
                    'The crazy fool misses and trips, scraping his knees and giving you a chance to escape'
                )
                tsleep(1)
            else:
                print(
                    f'You are stabbed with the poopy shank losing {stab} Mechs.health. He scurries away like a cockroach into the darkness.\n'
                )
                tsleep(1)
                if Mechs.health > 0:
                    print(
                        'You patch yourself up as best you can and move on deeper into the dungeon.'
                    )
                    tsleep(1)
                else:
                    print(
                        'You quickly bleed out, killed by a creep. This is certainly not the best way to end an adventure.'
                    )
                    tsleep(1)
                    Mechs.deathmenu()

    #elif puzzle_choice == 2 :
    #print()
    #print('An Orc with glasses blocks your path. "What is 15 multiplied by 30 minus 7? You have 15 seconds to figure this out or i will throw biting spiders in your pants!"')


#--------------------------------------------------------------------------------------
##################################################################### MAIN COMBAT FUNCTION
#--------------------------------------------------------------------------------------


def combat(Encounter):
    global isEnemy
    global flee
    global player_turn
    global colorlist

    flee = False
    isEnemy = copy.copy(Encounter)
    colorcheck()
    roll_initiative()
    if isEnemy.Health > 0:
        print(isEnemy.Catchphrase)
    while Mechs.health > 0 and isEnemy.Health > 0:
        Magic.Status_Effects()
        while player_turn == True:
            print(f"Your battle with {isEnemy.Name} rages on.")
            tsleep(1)
            print("       What will you do?")
            print("(a) - Attack       (i) - Item")
            print("(m) - Magic        (f) - Flee\n")
            playerinput = input().lower()
            if playerinput == "a":
                player_combat()
            elif playerinput == "s":
                print("You have skipped your turn!")
                player_turn = False
            elif playerinput == "i":
                items()
            elif playerinput == "f":
                fleefunc()
                player_turn = False
                if flee == True:
                    break
            elif playerinput == "m":
                magic()
            else:
                print("That is not a valid input!")
        if isEnemy.Health > 0:
            enemy_combat()
    Magic.SE_Combat_End()
    if Mechs.health <= 0 and flee == False:
        print(f"{isEnemy.Name} has slain you!")
        tsleep(1)
        Mechs.deathmenu()
    elif isEnemy.Health <= 0 and flee == False:
        print("You did it!\n\n\n")
        Quests.killquest_check(isEnemy.Name)
        Mechs.xp_system(isEnemy.Exp)
        print(f"You have gained {isEnemy.Exp} experience! \n \
    You now have {Mechs.xp_have}/{Mechs.xp_needed}")
        tsleep(1)
    elif flee == True:
        print("Coward!")
        tsleep(1)


def block():
    print("lol blocking doesnt actually work")
    tsleep(1)


colorlist = [
    "Golden", 'Green', 'Aqua', 'Yellow', 'Maroon', 'Emerald', 'Saffron',
    'Lavender'
]


def colorcheck():
    global isEnemy
    if isEnemy.Name == "Dragon" \
    or isEnemy.Name == "Template" \
    or isEnemy.Name == "Wolf"\
    or isEnemy.Name == "Template":
        tempstorage = isEnemy.Name
        color = random.choice(colorlist)
        isEnemy.Name = (f"{color} {tempstorage}")


#--------------------------------------------------------------------------------------
##################################################################### ITEMS
#--------------------------------------------------------------------------------------


def items():
    print(
        f"You have {Mechs.H_Potion} health potions and {Mechs.M_Potion} mana potions!\n Would you like to use one?"
    )
    tsleep(1)
    item_open = True
    while item_open == True:
        tempinput = input(
            "(h) Health     (m) Mana \n     (b) Go back\n").lower()
        if tempinput == "h" and Mechs.H_Potion > 0:
            Mechs.H_Potion -= 1
            Mechs.health += math.ceil(Mechs.Weapon.Maxhealth * .2)
            if Mechs.health > Mechs.Weapon.Maxhealth:
                Mechs.health = Mechs.Weapon.Maxhealth
            print(
                f"Congrations, you now have {Mechs.health}/{Mechs.Weapon.Maxhealth} health"
            )
            item_open = False
            break
        elif tempinput == ("h") and Mechs.H_Potion == 0:
            print("Hey bud! You don't have a health potion to use!")
        elif tempinput == ("m") and Mechs.M_Potion > 0:
            Mechs.M_Potion -= 1
            Mechs.mana += math.floor(Mechs.maxmana * .2)
            if Mechs.mana > Mechs.maxmana:
                Mechs.mana = Mechs.maxmana
            print(
                f"Congrations, you now have {Mechs.mana}/{Mechs.maxmana} mana")
            item_open = False
            break
        elif tempinput == "m" and Mechs.M_Potion == 0:
            print("Hey bud! You don't have a mana potion to use!")
        elif tempinput == "b":
            item_open = False
            break
        else:
            print("Hey, that's not a valid input!")

    tsleep(1)


#--------------------------------------------------------------------------------------
########################################################### Random Encounter Function
#--------------------------------------------------------------------------------------


def random_encounter(low, high):
    Dice_roll = random.randint(low, high) + (Mechs.level * 8)
    if Dice_roll > 170:
        Dice_roll = random.randint(120, 250)
    if Dice_roll <= 50:
        combat(Enemies.Goobo)
    elif Dice_roll <= 70:
        combat(Enemies.Goblin)
    elif Dice_roll <= 90:
        combat(Enemies.Wolf)
    elif Dice_roll <= 110:
        combat(Enemies.Slef)
    elif Dice_roll <= 130:
        combat(Enemies.Bingus)
    elif Dice_roll <= 170:
        combat(Enemies.Gorblin_Ramsay)
    else:
        combat(Enemies.Dragon)


# Enemies sorted by difficulty sort of
# Goobo
# Goblin
# Wolf
# Slef
# Bingus
# Gorblin_Ramsay
# Dragon

isEnemy = ()
#--------------------------------------------------------------------------------------
########################################################### Combat Function
#-------------------------------------------------------------------------------------


def player_combat():
    global isEnemy
    global player_turn
    attack = random.randint(
        1, 20) + Mechs.Weapon.Hit + (Magic.Bloodlust_Used * 20)
    ## critical scenario
    if attack >= Mechs.Weapon.Crit:
        damagedealt = Mechs.Weapon.Damage * 2 + (Magic.Bloodlust_Used *
                                                 Mechs.Weapon.Damage)
        isEnemy.Health -= damagedealt
        print(
            f"A CRITICAL STRIKE!! {Mechs.Weapon.Action}, dealing {damagedealt} damage to {isEnemy.Name}, Bringing it down to {isEnemy.Health} health!"
        )
## normal hit scenario
    elif attack >= isEnemy.Armor:
        isEnemy.Health -= Mechs.Weapon.Damage
        print(
            f"{Mechs.Weapon.Action} doing {Mechs.Weapon.Damage} damage to {isEnemy.Name}, Bringing him down to {isEnemy.Health} health!"
        )
## miss scenario
    elif attack < isEnemy.Armor:
        poo = random.randint(1, 2)
        if poo == 1:
            print("Sucks to suck, I guess. You missed.")
        else:
            print(
                f"You strike but the {Mechs.Weapon.Projectile} bounces off like a toy."
            )


## you fuckin rolled a 1 lol
    elif 1 == (attack - Mechs.Weapon.Hit()):
        Mechs.health -= 1
        print(
            f"You missed so bad that it hurts. Your health is now {Mechs.health}"
        )
    player_turn = False
    Magic.Bloodlust_Used = 0


def enemy_combat():
    global isEnemy
    global armor
    global player_turn

    does_enemy_hit = random.randint(1, 20) + isEnemy.Hit
    ## enemy crit
    if does_enemy_hit >= isEnemy.Crit:
        print(
            f'{isEnemy.Name} does a devestating blow of {isEnemy.Damage * 2}.')
        Mechs.health -= isEnemy.Damage * 2
## enemy hit
    elif does_enemy_hit >= Mechs.Weapon.Armor:
        Mechs.health -= isEnemy.Damage
        print(
            f"{isEnemy.Name} has struck you for {isEnemy.Damage} damage! You now have {Mechs.health} health!"
        )
## enemy miss
    elif does_enemy_hit < Mechs.Weapon.Armor:
        print(f"{isEnemy.Name} has attacked, but missed!")

    player_turn = True


## DIE

#----------------------------------------------------------------------------------
############################    FLEE!     ########################################
#----------------------------------------------------------------------------------
flee = False


def fleefunc():
    global isEnemy
    global flee

    runaway = random.randint(0, Mechs.health)
    if runaway < 5:
        runaway = 5
    noEscape = random.randint(0, isEnemy.Health)

    for fleeing in range(2):
        if runaway <= noEscape:
            print('You cannot escape!')
            break
        elif runaway == noEscape:
            temp123 = math.ceil(isEnemy.Exp * .5)
            Mechs.xp_system(temp123)
            print(
                f'You narrowly escape, and get half of the {isEnemy.Exp} enemy XP for some reason!'
            )
        else:
            print(
                'You run like the wind with your life intact but your pride shattered.'
            )
            flee = True
            break


#--------------------------------------------------------------------------------------
################################################################## ROLL WHO HIT FIRST
#--------------------------------------------------------------------------------------


def roll_initiative():
    global isEnemy

    roll = random.randint(1, 2)
    if roll == 1:
        print(
            f"You walk into the next room, and see {isEnemy.Name} facing the other direction, playing with a Rubiks cube or something. You sneak up behind it and strike!"
        )
        tsleep(2)
        player_combat()
    if roll == 2:
        print(
            f"You walk into the next room and get spooked by a {isEnemy.Name}!"
        )
        tsleep(1)
        enemy_combat()


#--------------------------------------------------------------------------------------
##################################################################### MAGIC MENU FUNCTION
#--------------------------------------------------------------------------------------


def magic():
    Magic.magic()


magic_rock = 0


def special_room():
    global magic_rock
    if Mechs.hasIronskin == True:
        combat(Enemies.Mage_Trial)
        if Mechs.health > 0:
            magic_rock = 1
    if Mechs.hasEagleEye == True:
        combat(Enemies.Archer_Trial)
    if Mechs.hasBloodlust == True:
        combat(Enemies.Berserker_Trial)
    else:
        treasure()
