def my_loop(num):
    for i in range(num):
        yield i

my_num = my_loop(5)

print(next(my_num))
print(next(my_num))
print(next(my_num))
print(next(my_num))
print(next(my_num))
print(next(my_num))
