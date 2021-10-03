import math

#--------------------------------------------------------------------------------------
########################################################################### Enemy Class
#--------------------------------------------------------------------------------------

class enemy:
  def __init__(self, Damage, Hit, Crit, Name, Armor, Catchphrase, Health, Exp):
    self.Damage = Damage
    self.Hit = Hit
    self.Crit = Crit
    self.Name = Name
    self.Armor = Armor
    self.Catchphrase = Catchphrase
    self.Health = Health
    self.Exp = Exp

#class bigenemy(enemy):

#--------------------------------------------------------------------------------------
######################################################################### Enemy Objects
#--------------------------------------------------------------------------------------

# Enemies sorted by difficulty sort of
# Goobo
# Goblin
# Wolf
# Slef
# Bingus
# Gorblin_Ramsay
# Dragon
# 
#

Template = enemy(
  0, # Damage
  0, # Hit (added to d20)
  0, # Crit (chance to crit, difference between x and 20 out of 20)
  0, # Name
  0, # Armor (Chance to take damage)
  0, # Catchphrase (put a new line in here if you want an approach line and a taunt)
  0, # Health
  0, # Exp (xp gained on enemy defeated)
)

Goblin = enemy(
  3, 
  1, 
  17, 
  'Goblin', 
  5, 
  'A goblin strolls on up to you and whispers in your ear, \n"Pee in butt"', 
  30, 
  15
)

Wolf = enemy(
  2, 
  1, 
  17, 
  'Wolf', 
  1, 
  'A wolf approaches! \n "Grrrr"', 
  30, 
  18
)


Goobo = enemy(
  4, 
  0, 
  22, 
  'Goobo', 
  5, 
  "The homie Goobo has joined the battle! \nBooger boy comin' at ya",
  6, 
  8
)

Slef = enemy(
  5, 
  1, 
  17, 
  'Slef', 
  7, 
  'Slef has appeared! \n"I am a mistake"', 
  40, 
  20
)

Bingus = enemy(
  8, # Damage
  2, # Hit (added to d20)
  18, # Crit (chance to crit, difference between x and 20 out of 20)
  "Bingus", # Name
  13, # Armor (Chance to take damage)
  'Bingus is your foe! \n "Bingus!!!"', # Catchphrase (put a new line in here if you want an approach line and a taunt)
  1, # Health
  35, # Exp (xp gained on enemy defeated)
)

Gorblin_Ramsay = enemy(
  16, 
  2, 
  18, 
  "Gorblin Ramsay", 
  69,
  '''A Greasy, Tall, Handsome Goblinoid Strolls up too you with great confidence. It's celebrity chef Gorblin Ramsay!'s\n "Get the fuck out of my kitchen"''', 
  180, 
  420
)

Dragon = enemy(
  20, # Damage
  11, # Hit (added to d20)
  15, # Crit (chance to crit, difference between x and 20 out of 20)
  'Dragon', # Name
  17, # Armor (Chance to take damage)
  'Deez nuts bruddah', # Catchphrase (put a new line in here if you want an approach line and a taunt)
  120, # Health
  1000, # Exp (xp gained on enemy defeated)
)

Mage_Trial = enemy(
  7, # Damage
  10, # Hit (added to 20)
  21, # Crit (chance to crit, difference between x and 20 out of 20)
  "Spectral Being", # Name
  10, # Armor
  "Magic Dust hangs in the air as a spectral being emerges", # Catchphrase
  60, # Health
  400, # Exp
)

Archer_Trial = enemy(
  8, # Damage
  9, # Hit (added to d20)
  19, # Crit (chance to crit, difference between x and 20 out of 20)
  'Cool fellow', # Name
  11, # Armor (Chance to take damage)
  "Hey man can you spare me a cig?", # Catchphrase (put a new line in here if you want an approach line and a taunt)
  150, # Health
  400, # Exp (xp gained on enemy defeated)
)

Berserker_Trial = enemy(
  13, # Damage
  -5, # Hit (added to d20)
  10, # Crit (chance to crit, difference between x and 20 out of 20)
  "Glenn", # Name
  0, # Armor (Chance to take damage)
  'A mysterious man sits in the middle of the dungeon, he looks absolutely fuckin shitfaced lol. \n"HEYO, GLENN HERE, BE CAREFUL BRO."', # Catchphrase (put a new line in here if you want an approach line and a taunt)
  65, # Health
  400, # Exp (xp gained on enemy defeated)
)


EnemyList = [Goblin, Wolf, Gorblin_Ramsay, Goobo, Slef]
