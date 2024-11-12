import pandas as pd
import sqlite3

def insert_csv (csv_address,db_address,table_name):
    df = pd.read_csv(csv_address, encoding='BIG5')  #讀取CSV資料集檔案

    with sqlite3.connect(db_address) as conn:
        df.to_sql(table_name, conn, if_exists='replace', index=False) #新增資料表
        select_check = pd.read_sql(f"SELECT * FROM  {table_name} WHERE Country='Togo'", conn)
        return select_check


