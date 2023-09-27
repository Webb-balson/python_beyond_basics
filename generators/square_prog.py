# yielding square of a number

def square(i):
    for i in range(i):
        yield i*i

my_gen = square(5)

while True:
    try:
        print(f"Result ==>> {next(my_gen)}")
    except StopIteration:
        print("Iterated all objects")
        break

# using for loop
# for i in my_gen:
#     print(f"Result ==>> {i}")