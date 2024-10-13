print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

# my solution
# bill_with_pepperoni_cheese = 0
# if extra_cheese=='Y':
#     if size == 'S':
#         size_bill = 15+1
#         if pepperoni == 'Y':
#             bill_with_pepperoni_cheese = size_bill+2
#
#     elif size == 'M':
#         size_bill = 20+1
#         if pepperoni == 'Y':
#             bill_with_pepperoni_cheese = size_bill+3
#
#     else:
#         size_bill = 25+1
#         if pepperoni == 'Y':
#             bill_with_pepperoni_cheese = size_bill+3
#
# else:
#     if size == 'S':
#         size_bill = 15
#         if pepperoni == 'Y':
#             bill_with_pepperoni_cheese = size_bill + 2
#
#     elif size == 'M':
#         size_bill = 20
#         if pepperoni == 'Y':
#             bill_with_pepperoni_cheese = size_bill + 3
#
#     else:
#         size_bill = 25
#         if pepperoni == 'Y':
#             bill_with_pepperoni_cheese = size_bill + 3
#
# print(f"Your final bill is: ${bill_with_pepperoni_cheese}")

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("You have chosen an invalid size.")


if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3


if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")

