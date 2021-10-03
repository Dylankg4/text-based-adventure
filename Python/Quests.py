import Mechs
import random

def tsleep(egg):
  Mechs.tsleep(egg)

class FetchQuest:
  def __init__(self, have, need, name, reward, whatkind):
    self.have = have
    self.need = need
    self.name = name
    self.reward = reward
    self.whatkind = whatkind

class KillQuest:
  def __init__(self, have, need, name, reward, whatkind):
    self.have = have
    self.need = need
    self.name = name
    self.reward = reward
    self.whatkind = whatkind


quest_complete = False

Template = KillQuest(
  0, # Have (leave at 0)
  5, # Need (if have >= need, quest complete)
  "name", # Name (describes goal of Quest)
  0, # quest reward
  "kill",
)

Goblins = KillQuest(
  0, # Have (leave at 0)
  2, # Need (if have >= need, quest complete)
  "Goblin", # Name (describes goal of Quest)
  100, #quest reward
  "kill",
)

Slefs = KillQuest(
  0, # Have (leave at 0)
  1, # Need (if have >= need, quest complete)
  "Slef", # Name (describes goal of Quest)
  69, # quest reward
  "kill",
)

Goobo = KillQuest(
  0, # Have (leave at 0)
  3, # Need (if have >= need, quest complete)
  "Goobo", # Name (describes goal of Quest)
  5, # quest reward
  "kill",
)

#####################################################################################
########################################################################## FETCH QUEST
#####################################################################################


Talisman = FetchQuest(
  0,
  1, 
  "Talisman", 
  100,
  "fetch"
)

Necklace = FetchQuest(
  0, # Have (leave at 0)
  1, # Need (if have >= need, quest complete)
  "Necklace", # Name (describes goal of Quest)
  0, # reward for completing quest
  "fetch"
)

Ring = FetchQuest(
  0, # Have (leave at 0)
  1, # Need (if have >= need, quest complete)
  "Ring", # Name (describes goal of Quest)
  0, # reward for completing quest
  "fetch"
)

Quests = [
  Goblins,
  Slefs,
  Goobo,

  Talisman,
  Necklace,
  Ring
]

active_quest = Template
questoffer = Template

def random_quest():
  global active_quest
  global questoffer

  questoffer = random.choice(Quests)


def killquest_check(name):
  global active_quest
  global quest_complete
  if name == active_quest.name:
    active_quest.have += 1
    if active_quest.have >= active_quest.need:
      print("Your quest is complete! Please return to the tavern to collect your reward!")
      quest_complete = True
    elif active_quest.have < active_quest.need:
      print(f"You're making progress on your quest! \nYou have killed {active_quest.have}/{active_quest.need} {active_quest.name}(s)")
  else:
    pass

def fetchquest_check():
  global active_quest
  global quest_complete
  roll = random.randint(1,10)
  if roll > 4 and active_quest.whatkind == 'fetch':
    quest_complete = True
    print(f"In the chest, you discover a {active_quest.name}, perhaps this is what the bartender was telling you about?")
  else:
    pass

def quest_turn_in():
  global active_quest
  global quest_complete

  Mechs.gold += active_quest.reward
  print(f"You gained {active_quest.reward} gold for finishing this quest!")
  active_quest.have = 0
  active_quest = Template
  quest_complete = False

def quest_menu():
  if active_quest == Template:
    quest_offer()
  elif quest_complete == True:
    quest_turn_in()
  elif active_quest != Template:
    print("Ding Dong, you're already on a quest!")
  else:
    print("Something went wrong, dunno what. lol.")

questgivernames = [
  "Bingus",
  "Jimbob",
  "Jarbon",
  "Flonk",
  "Steve",
  "Markus, but with a Q"
]

def quest_offer():
  global questoffer
  global active_quest
  global questgivernames
  questgivername = random.choice(questgivernames)

  random_quest()
  print(f'''"So I know this guy, {questgivername}, and he needs a brave adventurer like you to do some stuff for him."\n''')
  tsleep(1)
  if questoffer.whatkind == "fetch":
    print(f'''"{questgivername} lost his {questoffer.name} somewhere in the dungeon, he thinks it fell into a chest.\n"''')
    tsleep(1)
    print(f'''"He's offering {questoffer.reward} gold for your efforts."\n''')
  elif questoffer.whatkind == "kill":
    print(f'''"A couple weeks ago, {questgivername} found a really cool bug in the dungeon."\n''')
    tsleep(1)
    print('''"He named it, even. He named it 'Harvey'. I've heard many stories about Harvey."\n''')
    tsleep(1)
    print(f'''"So Harvey was doing his signature backflip trick, yeah? and out of NOWHERE, this {questoffer.name} comes up and just whacks poor Harvey right in the thorax."\n''')
    tsleep(2)
    print(f'''"Instant death, my dude."\n''')
    tsleep(1)
    print(f'''"{questgivername} just wants you to go into that dungeon, and kill {questoffer.need} goblins to get revenge for poor Harvey. Whaddaya say?"\n''')
    tsleep(2)
    print(f'''"He's offering {questoffer.reward} gold for your efforts."\n''')
  tsleep(1)
  print("type 'a' to accept, or 'd' to decline")
  playerinput = input().lower()
  if playerinput == "a":
    print('''"Great! That's a good deal. Come back here when you finish that up, I'll give ya the gold."\n''')
    active_quest = questoffer
  elif playerinput == 'd':
    print('''"That's not very cash money of you, my dude."\n''')
  else:
    print("That's not a valid input, bucko!\n")