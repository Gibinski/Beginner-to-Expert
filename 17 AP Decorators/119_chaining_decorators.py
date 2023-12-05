# --------------------------------------------------------------
# --------------**## Arguments and keywords arguments ##**--------------


# --**--**--**--**--** Ecample 10 
def info_name(func):

    def full_name(*args):
        
        func(*args)

    return full_name


def info_last_name(func):
    
    def full_name(*args):
        
        func(*args)

    return full_name


@info_last_name
@info_name
def info(name, lastname):
    print(f"My full name ist {name} {lastname}.")

info("Lyubomir", "Gibinski")