from time import time, sleep
import requests
import threading
from random import randint
from multiprocessing import Process, Pipe
import asyncio


def download(url):
    response = requests.get(url)
    print(f"Download {url} (size: {len(response.content)} bytes)")

def give_nums(con):
    nums = []
    for _ in range(100):
        nums.append(randint(-1000000, 1000000))
    con.send(nums)
    con.close()

def square(con):
    nums = con.recv()
    square_nums = [num * num for num in nums]
    con.close()
    
def work1():
    sleep(1)

def work2():
    sleep(2)

async def work1_a():
    await asyncio.sleep(1)

async def work2_a():
    await asyncio.sleep(2)

async def run():
    task1 = asyncio.create_task(work1_a())
    task2 = asyncio.create_task(work2_a())
    await task1
    await task2

def task1():
    print('ЗАДАНИЕ 1')
    start = time()
    download("https://www.youtube.com/")
    download("https://www.x.com/")
    download("https://www.facebook.com/")
    download("https://habr.com/")
    download("https://stackoverflow.com/")
    download("https://www.wikipedia.org/")
    download("https://telegram.org/")
    download("https://rutracker.org/")
    download("https://shikimori.one/")
    download("https://github.com/")
    print(f'Обычное выполнение: {time() - start} сек')

    start = time()
    t1 = threading.Thread(target=download, args=("https://www.youtube.com/",), daemon=True)
    t2 = threading.Thread(target=download, args=("https://www.x.com/",), daemon=True)
    t3 = threading.Thread(target=download, args=("https://www.facebook.com/",), daemon=True)
    t4 = threading.Thread(target=download, args=("https://habr.com/",), daemon=True)
    t5 = threading.Thread(target=download, args=("https://stackoverflow.com/",), daemon=True)
    t6 = threading.Thread(target=download, args=("https://www.wikipedia.org/",), daemon=True)
    t7 = threading.Thread(target=download, args=("https://telegram.org/",), daemon=True)
    t8 = threading.Thread(target=download, args=("https://rutracker.org/",), daemon=True)
    t9 = threading.Thread(target=download, args=("https://shikimori.one/",), daemon=True)
    t10 = threading.Thread(target=download, args=("https://github.com/",), daemon=True)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t9.start()
    t10.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    t7.join()
    t8.join()
    t9.join()
    t10.join()
    print(f'Многопоточность: {time() - start} сек')

def task2():
    print('ЗАДАНИЕ 2')
    con_square_nums, con_nums = Pipe()
    p1 = Process(target=give_nums, args=(con_nums,))
    p2 = Process(target=square, args=(con_square_nums,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print('Выполнено')

def task3():
    print('ЗАДАНИЕ 3')
    start = time()
    work1()
    work2()
    print(f'Обычное выполнение: {time() - start} сек')

    start = time()
    asyncio.run(run())
    print(f'Ассинхроность: {time() - start} сек')
