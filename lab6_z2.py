# Deros. All rights reserved.
# ==========================

import threading
import queue
import random
import time


class Process:

    def __init__(self):
        self.queue = queue.Queue(maxsize=10)
        self.stop_event = threading.Event()

    def proiz(self):
        while not self.stop_event.is_set():
            value = random.randint(1, 100)

            if not self.queue.full():
                self.queue.put(value)
                print(f'Создано {value}')
            else:
                print(f'Очередь полна')

            time.sleep(random.uniform(0.5, 2.0))

    def potr(self):
        while not self.stop_event.is_set() or not self.queue.empty():
            if not self.queue.empty():
                zn = self.queue.get()

                print(f': Обработано {zn}')

                self.queue.task_done()
            time.sleep(random.uniform(0.5, 2.0))

    def potok(self):
        threads = []

        for i in range(2):
            t = threading.Thread(target=self.proiz, args=())
            threads.append(t)

        for i in range(2):
            t = threading.Thread(target=self.potr, args=())
            threads.append(t)

        for t in threads:
            t.start()

        time.sleep(10)
        self.stop_event.set()

        for t in threads:
            t.join()

        print('Всё')


def main():
    syp = Process()
    syp.potok()


if __name__ == '__main__':
    main()
