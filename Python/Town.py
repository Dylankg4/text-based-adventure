import Mechs
import Visual
import random
import math
import Quests

gold = Mechs.gold

def tsleep(egg):
  Mechs.tsleep(egg)

#-------------------------------------------------------------------------------------------
################################################################# TOWN
#-------------------------------------------------------------------------------------------

def Town():
  global magic_rock
  
  Visual.town()
  InTown = True
  if Mechs.magic_rock == 1:
    magic_rock = 1
  while InTown == True:
    print("(t) Tavern      (s) Shop\n(b) Blacksmith  (w) Wizard's Tower\n     (l) Leave Town")
    playerinput = input().lower()
    if playerinput == "t":
      Tavern()
    elif playerinput == "s":
      Merchant()
    elif playerinput == "b":
      Blacksmith()
    elif playerinput == "w":
      Tower()
    elif playerinput == "l":
      InTown = False
    else:
      print("That is not a valid input!")



#-------------------------------------------------------------------------------------------
################################################################# TAVERN
#-------------------------------------------------------------------------------------------

def Tavern():
  print('You walk up to the bar\n')
  tsleep(1)
  inBarkeep = True
  hasTalked = False
  while inBarkeep == True:
    if hasTalked == False:
      print('Ho adventurer. You looking for quests, or do you need a drink?\n')
      hasTalked = True
    print('         (L) leave               (q)      (d) [replenish stats]')
    player_input = input().lower()
    if player_input == 'l':
      print('seeya friend.\n')
      tsleep(1)
      break
    elif player_input == 'd':
      print('Drink up fella!')
      tsleep(1)
      Mechs.health = Mechs.Weapon.Maxhealth
      Mechs.mana = Mechs.maxmana
      print(f'Your health and mana max out! {Mechs.health} health, {Mechs.mana} mana.')
    elif player_input == 'q':
      print("")
      Quests.quest_menu()
    else:
      print('Speak up fella I couldnt understand you!')

#-------------------------------------------------------------------------------------------
################################################################# BLACKSMITH
#-------------------------------------------------------------------------------------------

def Blacksmith():
  inBlacksmith = True
  hastalked = False
  print("You walk into the smithy and are greeted by a very friendly man, he even has a nametag.")
  tsleep(2)
  print("You can't read it, because you can't read.")
  while inBlacksmith == True:
    if Mechs.hasIronskin == True:
      tsleep(1)
      print('''"Hey bud, hold on a second. I think the wizard's tower might be a better place for ya, I can't really do much to that wand!"''')
      inBlacksmith = False
      break
    else:
      tsleep(1)
      if hastalked == False:
        print(f'''"Hey there bud! That's a pretty nice {Mechs.Weapon.Name} you got there. For a measly 50 gold pieces, I can whack at it with my hammer and maybe make it better for ya!"''')
        print("(y) Yes       or      (n) No\n")
        hastalked = True
      elif hastalked == True:
        print(f"Want me to upgrade that {Mechs.Weapon.Name} for ya?")
        print("(y) Yes       or      (n) No\n")
      tempinput = input().lower()
      if tempinput == "y" and Mechs.gold >= 50:
        Mechs.gold -= 50
        print("Alrighty bud, wish me luck!")
        tsleep(.5)
        print("...")
        tsleep(.5)
        print("...")
        tsleep(.5)
        blacksmithluck = random.randint(1,20)
        if blacksmithluck <= 2:

          print('"Ah jeez, bud. I think I did a bad."')
          tsleep(1)
          Mechs.Weapon.Damage = math.ceil(Mechs.Weapon.Damage * .8)
          print(f'The blacksmith whacked your {Mechs.Weapon.Name} a little too hard! It now only does {Mechs.Weapon.Damage} damage.')
          tsleep(2)
          blacksmithgoodwill = random.randint(1,5)
          if blacksmithgoodwill >= 4:
            print('''"Tell ya what bud, I'm sorry about that. I'm only gonna charge you 10 gold for the labor."''')
          elif blacksmithgoodwill < 4:
            print('''"Well, that's ok I guess. It's in the past. I'll do better next time!"''')
            tsleep(1)
            print("His relentless positivity infuriates you.")
        elif blacksmithluck <= 7:
          print('"Heyo! This is looking pretty good!"')
          tsleep(.5)
          print("...")
          tsleep(.5)
          print('''"Y'know, on second thought, this is pretty much the same. But hey! At least it still works, right?"''')
          tsleep(1)
          print("Your weapon remains unchanged.")
        elif blacksmithluck > 7:
          print('"Heyo! This is looking pretty good!"')
          tsleep(.5)
          print("...")
          tsleep(.5)
          print(f'''"Yeah yeah! This is pretty good! There's a nice little twinkle to your {Mechs.Weapon.Name} now!"''')
          tsleep(1)
          print(f'''"If I had to guess, this thing is probably like ten times as good now!"''')
          tsleep(1)
          Mechs.Weapon.Damage = math.ceil(Mechs.Weapon.Damage * 1.2)
          print(f'''Your weapon now deals {Mechs.Weapon.Damage} damage, a 20% improvement.''')
      elif tempinput == "y" and Mechs.gold < 50:
        tsleep(1)
        print('''"Hey bud, I appreciate your business and all, but you don't have enough gold!""''')
        tsleep(2)
        print('''"I would do it for cheaper, but my financial advisor says I can't do afford it no more."''')
        tsleep(2)
      elif tempinput == "n":
        print('''"Okay bud! That's okay! I'll see ya around, you betcha."''')
        inBlacksmith = False
        break
      else:
        tsleep(1)
        print(f'''"I don't really know what you mean by {tempinput} bud!"''')

