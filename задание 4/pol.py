import pandas as pd



class Summa_cash:

    def __init__(self): 
        self.file = pd.read_csv('var10.csv')

    def __pos__(self): 
        self.df = self.file.drop_duplicates() 
        first_count = self.file.shape[0] 
        second_count = self.df.shape[0]
        dropped = first_count - second_count
        print(f'В файле удалено {dropped} дубликатов')

    def oper(self): 
        self.df1 = self.df[self.df['Сумма cash-back'] > 0]   
        self.df2 = self.df[self.df['Сумма cash-back'] == 0]    
        self.df1.to_csv('first.csv')
        self.df2.to_csv('second.csv')

    def __del__(self):
        print('Датафрейм удален')