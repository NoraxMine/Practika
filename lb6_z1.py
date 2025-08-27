#Deros.all rights reserved.
#==========================

import subprocess
import threading
from time import time
import random


class Ddos:

    def __init__(self):
        self.ips = [f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}" for _ in range(10)]

    def ping(self, ip):
        result = subprocess.run(["ping", "-c", "3", ip], capture_output=True)
        print(f"{ip} is {'up' if result.returncode == 0 else 'down'}")

    def vrm(self):
        start = time()
        for ip in self.ips:
            self.ping(ip)
        opt = time() - start
        print(f'Время одного потока: {opt}')

        threads = []
        start = time()
        for ip in self.ips:
            thread = threading.Thread(target=self.ping, args=(ip,))
            threads.append(thread)
            thread.start()
        for thread in threads:
            thread.join()

        mpt = time() - start
        print(f'Время выполнения (многопоточно): {mpt}')

        if mpt < opt:
            print('Многопотчка')
        else:
            print('Однопоточка')


def main():
    pinggg = Ddos()
    pinggg.vrm()


if __name__ == '__main__':
    main()