#-----------------------------------------------------------------------------------------
################################################################# SHOP
#-------------------------------------------------------------------------------------------

H_Potion = 0
M_Potion = 0

def Merchant():
  global gold
  gold = Mechs.gold
  inMerchant = True
  while inMerchant == True:
    print('''"What'll it be, fella?"''')
    Mechs.tsleep(1)
    print('''"Health or Mana potions?..."''')
    print('''   (h)      (m)''')
    Mechs.tsleep(1)
    print('''"I guess you could also just leave, but please don't."''')
    print('''                              (l)''')
    playerinput = input().lower()
    if playerinput == "h":
      Buy_Potion("health")
    if playerinput == "m":
      Buy_Potion("mana")
    if playerinput == 'l':
      inMerchant = False
    else:
      print("That is not a valid input!")
    
def Buy_Potion(kind):
  global gold
  global M_Potion
  global H_Potion

  if kind == "mana":
    potionbuy = M_Potion
    price = 10
  elif kind == "health":
    potionbuy = H_Potion
    price = 15
  else:
    print("Error: invalid kind entered for buy_potion function, only accepts 'mana' and 'health'")
    potionbuy = 10

  if potionbuy > 10:
    print('"Hey there buddy, leave some potions to the rest of us. You have too many already."')
    Mechs.tsleep(1)
  else:
    if gold > price:
      print('"Here ya go!"')
      Mechs.tsleep(1)
      potionbuy += 1
      gold -= price
      if kind == "mana":
        M_Potion = potionbuy
      if kind == "health":
        H_Potion = potionbuy
      print(f'You now have {potionbuy} potions. and {gold} gold')
      Mechs.gold = gold
      Mechs.M_Potion = M_Potion
      Mechs.H_Potion = H_Potion
    else:
      print('"Get outta here you broke bitch."')
      Mechs.tsleep(1)
      print("You shed a tear.")
      Mechs.tsleep(1)

#-------------------------------------------------------------------------------------------
################################################################# MAGIC TOWER
#-------------------------------------------------------------------------------------------


# Berserker Spells
  # Bloodlust - Double Damage, Half Armor, 3 turns?

# Archer Spells
  # Eagle Eye - 100% hit and crit chance, also attacks, 2 turns

# Mage Spells
  #Fire ball - ball of Fire. level 2 - flamethrower 
  #Ironskin - increase armor/maybe health?. level 2 - steelskin
  #Slow down - makes enemies attack less. leavel 2 or 3 freeze- enemy stops attacking for a few turns
  

magic_rock = 0
learned_all = False
def Tower():
  global learned_all
  global magic_rock

  Wizardin = True
  if Mechs.Weapon.Name != 'Wand':
    tsleep(1)
    print('You are not worthy of my teachings! Begone simpleton!\n')
  else:
    hastalked = False
    while Wizardin == True:
      if Mechs.hasBlizzard == True and Mechs.hasFireball == True:
        learned_all = True
      if hastalked == False:
        print('What brings you to my astral tower?')
        tsleep(1)
        hastalked == True
      print('Do you want to learn spells or upgrade your wand? Otherwise you must leave')
      print('                     (s)       (u)                                   (L)')
      playerinput = input().lower() 
      if playerinput == 's':
        print('Let me see...')
        if learned_all == True:
          print('You have learned everything that I can teach you. Go get em tiger ;) ')
        elif learned_all == False and magic_rock > 0:
          learn_spell()
        else:
          print('You do not meet my requirments to ascend your mind. Come back when you have more magic artifacts.')
          break
          
      elif playerinput == 'u':
        upgrade_wand()
      elif playerinput == 'l':
        print('Begone then!!!')
        Wizardin = False 
      else:
        print('Invalid and also stupid input. Try again dum dum :)\n')

