import pandas as pd
import os

class Processing:

    def __init__(self, csv):
        try:   
            self.csv = pd.read_csv(csv)
            if os.path.isfile('var5.csv'): #Проверяем файл нв существование
                print("Файл существует")
            else:
                raise SystemExit()
        except FileNotFoundError:
            print("Нет файла") 
            raise SystemExit()     
        except pd.errors.EmptyDataError:
            print("Файл пуст")
            raise SystemExit()
        try:
            stolb_1 = self.csv.columns.to_list() #Получаем список названий столбцов
            self.df_2 = pd.read_csv('var5.csv')
            stolb_2 = self.df_2.columns.to_list()
            if stolb_1 != stolb_2:
                raise TypeError 
        except TypeError:
            print('В исходном файле не те колоки')
        try:
            self.file_types = str(self.csv.dtypes) #Получаем типы данных столбцов
            self.file_types_2 = str(self.df_2.dtypes)
            if self.file_types != self.file_types_2:
                raise TypeError('Неверные типы данных')
            else:
                print('Названия столбцов и типы данных совпадают')
        except TypeError:
            print(f'Файлы не совпадают \n, ожидалось: {self.file_types_2}, Фактические:{self.file_types} ')

    def __del__(self):
        print('')
    # Del Done

def main():
    csv = 'var5.csv'            
    df = Processing(csv)

if __name__ == "__main__":
    main()