def new_pretty(func):
    def new_inner():
        print("Hi, I am decorated")
        func()
    return new_inner


# def the_normal():
#     print("I am normal func")

# print(new_pretty(the_normal)())

# Decorating function
@new_pretty
def the_normal():
    print("What just happened")

print(the_normal())
