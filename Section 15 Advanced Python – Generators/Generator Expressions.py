# ----------------- Generator Expressions

# --**--**--**--**--** Example 3 ->>>> Creating Generator Expresion
numbers = [1, 2, 11, 9, 5, 2, 0, 12, -1, -11]

# squaring each item using list comprehension
# sqrt_nums_LC = [x**2 for x in numbers]
# print(sqrt_nums_LC)

# squering each item using generator expression
sqrt_nums_GE = (x ** 2 for x in numbers)
print(sqrt_nums_GE)

# print(next(sqrt_nums_GE))
# print(next(sqrt_nums_GE))
# print(next(sqrt_nums_GE))
# print(next(sqrt_nums_GE))
# print(next(sqrt_nums_GE))
# print(next(sqrt_nums_GE))
# print(next(sqrt_nums_GE))
# print(next(sqrt_nums_GE))
# print(next(sqrt_nums_GE))

# --**--**--**--**--** Example 4 ->>>> Generator Expresion as function argument
print(sum(x * 2 for x in numbers))

print(max(x ** 2 for x in numbers))

print(min(x for x in numbers))