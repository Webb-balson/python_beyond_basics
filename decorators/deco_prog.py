

def calling():
    print("Outer Func")
    def what():
        print("Inner Func")
    return what

# print(calling())

new = calling()
new()