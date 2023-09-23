# Rules
# Rock wins against scissors.
# Scissors win against paper.
# Paper wins against rock

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
import random
print('Welcome to Rock-Paper-scissors Game:')

game_pics = [rock, paper, scissors]
choose_type = int(input('what do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors\n'))


if choose_type >=3 or choose_type <0:
  print('You type invalid number, you lose!')
else:
  print(game_pics[choose_type])

  computer_choice = random.randint(0,2)
  print('Computer Choice :')
  print(game_pics[computer_choice])
  if computer_choice == 0 and choose_type == 2:
    print('You lose')
  elif choose_type == 0 and computer_choice == 2:
    print('You win')
  elif computer_choice > choose_type :
    print('You Lose')
  elif choose_type > computer_choice:
    print('you win')
  elif choose_type == computer_choice:
    print('its a draw')



