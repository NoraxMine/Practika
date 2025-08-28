import asyncio

async def func():
    await asyncio.sleep(5) 
    return 'Функция завершена'

async def main():
    try:
        result = await asyncio.wait_for(func(), timeout=3)
        print(result)
    except asyncio.TimeoutError:
        print('А фсё')

if __name__ == "__main__":
    asyncio.run(main())