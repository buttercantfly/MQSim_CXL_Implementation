import os

def calculate_percentage_below_threshold(file_path, threshold=1000):
    """
    讀取檔案內容，並計算數值低於閾值的比例（百分比）。
    :param file_path: latency_result.txt 的路徑
    :param threshold: 閾值，預設為 1000
    :return: 檔案內數值低於閾值的比例（百分比）
    """
    try:
        with open(file_path, 'r') as file:
            numbers = [float(line.strip()) for line in file if line.strip().isdigit() or is_float(line.strip())]
        if numbers:
            below_threshold = [num for num in numbers if num < threshold]
            percentage = (len(below_threshold) / len(numbers)) * 100
            return percentage
        else:
            print(f"檔案 {file_path} 沒有有效的數字。")
            return None
    except Exception as e:
        print(f"讀取檔案 {file_path} 時發生錯誤: {e}")
        return None

def is_float(value):
    """檢查字串是否為有效的浮點數"""
    try:
        float(value)
        return True
    except ValueError:
        return False

def process_directory(root_dir, output_file):
    """
    遍歷目錄，找到所有名為 latency_result.txt 的檔案並計算數值低於閾值的比例。
    :param root_dir: 根目錄
    :param output_file: 儲存結果的檔案
    """
    results = []
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename == "latency_result.txt":
                file_path = os.path.join(dirpath, filename)
                print(f"處理檔案: {file_path}")
                percentage = calculate_percentage_below_threshold(file_path)
                if percentage is not None:
                    result = f"檔案 {file_path} 的數值低於 1000 的比例為: {percentage:.2f}%"
                    print(result)
                    results.append(result)
    # 將結果寫入檔案
    try:
        with open(output_file, 'w') as output:
            output.write("\n".join(results))
        print(f"所有結果已儲存至 {output_file}")
    except Exception as e:
        print(f"寫入結果檔案 {output_file} 時發生錯誤: {e}")

if __name__ == "__main__":
    root_directory = "E:\\cache policy"
    output_file_path = "E:\\cache policy\\ms_ratio.txt"
    if os.path.isdir(root_directory):
        process_directory(root_directory, output_file_path)
    else:
        print("提供的路徑不是有效的目錄！")