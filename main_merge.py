import pandas as pd
import sqlite3
import xlsx2csv
import trans_big5
import choose
import insert_csv as csv
import insert2 
import etl_insert
import column_modify as cm
import check
import analysis
import output

folder_path = f".\csv"
csv_name = "二期總表_20240722"
csv_name2 = "Ami-2024-11-18-1705"
csv_name3 = "AMI-108-ETL-2024-11-17"
csv_name4 = "電號"
xlsx_path1 = f".\csv\{csv_name}.xlsx"
xlsx_path2 = f".\csv\{csv_name2}.xlsx"
xlsx_path3 = f".\csv\{csv_name3}.xlsx"
xlsx_path4 = f".\csv\{csv_name4}.xlsx"
csv_path1 = f".\csv\{csv_name}.csv"
csv_path2 = f".\csv\{csv_name2}.csv"
csv_path3 = f".\csv\{csv_name3}.csv"
output_address = ".\csv\\table_1.xlsx"
output_address2 = ".\csv\\table_2.xlsx"
output_address3 = ".\csv\\table_3.xlsx"
output_address4 = ".\csv\\table_4.xlsx"
table_name = "customers"
table_name2 = "customers_2"
db_address = ".\db\customers-2000000.db" 
add_c = "期數"
add_text = "108"
delete_c = "analysis_status"
on = "11碼電號"
on_2 = "電號"
on_etl = f"表號_{csv_name2}"
on_etl_2 = "電表 ID"
on_c = "電號"
check_status = "check_number"
analysis_status = "analysis_status"
MN_status = "MN_check"
check_col1 = f"11碼電號_{csv_name}"
check_col2 = f"表號_{csv_name2}"
check_col3 = f"FAN 號_{csv_name2}"
check_col4 = f"施工問題_{csv_name2}"
check_col5 = f"MN Count_{csv_name3}"
subset = f"11碼電號_{csv_name}"
check_text = '無'
check_text2 = "0"
pattern1 = r'^\d{11}$'
pattern2 = r'^[A-Z]{2}\d{8}$'
pattern3 = r'^[A][D]\d{10}$'


    # ^：表示字串的開始。
    # [A-Za-z]：表示第1個字元為英文字母（大小寫均可）。
    # \d{5}：表示接下來的5個字元為數字。
    # [A-Za-z]{9}：表示接下來的9個字元為英文字母（大小寫均可）。
    # $：表示字串的結束。


# c_return = cm.add_column (db_address,table_name, add_c, add_text)
# text = cm.delete_column (db_address,table_name2,delete_c)


# selected_files = choose.select_files(folder_path)
# xlsx2csv.xlsx_path_to_csv (selected_files[0])
# xlsx2csv.xlsx_path_to_csv (selected_files[1])
# xlsx2csv.xlsx_path_to_csv (selected_files[2])


# xlsx2csv.xlsx_to_csv_keep_zeros (xlsx_path1, csv_path1)
# xlsx2csv.xlsx_to_csv_keep_zeros (xlsx_path2, csv_path2)
# xlsx2csv.xlsx_to_csv_keep_zeros (xlsx_path3, csv_path3)


# insert2.insert_csv (csv_path1,csv_path2,db_address,table_name,on,on_2,csv_name,csv_name2)
# etl_insert.insert_csv (csv_path3,db_address,table_name,table_name2,on_etl,on_etl_2,csv_name3)


# check.check_number (db_address,table_name2,check_status,check_col1,pattern1)
# check.check_number (db_address,table_name2,check_status,check_col2,pattern2)
# check.check_number (db_address,table_name2,check_status,check_col3,pattern3)
# check.text_check (db_address,table_name2,check_status,check_col4,check_text)
# check.MN_check (db_address,table_name2,MN_status,check_col5,check_text2)

analysis.status(db_address, table_name2, csv_name,  csv_name2, csv_name3, on, on_2, on_etl, analysis_status)

# output.xlsx (db_address,table_name,output_address)
# output.xlsx (db_address,table_name2,output_address2)
# output.unduplicate_xlsx (db_address,table_name2,subset,output_address3)
# output.default_xlsx(db_address, table_name2, output_address4)
# output.choice_column_xlsx (db_address,table_name2,output_address4)
output.choice_meter_default_xlsx(db_address, table_name2, xlsx_path4, check_col1, on_c, output_address4)