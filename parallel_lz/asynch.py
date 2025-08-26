import asyncio

async def func():
    await asyncio.sleep(5) 
    return 'Выполнено'

async def main():
    try:
        result = await asyncio.wait_for(func(), timeout=2)
        print(result)
    except asyncio.TimeoutError:
        print('Программа выполнена')

if __name__ == "__main__":
    asyncio.run(main())