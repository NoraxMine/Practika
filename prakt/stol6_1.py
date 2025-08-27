import multiprocessing
from random import random


def mc(number):
    inside = 0
    for _ in range(number):
        x, y = random(), random()
        if x*x + y*y <= 1:
            inside += 1
    return inside

def proc_main():
    print('\nПроцессы:')
    nums = 1000
    data = list(range(nums))
    all_points = sum(data)
    num_processes = 10
    with multiprocessing.Pool(processes = num_processes) as pool:
        points_inside = pool.map(mc, data)
    points = sum(points_inside)
    PI = 4 * points / all_points
    print(PI)