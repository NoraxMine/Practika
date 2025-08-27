#Deros.All rights reserved
#=======================

import pandas as pd

class Tester:
    def __init__(self, csv):
        try:
            self.csv = pd.read_csv(csv)
        except FileNotFoundError:
            print(f'Файл отсутствует')
            raise SystemExit()
        except pd.errors.EmptyDataError:
            print('Файл пустой')
            raise SystemExit()
        except:
            print('Файл отсутствует')
            raise SystemExit()
        try:
            st_i = self.csv.columns.to_list()
            self.df_o = pd.read_csv('var3_2git.csv')
            st_s = self.df_o.columns.to_list()
            if st_i != st_s:
                raise TypeError 
        except TypeError:
            print('Структура файла нарушена')
        try:
            self.f_t = str(self.csv.dtypes)
            self.o_t = str(self.df_o.dtypes)
            if self.f_t != self.o_t:
                raise TypeError('Неверные типы данных')
            else:
                print('Файл готов к использованию')
        except TypeError:
            print(f'Файлы не совпадают \n, ожидалось: {self.o_t}, а есть:{self.f_t} ')


def main():
    csv = 'var3_2 bad.csv'            
    df = Tester(csv)

if __name__ == "__main__":
    main()

        
        