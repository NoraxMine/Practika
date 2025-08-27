from lb6_z1 import main as m1
from lab6_z2 import main as m2
from lab6_z3 import main as m3


def main():
    user_choise = input('Введите 1 если хотите увидеть 1 задание 6 лабы\nВведите 2 если хотите увидеть 2 задание 6 лабы\nВведите 3 если хотите увидеть 3 задание 6 лабы')
    if user_choise.lower() == '1':
        m1()
    elif user_choise.lower() == '2':
        m2()
    elif user_choise.lower() == '3':
        m3()
    else:
        print('не то')


if __name__ == '__main__':
    main()