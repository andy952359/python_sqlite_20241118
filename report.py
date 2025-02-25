import os
import pandas as pd
import sqlite3
import choose
import xlsx2csv
import insert2
from pathlib import Path
import numpy as np

def meter_reading_comparison(db_address, table_name, xlsx_address, on, on_c, on_plus, output_address):
    folder_path = f".\csv"
    
    # 讀取資料表
    with sqlite3.connect(db_address) as conn:
        df_sql = pd.read_sql(f"SELECT * FROM {table_name}", conn)

    df = pd.read_excel(xlsx_address, dtype=str)  # 讀取CSV資料集檔案
    df_trans_column = df_sql.merge(df, left_on = on, right_on = on_c, how="inner")    

    columns = df_trans_column.columns.tolist()
    selected_cols = [1, 103, 7, 36, 99, 101, 42, 84, 51, 22, 61, 88]  # 儲存使用者選擇的欄位
    # 過濾索引，將有效的對應欄位加入列表
    selected_cols = [columns[i] for i in selected_cols if 0 <= i < len(columns)]


    # 建立新的 DataFrame
    choice_df = df_trans_column[selected_cols]
    choice_df.insert(0, '項次', choice_df.reset_index().index + 1)
    choice_df["人工讀值_Ami-2025-02-05-1119"] = pd.to_numeric(choice_df["人工讀值_Ami-2025-02-05-1119"], errors='coerce')


    selected_files = choose.select_files(folder_path)
    csv_path1 = xlsx2csv.xlsx_path_to_csv (selected_files[0])
    csv_name1 = Path(csv_path1).stem
    csv_path2 = xlsx2csv.xlsx_path_to_csv (selected_files[1])
    csv_name2 = Path(csv_path2).stem
    csv_path3 = xlsx2csv.xlsx_path_to_csv (selected_files[2])
    csv_name3 = Path(csv_path3).stem

    df_path1 = pd.read_csv(csv_path1, dtype=str)  # 讀取CSV資料集檔案
    # 進行 merge，將 df1 的第 24 欄 (col_24) 插入 df2 的第 4 欄 (col_4)
    choice_df = choice_df.merge(df_path1[["電號", "通訊技術"]], left_on="11碼電號_四期_20250218", right_on="電號", how="left").drop(columns=["電號"])

    df_path2 = pd.read_csv(csv_path2, dtype=str)  # 讀取CSV資料集檔案
    choice_df = choice_df.merge(df_path2[[f"11碼電號",f"通訊改善中"]], left_on="11碼電號_四期_20250218", right_on="11碼電號", how="left").drop(columns=["11碼電號"])
    
    df_path3 = pd.read_csv(csv_path3, dtype=str)  # 讀取CSV資料集檔案
    choice_df = choice_df.merge(df_path3[[f"表號",f"HES用電",f"HES時間"]], left_on="表號_Ami-2025-02-05-1119", right_on="表號", how="left").drop(columns=["表號"])

    choice_df["人工讀值_Ami-2025-02-05-1119"] = pd.to_numeric(choice_df["人工讀值_Ami-2025-02-05-1119"], errors='coerce')
    choice_df["HES用電"] = pd.to_numeric(choice_df["HES用電"], errors='coerce')
    choice_df["測試結果"] = np.where(choice_df["HES用電"] < choice_df["人工讀值_Ami-2025-02-05-1119"], "HES系統讀值kWh < 人工讀值kWh", "HES系統讀值kWh ≧ 人工讀值kWh")
    choice_df["FAN紅燈(電源燈)"] = "紅燈常亮"
    choice_df["FAN綠燈(通訊燈)"] = "綠燈常亮"
    choice_df["連線判斷"] = "已連線"
    choice_df["批次"] = "四期第5-1批"
    choice_df["HES系統讀表次數"] = "96"
    choice_df["異常原因"] = choice_df["異常原因"].fillna('#N/A')
    choice_df["通訊改善中"] = choice_df["通訊改善中"].fillna('#N/A')
    choice_df = choice_df.iloc[:, [0,1,2,3,13,4,5,6,7,8,18,19,20,21,9,10,16,15,22,17,12,14]] 
    



    # 將結果存為 Excel
    choice_df.to_excel(output_address, index=False, engine='openpyxl')

