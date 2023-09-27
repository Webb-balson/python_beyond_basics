def best_division(func):
    def inner(x, y):
        print(f"We're going to divide {x} and {y}.")
        if y == 0:
            print("Sorry, cannot divide")
            return
        return func(x, y)

    return inner

@best_division
def division(x, y):
    print(x/y)

division(333, 3)