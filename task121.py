import time
from threading import Thread

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']


def my_funk(*args):
    for i in args:
        print(i)
        time.sleep(1)

thread = Thread(target=my_funk, args=num)
thread2 = Thread(target=my_funk, args=letter)
thread.start()
thread2.start()
thread.join()
thread2.join()