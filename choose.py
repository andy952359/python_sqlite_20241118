import os

def select_files(folder_path):

    try:
        # 確保資料夾存在
        if not os.path.exists(folder_path):
            print("資料夾不存在！")
            return None

        # 列出所有檔案
        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        if not files:
            print("資料夾中沒有檔案！")
            return None

        # 顯示檔案列表
        print("檔案列表：")
        for i, file in enumerate(files, start=1):
            print(f"{i}. {file}")

        selected_files = []  # 儲存使用者選擇的檔案

        # 要求使用者選擇三次
        for attempt in range(3):
            while True:
                try:
                    choice = int(input(f"請輸入第 {attempt + 1} 個檔案編號 (輸入0退出)： "))
                    if choice == 0:
                        print("已退出選擇。")
                        return selected_files if selected_files else None
                    elif 1 <= choice <= len(files):
                        selected_file = os.path.join(folder_path, files[choice - 1])
                        print(f"你選擇的檔案是：{selected_file}")
                        selected_files.append(selected_file)
                        break  # 進入下一次選擇
                    else:
                        print("無效的編號，請重新輸入！")
                except ValueError:
                    print("請輸入有效的編號！")

        print("你選擇的檔案如下：")
        for file in selected_files:
            print(file)

        return selected_files
    except Exception as e:
        print(f"發生錯誤：{e}")
        return None


