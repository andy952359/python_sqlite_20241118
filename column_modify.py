import pandas as pd
import sqlite3
   
def add_column(db_address,table_name, add_c, add_text):
# 連接到 SQLite 資料庫
    with sqlite3.connect(db_address) as conn:
        c = conn.cursor()  # 建立 cursor
        
        sql_alter = f'''
        ALTER TABLE "{table_name}" ADD COLUMN "{add_c}" TEXT;
        '''
        c.execute(sql_alter)  # 執行 ALTER TABLE 語句
    
        sql_update = f'''
        UPDATE "{table_name}" SET "{add_c}" = "{add_text}";
        '''
        c.execute(sql_update)  # 更新所有資料的 Status 欄位
        
        # 確認改動
        conn.commit()
        
        i_c_check = "add_OK"
        return i_c_check


def delete_column(db_address,table_name,delete_c):
# 連接到 SQLite 資料庫
    with sqlite3.connect(db_address) as conn:
        c = conn.cursor()  # 建立 cursor
        
        sql_delete = f'''
        ALTER TABLE "{table_name}" DROP COLUMN "{delete_c}" ;
        '''
        c.execute(sql_delete)  # 執行 ALTER TABLE 語句

        
        # 確認改動
        conn.commit()
        
        d_c_check = "delete_OK"
        return d_c_check