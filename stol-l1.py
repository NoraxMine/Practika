from math import sqrt, pi, sin, cos
import matplotlib.pyplot as plt


class Octagon:
     #свойства октагона
    def __init__(self, stra): 
        self.stra = stra
        self.ugol = 45
        self.k = 1 + sqrt(2)
        

    def r_opis(self):
        #вычисление параметров описанной окружности
        r =  sqrt(self.k / (self.k - 1)) * self.stra
        print("вычисление радиуса", r)
        return r          


    def S_opis(self):    
        s = (pi * (self.r_opis()**2.0))
        print("вычисление площади", s)
        return s
         

    def r_vpis(self):    
        r = ((self.stra/2)*self.k)
        print("вычисление радиуса", r)
        return r
    

    def S_vpis(self):    
        s = (pi * (self.r_vpis()**2))
        print("вычисление площади", s)
        return s
        

    def S_oct(self):    
        s = (2 * self.stra**2 * ( self.k ))
        print("вычисление площади октагона", s)
        return s
        

    def P_oct(self):    
        p = (8 * self.stra)
        print("вычисление периметра октагона", p)
        return p
    

    def versh(self) -> list:
        versh_x = []
        versh_y =[]

        for i in range(7):#Создание списка вершин
            x = self.r_opis() * cos((pi/8) + i * (pi/4))
            y = self.r_opis() * sin((pi/8) + i * (pi/4))

            versh_x.append(x)
            versh_y.append(y)


        #первая координата
        versh_x.append(versh_x[0])
        versh_y.append(versh_y[0])
        return versh_x, versh_y
    

    #черчение описанной окружности
    def paint(self):
        circle1 = plt.Circle((0, 0 ), self.r_opis(), color='r', fill=False)
        ax=plt.gca()
        ax.add_patch(circle1)
        
        #вписанная окружность
        circle2 = plt.Circle((0,0 ), self.r_vpis(), color='r', fill=False)
        
        ax=plt.gca()
        ax.add_patch(circle2)

        #октагон
        x,y = self.versh()

        plt.plot(x, y)
        
        plt.show()


    def __del__(self):
        print('удалено')


def left():
    stra = int(input('введите сторону: '))
    octa = Octagon(stra)
    octa.r_opis()
    octa.S_opis()
    octa.r_vpis()
    octa.S_vpis()
    octa.P_oct()
    octa.S_oct()
    

def main():
    left()   
    
if __name__ == '__main__':

    main()