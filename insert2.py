import pandas as pd
import sqlite3

def insert_csv (csv_address,csv_address2,db_address,table_name,on,on_2,csv_name,csv_name2):
    df = pd.read_csv(csv_address, dtype=str)  # 讀取CSV資料集檔案
    df2 = pd.read_csv(csv_address2, dtype=str)  # 讀取CSV資料集檔案

    df, df2 = df.align(df2, join='outer', axis=None)  # 對齊、補值

    
    df_trans_column = df.merge(df2, left_on = f"{on}", right_on = f"{on_2}", how='inner', suffixes=(f"_{csv_name}", f"_{csv_name2}"))
    # 比對on，吻合的補到最左欄，重複不剃除，欄位名稱衝突分開列出
    df_trans_column = df_trans_column.assign(status = f"{csv_name}_{on}={csv_name2}_{on_2}") # 新增status欄

    
    df2_suffix = df2.rename(columns={col: f"{col}_{csv_name2}" for col in df2.columns}) # 手動為 df2 欄位加上後綴 '_df2'
    df2_only = df2_suffix.loc[~df2_suffix[f"{on_2}_{csv_name2}"].isin(df[on])].copy() # 不吻合放到最下列
    df2_only = df2_only.dropna(how='all')
    df2_only['status'] = f"~{csv_name2}"
    
    
    df_suffix = df.rename(columns={col: f"{col}_{csv_name}" for col in df.columns}) # 手動為 df2 欄位加上後綴 '_df2'
    df_only = df_suffix.loc[~df_suffix[f"{on}_{csv_name}"].isin(df2[on_2])].copy()
    df_only = df_only.dropna(how='all')
    df_only['status'] = f"~{csv_name}"
    

    # Step 5: 拼接合併結果、df2_only 和 df_only
    df_final = pd.concat([df_trans_column, df2_only, df_only], ignore_index=True)


    with sqlite3.connect(db_address) as conn:
        df_final.to_sql(table_name, conn, if_exists='replace', index=False) # 新增資料表


def insert_plus (csv_address,csv_address2,on,on_2,on_3):
    df = pd.read_csv(csv_address, dtype=str)  # 讀取CSV資料集檔案
    df2 = pd.read_csv(csv_address2, dtype=str)  # 讀取CSV資料集檔案

    # 只保留 df2 中的 `on_3` 欄位
    df2_filtered = df2[[on_2, on_3]]

    # 進行合併，只補 `on_3` 欄位到 `df`
    df_trans_column = df.merge(df2_filtered, left_on=on, right_on=on_2, how='left')

    return df_trans_column  # 回傳處理後的 DataFrame


def insert_kill (csv_address,csv_address2,on,on_2,on_3):
    df = pd.read_csv(csv_address, dtype=str)  # 讀取CSV資料集檔案
    df2 = pd.read_csv(csv_address2, dtype=str)  # 讀取CSV資料集檔案

    # 取得 df2 中符合 on_2 的 on_3 值
    matched_on_3 = df2[df2[on_2].isin(df[on])][on_3].dropna().unique()

    # 刪除 df 中 on_3 欄位內包含 matched_on_3 的列
    df_cleaned = df[~df[on_3].isin(matched_on_3)]

    return df_cleaned  # 回傳刪除後的 DataFrame