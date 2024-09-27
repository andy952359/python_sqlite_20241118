import pandas as pd
import sqlite3

def insert_csv ():
    df = pd.read_csv('customers-100.csv')  #讀取CSV資料集檔案

    with sqlite3.connect('customers-100.db') as conn100:
        df.to_sql('customers', conn100, if_exists='replace', index=False) #新增資料表
        togo = pd.read_sql("SELECT * FROM customers WHERE Country='Togo'", conn100)
        return togo


