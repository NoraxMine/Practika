import inherit_lz


if __name__ == '__main__':
    animal = inherit_lz.Animal('Silk', 1, '-')
    animal.info()
    animal.make_sound()
    dog = inherit_lz.Dog('Bobik', 2, '-', '--', '---')
    dog.info()
    dog.make_sound()
    dog.guard_house()