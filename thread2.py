import threading
from utils import is_prime


class CustomThread(threading.Thread):
    def __init__(self, limit, queue, *args, **kwargs):
        self.limit = limit
        self.queue = queue
        super().__init__(*args, **kwargs)

    def run(self):
        for _ in range(self.limit):
            number = self.queue.get()
            is_prime(number)
            print(f"{self.name} QSize: {self.queue.qsize()}")

        # counter = 0
        # while counter < self.limit:
        #     number = self.queue.get()
        #     is_prime(number)
        #     counter += 1


class SiteCrawler(threading.Thread):
    running = True

    def __init__(self, start_point, *args, **kwargs):
        self.start_point = start_point
        super().__init__(*args, **kwargs)

    def run(self):
        while self.running:
            super().run()
