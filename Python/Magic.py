import random
import Mechs
import Dungeon
import math

def tsleep(thyme):
  Mechs.tsleep(thyme)

#----------------------------------------------------------------------------------------
########################################################################## MAGIC MENU
#----------------------------------------------------------------------------------------

def magic():
  
  magicmenu = True
  while magicmenu == True:
    print("Cast a spell, little bitch boi")
    print("type 'esc' to go back")
    if Mechs.hasFireball == True:
      print("f - Fireball")
    if Mechs.hasBlizzard == True:
      print("b - Blizzard")
    if Mechs.hasIronskin == True:
      print("i - Ironskin")
    if Mechs.hasBloodlust == True:
      print("b - Bloodlust")
    if Mechs.hasEagleEye == True:
      print("e - Eagle Eye")
    tempinput = input().lower()
    if tempinput == "f" and Mechs.hasFireball == True:
      Fireball()
      magicmenu = False
      break
    if tempinput == "b" and Mechs.hasBlizzard == True:
      Blizzard()
      magicmenu = False
      break
    if tempinput == "i" and Mechs.hasIronskin == True:
      Harden()
      magicmenu = False
      break
    if tempinput == "b" and Mechs.hasBloodlust == True:
      Bloodlust_Cast()
      magicmenu = False
      break
    if tempinput == "e" and Mechs.hasEagleEye == True:
      Eagle_Eye_Cast()
      magicmenu = False
      break
    elif tempinput == "esc":
      magicmenu = False
      break
    else:
      print("That is not a valid input, stinky!")


#---------------------------------------------------------------------------------
########################################################## Magic functions
#--------------------------------------------------------------------------------

def Fireball():

  global Enemy_Is_Burning

  damage = random.randint(math.ceil(Mechs.Weapon.Damage * 1.3),Mechs.Weapon.Damage * 2)
  hit = random.randint(1,5)
  
  if Mechs.mana <= 5:
    print('You cannot summon the strength to cast this magic!')
  else:
    print(f'You cast a fireball and aim it at {Dungeon.isEnemy.Name}, consuming 5 mana!')
    Mechs.mana -= 5
    Dungeon.player_turn = False
    if hit <= 2:
      print('Your fireball gracefully flies over the enemies head...')
    else:
      print(f'Your fireball consumes the enemy for a few seconds doing {damage} damage!')
      Dungeon.isEnemy.Health -= damage
      if hit == 5:
        print(f'{Dungeon.isEnemy.Name} is burning!')
        Enemy_Is_Burning = 3


def Blizzard():

  global Enemy_Is_Frozen
  global Enemy_Is_Burning
  
  freeze = random.randint(1,8)
  damage = random.randint(math.ceil(Mechs.Weapon.Damage * 1.2),math.ceil(Mechs.Weapon.Damage * 1.8))

  if Mechs.mana <= 10:
    print('You cannot muster the energy to summon a freezing gale!')
  else:  
    print(f'You summon a freezing wind and rain it down on {Dungeon.isEnemy.Name} consuming 10 mana!')
    Mechs.mana -= 10
    Dungeon.player_turn = False
    if freeze <= 3:
      print(f'The freezing wind was not enough to damage {Dungeon.isEnemy.Name}!')
    else: 
      print(f'You manage to shred {Dungeon.isEnemy.Name} with ice and wind!')
      Dungeon.isEnemy.Health -= damage
      if Dungeon.isEnemy.Health > 0:
        if freeze >= 4:
          print(f'{Dungeon.isEnemy.Name} froze solid!')
          Enemy_Is_Frozen = 2
          Dungeon.player_turn = True
          if Enemy_Is_Burning > 0:
            print(f"You put out the flame on {Dungeon.isEnemy.Name}")
            Enemy_Is_Burning = 0

temparmor = 0
def Harden():
  global health
  global temparmor
  global Ironskin
  if Mechs.mana < 10:
    print("You don't have enough mana for this!")
  else:
    print("You cast ironskin, consuming 10 mana!")
    Mechs.mana -= 10
    if Ironskin == 0:
      temparmor = Mechs.Weapon.Armor
      Mechs.Weapon.Armor += 6
      print(f'You are hard. {Mechs.Weapon.Armor} hard. ;)')
      Ironskin = 3
    elif Ironskin > 0:
      Ironskin = 3
      print('You recast your Ironskin spell!')
      


temphit = 0
tempcrit = 0
EE_Used = 0

