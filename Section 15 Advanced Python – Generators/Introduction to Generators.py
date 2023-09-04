# ----------------- Introduction to Generators

# __iter__() and __next__() are implemented automaticly


"""
Normal Func --**--**--**--**--**
1- rturn
2- after the return, the varialble are garbage collected 
3- return terminates a func
4- performs a task or calculates a value

Geb Func --**--**--**--**--**
1- yield
2- acces ti variables after func execution
3- yild does not terminates a func
4- returs an iterator object
"""

# --**--**--**--**--** Example 1 ->>>> creating a generator
def first_generator():
    x = 1
    print("1st iteration")
    yield x

    x += 1.1
    print("2nd iteration")
    yield x

    x += 1.2
    print("3rd iteration")
    yield x


my_gen = first_generator()
# print(my_gen)
# print(type(my_gen))

# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))

# --**--**--**--**--** Example 2 ->>>> using a for loop
for element in first_generator():
    print(element)
