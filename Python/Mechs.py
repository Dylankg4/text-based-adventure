

import random
import copy
import sys
import time
import math
import Visual
import Dungeon
import Quests

H_Potion = 0
M_Potion = 0
gold = 10
Weapon = ()
equip = ()
xp_have = 0
xp_needed = 50
level = 1
PlayerQuit = False
has_quest_item = False
has_key = False
mana = 50
maxmana = 50

def tsleep(thyme):
  #thyme = thyme *.25
  #time.sleep(thyme)
  thyme = ()
  pass

magic_rock = 0
def Go_Dungeon():
  global magic_rock
  Dungeon.Dungeon()
  if Dungeon.magic_rock == 1:
    magic_rock = 1

# Magic Initialize
hasEagleEye = False
hasBloodlust = False
hasFireball = False
hasBlizzard = False
hasIronskin = False

#--------------------------------------------------------------------------------------
########################################################################## Weapon Class
#--------------------------------------------------------------------------------------

class WeaponType:
  def __init__(self, Damage, Hit, Crit, Name, Action, Maxhealth, Armor, Projectile):
    self.Damage = Damage
    self.Hit = Hit
    self.Crit = Crit
    self.Name = Name
    self.Action = Action
    self.Maxhealth = Maxhealth
    self.Armor = Armor
    self.Projectile = Projectile

#--------------------------------------------------------------------------------------
######################################################################## Weapon Objects
#--------------------------------------------------------------------------------------

Sword = WeaponType(7, 0, 18, "Sword", "You swing your sword,", 30, 10, 'sword')
Bow = WeaponType(10, -5, 14, "Bow", "You shoot an arrow at your foe,", 20, 6, 'arrow')
Wand = WeaponType(5, 20, 41, "Wand", "You shoot some magic dust at your enemy,", 20, 5, 'magic bolt')
has_weapon = False

#--------------------------------------------------------------------------------------
############################################## Choose weapon function to start the game
#--------------------------------------------------------------------------------------

def ChooseWeapon():
  global equip
  global has_weapon
  global Weapon
  global health
  global hasFireball
  global hasBlizzard
  global hasIronskin
  global hasEagleEye
  global hasBloodlust

  print('"HEY KID," you hear a voice call from behind you.\n')
  tsleep(2)
  print("...\n")
  tsleep(1)
  print('"YOU LOOK LIKE A MiiIIIIIIIGHTY FINE ADVENTURER IF I DO SAY SO MYSELF." you turn around to see a scraggly old man with no bones, a puddle on the floor with a face speaking to you.\n')
  tsleep(5)
  print('"TELL ME SOMETHING, BOI." You hold back tears.\n')
  tsleep(3)
  print('"WHAT KINDA ADVENTURER ARE YA? DO YA LIKE TO UHHHHHHHHHH, SHOOT BOW??? FUCKIN UHHHHHHHH HIT EM WITH A BASEBALL BAT? SHOOT MAGIC DUST?" You try to ignore it.\n')
  tsleep(2)
  print('"TELL ME, PLEASE."\n')
  tsleep(2)
  has_weapon = False
  while has_weapon == False:
    equip = input("Choose your class!: Archer!, Berserker!, or Wizard! \n").lower()
    if equip == "berserker" or equip == 'b':
      Weapon = Sword
      print(f'''\n"HEY HEY, ME TOO. I AM ALSO THAT CLASS. HERE KID, I GOT A SPARE {Weapon.Name.upper()} FOR YA" A {Weapon.Name} oozes out of the side of the man, you do not know what to feel, or how to feel anymore. You grab it.\n''')
      tsleep(2)
      health = Weapon.Maxhealth
      has_weapon = True
      hasBloodlust = True
    elif equip == "archer" or equip == 'a':
      has_weapon = True
      Weapon = Bow
      print(f'''\n"HEY HEY, ME TOO. I AM ALSO THAT CLASS. HERE KID, I GOT A SPARE {Weapon.Name.upper()} FOR YA" A {Weapon.Name} oozes out of the side of the man with some chuncks of the goopy man still on it. You do not know what to feel, or how to feel anymore. You grab it.\n''')
      tsleep(2)
      health = Weapon.Maxhealth
      hasEagleEye = True
    elif equip == "wizard" or equip == 'w':
      has_weapon = True
      Weapon = Wand
      print(f'''\n"HEY HEY, ME TOO. I AM ALSO THAT CLASS. HERE KID, I GOT A SPARE {Weapon.Name.upper()} FOR YA" A {Weapon.Name} oozes out of the side of the man, magic dust glistens in his eyes. You do not know what to feel, or how to feel anymore. You grab it.\n''')
      tsleep(2)
      health = Weapon.Maxhealth
      hasIronskin = True
    elif equip == "wand":
      has_weapon = True
      Weapon = Wand
      print(f"You have selected {Weapon.Name}")
      health = Weapon.Maxhealth
    else:
      print(f"Ay bruh, '{equip}' is not a valid class, try again")
      has_weapon = False

