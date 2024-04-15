class InvalidData(Exception):
    pass
class Processing(Exception):
    pass
def aaa(name):
    print(f'{name}. Добро пожаловать в сказку!')
    try:
        if name == 'Иванушка':
            raise InvalidData(f'{name}! Не пей из лужицы!')
        elif name == 'Аленушка':
            raise Processing(f'{name}! Предупреди братца!')
    except InvalidData as exc:
        print(f'Ошибка: {exc}')
        raise
    except Processing as exc:
        print(f'Внимание: {exc}')
    finally:
        print('Сказка начинается........))))))))')

aaa('Иванушка')
aaa('Аленушка')
aaa('Bob')
