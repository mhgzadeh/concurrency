import threading
import time

x = 0


def increment_x():
    global x
    x += 1
    return x


# def worker(num):
#     for i in range(100000):
#         inc_x = increment_x()
#     print(f"worker num__{num} start summation at x = {inc_x}, time {time.time()}")


def worker(lock):
    for i in range(100000):
        lock.acquire()
        increment_x()
        lock.release()


def run_threads():
    global x
    x = 0

    lock = threading.Lock()

    threads_list = list()
    for i in range(3):
        t = threading.Thread(target=worker, args=(lock,))
        t.start()
        threads_list.append(t)

    for tr in threads_list:
        tr.join()


if __name__ == "__main__":
    for i in range(7):
        run_threads()
        print(f"Turn {i}, x = {x}")
