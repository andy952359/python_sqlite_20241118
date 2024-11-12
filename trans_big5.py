import chardet
import pandas as pd

# 指定 CSV 檔案路徑
csv_address3 = ".\\csv\\test-utf-8.csv"
utf8_csv_address = ".\\csv\\customers-102-unicode-trans.csv"  # 新的 UTF-8 文件保存路徑

# 檢測文件的編碼
with open(csv_address3, 'rb') as f:
    raw_data = f.read()
    result = chardet.detect(raw_data)
    encoding = result['encoding']
    print(f"檢測到的編碼：{encoding}")

# 使用檢測的編碼讀取文件
try:
    df3 = pd.read_csv(csv_address3, encoding='BIG5')
    print("文件成功讀取：")
    print(df3.head())
except Exception as e:
    print(f"讀取文件失敗：{e}")


df = pd.read_csv(csv_address3, encoding='BIG5')

pattern = r'^[好六喔]'
df['e_number_check'] = df['AB126'].str.match(pattern)

# 保存為 BIG5 格式的 CSV 文件
df.to_csv(utf8_csv_address, encoding='big5', index=False)
print(f"CSV 文件已保存為 BIG5 格式：{utf8_csv_address}")
