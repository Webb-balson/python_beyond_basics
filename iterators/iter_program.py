

class NewNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

    
myclass = NewNumbers()

myiter = iter(myclass)

# To print all numbers
for i in myiter:
    print(i)

# To print a single number or raising StopIteration exception
print(next(myiter))
