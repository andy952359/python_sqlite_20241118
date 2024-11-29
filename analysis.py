import pandas as pd
import sqlite3

def status(db_address, table_name, analysis_status):

    # 讀sql
    with sqlite3.connect(db_address) as conn:
        df_sql = pd.read_sql(f"SELECT * FROM {table_name}", conn)

    if f"{analysis_status}" not in df_sql.columns:
        df_sql[f"{analysis_status}"] = ""  # 初始化為空字串 

    i = 0
    j = 1    

    # for i in range(len(df_sql)):
    for i in range(j):
        x = df_sql.loc[i, "status"]  # 取第一行的 status
        y = df_sql.loc[i, "status_etl"]  # 取第一行的 status_etl
        # 使用 match-case 判斷條件
        match (x, y):
            case (x, y) if "=" in x and "satisify" in y:
                print("Both conditions are satisfied.")
                df_sql.loc[i, analysis_status] = "安裝且納管"
            case _:
                return 0


    with sqlite3.connect(db_address) as conn:
        df_sql.to_sql(table_name, conn, if_exists='replace', index=False) # 新增資料表        