from inherit import Player, Warrior

def funс():
    p1 = Player("Moko", 1, 50)
    p1.show_stats()
    p1.gain_exp(500)
    p1.show_stats()

    w1 = Warrior("Vori", 5, 1, 1, 20)
    w1.show_info()
    w1.gain_exp(2100)
    w1.show_info()

def main():
    funс()

if __name__ == "__main__":
    main()
