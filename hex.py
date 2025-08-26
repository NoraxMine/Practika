#Deros.all rights reserved.
#==========================

from math import sqrt, pi, cos, sin
import matplotlib.pyplot as plt 


class Hexagon:
    def __init__(self, st: int):
        self.st = st  # сторона шестиугольника
        self.n = 6    # число сторон
        self.grad = 60

    def rad_opis(self) -> float:  # радиус описанной окружности
        return self.st

    def rad_vpis(self) -> float:  # радиус вписанной окружности
        return (sqrt(3) / 2) * self.st

    def s(self) -> float:  # площадь шестиугольника
        s = (3 * sqrt(3) / 2) * (self.st ** 2)
        print(f'Площадь шестиугольника: {s}\n')
        return s

    def per(self) -> float:  # периметр шестиугольника
        p = self.st * 6
        print(f'Периметр шестиугольника: {p}\n')
        return p

    def peaks(self) -> list:  # нахождение вершин
        peaks_x = []
        peaks_y = []

        for i in range(self.n):
            x = self.rad_opis() * cos(i * (2 * pi / self.n))
            y = self.rad_opis() * sin(i * (2 * pi / self.n))
            peaks_x.append(x)
            peaks_y.append(y)

        #1 точка в конец
        peaks_x.append(peaks_x[0])
        peaks_y.append(peaks_y[0])
        return peaks_x, peaks_y

    def paint(self):  # рисование фигур
        # описанная окружность
        circle1 = plt.Circle((0, 0), self.rad_opis(), color='b', fill=False)
        ax = plt.gca()
        ax.add_patch(circle1)

        # вписанная окружность
        circle2 = plt.Circle((0, 0), self.rad_vpis(), color='r', fill=False)
        ax = plt.gca()
        ax.add_patch(circle2)

        # шестиугольник по вершинам
        x, y = self.peaks()
        plt.plot(x, y, color='g')

        plt.axis('scaled')
        plt.show()

    def __del__(self):
        print('Hexagon has been deleted')


def left():
    zn = input('Введите сторону шестиугольника\n')
    hexagon = Hexagon(int(zn))
    print(f"Радиус описанной окружности: {hexagon.rad_opis()}")
    print(f"Радиус вписанной окружности: {hexagon.rad_vpis()}")
    hexagon.s()
    hexagon.per()
    hexagon.paint()
    print('============')
    x, y = hexagon.peaks()
    print(x)
    print(y)


def main():
    left()


if __name__ == '__main__':
    main()
