import pandas as pd
import sqlite3

def xlsx (db_address,table_name,output_address):
    # 讀sql
    with sqlite3.connect(db_address) as conn:
        df_sql = pd.read_sql(f"SELECT * FROM {table_name}", conn)

    df_sql.to_excel(output_address, index=False, engine='openpyxl')


def unduplicate_xlsx (db_address,table_name,subset,output_address):
    # 讀sql
    with sqlite3.connect(db_address) as conn:
        df_sql = pd.read_sql(f"SELECT * FROM {table_name}", conn)

    duplicate_rows = df_sql[~df_sql.duplicated(subset=[subset], keep=False)]
    duplicate_rows.to_excel(output_address, index=False, engine='openpyxl')


def default_xlsx(db_address, table_name, output_address):
    # 讀取資料表
    with sqlite3.connect(db_address) as conn:
        df_sql = pd.read_sql(f"SELECT * FROM {table_name}", conn)

    columns = df_sql.columns.tolist()
    selected_cols = [1, 103, 7, 125, 156, 132, 158, 22, 36, 99, 101, 42, 84, 51, 143, 61, 29, 
                     162, 84, 134, 145, 146, 147, 148, 144, 152, 153, 155, 21, 165, 166, 167, 168]  # 儲存使用者選擇的欄位
    

    # 過濾索引，將有效的對應欄位加入列表
    selected_cols = [columns[i] for i in selected_cols if 0 <= i < len(columns)]


    # 建立新的 DataFrame
    choice_df = df_sql[selected_cols]
    # 將結果存為 Excel
    choice_df.to_excel(output_address, index=False, engine='openpyxl')


def choices_column_xlsx(db_address, table_name, output_address):
    # 讀取資料表
    with sqlite3.connect(db_address) as conn:
        df_sql = pd.read_sql(f"SELECT * FROM {table_name}", conn)

    # 列出所有欄位名稱
    col = df_sql.columns.tolist()
    print("欄位列表：")
    for i, column in enumerate(col, start=1):
        print(f"{i}. {column}")

    selected_cols = []  # 儲存使用者選擇的欄位

    # 多次選擇欄位，直到使用者結束
    while True:
        try:
            choice = int(input("請輸入需求欄位編號 (輸入0結束選擇)： "))
            if choice == 0:
                if not selected_cols:
                    print("尚未選擇任何欄位！請至少選擇一個。")
                    continue
                print("已完成選擇。")
                break
            elif 1 <= choice <= len(col):
                selected_col = col[choice - 1]
                if selected_col not in selected_cols:
                    selected_cols.append(selected_col)
                    print(f"已選擇欄位：{selected_col}")
                else:
                    print("欄位已選過，請選擇其他欄位！")
            else:
                print("無效的編號，請重新輸入！")
        except ValueError:
            print("請輸入有效的編號！")

    # 按選擇的欄位過濾 DataFrame
    choice_df = df_sql[selected_cols]
    print(f"已建立新 DataFrame，包含的欄位：{selected_cols}")

    # 將結果存為 Excel
    choice_df.to_excel(output_address, index=False, engine='openpyxl')


def choice_meter_default_xlsx(db_address, table_name, xlsx_address, on, on_c, output_address):
    # 讀取資料表
    with sqlite3.connect(db_address) as conn:
        df_sql = pd.read_sql(f"SELECT * FROM {table_name}", conn)

    df = pd.read_excel(xlsx_address, dtype=str)  # 讀取CSV資料集檔案
    df_trans_column = df_sql.merge(df, left_on = on, right_on = on_c, how="inner")    

    columns = df_trans_column.columns.tolist()
    selected_cols = [1, 103, 7, 125, 156, 132, 158, 22, 36, 99, 101, 42, 84, 51, 143, 61, 29, 
                     162, 84, 134, 145, 146, 147, 148, 144, 152, 153, 155, 21, 165, 166, 167, 168]  # 儲存使用者選擇的欄位
    

    # 過濾索引，將有效的對應欄位加入列表
    selected_cols = [columns[i] for i in selected_cols if 0 <= i < len(columns)]


    # 建立新的 DataFrame
    choice_df = df_trans_column[selected_cols]
    # 將結果存為 Excel
    choice_df.to_excel(output_address, index=False, engine='openpyxl')
