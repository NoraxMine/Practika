import pandas as pd
import matplotlib.pyplot as plt 

class Avocado:
    def __init__(self, link: str):
        self.link = link
    
    def graf(self):
        df = pd.read_csv(self.link)
        data_price = dict(zip(df['Date'], df['AveragePrice']))
        sorted_price = dict(sorted(data_price.items()))
        
        xlist = list(sorted_price.keys())
        ylist = list(sorted_price.values())

        fig, ax = plt.subplots()
        ax.plot(xlist, ylist, color='blue')
        ax.set_title("СТОИМОСТЬ АВОКАДО")  # заголовок графика
        ax.grid()
        plt.show()

    def __del__(self):
        print('Plot has been deleted')


if __name__ == '__main__':
    avc = Avocado('avocado.csv')
    avc.graf()
