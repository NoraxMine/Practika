#Deros.all rights reserved.
#==========================

import pandas as pd 


class Mtb:
    def __init__(self, file):
        self.df = pd.read_csv(file)

    def __pos__(self):
        return self.df.drop_duplicates()

    def delil(self):
        df = Mtb('var3.csv')
        df = +df
        df1 = self.df[self.df["Сумма операции"] < 1000]
        df2 = self.df[self.df["Сумма операции"] >= 1000]

        print(100000 - (len(df1) + len(df2)),  'строк удалено')

        df1.to_csv("df1.csv", index=False)
        df2.to_csv("df2.csv", index=False)

    def __del__(self):
        print('Mtb has been deleted')

def main():
    q = Mtb('var3.csv')
    q.delil()

if __name__ == '__main__':
    main()