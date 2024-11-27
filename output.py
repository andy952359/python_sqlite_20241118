import pandas as pd
import sqlite3



def xlsx (db_address,table_name,output_address):

    # 讀sql
    with sqlite3.connect(db_address) as conn:
        df_sql = pd.read_sql(f"SELECT * FROM {table_name}", conn)

    df_sql.to_excel(output_address, index=False, engine='openpyxl')
    