import asyncio

async def ah(seconds):
    await asyncio.sleep(seconds)
    print("все верно")

def async_main():
    print('асинхрон:')
    seconds = int(input('давай быстрее: '))
    asyncio.run(ah(seconds))