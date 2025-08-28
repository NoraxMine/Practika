import pandas as pd
import time
import os


def decorator(function):
    def wrap(*args, **kwargs):
        user_name = os.getlogin()
        function_name = function.__name__

        seconds = time.time()
        user_time = time.localtime(seconds)
        formatted_date = time.strftime("%d.%m.%Y", user_time)
        formatted_time = time.strftime("%H:%M:%S", user_time)

        if os.path.isfile("log.csv"): # если существует log.csv
            df = pd.read_csv("log.csv")
            data = {"id": [len(df) + 1], "pc username": user_name, "function name": function_name, "Date": formatted_date, "Time": formatted_time}        
            df = pd.DataFrame(data)
            df.to_csv("log.csv", mode="a", index=False,  header=False)
        else: # если не существует log.csv
            data = {"id": [1], "pc username": user_name, "function name": function_name, "Date": formatted_date, "Time": formatted_time}
            df = pd.DataFrame(data)
            df.to_csv("log.csv", index=False)
        return function(*args, **kwargs)
    return wrap
