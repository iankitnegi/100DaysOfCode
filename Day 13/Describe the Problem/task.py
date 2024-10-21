# def my_function():
#     for i in range(1, 20):
#         if i == 20:
#             print("You got it")
#
#
# my_function()

# Describe the Problem - Write your answers as comments:
# 1. What is the for loop doing? : 'i' will never reach to 20 because in range(1, 20) 20 is exclusive
# 2. When is the function meant to print "You got it"? : when i reaches at 20
# 3. What are your assumptions about the value of i? : 'i' starts with 1


def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")


my_function()