def Eagle_Eye_Cast():
  ## storing temporary values for hit and crit to turn them back to normal when EE wears off
  global temphit
  global tempcrit
  global EE_Used
  global Eagle_Eye

  Eagle_Eye = 3

  temphit = Mechs.Weapon.Hit
  tempcrit = Mechs.Weapon.Crit
  if EE_Used == 0:
    EE_Used -= 1
    Dungeon.player_turn = True
    Mechs.Weapon.Hit = 100
    Mechs.Weapon.Crit = 100
    print('Your eyes become the eyes of an EAGLE!\n')
    print('You will never miss, and always do critical damage!\n')
  else:
    print('You cannot use this ability anymore!')

Bloodlust_Used = 0
def Bloodlust_Cast():
  global Bloodlust_Used

  Bloodlust_Used = 1
  temphealth = Mechs.health
  Mechs.health -= math.floor(Mechs.health *.75)
  healthlost = temphealth - Mechs.health
  print("You have used Bloodlust!")
  tsleep(1)
  print(f"You lost {healthlost} health and you now have {Mechs.health} health!")
  Dungeon.player_turn = False
  Dungeon.player_combat()

#----------------------------------------------------------------------------------
############################################################### Status Effects
#----------------------------------------------------------------------------------

Eagle_Eye = 0
Bloodlust = 0
Enemy_Is_Burning = 0
burn_damage = 0
Enemy_Is_Frozen = 0
Ironskin = 0
Eagle_Eye_Wearoff = False

def Status_Effects():
  global Eagle_Eye
  global Bloodlust_Used
  global Enemy_Is_Burning
  global Enemy_Is_Frozen
  global Ironskin

  if Bloodlust_Used == 1:
    Bloodlust_Used = 0

  if Eagle_Eye > -1:
    SE_Eagle_Eye()
    Eagle_Eye -=1
  if Enemy_Is_Burning > 0:
    SE_Enemy_Is_Burning()
    Enemy_Is_Burning -=1
  if Enemy_Is_Frozen > 0:
    Enemy_Is_Frozen -=1
  if Ironskin > 0:
    SE_Ironskin()
    Ironskin -=1

def SE_Combat_End():
  global Eagle_Eye
  global Bloodlust
  global Enemy_Is_Burning
  global Enemy_Is_Frozen
  global Ironskin
  
  if Ironskin > 0:
    SE_End_Ironskin()
  if Eagle_Eye > 0:
    SE_End_Eagle_Eye()

  Eagle_Eye = 0
  Bloodlust = 0
  Enemy_Is_Burning = 0
  Enemy_Is_Frozen = 0
  Ironskin = 0

def SE_End_Eagle_Eye():
  global temphit
  global tempcrit
  
  Mechs.Weapon.Hit = temphit
  Mechs.Weapon.Crit = tempcrit

  



def SE_End_Ironskin():
  global temparmor

  Mechs.Weapon.Armor = temparmor
  


def SE_Eagle_Eye():
  global Eagle_Eye
  global Eagle_Eye_Wearoff
  global temphit
  global tempcrit

  
  if Eagle_Eye_Wearoff == True:
    Mechs.Weapon.Hit = temphit
    Mechs.Weapon.Crit = tempcrit
    print('Your eyes become normal again!')

  elif Eagle_Eye == 1:
    print("Your Eagle Eye has only one attack left, make it count!")
    Eagle_Eye_Wearoff = True
  elif Eagle_Eye > 1:
    print(f"Your Eagle Eye is active for {Eagle_Eye} more turns!")


def SE_Enemy_Is_Burning():
  global burn_damage

  global player_turn

  burn_damage = random.randint(2,4)
  Dungeon.isEnemy.Health -= burn_damage

  print(f"{Dungeon.isEnemy.Name} burns for {burn_damage} points of damage, bringing it down to {Dungeon.isEnemy.Health} health!")

  if Dungeon.isEnemy.Health <= 0:
    Dungeon.player_turn = False

def SE_Enemy_Is_Frozen():

  
  print(f"{Dungeon.isEnemy.Name} is frozen by your magic!")
  
  
def SE_Ironskin():
  global Ironskin

  if Ironskin > 1:
    print(f"Your skin is as hard as metal for {Ironskin - 1} more turns!")
  if Ironskin == 1:
    SE_End_Ironskin()
    print(f"You feel your skin start to soften. You go back to {Mechs.Weapon.Armor} armor.")