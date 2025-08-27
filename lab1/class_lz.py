from math import sqrt, pi, cos, sin
import matplotlib.pyplot as plt


class Triangle:
    def __init__(self, side):
        self.side = side
        self.ANGLE = 60
        self.K = sqrt(3)
    
    def circumscribed_circle_radius(self): # радиус описанной окружности
        return self.side / self.K

    def circumscribed_circle_area(self): # площадь описанной окружности
        return pi * self.circumscribed_circle_radius() * self.circumscribed_circle_radius()

    def inscribed_circle_radius(self): # радиус вписанной окружности
        return self.side * self.K / 6

    def inscribed_circle_area(self): # площадь вписанной окружности
        return pi * self.inscribed_circle_radius() * self.inscribed_circle_radius()

    def triangle_area(self): # площадь правл. треугольника
        return self.side * self.K * self.side / 4

    def triangle_perimeter(self): # периметр правл. треугольника
        return 3 * self.side

    def plot(self):
        r_cir = self.circumscribed_circle_radius()
        r_ins = self.inscribed_circle_radius()

        vertices = []
        for angle in [pi/2, 7*pi/6, 11*pi/6]:
            x = r_cir * cos(angle)
            y = r_cir * sin(angle)
            vertices.append((x, y))

        x = [vertex[0] for vertex in vertices] + [vertices[0][0]]
        y = [vertex[1] for vertex in vertices] + [vertices[0][1]]

        plt.figure(figsize=(6,6))
        plt.plot(x, y, lw=2)
        circle_in = plt.Circle((0,0), r_ins, color='green', fill=False)
        circle_out = plt.Circle((0,0), r_cir, color='red', fill=False)

        plt.gca().add_patch(circle_in)
        plt.gca().add_patch(circle_out)
        plt.grid(True)
        plt.show()

    def __del__(self):
        print('del done')
