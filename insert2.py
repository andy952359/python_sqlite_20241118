import pandas as pd
import sqlite3

def insert_csv (csv_address,csv_address2,db_address,table_name):
    df = pd.read_csv(csv_address)  # 讀取CSV資料集檔案
    df2 = pd.read_csv(csv_address2)  # 讀取CSV資料集檔案

    path = 'output.txt'
    # df_compare_every = df == df2 # 檢查所有對應儲存格內容是否相同
                           # Can only compare identically-labeled (both index and columns) DataFrame objects 
    # df_compare_every_list = df[(df_compare_every).all(axis=1) == False] #列出不完全相同資料列
    df, df2 = df.align(df2, join='outer', axis=None)  # 對齊、補值
    # df_compare = df[df['Customer Id'] != df2['Customer Id']] # 比對特定欄位，不吻合保留
    
    
    df_trans_column = df.merge(df2, on='Customer Id', how='inner', suffixes=('', '_df2'))
    # 比對on，吻合的補到最左欄，重複不剃除
    df_trans_column = df_trans_column.assign(status="df_id == df2_id")

    
    df2_suffix = df2.rename(columns={col: f"{col}_df2" for col in df2.columns}) # 手動為 df2 欄位加上後綴 '_df2'
    df2_only = df2_suffix[~df2_suffix['Customer Id_df2'].isin(df['Customer Id'])] # 不吻合放到最下列
    df2_only['status'] = '~df2'

    
    df_only = df[~df['Customer Id'].isin(df2['Customer Id'])]
    df_only['status'] = '~df'

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
