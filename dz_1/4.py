"""

Задание №4
Работа в консоли в режиме интерпретатора Python.
Решите квадратное уравнение
5x^2-10x-400=0 последовательно
сохраняя переменные a, b, c, d, x1 и x2.
Попробуйте решить уравнения с другими значениями a, b, c.

"""

from math import sqrt

def solve_quadratic_equation(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        x1 = (-b + sqrt(discriminant)) / (2 * a)
        x2 = (-b - sqrt(discriminant)) / (2 * a)
        return x1, x2
    elif discriminant == 0:
        x1 = -b / (2 * a)
        return x1

a = 5
b = 10
c = 400

result = solve_quadratic_equation(a, b, c)
if result is None:
    print("Уравнение не имеет действительных корней")
elif isinstance(result, tuple):
    print(f"Корни уравнения: x1 = {result[0]}, x2 = {result[1]}")
else:
    print(f"Корень уравнения: x = {result}")


