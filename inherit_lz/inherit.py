import math

class Player:
    def __init__(self, name, level, exp):
        self.name = name
        self.level = level
        self.exp = exp

    def gain_exp(self, value):   # добавляем опыт
        self.exp += value
        # простая таблица опыта
        levels = {1:100, 2:200, 3:400, 4:800, 5:1600, 6:3200, 7:6400, 8:12800, 9:25600, 10:51200}
        for lvl, need in levels.items():
            if self.exp >= need:
                self.level = lvl

    def show_stats(self):   # вывод информации
        print(f"name:{self.name}, level:{self.level}, exp:{self.exp}")


class Warrior(Player):
    def __init__(self, name, level, exp, weapon, armor):
        super().__init__(name, level, exp)
        self.weapon = weapon
        self.armor = armor

    def attack(self):   # атака
        return (self.level / 2) * self.weapon

    def defend(self):   # защита
        if self.exp > 0:
            return math.log(self.exp) * self.armor
        return 0

    def show_info(self):   # вывод всей информации
        self.show_stats()
        print(f"weapon:{self.weapon}, armor:{self.armor}, attack:{self.attack():.2f}, defend:{self.defend():.2f}")


def func():
    p1 = Player("Moko", 1, 50)
    p1.show_stats()
    p1.gain_exp(500)
    p1.show_stats()

    w1 = Warrior("Vori", 5, 1, 1, 20)
    w1.show_info()
    w1.gain_exp(5000)
    w1.show_info()


def main():
    func()


if __name__ == "__main__":
    main()
