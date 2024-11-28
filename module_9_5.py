class StepValueError(ValueError):
    pass


class Iterator:
    def __init__(self, start, stop, step, pointer=1):
        self.step = step
        if self.step == 0:
            raise StepValueError(f'шаг не может быть равен {self.step}')

        self.start = start
        self.stop = stop
        self.pointer = pointer

    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        if self.pointer < self.stop:
            current_value = self.pointer
            self.pointer += self.step
            return current_value
        else:
            raise StopIteration

try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(5, 10, 2)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(-5, 1, 1)
iter5 = Iterator(10, 100, 2)



for i in iter2:
    print(i, end=' ')
else:
    print("\n")

for i in iter3:
    print(i, end=' ')
else:
    print("\n")

for i in iter4:
    print(i, end=' ')
else:
    print("\n")

for i in iter5:
    print(i, end=' ')
else:
    print("\n")


