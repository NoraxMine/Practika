import matplotlib.pyplot as plt
import pandas as pd


class Graphical_Statistics:
    def __init__(self):
        self.df = pd.read_csv('lab3\\steam_players.csv')

    def create(self):
        country_counts = self.df['country'].value_counts()
        plt.figure(figsize=(13, 8))
        country_counts.plot(kind='bar')
        plt.title('Количество игроков Steam')
        plt.tight_layout()
        plt.show()


# file = Graphical_Statistics()
# file.create()