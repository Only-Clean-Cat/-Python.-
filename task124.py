import time
from collections import defaultdict
import queue
import threading

class Table(threading.Thread):

    def __init__(self, number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.number = int(number)
        self.is_busy = bool


class Cafe(threading.Thread):

    def __init__(self, *args, **kwargs):
        self.queue = queue.Queue(maxsize=3)



    def customer_arrival(self):
        for customer in range(1,21):
            time.sleep(1)
            print(f'Посетитель номер {customer} прибыл.')
        return customer




    def serve_customer(self, customer):
        pass


class Customer(threading.Thread):
    pass


table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1,table2,table3]
cafe = Cafe(tables)
customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()
customer_arrival_thread.join()
