import random

# random_int = random.randint(1,10)
# print(random_int)
#
# random_decimal_0_to_1 = random.random() *10
# print(random_decimal)
#
# random_float = random.uniform(0,10)
# print(random_float)

head_or_tail = random.randint(0,1)
if head_or_tail == 0:
    print("Heads")
else:
    print("Tails")