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
delete_c = "期數"
on = "11碼電號"
on_2 = "電號"
on_etl = "表號"
on_etl_2 = "電表 ID"
csv_name = "二期總表_20240722"
csv_name2 = "Ami-2024-11-18-1705"
csv_name3 = "AMI-108-ETL-2024-11-17"
check_col = "Customer Id"
check_col2 = "Country_customers-102.csv"
check_text = '無'
pattern1 = r'^[A-Za-z]\d{5}[A-Za-z]{9}$'
pattern2 = r'^[a][A]'


# xlsx2csv.xlsx_to_csv_keep_zeros(xlsx_path1, csv_path1)
# xlsx2csv.xlsx_to_csv_keep_zeros(xlsx_path2, csv_path2)
# xlsx2csv.xlsx_to_csv_keep_zeros(xlsx_path3, csv_path3)

# select_check = csv.insert_csv (csv_path3,db_address,table_name)
# print(select_check)

# select_check = insert2.insert_csv (csv_path1,csv_path2,db_address,table_name,on,on_2,csv_name,csv_name2)
# print(select_check)

select_check = etl_insert.insert_csv (csv_path3,db_address,table_name,table_name2,on_etl,on_etl_2,csv_name3)
print(select_check)


# select_check = check.e_number (db_address,table_name2,check_col,check_col2,check_text,pattern1)
# select_check = check.FAN_number (db_address,table_name2,check_col,check_col2,pattern2)
# select_check = check.text_check (db_address,table_name2,check_col2,check_text)

# c_return = cm.add_column(db_address,add_c,add_text)
# text = cm.delete_column(db_address,delete_c)
# print(c_return)
