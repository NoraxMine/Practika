import multiprocessing
import random

def func(counter, lock, array):
    for i in range(270):
        with lock:
            counter.value += 1
            array.append(counter.value)


def main():
    count = multiprocessing.Value('i', 0)
    lock = multiprocessing.Lock()
    manager = multiprocessing.Manager()
    array = manager.list()
    processing = [multiprocessing.Process(target=func, args=(count, lock, array)) for i in range(5)]
    
    for p in processing:
        p.start()
    for p in processing:
        p.join()
    print(array)


if __name__ == '__main__':
    main()