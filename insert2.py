import pandas as pd
import sqlite3

def insert_csv (csv_address,csv_address2,db_address,table_name,on,on_2,csv_name,csv_name2):
    df = pd.read_csv(csv_address, encoding='utf-8-sig')  # 讀取CSV資料集檔案
    df2 = pd.read_csv(csv_address2, encoding='utf-8-sig')  # 讀取CSV資料集檔案

    # path = 'output.txt'

    # df_compare_every = df == df2 # 檢查所有對應儲存格內容是否相同
                           # Can only compare identically-labeled (both index and columns) DataFrame objects 
    # df_compare_every_list = df[(df_compare_every).all(axis=1) == False] #列出不完全相同資料列
    df, df2 = df.align(df2, join='outer', axis=None)  # 對齊、補值
    # df_compare = df[df['Customer Id'] != df2['Customer Id']] # 比對特定欄位，不吻合保留
    
    
    df_trans_column = df.merge(df2, left_on = f"{on}", right_on = f"{on_2}", how='inner', suffixes=(f"_{csv_name}", f"_{csv_name2}"))
    # 比對on，吻合的補到最左欄，重複不剃除，欄位名稱衝突分開列出
    df_trans_column = df_trans_column.assign(status = f"{csv_name}_{on}={csv_name2}_{on_2}") # 新增status欄

    
    df2_suffix = df2.rename(columns={col: f"{col}_{csv_name2}" for col in df2.columns}) # 手動為 df2 欄位加上後綴 '_df2'
    df2_only = df2_suffix[~df2_suffix[f"{on_2}_{csv_name2}"].isin(df[on_2])].copy() # 不吻合放到最下列
    df2_only['status'] = f"~{csv_name2}"

    
    df_only = df[~df[on].isin(df2[on])].copy()
    df_only['status'] = f"~{csv_name}"

    # Step 5: 拼接合併結果、df2_only 和 df_only
    df_final = pd.concat([df_trans_column, df2_only, df_only], ignore_index=True)

    # f = open(path, 'w')
    # f.write(df_compare.astype(str).to_string())
    # f.close()

    # with open(path, 'w') as f:
    #     f.write(df_compare.astype(str).to_string())


    # df_merge = pd.concat([df,df2], ignore_index=True, sort=False) #合併
    # df_merge = df_merge.drop_duplicates() # 剃除完全重複

    with sqlite3.connect(db_address) as conn:
        df_final.to_sql(table_name, conn, if_exists='replace', index=False) # 新增資料表
        select_check = pd.read_sql(f"SELECT * FROM  {table_name} WHERE Country='Togo'", conn)
        return select_check
