def square_number(x):
    return x ** 2


def is_odd(x):
    return x % 2


numbers = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]

result = map(square_number, filter(is_odd, numbers))
print(list(result))
