import pandas as pd

class Dates:

    def __init__(self):
        self.df = pd.read_csv('var7.csv')
        self.df_clear = None
        self.removed_duplicates = 0

    def __invert__(self):
        initial_len = len(self.df)
        self.df_clear = self.df.drop_duplicates()
        self.df_clear.to_csv('clear.csv', index=False)
        self.removed_duplicates = initial_len - len(self.df_clear)
        return self  # для возможности цепочки вызовов

    def duplicates(self):
            print(f'Количество удалённых дубликатов: {self.removed_duplicates}')


    def location(self):
        if 'Место оплаты' not in self.df.columns:
            print('В датасете нет колонки "Место оплаты".')
            return

        minsk_df = self.df[self.df['Место оплаты'].str.strip().str.lower() == 'минск']
        mogilev_df = self.df[self.df['Место оплаты'].str.strip().str.lower() == 'могилев']
        brest_df = self.df[self.df['Место оплаты'].str.strip().str.lower() == 'брест']
        gomel_df = self.df[self.df['Место оплаты'].str.strip().str.lower() == 'гомель']
        grodno_df = self.df[self.df['Место оплаты'].str.strip().str.lower() == 'гродно']
        vitebsk_df = self.df[self.df['Место оплаты'].str.strip().str.lower() == 'витебск']

        minsk_df.to_csv('minsk.csv', index=False)
        mogilev_df.to_csv('mogilev.csv', index=False)
        brest_df.to_csv('brest.csv', index=False)
        gomel_df.to_csv('gomel.csv', index=False)
        grodno_df.to_csv('grodno.csv', index=False)
        vitebsk_df.to_csv('vitebsk.csv', index=False)

    def __del__(self):
        print('del done')
