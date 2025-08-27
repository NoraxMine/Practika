import lab1.class_lz as class_lz
import lab2.inherit_lz as inherit_lz
import lab3.capsule_lz as capsule_lz
import lab4.polymorf_lz as polymorf_lz
import lab5.except_lz as except_lz
import lab6.parallel_lz as parallel_lz


if __name__ == "__main__":
    print('Лаб. работа 1')
    triangle = class_lz.Triangle(3)
    triangle.plot()
    _ = input('Нажмите Enter для продолжения...')

    print('Лаб. работа 2')
    animal = inherit_lz.Animal('Silk', 1, '-')
    animal.info()
    animal.make_sound()
    dog = inherit_lz.Dog('Bobik', 2, '-', '--', '---')
    dog.info()
    dog.make_sound()
    dog.guard_house()
    _ = input('Нажмите Enter для продолжения...')

    print('Лаб. работа 3')
    steam = capsule_lz.Graphical_Statistics()
    steam.create()
    _ = input('Нажмите Enter для продолжения...')

    print('Лаб. работа 4')
    bank = polymorf_lz.Data_Processing()
    -bank
    bank.duplicates()
    bank.sort('lab4\\clear.csv')
    _ = input('Нажмите Enter для продолжения...')

    print('Лаб. работа 5')
    csv_check = except_lz.Data_Processing()
    _ = input('Нажмите Enter для продолжения...')

    print('Лаб. работа 6')
    parallel_lz.task1()
    parallel_lz.task2()
    parallel_lz.task3()
