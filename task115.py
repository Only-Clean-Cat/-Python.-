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
                result = self.i
                if self.i > self.end:
                    raise StopIteration()
                return result
en = EvenNumbers(10, 25)
for i in en:
    print(i)
