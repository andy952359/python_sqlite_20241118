import pandas as pd
import sqlite3
   
def add_column():
# 連接到 SQLite 資料庫
    with sqlite3.connect('.\db\customers-100.db') as conn:
        c = conn.cursor()  # 建立 cursor
        
        sql_alter = '''
        ALTER TABLE customers ADD COLUMN Status TEXT;
        '''
        c.execute(sql_alter)  # 執行 ALTER TABLE 語句
    
        sql_update = '''
        UPDATE customers SET Status = "108";
        '''
        c.execute(sql_update)  # 更新所有資料的 Status 欄位
        
        # 確認改動
        conn.commit()
        
        i_c_check = "OK"
        return i_c_check