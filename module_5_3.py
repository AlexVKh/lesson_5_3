class House:
    def __init__(self, name, floors):
        self.name = name
        self.number_of_floors = floors

    def go_to(self, new_floor):
        if new_floor <= self.number_of_floors:
            for i in range(int(new_floor)):
                print(i+1)
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует')

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.number_of_floors}'

    def __eq__(self,other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        if isinstance(other, int):
            return self.number_of_floors == other

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        self.number_of_floors += int(value)
        return self

    def __radd__(self, value):
        self.number_of_floors += int(value)
        return self

    def __iadd__(self, value):
        self.number_of_floors += int(value)
        return self

    def __sub__(self, value):
        self.number_of_floors -= int(value)
        return self

    def __rsub__(self, value):
        self.number_of_floors = int(value) - self.number_of_floors
        return self

    def __isub__(self, value):
        self.number_of_floors -= int(value)
        return self

    def __mul__(self, value):
        self.number_of_floors *= int(value)
        return self

    def __rmul__(self, value):
        self.number_of_floors *= int(value)
        return self

    def __imul__(self, value):
        self.number_of_floors *= int(value)
        return self


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__

h3 = House('ЖК Этажи', 40)
h3 = h3 - 10 # __sub__
print(h3)
h3 -= 10 # __isub__
print(h3)
h3 = 30 - h3 # __rsub__
print(h3)

h3 = h3 * 10 # __mul__
print(h3)
h3 *= 10 # __imul__
print(h3)
h3 = 10 * h3 # __rmul__
print(h3)
print(h3 == 10000)


