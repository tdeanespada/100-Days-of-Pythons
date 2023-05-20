import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
computer_chose = random.randint(0,2)


game_images = [rock,paper,scissors]
choice = int(choice)
 

if choice >= 3 or choice < 0:
    print("You typed an invalid number, you lose!")
elif computer_chose ==0 and choice ==2:
    print(f"Computer choice: \n {game_images[computer_chose]}\n Your choice:   {game_images[choice]} ")
    print("You lose!")
elif computer_chose ==2 and choice ==0:
    print(f"Computer choice:  \n {game_images[computer_chose]}\n Your choice:   {game_images[choice]} ")
    print("You win!")
elif choice > computer_chose:
    print(f"Computer choice:  \n {game_images[computer_chose]}\n Your choice:   {game_images[choice]} ")
    print("You win!")
elif choice < computer_chose:
    print(f"Computer choice:  \n {game_images[computer_chose]}\n Your choice:   {game_images[choice]} ")
    print("You lose!")
elif computer_chose==choice:
    print("Draw!")


