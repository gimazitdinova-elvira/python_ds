import math
def square(side):
    return math.ceil(side ** 2)
side_square = float(input("Введите сторону квадрата: "))
print(f"Площадь квадрата: {square(side_square)}")