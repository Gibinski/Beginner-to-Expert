# --------------------------------------------------------------
# --------------**## Decorators  prerequistes ##**--------------

# __call__() ->>>> callable


# --**--**--**--**--** Ecample 4 ->>>> a decorator
# decorator
# def operations(func):

#     def increment():
#         print("before the func")
        
#         # The execution of decrement function.
#         func()
        
#         print("after the func")
#     return increment


# decorated
# def decremen():
#     print("The number has decremented")


# decremen()
# operations(decremen)

# decoration_functiuon = operations(decremen)
# decoration_functiuon()

# --**--**--**--**--** Ecample 5 ->>>> the syntactis suger of decorator


# decorator
def operations(func):

    def increment():
        print("before the func")
        
        # The execution of decrement function.
        func()
        
        print("after the func")
    return increment


@operations
def decremen():
    print("The number has decremented")

decremen()

# @operations ==  decremen  = operations(decremen)
