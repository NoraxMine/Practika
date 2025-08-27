# Deros. All rights reserved.
# ==========================

import asyncio
import random

async def gena():
    num = 1
    while num <= 1_000_000:
        yield num
        step = random.randint(1, 10)
        num += step
        await asyncio.sleep(0.1)

async def oct_gen():
    try:
        async for number in gena():
            print(f'Сделанно: {number}')
            if random.random() < 0.1:
                await asyncio.sleep(0)
    except asyncio.CancelledError:
        print('Остановка')

async def start():
    print('Запуск')
    task = asyncio.create_task(oct_gen())
    await asyncio.sleep(5)
    task.cancel()
    await task
    print('Стоп')


def main():
    asyncio.run(start())


if __name__ == "__main__":
    main()