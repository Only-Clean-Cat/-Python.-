
def string_to_int(s): # добавить обработку ValueError
   return int(s)
try:
    print(string_to_int('a'))
except ValueError as exc:
    print(f'Ошибка: {exc}! Аргумент в методе "string_to_int()" требует на вход цифровой литерал!')


def read_file(filename): # добавить обработку FileNotFoundError, IOError
    with open(filename, 'r') as file:
        return file.read()
try:
    filename = 'aaa.txt'
    print(read_file('aaa.txt'))
except FileNotFoundError as exc:
    print(f'Ошибка: {exc}! Запрашиваемый файл: {filename} не найден')
except IOError as exc:
    print(f'Ошибка: {exc}! Ошибка ввода\выводв: {filename}')


def divide_numbers(a, b): # добавить обработку ZeroDivisionError, TypeError
    return a / b
try:
    print(divide_numbers(5,0))
    print(divide_numbers(5,'c'))
except ZeroDivisionError as exc:
    print(f'Ошибка: {exc}! Недопустимое деление на 0!')
except TypeError as exc:
    print(f'Ошибка: {exc}! Недопустимое сочетание типов данных')

def access_list_element(lst, index): # добавить обработку IndexError, TypeError
    return lst[index]
try:
    aaa = [1, 2, 3]
    print(access_list_element(aaa, 5))
    print(access_list_element(aaa, 'c'))
except IndexError as exc:
    print(f'Ошибка: {exc}! Данный индекс отсутствует в списке!')
except TypeError as exc:
    print(f'Ошибка: {exc}! Недопустимый тип данных индекса!')

