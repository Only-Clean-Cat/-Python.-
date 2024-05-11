import time
from threading import Thread, Lock###

class Table():
    def __init__(self, number):
        self.number = number
        self.is_busy = False

class Cafe():
    def __init__(self, tables):
        self.queue_ = []
        self.tables = tables
        self.tables_lock = Lock()

    def customer_arrival(self):
        customer_number = 1
        while customer_number < 21:  # Ограничиваем количество посетителей до 20
            time.sleep(1)
            print(f'Посетитель номер {customer_number} прибыл.', flush=True)
            customer = Customer(customer_number, self)
            customer_number += 1  # Увеличиваем счетчик посетителей
            with self.tables_lock:
                if self.serve_customer(customer):
                    customer.start()
                else:
                    self.queue_.append(customer)
                    #customer.start()
        #print("Кафе больше не принимает посетителей.")

    def serve_customer(self, customer):
        for table in self.tables:
            if not table.is_busy:
                table.is_busy = True
                customer.table = table
                print(f'Посетитель номер {customer.number} сел за стол {table.number}.', flush=True)
                return True
        print(f'Посетитель номер {customer.number} ожидает свободный стол.', flush=True)
        return False################

class Customer(Thread):
    def __init__(self, number, cafe, table=None):###
        Thread.__init__(self)
        self.number = number
        self.cafe_ = cafe
        self.table = table

    def run(self):
        time.sleep(5)
        print(f'Посетитель номер {self.number} покушал и ушел.', flush=True)

        with self.cafe_.tables_lock:#####
            self.table.is_busy = False
            if self.cafe_.queue_:
                next_customer = self.cafe_.queue_.pop(0)
                self.cafe_.serve_customer(next_customer)
                next_customer.table = self.table ### # Назначаем освободившийся стол следующему клиенту
                next_customer.start()


# Создаем столики в кафе
table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

# Инициализируем кафе
cafe = Cafe(tables)

# Запускаем поток для прибытия посетителей
customer_arrival_thread = Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()

# Ожидаем завершения работы прибытия посетителей
customer_arrival_thread.join()