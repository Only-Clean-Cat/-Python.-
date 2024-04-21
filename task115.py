class EvenNumbers():
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.i = 0

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        self.i += 1
        if self.i >= self.start:
            if self.i % 2 == 0:
                if self.i > self.end:
                    raise StopIteration()
                return self.i
en = EvenNumbers(10, 25)
for i in en:
    if i is not None:
        print(i)
