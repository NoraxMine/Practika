from math import sqrt, pi, sin, cos
import matplotlib.pyplot as plt

class Square:
    def __init__(self, side):
        self.side = side
        self.angle = 90  # внутренний угол
        self.k = sqrt(2)  

    def r_opis(self):
        # радиус опис окр
        r = (self.side * self.k) / 2
        print("радиус описанной окружности", r)
        return r

    def S_opis(self):
        # площадь опис окр
        s = pi * (self.r_opis() ** 2)
        print("площадь описанной окружности", s)
        return s

    def r_vpis(self):
        # радиус вписанной окружности 
        r = self.side / 2
        print("радиус вписанной окружности", r)
        return r

    def S_vpis(self):
        # площадь впис окр
        s = pi * (self.r_vpis() ** 2)
        print("площадь вписанной окружности", s)
        return s

    def S_kv(self):
        s = self.side ** 2
        print("площадь квадрата", s)
        return s

    def P_kv(self):
        p = 4 * self.side
        print("периметр квадрата", p)
        return p

    def versh(self):
        """Список координат вершин квадрата, вписанного в окружность"""
        versh_x = []
        versh_y = []
        for i in range(4):
            x = self.r_opis() * cos((pi/4) + i * (pi/2))
            y = self.r_opis() * sin((pi/4) + i * (pi/2))
            versh_x.append(x)
            versh_y.append(y)
        versh_x.append(versh_x[0])
        versh_y.append(versh_y[0])
        return versh_x, versh_y

    def paint(self):
        # описанная окружность
        circle1 = plt.Circle((0, 0), self.r_opis(), color='r', fill=False)
        ax = plt.gca()
        ax.add_patch(circle1)

        # вписанная окружность
        circle2 = plt.Circle((0, 0), self.r_vpis(), color='b', fill=False)
        ax.add_patch(circle2)

        # квадрат
        x, y = self.versh()
        plt.plot(x, y)

        plt.axis('equal')
        plt.show()

    def __del__(self):
        print("Объект удален")


def left():
    side = float(input("Введите сторону квадрата: "))
    sq = Square(side)
    sq.r_opis()
    sq.S_opis()
    sq.r_vpis()
    sq.S_vpis()
    sq.P_kv()
    sq.S_kv()
    sq.paint()


def main():
    left()

if __name__ == '__main__':
    main()