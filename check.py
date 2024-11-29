import pandas as pd
import sqlite3
import numpy as np


def check_number (db_address,table_name2,check_status,check_col,pattern):
    # 讀sql
    with sqlite3.connect(db_address) as conn:
        df_sql = pd.read_sql(f"SELECT * FROM {table_name2}", conn)
        conn.commit()

    if f"{check_status}" not in df_sql.columns:
        df_sql[f"{check_status}"] = ""  # 建立欄
 

    df_sql[f"{check_status}"] = np.where(
    df_sql[f"{check_status}"].notna(),  # 檢查欄位是否已有值
    df_sql[f"{check_status}"]  + np.where(df_sql[check_col].str.match(pattern),"",f"{check_col}_number_error; ")
    ,np.where(df_sql[check_col].str.match(pattern),"",f"{check_col}_number_error; ")   
    )
    ## check
    with sqlite3.connect(db_address) as conn:
        df_sql.to_sql(table_name2, conn, if_exists='replace', index=False) # 新增資料表
        



def text_check (db_address,table_name2,check_status,check_col,check_text):
    # 讀sql
    with sqlite3.connect(db_address) as conn:
        df_sql = pd.read_sql(f"SELECT * FROM {table_name2}", conn)
        conn.commit()

    if f"{check_status}" not in df_sql.columns:
        df_sql[f"{check_status}"] = ""  # 初始化為空字串   

    df_sql[f"{check_status}"] = np.where(
    df_sql[f"{check_status}"].notna(),  # 檢查欄位是否已有值
    df_sql[f"{check_status}"] + np.where(df_sql[check_col] == check_text,
        f"",
        f"{check_col} != {check_text}; ")
    ,np.where(df_sql[check_col] == check_text, 
        f"",
        f"{check_col} != {check_text}; ")   
    )
    ## check
    with sqlite3.connect(db_address) as conn:
        df_sql.to_sql(table_name2, conn, if_exists='replace', index=False) # 新增資料表



def MN_check (db_address,table_name2,check_status,check_col,check_text):
    with sqlite3.connect(db_address) as conn:
        df_sql = pd.read_sql(f"SELECT * FROM {table_name2}", conn)
        conn.commit()

    if f"{check_status}" not in df_sql.columns:
        df_sql[f"{check_status}"] = ""  # 建立欄
    else:
        df_sql[f"{check_status}"] = ""    

    df_sql[f"{check_status}"] = np.where(
    df_sql[f"{check_status}"].notna(),  # 檢查欄位是否已有值
    df_sql[f"{check_status}"] + np.where((df_sql[check_col] != check_text) & (df_sql[check_col].notna()), "1", "0")
    ,np.where((df_sql[check_col] != check_text) & (df_sql[check_col].notna()), "1", "0"))

    ## check
    with sqlite3.connect(db_address) as conn:
        df_sql.to_sql(table_name2, conn, if_exists='replace', index=False) # 新增資料表    