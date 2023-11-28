# --------------------------------------------------------------
# --------------**## Decorators  prerequistes ##**--------------


# --**--**--**--**--** Ecample 6 ->>>> function with parameters

# def operation(x, y):
#     return x /  y


# print(operation(10, 20))
# print(operation(101, 32))
# print(operation(45, 0))


# to use decorator
def operation(func):
    def inner(x, y):
        print(f"{x} / {y} = ", end="")

        if y == 0:
            print()
            print("cannot divide be zero")
            return

        return func(x, y)
    return inner

@operation
def divide(x, y):
    print(x / y)

divide(2, 5)
print()
divide(20, 5)
print()
divide(72, 0)
