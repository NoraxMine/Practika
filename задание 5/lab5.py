import pandas as pd

class lab:
    def __init__(self, file):
        self.file = file
        try:
            text = pd.read_csv(file)
        except Exception as e:
            print(e.__class__.__name__)
        else:
            self.check(file)
        
    def check(self, file):
        try:
            text = pd.read_csv(file)
            name_pattern = ['Участники гражданского оборота', 'Тип операции', 'Сумма операции', 'Вид расчета', 'Место оплаты', 'Терминал оплаты', 'Дата оплаты', 'Время оплаты', 'Результат операции', 'Cash-back', 'Сумма cash-back']
            first_row = text.columns.to_list()
            if len(first_row) != 11:
                print("ожидалось столбцов: 11 \nполучено столбцов:",len(first_row))
                raise NameError
            else:
                if name_pattern != first_row:
                    print("Название столбцов не совпал с ожидаемым.") 
                    print("Oжидалось:", name_pattern)
                    print("Получено:", first_row)
                    raise NameError
                else:
                    type_pattern = pd.read_csv("type.csv")
                    type_check = type_pattern.dtypes.to_list()
                    type_collums = text.dtypes.to_list()
                    print(type_check)
                    for numb in range(0, len(type_check)):
                        if type_check[numb] != type_collums[numb]:
                            print("несовпадение типов данных в столбцах под номером:", numb )
                            print('ожидалось:', type_check[numb])
                            print('получено:', type_collums[numb])
                            raise NameError
        except NameError:
            pass
        except Exception as e:
            print(e.__class__.__name__) 
        else:
            print("обработка файла прошла успешно! наверно.....")       
        
    def __del__(self):
        
        pass

file = lab("var11.csv")

