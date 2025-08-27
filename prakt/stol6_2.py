import time
from queue import Queue
from threading import Thread
from random import randint


def producer(queque):
    while True:
        queque.put(randint(10, 100))
        print('Задача появилась')
        time.sleep(0.5)
        queque.join()

def consumer(queque):
    while True:
        try:
            number = queque.get()
            number += 10
            queque.task_done()
            print('Задача выполнилась')
        except Exception as error:
            print(error.__class__.__name__)

def main():
    print('Потоки:')
    queque = Queue(maxsize=10)
    producer_thread = Thread(target=producer, args=(queque,))
    producer_thread.start()

    consumer_thread = Thread(target=consumer, args=(queque,))
    consumer_thread.start()

    consumer_thread.join()
    producer_thread.join()