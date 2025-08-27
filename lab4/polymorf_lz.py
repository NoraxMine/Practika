import pandas as pd


class Data_Processing:
    def __init__(self):
        self.df = pd.read_csv('lab4\\var1.csv')

    def __neg__(self):
        self.df_clear = self.df.drop_duplicates()
        self.df_clear.to_csv('lab4\\clear.csv', index=False)

    def duplicates(self):
        print(f'Кличество дубликатов: {len(self.df) - len(self.df_clear)}')
    
    def sort(self, file_name):
        df = pd.read_csv(file_name)
        df_individual = df.loc[df['Участники гражданского оборота'] == 'физ. лицо']
        df_individual.to_csv('lab4\\individual.csv', index=False)
        df_legal = df.loc[df['Участники гражданского оборота'] == 'юр. лицо']
        df_legal.to_csv('lab4\\legal.csv', index=False)
    
    def __del__(self):
        print('del done')
