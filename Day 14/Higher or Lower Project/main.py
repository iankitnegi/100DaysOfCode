# import random
# import game_data
# import art
#
# def compare_a():
#     dict_a = random.choice(game_data.data)
#     print(f"Compare A: {dict_a['name']}, a {dict_a['description']}, from {dict_a['country']}.")
#     #print(f"Follower: {dict_a['follower_count']}")
#     return dict_a['follower_count']
#
# def compare_b():
#     dict_b = random.choice(game_data.data)
#     print(f"Against B: {dict_b['name']}, a {dict_b['description']}, from {dict_b['country']}.")
#     #print(f"Follower: {dict_b['follower_count']}")
#     return dict_b['follower_count']
#
# print(art.logo)
# follower_count_of_a = compare_a()
# print(art.vs)
# follower_count_of_b = temp = compare_b()
#
# if follower_count_of_a != follower_count_of_b:
#     flag = 1
#     score = 0
#     while flag == 1:
#
#         # if score == -1:
#         #     print(art.logo)
#         #     follower_count_of_a = compare_a()
#         #     print(art.vs)
#         #     follower_count_of_b = compare_b()
#
#         user_input = input("Who has more followers? Type 'A' or 'B': ").upper()
#         if user_input == 'A':
#             if follower_count_of_a > follower_count_of_b:
#                 score += 1
#                 print(art.logo)
#                 print(f"You're right! Current score: {score}.")
#
#
#
#
#                 follower_count_of_a = compare_a()
#                 print(art.vs)
#                 follower_count_of_b = compare_b()
#             else:
#                 print(art.logo)
#                 print(f"Sorry, that's wrong. Final score: {score}")
#                 break
#
#         elif user_input == 'B':
#             if follower_count_of_b > follower_count_of_a:
#                 score += 1
#                 print(art.logo)
#                 print(f"You're right! Current score: {score}.")
#                 follower_count_of_a = compare_a()
#                 print(art.vs)
#                 follower_count_of_b = compare_b()
#             else:
#                 print(art.logo)
#                 print(f"Sorry, that's wrong. Final score: {score}")
#                 break
#
#         else:
#             print(art.logo)
#             print(f"Sorry, that's wrong. Final score: {score}")
#             break

def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"


def check_answer(a_followers, b_followers):
    """Take a user's guess and the follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

from art import logo, vs
import random
from game_data import data

print(logo)
score = 0
game_should_continue = True
# Generate a random account from the game data
account_b = random.choice(data)

# Make the game repeatable.
while game_should_continue:

    # Making account at position B become the next account at position A.
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    # Ask user for a guess.
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Clear the screen
    print("\n" * 20)
    print(logo)

    # - Get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    # Check if user is correct.
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Give user feedback on their guess.
    # score keeping.
    if is_correct:
        score += 1
        print(f"You're right! Current score {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        game_should_continue = False
