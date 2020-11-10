class EvenNumbers:

    def __init__(self):
        self.number=2

    def __iter__(self):
        return self

    def __next__(self):
        if self.number<=10:
            evens=self.number
            self.number=self.number+2
            return evens
        else:
            raise StopIteration


e1=EvenNumbers()

print(e1.__next__())
print(next(e1))

for i in e1:
    print(i)