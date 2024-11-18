import pandas as pd
import sqlite3
import numpy as np



def e_number (db_address,table_name2,check_col):
    # 讀sql
    with sqlite3.connect(db_address) as conn:
        df_sql = pd.read_sql(f"SELECT * FROM {table_name2}", conn)
        

    # ^：表示字串的開始。
    # [A-Za-z]：表示第1個字元為英文字母（大小寫均可）。
    # \d{5}：表示接下來的5個字元為數字。
    # [A-Za-z]{9}：表示接下來的9個字元為英文字母（大小寫均可）。
    # $：表示字串的結束。

    pattern = r'^[A-Za-z]\d{5}[A-Za-z]{9}$'
    # 添加一個新欄位來檢查是否符合格式
    df_sql['e_number_check'] = df_sql[check_col].str.match(pattern)

    with sqlite3.connect(db_address) as conn:
        df_sql.to_sql(table_name2, conn, if_exists='replace', index=False) # 新增資料表
        select_check = pd.read_sql(f"SELECT * FROM  {table_name2} WHERE Country='Togo'", conn)
        return select_check



def FAN_number (db_address,table_name2,check_col):
    # 讀sql
    with sqlite3.connect(db_address) as conn:
        df_sql = pd.read_sql(f"SELECT * FROM {table_name2}", conn)
        conn.commit()
    
    pattern = r'^[a][A]'

    # 添加一個新欄位來檢查是否符合格式
    df_sql['FAN_number_check'] = df_sql[check_col].str.match(pattern)

    with sqlite3.connect(db_address) as conn:
        df_sql.to_sql(table_name2, conn, if_exists='replace', index=False) # 新增資料表
        select_check = pd.read_sql(f"SELECT * FROM  {table_name2} WHERE Country='Togo'", conn)
        return select_check


def text_check (db_address,table_name2,check_col2,check_text):
    # 讀sql
    with sqlite3.connect(db_address) as conn:
        df_sql = pd.read_sql(f"SELECT * FROM {table_name2}", conn)
        conn.commit()

    df_sql[f"{check_col2} satisify"] = np.where(df_sql[check_col2] == check_text,                                          
    f"{check_col2} == {check_text}", 
    f"{check_col2} != {check_text}")

    with sqlite3.connect(db_address) as conn:
        df_sql.to_sql(table_name2, conn, if_exists='replace', index=False) # 新增資料表
        select_check = pd.read_sql(f"SELECT * FROM  {table_name2} WHERE Country='Togo'", conn)
        return select_check
    