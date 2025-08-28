from math import pi, cos, sin, tan
import matplotlib.pyplot as plt 


class Octagon:  
    def __init__(self, st: int):
        self.st = st
        self.n = 15  
        self.grad = (self.n - 2) * 180 / self.n 

    def rad_opis(self) -> float:  
        return self.st / (2 * sin(pi / self.n))

    def s_opis(self):  
        r = self.rad_opis()
        return pi * r ** 2

    def rad_vpis(self) -> float: 
        return self.st / (2 * tan(pi / self.n))

    def s_vpis(self): 
        r = self.rad_vpis()
        return pi * r ** 2

    def s(self): 
        s = (self.n * self.st ** 2) / (4 * tan(pi / self.n))
        print(f'Площадь 15-гранника: {s:.4f}\n')

    def per(self):  
        print(f'Периметр 15-гранника: {self.st * self.n}\n')

    def peaks(self) -> list:
        peaks_x = []
        peaks_y = []

        r = self.rad_opis()
        for i in range(self.n):
            angle = (2 * pi * i) / self.n
            x = r * cos(angle)
            y = r * sin(angle)
            peaks_x.append(x)
            peaks_y.append(y)

        peaks_x.append(peaks_x[0])
        peaks_y.append(peaks_y[0])
        return peaks_x, peaks_y

    def paint(self):  
        circle1 = plt.Circle((0, 0), self.rad_opis(), color='b', fill=False)
        circle2 = plt.Circle((0, 0), self.rad_vpis(), color='r', fill=False)
        ax = plt.gca()
        ax.add_patch(circle1)
        ax.add_patch(circle2)

        x, y = self.peaks()
        plt.plot(x, y, color='g')

        plt.axis('scaled')
        plt.title(f'Правильный 15-гранник\nВнутренний угол: {self.grad:.2f}°')
        plt.show()

    def __del__(self):
        print('15-gon has been deleted')


def main():
    zn = input('Введите сторону 15-гранника\n')
    oct = Octagon(int(zn))
    print(f'Радиус описанной окружности: {oct.rad_opis():.4f}')
    print(f'Радиус вписанной окружности: {oct.rad_vpis():.4f}')
    oct.s()
    oct.per()
    oct.paint()
    print('============')
    x, y = oct.peaks()
    print('Координаты вершин:')
    print(x)
    print(y)


if __name__ == '__main__':
    main()
