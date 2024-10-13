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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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

left_right = input("You're at a cross road. Where do you want to go?\n \tType 'left' or 'right': ").lower()
if left_right == "left":
    wait_swim = input("You've come to a lake. There is an island in the middle of the lake.\n \tType 'wait' to wait for a boat. Type 'swim' to swim across: ").lower()

    if wait_swim == "wait":
        yellow_red_blue = input("You arrive at the island unharmed. There is a house with 3 doors.\n \tOne red, one yellow and one blue. Which colour do you choose? ").lower()
        if yellow_red_blue == "yellow":
            print("You found the treasure! You Win!")
        elif yellow_red_blue == "red":
            print("Burned by fire.\n \tGAME OVER")
        elif yellow_red_blue == "blue":
            print("Eaten by beasts.\n \tGAME OVER")
        else:
            print("GAME OVER")

    elif wait_swim == "swim":
        print("Attacked by trout.\n \tGAME OVER")
    else:
        print("Attacked by trout.\n \tGAME OVER")

elif left_right == "right":
    print("Fall into a hole.\n \tGAME OVER")
else:
    print("Fall into a hole.\n \tGAME OVER")