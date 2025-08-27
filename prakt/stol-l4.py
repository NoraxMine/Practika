

import pandas as pd


class Sumop:
    def __init__(self, filename: str):
        self.filename = filename
        self.df = pd.read_csv(filename)

    def __neg__(self):

        return self.df.drop_duplicates()

    def dann(self):
        # удалени дубликатов
        self.df = -self

        # фильтрация 
        df_nal = self.df[self.df['Тип операции'].str.strip() == 'наличный']
        df_bez = self.df[self.df['Тип операции'].str.strip() == 'безналичный']

        # вывод статистики
        total_rows = len(self.df)
        removed_rows = len(pd.read_csv(self.filename)) - total_rows
        print(f'Количество удалённых строк: {removed_rows}')

        # сохранение в CSV
        df_nal.to_csv('df_nal.csv', index=False)
        df_bez.to_csv('df_bez.csv', index=False)

    def __del__(self):
        print('Удаление объекта')


def main():
    smop = Sumop('var2.csv')
    smop.dann()


if __name__ == '__main__':
    main()