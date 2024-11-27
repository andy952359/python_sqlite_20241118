import pandas as pd
import sqlite3
import xlsx2csv
import trans_big5
import insert_csv as csv
import insert2 
import etl_insert
import column_modify as cm
import check

xlsx_path1 = ".\csv\二期總表_20240722.xlsx"
xlsx_path2 = ".\csv\Ami-2024-11-18-1705.xlsx"
xlsx_path3 = ".\csv\AMI-108-ETL-2024-11-17.xlsx"
csv_path1 = ".\csv\二期總表_20240722.csv"
csv_path2 = ".\csv\Ami-2024-11-18-1705.csv"
csv_path3 = ".\csv\AMI-108-ETL-2024-11-17.csv"
table_name = "customers"
table_name2 = "customers_2"
db_address = ".\db\customers-2000000.db" 
add_c = "期數"
add_text = "108"
delete_c = "check_status"
on = "11碼電號"
on_2 = "電號"
on_etl = "表號"
on_etl_2 = "電表 ID"
csv_name = "二期總表_20240722"
csv_name2 = "Ami-2024-11-18-1705"
csv_name3 = "AMI-108-ETL-2024-11-17"
check_status = "check_status"
check_col1 = "11碼電號"
check_col2 = "FAN號"
check_col3 = "施工問題"
check_text = '無'
pattern1 = r'^\d{11}$'
pattern2 = r'^[AD]\d{10}$'

    # ^：表示字串的開始。
    # [A-Za-z]：表示第1個字元為英文字母（大小寫均可）。
    # \d{5}：表示接下來的5個字元為數字。
    # [A-Za-z]{9}：表示接下來的9個字元為英文字母（大小寫均可）。
    # $：表示字串的結束。

# c_return = cm.add_column(db_address,table_name, add_c, add_text)
text = cm.delete_column(db_address,table_name2,delete_c)

# xlsx2csv.xlsx_to_csv_keep_zeros(xlsx_path1, csv_path1)
# xlsx2csv.xlsx_to_csv_keep_zeros(xlsx_path2, csv_path2)
# xlsx2csv.xlsx_to_csv_keep_zeros(xlsx_path3, csv_path3)

# select_check = csv.insert_csv (csv_path3,db_address,table_name)
# print(select_check)

# select_check = insert2.insert_csv (csv_path1,csv_path2,db_address,table_name,on,on_2,csv_name,csv_name2)
# print(select_check)

# select_check = etl_insert.insert_csv (csv_path3,db_address,table_name,table_name2,on_etl,on_etl_2,csv_name3)
# print(select_check)


select_check = check.check_number (db_address,table_name2,check_status,check_col1,pattern1)
select_check = check.check_number (db_address,table_name2,check_status,check_col2,pattern2)
select_check = check.text_check (db_address,table_name2,check_status,check_col3,check_text)



