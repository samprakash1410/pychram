class Oddnumber:
    def __iter__(self):
        self.n = 3
        return self

    def __next__(self):
        x = self.n
        self.n += 3
        return x

Oddnumber=Oddnumber()
it=iter(Oddnumber)

print(next(it))
print(next(it))
print(next(it))
print(next(it))


