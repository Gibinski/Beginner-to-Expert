# --------------------------------------------------------------
# --------------**## Decorators  prerequistes ##**--------------


# --**--**--**--**--** Ecample 1 ->>>> functions with different names
# def name1(name: str):
#     print(name)

# name1("John")

# name2 = name1
# name2("Jane")

# print(id(name1("John")))
# print(id(name2("Jane")))

# --**--**--**--**--** Ecample 2 ->>>> high er order functions
# def increment(x):
#     return x + 1

# def decrement(x):
#     return x - 1

# def operation(result, x):
#     output = result(x)

#     return output


# number_inc = operation(increment, 50)
# number_dec = operation(decrement, 10)

# print(number_inc)
# print(number_dec)


# --**--**--**--**--** Ecample 3 ->>>> a function returning another  functions

def operation():

    def increment():
        print("The number has been added")
    
    return increment


number_inc = operation()
number_inc()

operation()()