import os

def calculate_average_from_file(file_path):
    """
    計算指定檔案中所有數值的平均值。
    檔案應該是一行一個數值。
    """
    try:
        with open(file_path, 'r') as file:
            numbers = [float(line.strip()) for line in file if line.strip()]
        if not numbers:
            return None  # 如果檔案是空的或無有效數字，返回 None
        return sum(numbers) / len(numbers)
    except Exception as e:
        print(f"無法處理檔案 {file_path}: {e}")
        return None

def process_folder_and_write_results(folder_path, output_file):
    """
    遍歷資料夾及其子資料夾，尋找 latency_result.txt 檔案，計算平均值，並寫入結果檔案。
    """
    results = []

    for root, _, files in os.walk(folder_path):
        for file in files:
            if file == "latency_result.txt":
                file_path = os.path.join(root, file)
                avg = calculate_average_from_file(file_path)
                if avg is not None:
                    results.append((file_path, avg))

    # 將結果寫入輸出檔案
    try:
        with open(output_file, 'w') as output:
            for file_path, avg in results:
                output.write(f"{file_path}: {avg}\n")
        print(f"處理完成！結果已寫入 {output_file}")
    except Exception as e:
        print(f"無法寫入結果檔案 {output_file}: {e}")

if __name__ == "__main__":
    # 使用者需要設定的目錄路徑與輸出檔案名稱
    folder_path = "E:\\cache policy"
    output_file = "E:\\cache policy\\latency_result_all.txt"

    if os.path.isdir(folder_path):
        process_folder_and_write_results(folder_path, output_file)
    else:
        print(f"無效的資料夾路徑: {folder_path}")
