import os
import datetime
import pandas as pd


user = os.getlogin()            #имя пользователя

def date():
    date = datetime.datetime.now().strftime('%Y-%m-%d')         #получаем дату
    return date
def time():
    time =datetime.datetime.now().strftime('%H:%M:%S')
    return time
    

def logger(func):
    def wrapper(*args, **kwargs):
        res  = func(*args, **kwargs)
        f_name = func.__name__

        log_file = 'logs.csv'

        if os.path.isfile('logs.csv'):
            csv = pd.read_csv('logs.csv')
            columns = {'': [len(csv)], "Пользователь": [user], "Действие": [f_name],"Дата": [date()],"Время":[time()]}
            DF = pd.DataFrame(columns)
            DF.to_csv('logs.csv', mode = 'a', index = False, header = False)
        else:
            columns = {"Пользователь": [user], "Действие": [f_name],"Дата": [date()],"Время":[time()]}
            DF = pd.DataFrame(columns)
            DF.to_csv('logs.csv')
        return res
    return wrapper
    
@logger
def yupi():
    print("yuppi")



