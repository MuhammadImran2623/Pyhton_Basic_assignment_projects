print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 
left_right = input("You're at a cross road,which way do u want to go Right or Left?")

lower_R_L = left_right.lower()
print(lower_R_L)

if lower_R_L == 'left':
  swimm_wait =input("There is river to cross would you like to Wait for the boat or Swim ?")
  if swimm_wait.lower() == 'wait':
    print("well done you crossed and Enter to the Treasure point Choose a door from these Red,Blue,Yellow color doors ")
    doors3 =input("Which Door color you want to choose?")
    if doors3.lower() == 'yellow':
     print('Congatulations you found the treasure and Won the Game too give party to your homies')
    elif doors3.lower() == 'red':
        print("game over There is a dragon in the room you got burned by dragon Fire")
    else :
     print("Game Over! there is a Beast in that room .")
  else :
    print("Oops! you choose to swim but the crocodiles like your flesh Game over!.....")
  

else:
  print("There is a hole in right side you fell in it and your is game over")
