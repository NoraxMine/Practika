from math import pi, cos, sin, tan
import matplotlib.pyplot as pl

class Octagon:
    
    def __init__(self, storona:int):
        self.storona = storona
        self.n_sides = 13  # теперь 13-угольник
        
    def rad_op(self) -> float:  # Вычисление радиуса описанной окружности
        radius = self.storona / (2 * sin(pi / self.n_sides))
        return radius
    
    def rad_vp(self) -> float:  # Вычисление радиуса вписанной окружности
        radius = self.storona / (2 * tan(pi / self.n_sides))
        return radius
    
    def s_op(self):
        S = pi * int(self.rad_op()) ** 2
        return S
        
    def s_vp(self):
        S = pi * int(self.rad_vp()) ** 2
        return S
    
    def per(self):  # Периметр 13-угольника
        print(f'Периметр 13-угольника равен: {self.storona * self.n_sides}\n')

    def S(self):  # Площадь 13-угольника
        S = (self.n_sides * self.storona ** 2) / (4 * tan(pi / self.n_sides))
        print(f'Площадь 13-угольника равна: {S}\n')
    
    def peaks(self) -> list:  # Находим вершины
        peaks_a = []
        peaks_b = []

        for i in range(self.n_sides):
            a = self.rad_op() * cos(2 * pi * i / self.n_sides)
            b = self.rad_op() * sin(2 * pi * i / self.n_sides)
            peaks_a.append(a)
            peaks_b.append(b)

        peaks_a.append(peaks_a[0])  # Замкнуть вершины
        peaks_b.append(peaks_b[0])
        return peaks_a, peaks_b
    
    def paint(self):  # Рисуем фигуру
        cir1 = pl.Circle((0, 0), self.rad_op(), color='black', fill=False)
        ax = pl.gca()
        ax.add_patch(cir1)

        cir2 = pl.Circle((0, 0), self.rad_vp(), color='pink', fill=False)
        ax.add_patch(cir2)
        
        a, b = self.peaks()  # Вершинный 13-угольник
        pl.plot(a, b, color='yellow')

        pl.axis('scaled')
        pl.show()

    def __del__(self):
        print('Октагон был удалён успешно!')
    

def left():
    znach = input('Введите длину стороны 13-угольника\n')
    oct = Octagon(int(znach))
    print(oct.rad_op())
    print(oct.rad_vp())
    oct.S()
    oct.paint()
    a, b = oct.peaks()
    print(a)
    print(b)


def main():
    left()


if __name__ == '__main__':
    main()
