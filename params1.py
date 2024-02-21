def print_params(arg):
    """ Эта функция в своем теле будет
     распечатывать переданное значение
     параметра из списка 2 раза"""
    print(arg)
    print(arg)


my_list = ['I believe in miracles', 666]

for element in my_list:
    print_params(arg=element)
