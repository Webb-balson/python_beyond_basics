

def my_gen_func():
    print("First Value")
    yield 20

    print("Second Value")
    yield 40

    print("Third Value")
    yield 60

my_gen = my_gen_func()

print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
# print(next(my_gen))