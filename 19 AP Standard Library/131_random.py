# ---------------------------------------------------------------------
# ---------------**## Working with random values ##**-----------------------
import random
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# *-*-*---*-**-*--*-*-*-* Between zero and one
# print(random.random())

# *-*-*---*-**-*--*-*-*-* Between two arbitrary numbers
# print(random.randint(1, 50))

# *-*-*---*-**-*--*-*-*-* Randomly choosing a list item
# print(random.choice(numbers))

# *-*-*---*-**-*--*-*-*-* Randomly choosing multiplye list items
# print(random.choices(numbers, k=2))
# print(random.choices(numbers, k=5))
# print(random.choices(numbers, k=15))

# *-*-*---*-**-*--*-*-*-* Shuffling a list
random.shuffle(numbers)
print(numbers)
