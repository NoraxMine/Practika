from f15 import Octagon

def main():
    figure = Octagon(20)
    print(f'Радиус описанной окружности:{figure.rad_opis()}')
    print(f'Радиус вписанной окружности:{figure.rad_vpis()}')
    print(f'Площадь описанной окружности:{figure.s_opis()}')
    print(f'Площадь вписанной окружности:{figure.s_vpis()}')
    print(f'Периметр октагона:{figure.s()}')
    print(f'Площадь октагона:{figure.per()}')
    figure.paint()
        

if __name__ == '__main__':
        main()