# --------------------------------------------------------------
# --------------**## Arguments and keywords arguments ##**--------------


# # --**--**--**--**--** Ecample 7 ->>>> *args
# def multiply(func):

#     def digits(*args):

#         func(*args)

#     return digits

# @multiply
# def operation(x, y, z):
#     print(x* y *z)

# operation(10, 20, 30)


# # --**--**--**--**--** Ecample 8 ->>>> *args
# def do_aretmetic(func):

#     def number(*numbers):
#         func(*numbers)

#     return number

# @do_aretmetic
# def operation(x, y, z, a, b, c):
#     print((a / b) + z + (x + y) / c)


# operation(100, 200, 300, 400, 500, 600)


# --**--**--**--**--** Ecample 9 ->>>> **kwargs
def do_aretmetic(func):

    def number(**kwargs):
        func(**kwargs)

    return number


@do_aretmetic
def operation(x, y, z, a, b, c, m, n, o):
    print(((a / b) * m + z * n + (x / o + y) / c + m * n + o) / o - n)

operation(x=100, y=200, z=300, a=400, b=500, c=600, m=700, n=800, o=900)