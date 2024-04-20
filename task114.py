import pprint
print('Задача 1: Фабрика фунуций')


def create_operation(operation):
    if operation == "*":
        def multiplication(x, y):
            return x * y
        return multiplication
    elif operation == "/":
        def division(x, y):
            if y == 0:
                print(f'Ошибка!. Деление на ноль недопустимо!')
            else:
                return x / y
        return division



my_func_add = create_operation("*")
print(my_func_add(1, 2))
my_func_add = create_operation("/")
print(my_func_add(1, 0))

print('Задача 2: Лямбда-Функции')

my_multiply = lambda x: x ** 2
print(my_multiply(4))


def multiply_def(x):
    return x ** 2


print(multiply_def(4))


print('Задача 3: Вызываемые Объекты')


class Rect:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        return self.a * self.b


area_figure = Rect
result = area_figure(a=2, b=4)
print(f'Площадь фигуры равна: {result()}')