#--------------------------------------------------------------------------------------
############################################################## Experience Gain Function
#--------------------------------------------------------------------------------------

def xp_system(xp_gain):
  global level
  global xp_have
  global xp_needed
  global isEnemy

  Dungeon.flv_xp += xp_gain

  xp_have = xp_have + xp_gain
  while xp_have >= xp_needed:
    LevelUp()
    xp_have = xp_have - xp_needed
    xp_needed = math.ceil(xp_needed * 1.2)

#--------------------------------------------------------------------------------------
################################################################## Level Up Function :)
#--------------------------------------------------------------------------------------

def LevelUp():
  global health
  global Weapon
  global level
  global mana
  global maxmana
  global hasIronskin

  ## changing player stats
  Weapon.Maxhealth = math.ceil(Weapon.Maxhealth *1.2)
  health = Weapon.Maxhealth

  Weapon.Hit = int(Weapon.Hit) + 1
  if hasIronskin == True:
    maxmana = math.ceil(maxmana * 1.1)
    mana = maxmana
  ## setting maximum hit value
  if Weapon.Hit >= 19:
    Weapon.Hit = 18
    print(f"Congration, you done it. \nYou can't get more accurate but you can handle up to {Weapon.Maxhealth} points of damage before fuckin dying lol")
    if hasIronskin == True:
      print(f"Also you have {mana} max mana now")
  else:
    print(f"Conglaturations you're health is now {health} and you're damage is now {Weapon.Damage}, also you're hit chance has increased!")
    if hasIronskin == True:
      print(f"Also you have {mana} max mana now")
  level = level + 1

#--------------------------------------------------------------------------------------
###################################################################### GET PLAYER STATS
#--------------------------------------------------------------------------------------

def get_player_stats():
  print(f"""You are level {level}\n\
  The mighty {Weapon.Name} you wield does a whopping {Weapon.Damage} damage, \n\
  and you have {health}/{Weapon.Maxhealth} health!""")
  print(f"You have {gold} gold in your pretty pink purse.")
  print(f"You have {M_Potion} mana potions and {H_Potion} health potions.")
  if magic_rock > 0:
    print(f"You have {magic_rock} magic rock.")
  if Quests.active_quest != Quests.Template:
    print(f"You are on a quest! You have {Quests.active_quest.have}/{Quests.active_quest.need}  {Quests.active_quest.name}!")
  if Quests.active_quest == Quests.Template:
    print(f"You are not on a quest! Go to the tavern")

#--------------------------------------------------------------------------------------
############################################################################ DEATH MENU  
#--------------------------------------------------------------------------------------

PlayerHasDied = False

def deathmenu():
  global health
  global PlayerQuit
  global PlayerHasDied

  print('Would you like to try again? [Yes, No]')
  
  while True:
    deathinput = input().lower()
    if deathinput == 'yes' or deathinput == 'y':
      print('You have returned to this world, weak, but ready to persevere')
      ## Re initialize the character???
      health = math.ceil(Weapon.Maxhealth *.5)
      print(f'You now have a measly {health} out of {Weapon.Maxhealth} health...')
      PlayerHasDied = True
      break
    elif deathinput == 'no' or deathinput == 'n':
      PlayerQuit = True
      break
    else:
      print("That's not a valid input!!!!!! FUCKIN WEEEEEEEB \n")

