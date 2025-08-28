import threading
from time import time 

flag1 = 0
flag2 = 0

def count1():
    global flag1
    flag1 += 1000
def count2():
    global flag2
    flag2 += 1000


def base_ch():
    start_t = time()
    for i in range(10):
        count1()
    delta = time()-start_t
    print(f'Время выполнения классическим способом:{delta}')

def thr_ch():

    start = time()
    threads = []
    for i in range(10):
        t = threading.Thread(target=count2)
        threads.append(t)
    for t in threads:
        t.start()
    delta = time() - start
    print(f"Многопоточная запись: {delta}")


def main():
    base_ch()
    thr_ch()

if __name__ == '__main__':
    main()
