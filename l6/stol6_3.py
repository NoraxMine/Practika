import asyncio

async def ah(seconds):
    await asyncio.sleep(seconds)
    print("Дождались")

def async_main():
    print('\nАсинхрон:')
    seconds = int(input('Сколько секунд еще ждать: '))
    asyncio.run(ah(seconds))