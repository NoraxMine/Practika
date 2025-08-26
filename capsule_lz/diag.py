import pandas as pd
import matplotlib.pyplot as plt
from logger import logger

class Diag:

    def __init__(self, filepath):
        self.filepath = filepath
        self.df = None 

    @logger
    def load_data(self):
        self.df = pd.read_csv(self.filepath)
        print(self.df.head())

    @logger
    def normal_bar(self):
        if self.df is None:
            raise ValueError("загрузите данные")

        
        df_copy = self.df.copy()
        state_col = df_copy.columns[0]

        # Убираем дубликаты
        df_group = df_copy.groupby(state_col).sum()

        # Нормируем значения по строкам
        df_norm = df_group.div(df_group.sum(axis=1), axis=0)

        # Рисуем график
        df_norm.plot(kind="bar", stacked=True, figsize=(10, 6), color=['yellow', 'red', 'purple'])
        plt.title("Гистограмма")
        plt.ylabel("Бюджет")
        plt.xlabel("Штаты")
        plt.legend(title="Тип бюджета")
        plt.tight_layout()
        plt.show()

