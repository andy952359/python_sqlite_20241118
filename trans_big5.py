import chardet
import pandas as pd

# 指定 CSV 檔案路徑
# csv_address = ".\\csv\\test-utf-8.csv"

def trans (csv_address):
    # 檢測文件的編碼
    with open(csv_address, 'rb') as f:
        raw_data = f.read()
        result = chardet.detect(raw_data)
        encoding = result['encoding']
        print(f"檢測到的編碼：{encoding}")

    # 使用檢測的編碼讀取文件
    try:
        df = pd.read_csv(csv_address, encoding='BIG5')
        print("文件成功讀取：")
        print(df.head())
    except Exception as e:
        print(f"讀取文件失敗：{e}")


    # df = pd.read_csv(csv_address, encoding='BIG5')

    # pattern = r'^[好六喔]'
    # df['e_number_check'] = df['AB126'].str.match(pattern)

    # 保存為 BIG5 格式的 CSV 文件
    df.to_csv(csv_address, encoding='big5', index=False)
    print(f"CSV 文件已保存為 BIG5 格式：{csv_address}")
