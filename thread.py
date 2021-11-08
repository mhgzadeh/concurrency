import queue
import threading
import time
import requests
from utils import is_prime, DEFAULT_NUMBERS

q = queue.Queue()


def worker(number):
    start = time.time()
    time.sleep(3)
    print(f"worker {number}, started at {start}, finished at {time.time()}.")


def get_page(number):
    # while not q.empty(): race condition
    while True:
        start = time.time()
        url = q.get()
        try:
            requests.get(url)
        except ValueError:
            print(f"Error occurred {url}")
        print(f"worker {number}\t get completed {url}\t queue size "
              f"{q.qsize()}\t duration {time.time() - start}")
        q.task_done()
        if q.empty():
            break


def show_prime(worker_id):
    while True:
        number = q.get()
        result = is_prime(number)
        q.task_done()
        print(f"worker id: {worker_id}\t result: {result}")
        if q.empty():
            break


def multi_thread():
    # for i in range(5):
    #     t = threading.Thread(target=worker, args=(i,))
    #     t.start()

    # links = ["https://yahoo.com",
    #          "https://7learn.ac",
    #          "https://google.com",
    #          "https://hft-stuttgart.de",
    #          "https://www.flake8rules.com",
    #          "https://www.python.org",
    #          "https://www.microsoft.com"
    #          ] * 3
    #
    # for link in links:
    #     q.put(link)

    for num in DEFAULT_NUMBERS:
        q.put(num)

    # threads = list()
    for i in range(4):
        t = threading.Thread(target=show_prime, args=(i,))
        # threads.append(t)
        """
        setDaemon Definition:
             All threads depend on the whole python script.
             When python script finish, the threads will be ended even though
             their task has not been finished
        """
        print(t.name)
        t.setDaemon(True)
        t.start()

    print("Thread not join yet")

    #
    q.join()
    # for tr in threads:
    #     """
    #     Join Threads: thread.join()
    #         Join will never let python interpreter to touch next lines
    #         until all treads finish their tasks
    #     """
    #     tr.join()

    """
    Differences between q.join() and thread.join():
        q.join lets python interpreter to touch the other lines after 
        finishing the task of threads but when it reaches the end of 
        python scripts, workers wait to get new task.
        thread.join() never let interpreter to touch other lines if 
        queue is used in input or out put function.
        if not use queue, it will touch other lines and finish the 
        script after finishing the tasks of threads.
    """

    print("Thread Finished.")
