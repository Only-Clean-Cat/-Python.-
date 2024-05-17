from collections import Counter
from multiprocessing import Process


class WarehouseManager(Process):
    data = {}

    def process_request(self, request):
        self.data1 = Counter({})
        self.data2 = Counter({})
        self.request = request
        for self.request in requests:
            if self.request[1] == "receipt":
                self.data1.update({self.request[0]: self.request[2]})
            if self.request[1] == "shipment":
                self.data2.update({self.request[0]: self.request[2]})
        WarehouseManager.data = self.data1 - self.data2
        return dict(WarehouseManager.data)

    def run(self, *args, **kwargs):
        for request in requests:
            return request
        requests.start()
        requests.join()


manager = WarehouseManager()
requests = [
    ("product1", "receipt", 100),
    ("product2", "receipt", 150),
    ("product1", "shipment", 30),
    ("product3", "receipt", 200),
    ("product2", "shipment", 50)
]
manager.run(requests)
print(manager.process_request(requests))
