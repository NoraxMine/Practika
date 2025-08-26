from multithread import main as mt
from multiproc import main as mp
from asynch import main as ah
import asyncio

def main():
    usr = input('Введите 1 для многопоточности \n Введите 2 для мультипроцессорности \n Введите 3 для асихнхрона\n')
    if usr == '1':
        mt()
    elif usr == '2':
        mp()
    elif usr =='3':
        asyncio.run(ah())
    else:
        print('Неверный ввод')


if __name__ == '__main__':
    main()