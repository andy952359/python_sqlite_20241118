import pandas as pd
import os

def xlsx_to_csv_keep_zeros(xlsx_path, csv_path, encoding='utf-8-sig'):
    # 將所有欄位讀取為字串
    df = pd.read_excel(xlsx_path, dtype=str)
    
    # 儲存為 CSV，確保中文和開頭的 0 被正確保留
    df.to_csv(csv_path, index=False, encoding=encoding)
    print(f"成功轉換，檔案保存至：{csv_path}")

def xlsx_path_to_csv(xlsx_path, encoding='utf-8-sig'):
    # 將所有欄位讀取為字串
    df = pd.read_excel(xlsx_path, dtype=str)
    csv_path = os.path.splitext(xlsx_path)[0] + ".csv"
    # 儲存為 CSV，確保中文和開頭的 0 被正確保留
    df.to_csv(csv_path, index=False, encoding=encoding)
    print(f"成功轉換，檔案保存至：{csv_path}")




