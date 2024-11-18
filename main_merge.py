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
on = "Customer Id"
on_etl = "First Name"
csv_name = "customers-100"
csv_name2 = "customers-101"
csv_name3 = "customers-102.csv"
check_col = "Customer Id"
check_col2 = "Country_customers-102.csv"
check_text = '無'


# select_check = csv.insert_csv (csv_address,db_address,table_name)
# print(select_check)

# select_check = insert2.insert_csv (csv_address,csv_address2,db_address,table_name,on,csv_name,csv_name2)
# print(select_check)

select_check = etl_insert.insert_csv (csv_address3,db_address,table_name,table_name2,on_etl,csv_name3)
print(select_check)


select_check = check.e_number (db_address,table_name2,check_col,check_col2,check_text)
select_check = check.FAN_number (db_address,table_name2,check_col)
select_check = check.text_check (db_address,table_name2,check_col2,check_text)

# c_return = cm.add_column(db_address,add_c,add_text)
# text = cm.delete_column(db_address,delete_c)
# print(c_return)
