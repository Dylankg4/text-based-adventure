
#
#            ADVENTURE WITH A 3 FOR AN E    
#            a cool math game (.com) by
#      8==D~~~~ binglberg  stubios ;P

import Mechs
import sys
import Visual
import Town

print('ADVENTURE WITH A 3 FOR AN E')
Mechs.tsleep(1)
print("You arrive in an unfamiliar land, having no recollection of anything...\n")
Mechs.tsleep(2)
print("The world is pretty flat, save for a village to your left and a funky looking rock labelled 'Dungeon' to your right.\n")
Mechs.tsleep(3)
while Mechs.has_weapon == False:
  Mechs.ChooseWeapon()
mmd = False
## Useful variable to break the while loop
isRunning = True
while isRunning == True:
  ## MAIN GAME BODY
  print("GO TO TOWN, DUNGEON, QUIT, OR VIEW STATS!")
  print("      (t)     (d)    (q)            (s)")
  if mmd == False:
    Visual.mainmenu()
    mmd = True
  playerinput = input()
  if playerinput == "town" or playerinput == "t":
    Town.Town()
    mmd = False
  elif playerinput == "dungeon" or playerinput == "d":
    Mechs.Go_Dungeon()
    mmd = False
    while Mechs.health <= 0:
      if Mechs.PlayerQuit == True:
        print("Your journey is over for now")
        isRunning = False
        break
      Mechs.deathmenu()
  elif playerinput == "stats" or playerinput == "s":
    Mechs.get_player_stats()
  elif playerinput == "give me money":
    Mechs.gold += 100
    print("ok")
  elif playerinput == "give me rock":
    Town.magic_rock = 1
    print("ok")
  elif playerinput == "can i get a level up please":
    print("ok")
    Mechs.LevelUp()
  elif playerinput == "quit" or playerinput == "q":
    #Use one statement or the other depending on how this while statement turns out
    print("Bye bye!")
    sys.exit()
  else:
    print("That is not a valid input!")


sys.exit()