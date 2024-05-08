import threading
import time


class Table(threading.Thread):
    def __init__(self, number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.number = int(number)
        self.is_busy = True


class Cafe(threading.Thread):
    def __init__(self, queue, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.queue = queue


    def customer_arrival(self):
        for visitor in range(1,21):
            time.sleep(1)
            print(f'Посетитель номер {visitor} прибыл.')




    def serve_customer(self, customer):
        pass


class Customer(threading.Thread):
    def flow_visitor(self):
        for visitor in range(20):
            visitor += 1
            return visitor


table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1,table2,table3]
cafe = Cafe(tables)
customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()
customer_arrival_thread.join()
