import pandas as pd
import sqlite3
import insert_csv as csv
import insert2 
import column_modify as cm

csv_address = ".\csv\customers-100.csv"
csv_address2 = ".\csv\customers-101.csv"
table_name = "customers"
db_address = ".\db\customers-100.db" 
add_c = "期數"
add_text = "108"
delete_c = "期數"

select_check = csv.insert_csv (csv_address,db_address,table_name)
print(select_check)


#c_return = cm.add_column(db_address,add_c,add_text)
#text = cm.delete_column(db_address,delete_c)
#print(c_return)
