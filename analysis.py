import pandas as pd
import sqlite3

def status(db_address, table_name, csv_name,  csv_name2, csv_name3, on, on_2, on_etl, analysis_status):

    # 讀sql
    with sqlite3.connect(db_address) as conn:
        df_sql = pd.read_sql(f"SELECT * FROM {table_name}", conn)
        df_sql.fillna("", inplace=True) 

    if f"{analysis_status}" not in df_sql.columns:
        df_sql[f"{analysis_status}"] = ""  # 初始化為空字串
        
    
    j = 0 # j+1 列 start
    k = 221965 # k 列 end  

    # for i in range(len(df_sql)):
    for i in range(j, len(df_sql)):
        x = df_sql.loc[i, "status"]  # 取第一行的 status
        y = df_sql.loc[i, "status_etl"]  # 取第一行的 status_etl

        # 使用 match-case 判斷條件
        match (x, y):
            case (x, y) if f"{csv_name}_{on}={csv_name2}_{on_2}" in x and f"{on_etl} satisify" in y:
                df_sql.loc[i, analysis_status] = "安裝且納管"
            case (x, y) if f"{csv_name}_{on}={csv_name2}_{on_2}" in x and f"~df_sql" in y:
                df_sql.loc[i, analysis_status] = "電表未納管"    
            case (x, y) if f"~{csv_name2}" in x and f"~df_sql" in y:
                df_sql.loc[i, analysis_status] = "供裝APP以輸入，但不存在於總表與ETL清單"
            case (x, y) if f"~{csv_name2}" in x and f"{on_etl} satisify" in y:
                df_sql.loc[i, analysis_status] = "安裝且納管，但不存在於總表清單"
            case (x, y) if  not x and f"~{csv_name3}" in y:
                df_sql.loc[i, analysis_status] = "只存在於ETL清單"               
            case _:
                return 0


    with sqlite3.connect(db_address) as conn:
        df_sql.to_sql(table_name, conn, if_exists='replace', index=False) # 新增資料表        