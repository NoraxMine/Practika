# import pandas as pd
# #from __ import __


# class sumop:
#     def __init__(self, data): 
#         self.data = data
#         self.df = pd.read_csv('var2.csv')
       
#     def __neg__(self):
#         return  self.df.drop_duplicates()  
    
#     def dann(self):
#         self.df = sumop('var2.csv')

#         self.df = -self.df
        
        
#         df_te = self.df[self.df['Тип операции'] == self.data]
#         if self.data == "безналичный":
#             print('количество удаленных строк:  ' ,100001 - (len(self.df1) + len(self.df2)),)
#             df_te.to_csv(f'Beznal.csv', index=False )
            
#         elif self.data == "наличный" :
#             print('количество удаленных строк:  ' ,100001 - (len(self.df1) + len(self.df2)),)
#             df_te.to_csv(f'Nal.csv', index=False )
        
#     def __del__(self):
#         print('удаление')


# def main():
#     smop = sumop('var2.csv')
#     smop.dann()

# if __name__ == '__main__':
#     main()


import pandas as pd

class Sumop:

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.df = pd.read_csv(self.file_path)

    def remove_duplicates(self) -> int:

        original_len = len(self.df)
        self.df = self.df.drop_duplicates()
        removed_count = original_len - len(self.df)
        return removed_count

    def split_and_save(self):

        removed = self.remove_duplicates()
        print(f"Количество удалённых строк: {removed}")

        # Фильтрация по типу операции
        df_cash = self.df[self.df['Тип операции'] == 'наличный']
        df_cashless = self.df[self.df['Тип операции'] == 'безналичный']

        # Сохранение в файлы
        df_cash.to_csv('Nal.csv', index=False, encoding='utf-8-sig')
        df_cashless.to_csv('Beznal.csv', index=False, encoding='utf-8-sig')
        print("Файлы 'Nal.csv' и 'Beznal.csv' успешно сохранены.")


if __name__ == '__main__':
    splitter = Sumop('var2.csv')
    splitter.split_and_save()