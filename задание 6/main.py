from sinc import main as m1
from proc import main as m2
from asc import main as m3
import asyncio

def main():
    usr = input('Введите 1 если хотите увидеть многопоточност\n Введите 2 если мультипроцессорность \n Введите 3 если асихнхрон\n')
    if usr == '1':
        m1()
    elif usr == '2':
        m2()
    elif usr =='3':
        asyncio.run(m3())
    else:
        print('Да на напиши ты нормально, блэт')


if __name__ == '__main__':
    main()