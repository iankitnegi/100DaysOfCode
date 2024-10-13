friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

import random
#Option 1
random_integer = random.randint(0,4)
print(friends[random_integer])

#Option 2
print(random.choice(friends))
