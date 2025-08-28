import multiprocessing
import random

def func(counter, lock, array):
    for i in range(150):
        with lock:
            counter.value += 1
            array.append(counter.value)


def main():
    counter = multiprocessing.Value('i', 0)
    lock = multiprocessing.Lock()
    manager = multiprocessing.Manager()
    array = manager.list()
    processes = [multiprocessing.Process(target=func, args=(counter, lock, array)) for i in range(10)]
    
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    print(array)


if __name__ == '__main__':
    main()