#Deros.all rights reserved.
#==========================

import pandas as pd
import matplotlib.pyplot as plt


class PSN:

    def __init__(self, file):
        self.file_name = file
        self.df = pd.read_csv(file)
        
    def draw(self):
        # Группируем данные по странам и считаем количество игроков в каждой стране
        con_nums = self.df['country'].value_counts()
        
        # Круговая диаграмма
        plt.figure(figsize=(8, 8))
        plt.pie(con_nums, labels=con_nums.index, autopct='%1.1f%%')
        plt.title('Количество игроков PS')
        plt.axis('equal')  
        plt.show()
    
    def __del__(self):
        print('PSN has been deleted')


def main():
    psp = PSN('playstation_players.csv')
    psp.draw()


if __name__ == '__main__':
    main()