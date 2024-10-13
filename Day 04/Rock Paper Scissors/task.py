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

# my_method
# list1 = [rock, paper, scissors]
# rock_paper_scissors = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
# print(list1[rock_paper_scissors])
#
# import random
# choice_by_pc = random.randint(0,2)
# print(f"Computer chose: {list1[choice_by_pc]}")
#
# # rock < paper, rock > scissors
# if rock_paper_scissors == 0:
#     if rock_paper_scissors == choice_by_pc:
#         print("It's a draw")
#     elif rock_paper_scissors < choice_by_pc and rock_paper_scissors == choice_by_pc-1:
#         print("You lose")
#     else:
#         print("You win!")
#
# if rock_paper_scissors == 1:
#     if rock_paper_scissors == choice_by_pc:
#         print("It's a draw")
#     elif rock_paper_scissors < choice_by_pc:
#         print("You lose")
#     else:
#         print("You win!")
#
# if rock_paper_scissors == 2:
#     if rock_paper_scissors == choice_by_pc:
#         print("It's a draw")
#     elif rock_paper_scissors > choice_by_pc and rock_paper_scissors-2 == choice_by_pc:
#         print("You lose")
#     else:
#         print("You win!")

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# Note: it's worth checking if the user has made a valid choice before the next line of code.
# If the user typed somthing other than 0, 1 or 2 the next line will give you an error.
# You could for example write:
# if user_choice < 0 or user_choice > 2:
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("It's a draw!")



















