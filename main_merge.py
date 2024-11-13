import pandas as pd
import sqlite3
import trans_big5
import insert_csv as csv
import insert2 
import etl_insert
import column_modify as cm
import check

csv_address = ".\csv\customers-100.csv"
csv_address2 = ".\csv\customers-101.csv"
csv_address3 = ".\csv\customers-102.csv"
table_name = "customers"
table_name2 = "customers_2"
db_address = ".\db\customers-100.db" 
add_c = "期數"
add_text = "108"
delete_c = "期數"


# select_check = csv.insert_csv (csv_address,db_address,table_name)
# print(select_check)

# select_check = insert2.insert_csv (csv_address,csv_address2,db_address,table_name)
# print(select_check)

select_check = etl_insert.insert_csv (csv_address3,db_address,table_name,table_name2)
print(select_check)

# select_check = check.e_number (db_address,table_name2)
# select_check = check.FAN_number (db_address,table_name2)

# c_return = cm.add_column(db_address,add_c,add_text)
# text = cm.delete_column(db_address,delete_c)
# print(c_return)
