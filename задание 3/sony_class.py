import pandas as pd
import matplotlib.pyplot as plt
from decorator import decorator


class SonyUsersDiagram:
    @decorator
    def __init__(self):
        self.df_countries = pd.read_csv('playstation_players.csv', index_col=False, names = ['playerid', 'nickname', 'country'], low_memory=False)
    
    @decorator
    def __calculate_countries(self):
        countries_counts = self.df_countries['country'].value_counts()
        countries_counts = countries_counts.to_dict()
        return countries_counts

    @decorator
    def __split_dict(self): # разделяет словарь и возврящает в порядке *значения, ключи* (useless функция т.к. lazy автор)
        dict = self.__calculate_countries()
        countries = list(dict.keys())
        users = list(dict.values())
        return countries, users

    @decorator
    def diagram(self):
        countries, users_amount = self.__split_dict()
        plt.pie(users_amount, labels=countries)
        plt.show()

    def __del__(self):
        print('del done')
