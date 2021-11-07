import multiprocessing
from multiprocessing import Pool
from utils import is_prime, DEFAULT_NUMBERS
import queue
import time

# q = queue.Queue()


# def worker(number):
#     # start = time.time()
#     # time.sleep(3)
#     # print(f"worker {number} started {start} ended {time.time()}")
#     while True:
#         job_id = q.get()
#         start = time.time()
#         time.sleep(3)
#         print(f"worker {number} job {job_id} started {start} ended {time.time()}")
#         if q.empty():
#             break


def multi_process():
    # for i in range(16):
    #     q.put(i)
    #
    # # processes = list()
    # for i in range(4):
    #     p = multiprocessing.Process(target=worker, args=(i,))
    #     # processes.append(p)
    #     p.start()
    #
    # # for process in processes:
    # #     process.join()
    # q.join()

    pool = Pool(4)
    with pool:
        pool.map(is_prime, DEFAULT_NUMBERS)

    print("All process finished.")
