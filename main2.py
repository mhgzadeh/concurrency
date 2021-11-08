from utils import DEFAULT_NUMBERS
from thread2 import CustomThread, SiteCrawler
import queue
import time

if __name__ == "__main__":
    q = queue.Queue()
    for num in DEFAULT_NUMBERS:
        q.put(num)
    print('create c1')
    c1 = CustomThread(25, q)
    print('create c2')
    c2 = CustomThread(25, q)
    print('create c3')
    c3 = CustomThread(25, q)
    print(f"\nstart c1 {'*' * 50} \tstart time: {time.time()}")
    c1.start()
    print(f"\nstart c2 {'*' * 50} \tstart time: {time.time()}")
    c2.start()
    print(f"\nstart c3 {'*' * 50} \tstart time: {time.time()}")
    c3.start()

    """
    Join: 
        it used to avoid the interpreter from touching other lines of script.
        so if it uses after start it will never let other threat to start their work.
    """
    c1.join()
    c2.join()
    c3.join()

    time.sleep(5)
    SiteCrawler.running = False
    print("all threads finished.")
