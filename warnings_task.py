import warnings
def my_namber(a,b):
    try:
        print('Перед генепацией предупреждения')
        if b < 1:
            warnings.warn('Значение делителя приближается к 0', UserWarning)
        print('После генерации предупреждения')
    except UserWarning as e:
        print(f'Предупреждение было перехвачено как исключение: {e}')
    return print(a/b)
my_namber(1, 0.5)
print('\n')
print('Пример 1: Фильтр "error"')
warnings.simplefilter('error', UserWarning)
my_namber(1, 0.1)
print('\n')
print('Пример 2: Фильтр "ignore"')
warnings.simplefilter('ignore', UserWarning)
my_namber(1, 0.2)
print('\n')
print('Пример 3: Фильтр "always"')
warnings.simplefilter('always', UserWarning)
my_namber(1, 0.9)