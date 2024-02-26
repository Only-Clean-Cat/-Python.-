def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [5, False, 'mango']
values_dict = dict(a=25, b='applle', c=False)
res = print_params(*values_list)
res = print_params(**values_dict)

values_list2 = [42]
values_dict = dict(b='applle', c=False)
res = print_params(*values_list2,**values_dict)

