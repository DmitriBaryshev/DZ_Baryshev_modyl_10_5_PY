# Задание 1
import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __add__(self, value):
        return Circle(self.radius + value)

    def __sub__(self, value):
        return Circle(self.radius - value)

    def __mul__(self, value):
        return Circle(self.radius * value)

    def __iadd__(self, value):
        self.radius += value
        return self

    def __isub__(self, value):
        self.radius -= value
        return self

    def __imul__(self, value):
        self.radius *= value
        return self

    def __str__(self):
        return f"Circle with radius: {self.radius}"


circle1 = Circle(5)
circle2 = Circle(7)

print(circle1 == circle2)
print(circle1 > circle2)
print(circle1 < circle2)
print(circle1 + 3)
print(circle2 - 2)
print(circle1 * 2)



# Задание 2
class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imaginary - other.imaginary)

    def __mul__(self, other):
        real_part = self.real * other.real - self.imaginary * other.imaginary
        imaginary_part = self.real * other.imaginary + self.imaginary * other.real
        return Complex(real_part, imaginary_part)

    def __truediv__(self, other):
        denominator = other.real**2 + other.imaginary**2
        real_part = (self.real * other.real + self.imaginary * other.imaginary) / denominator
        imaginary_part = (self.imaginary * other.real - self.real * other.imaginary) / denominator
        return Complex(real_part, imaginary_part)

    def __str__(self):
        return f"{self.real} + {self.imaginary}i"


c1 = Complex(2, 3)
c2 = Complex(5, 7)

print(c1 + c2)
print(c1 - c2)
print(c1 * c2)
print(c1 / c2)


# Задание 3
class Airplane:
    def __init__(self, model, max_passengers, current_passengers=0):
        self.model = model
        self.max_passengers = max_passengers
        self.current_passengers = current_passengers

    def __eq__(self, other):
        return self.model == other.model

    def __add__(self, num_passengers):
        if self.current_passengers + num_passengers <= self.max_passengers:
            self.current_passengers += num_passengers
        else:
            print("Невозможно добавить пассажиров, превышающих максимальную вместимость.")

    def __sub__(self, num_passengers):
        if self.current_passengers - num_passengers >= 0:
            self.current_passengers -= num_passengers
        else:
            print("Невозможно удалить пассажиров, на борту менее 0 пассажиров.")

    def __iadd__(self, num_passengers):
        self.__add__(num_passengers)
        return self

    def __isub__(self, num_passengers):
        self.__sub__(num_passengers)
        return self

    def __gt__(self, other):
        return self.max_passengers > other.max_passengers

    def __lt__(self, other):
        return self.max_passengers < other.max_passengers

    def __ge__(self, other):
        return self.max_passengers >= other.max_passengers

    def __le__(self, other):
        return self.max_passengers <= other.max_passengers


plane1 = Airplane("Boeing 747", 500)
plane2 = Airplane("Airbus A380", 501)

print(plane1 == plane2)

plane1 += 300
print(plane1.current_passengers)

plane1 -= 150
print(plane1.current_passengers)

print(plane1 > plane2)


# Задание 4
class Flat:
    def __init__(self, area, price):
        self.area = area
        self.price = price

    def __eq__(self, other):
        return self.area == other.area

    def __ne__(self, other):
        return self.area != other.area

    def __gt__(self, other):
        return self.price > other.price

    def __lt__(self, other):
        return self.price < other.price

    def __ge__(self, other):
        return self.price >= other.price

    def __le__(self, other):
        return self.price <= other.price


flat1 = Flat(100, 100000)
flat2 = Flat(120, 120000)

print(flat1 == flat2)

print(flat1 != flat2)

print(flat1 <= flat2)
