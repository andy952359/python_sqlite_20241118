import pandas as pd
import sqlite3
import numpy as np
import chardet
# -*- coding: utf-8 -*-



def insert_csv (csv_address3,db_address,table_name,table_name2):
    
    df3 = pd.read_csv(csv_address3, encoding='BIG5')  # 讀取CSV資料集檔案，BIG5
    print(df3)

    # 讀sql
    with sqlite3.connect(db_address) as conn:
        df_sql = pd.read_sql(f"SELECT * FROM {table_name}", conn)

    
    df3_suffix = df3.rename(columns={col: f"{col}_df3" for col in df3.columns}) # 手動為 df3 欄位加上後綴 '_df3'
    df_sql, df3 = df_sql.align(df3, join='outer', axis=None)  # 對齊、補值
    ## A4 == B1 & B12 == 'OK' ## A4 == B1 & B12 != 'OK'
    

    df_trans_column = df_sql.merge(df3_suffix, left_on='First Name', right_on='First Name_df3', how='inner')
    # 比對on，吻合的補到最左欄，重複不剃除

    df_trans_column['status_etl'] = np.where(df_trans_column['Country'] == 'Togo', 
    "A4 == B1 & B12 == 'OK'", 
    "A4 == B1 & B12 != 'OK'")

    ## ~A4
    df3_only = df3_suffix[~df3_suffix['First Name_df3'].isin(df_sql['First Name'])] # 不吻合放到最下列
    df3_only['status_etl'] = '~df3'

    ## ~B1
    df_sql_only = df_sql[~df_sql['First Name'].isin(df3_suffix['First Name_df3'])]
    df_sql_only['status_etl'] = '~df_sql'

    # Step 5: 拼接合併結果、df2_only 和 df_only
    df_final = pd.concat([df_trans_column, df3_only, df_sql_only], ignore_index=True)
    



    ## check
    with sqlite3.connect(db_address) as conn:
        df_final.to_sql(table_name2, conn, if_exists='replace', index=False) # 新增資料表
        select_check = pd.read_sql(f"SELECT * FROM  {table_name} WHERE Country='Togo'", conn)
        return select_check
