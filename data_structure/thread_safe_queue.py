import threading
from queue import Queue


class ThreadSafeQueue:
    def __init__(self):
        self.__queue = Queue(maxsize=0)

    def pop(self):
        return self.__queue.get(block=True, timeout=None)

    def push(self, data):
        self.__queue.put(data)


# Test code
if __name__ == "__main__":
    queue = ThreadSafeQueue()
    thread1 = threading.Thread(target=lambda q, d: q.push(d), args=(queue,3))
    thread2 = threading.Thread(target=lambda q: print(q.pop()), args=(queue,))  # 쓰레드 생성
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