maybeSpell = []

def learn_spell():
  global maybeSpell
  global learned_all
  global magic_rock

  print('You possess some artifacts from the dungeon. I can use this to imbue you with more power.\n')

  
  while Mechs.gold >= 50:
    if magic_rock < 1:
      print('No more rock dummy, begone.')
      break
    else:
      if Mechs.hasBlizzard == False and Mechs.gold >= 60:
        print('You can learn to blast the biting winds of the frozen mountains for 60 gold...')
        if '(b) Blizzard' not in maybeSpell:
          maybeSpell.append('(b) Blizzard')
      if Mechs.hasFireball == False:
        print('I could teach you to unleash the flames of hell for 50 gold...')
        if '(i) Ironskin' not in maybeSpell:
          maybeSpell.append('(f) Fireball')
      print('What will you learn, or would like to leave...')
      print(maybeSpell)
      choose_spell = input().lower()
      if choose_spell == 'f':
        print('The old man shows you what it means to be hot :)')
        Mechs.hasFireball = True
        Mechs.gold -= 50
        maybeSpell.remove('(f) Fireball')
        magic_rock -= 1
      elif choose_spell == 'b':
        print('The old man shows you how to blow good huehue...')
        Mechs.hasBlizzard = True
        Mechs.gold -= 60
        maybeSpell.remove('(b) Blizzard')
        print(maybeSpell)
        magic_rock -= 1
      elif choose_spell == 'l':
        break
      else:
        print("That is not a valid input!")
  if Mechs.gold < 50 and magic_rock == 1:
    print("You have the rock, but you do not have the gold!")
  print("no more spells")


def upgrade_wand():
  
  while True:
    print(f'''"Your wand can get stronger! With my expertice and 50 gold pieces it could become a powerful enchanted weapon!"''')
    print("(y) Yes       or      (n) No\n")
    tempinput = input().lower()
    if tempinput == "y" and Mechs.gold >= 50:
      Mechs.gold -= 50
      print("Upgrade ho!")
      tsleep(.5)
      print("...")
      tsleep(.5)
      print("...")
      tsleep(.5)
      blacksmithluck = random.randint(1,20)
      if blacksmithluck <= 2:

        print('"I think your wand is defective."')
        tsleep(1)
        Mechs.Weapon.Damage = math.ceil(Mechs.Weapon.Damage * .8)
        print(f'The wizard shot his magic cream onto your wand making it soggy and unable to stand up it now does a measly {Mechs.Weapon.Damage} damage.')
        tsleep(2)
        blacksmithgoodwill = random.randint(1,5)
        if blacksmithgoodwill >= 4:
          print('''"You are a good customer. I'll give you a lil somethin' for this blunder"''')
          Mechs.gold += 40
        elif blacksmithgoodwill < 4:
          print('''"Did you learn your lesson? I can't make trash stronger!"''')
          tsleep(1)
          print("What an asshole!")
      elif blacksmithluck <= 8:
        print('"Zippity bop, coolio hmmpop!"')
        tsleep(.5)
        print("...")
        tsleep(.5)
        print('''"I think I pulled something in my back this morning. I couldn't imbue your wand with any more power."''')
        tsleep(1)
        print("Your wand remains unchanged.")
      elif blacksmithluck > 8:
        print('"Shimmity skeet, you will now smell feet!"')
        tsleep(.5)
        print("...")
        tsleep(.5)
        print(f'''"My genius has made your wand much more impressive! There's a nice little twinkle to your {Mechs.Weapon.Name} now!"''')
        tsleep(1)
        print(f'''"You should tell other wizards about me so I can make more money!"''')
        tsleep(1)
        Mechs.Weapon.Damage = math.ceil(Mechs.Weapon.Damage * 1.2)
        print(f'''Your wand now deals {Mechs.Weapon.Damage} damage, a 20% improvement.''')
    elif tempinput == "y" and Mechs.gold < 50:
      tsleep(1)
      print('''"I don't work with poor people! Come back when you have money!""''')
      tsleep(2)
      break
    elif tempinput == "n":
      print('''"Hmm. Come back if you want real power!"''')
      break
    else:
      tsleep(1)
      print(f'''"are you speaking goblin? what does {tempinput} mean?"''')