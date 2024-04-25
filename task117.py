def is_prime(func):
    def surrogate(*args, **kwargs):
        result = func(*args, **kwargs)
        k = 0
        for i in range(2, result // 2 + 1):
            if result % i == 0:
                k = k + 1
            if k == 0:
                print('Простое')
            else:
                print('Составное')
            return result

    return surrogate


@is_prime
def sum_three(x, y, z):
    my_sum = x + y + z
    return my_sum


result = sum_three(2, 3, 6)
print(result)
result = sum_three(2, 3, 9)
print(result)