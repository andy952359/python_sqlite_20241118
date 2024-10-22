import pandas as pd
import sqlite3

def insert_csv (csv_address,csv_address2,db_address,table_name):
    df = pd.read_csv(csv_address)  #讀取CSV資料集檔案
    df2 = pd.read_csv(csv_address2)  #讀取CSV資料集檔案

    path = 'output.txt'
    df_compare = df == df2 #檢查儲存格內容是否相同
                           #Can only compare identically-labeled (both index and columns) DataFrame objects 
    # df_different = df[(df_compare).all(axis=1) == False] #不完全相同資料列
    df_different = df[df['Customer Id'] != df2['Customer Id']] #比對特定欄位
    # f = open(path, 'w')
    # f.write(df_compare.astype(str).to_string())
    # f.close()

    with open(path, 'w') as f:
        #f.write(df_compare.astype(str).to_string())
        f.write(df_different.astype(str).to_string())
    
    df_merge = pd.concat([df,df2], ignore_index=True, sort=False)
    df_merge = df_merge.drop_duplicates() #完全相同資料刪除



    with sqlite3.connect(db_address) as conn:
        df_merge.to_sql(table_name, conn, if_exists='replace', index=False) #新增資料表
        select_check = pd.read_sql(f"SELECT * FROM  {table_name} WHERE Country='Togo'", conn)
        return select_check
