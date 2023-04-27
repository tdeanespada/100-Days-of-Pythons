print('''
*******************************************************************************
                                                                o .,<>., o
                                                                |\/\/\/\/|
                                                                '========'
                                                                (_ SSSSSSs
                                                                )a'`SSSSSs
                                                               /_   SSSSSS
                                                               .=## SSSSS
                                                               .####  SSSSs
                                                               ###::::SSSSS
                                                              .;:::""""SSS
                                                             .:;:'  . .  \\
                                                            .::/  '     .'|
                                                           .::( .         |
                                                           :::)           \
                                                           /\(            /
                                                          /)            ( |
                                                        .'  \  .       ./ /
                                                     _-'    |\  .        |
                                   _..--..   .  /"---\      | ` |      . |
           -=====================,' _     \=(*#(7.#####()   |  `/_..   , (
                       _.-''``';'-''-) ,.  \ '  '+/// |   .'/   \  ``-.) \
                     ,'  _.-  ((    `-'  `._\    `` \_/_.'  )    /`-._  ) |
                   ,'\ ,'  _.'.`:-.    \.-'                 /   <_L   )"  |
                 _/   `._,' ,')`;  `-'`'                    |     L  /    /
                / `.   ,' ,|_/ / \                          (    <_-'     \
                \ / `./  '  / /,' \                        /|`         `. |
                )\   /`._   ,'`._.-\                       |)            \'
               /  `.'    )-'.-,' )__)                      |\            `|
              : /`. `.._(--.`':`':/ \                      ) \             \
              |::::\     ,'/::;-))  /                      ( )`.            |
              ||:::::  . .::':  :`-(                       |/    .          |
              ||::::|  . :|  |==[]=:                       .        -       \
              |||:::|  : ||  :  |  |                      /\           `     |
  ___ ___     '|;:::|  | |'   \=[]=|                     /  \                \
 |   /_  ||``|||:::::  | ;    | |  |                     \_.'\_               `-.
 :   \_``[]--[]|::::'\_;'     )-'..`._                 .-'\``:: ` .              \
  \___.>`''-.||:.__,'     SSt |_______`>              <_____:::.         . . \  _/
                                                            `+a:f:......jrei
                                                            
************************************************************************************''')
print("Welcome to the Land of Ashura.")
print("Your mission in this new land is to get stronger and survive.") 


#Write your code below this line 👇

direction = input("You have arrived in Ashura. Which direction would you like to go? East or West? ")
direction = direction.lower()

if(direction=="east"):
  print("You have arrived in the land of the Warrior King.")
  choice1 = input("Would you like to hunt animals to get stronger or people? ")
  choice1=choice1.lower()
  
  if choice1 == "people":
    print("You have been branded a murderer by the Warrior King for killing outside the colliseum: Game Over!!!")
    
  else:
    print("Congratulations, after 10 weeks you have now leveled up to Level 70 thanks to your 'Extra EP' skill")
    challenge = input("Would you like to challenge the King for supremacy, his Head Knight to become the Kings loyal knight, or 'enlist' without fight? King, Knight, or enlist?")
    challenge = challenge.lower()
    
    if challenge == "king":
      print("The odds are in your favor as the King has already been poisoned by his mistress for forsaking their love child. You easily slay him and become the one true King!") 
      print("LONG LIVE THE KING!!!")
      print("YOU WIN!!!")
    elif challenge == "enlist":
      print("You lack heart and are hereby banished from this Kingdom! "
      print("Game Over !!!)
    elif challenge =="knight":
      print(" You managed to slay the Knight and become the Head Knight only to be tricked and killed by a jealous king. ")
      print("GAME OVER!!!")
    else:
            print("That is not a choose the King gives you. You are sentenced to death for defying the King")
    
else:
  print("You have crossed into the land of the Red Baron(a vicous royal demon), and will be killed on site")
  print("GAME OVER!!!")
  
