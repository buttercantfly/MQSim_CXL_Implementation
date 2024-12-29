import os, sys
from utils import extract_file_path, copy_folder, create_text_file, extract_config_values

# 參數檔路徑 可替換為當前執行環境的
config_file_path = "C:\\Workspace\\MQSim_CXL-master\\config.txt"
xml_file_path = "C:\\Workspace\\MQSim_CXL-master\\workload.xml"

# Results資料夾路徑與目的地
source_folder = "C:\\Workspace\\MQSim_CXL-master\\Results"       # 來源資料夾路徑
storage_folder = "D:\\Workspace Data\\CXL_simulation_results"    # 目標資料夾路徑(上層)


# 讀取 config 資料 -------------------------------------------------
config_values = extract_config_values(config_file_path)

if config_values:
    print(f"DRAM_size: {config_values['DRAM_size']}")
    print(f"Has_cache: {config_values['Has_cache']}")

cache_on = int(config_values['Has_cache'])
file_name = ""

# xml file value process -------------------------------------------------
file_path_value = extract_file_path(xml_file_path)
trace_type = os.path.splitext(os.path.basename(file_path_value))[0]
num_gb = str(round(int(config_values['DRAM_size'])/1073741824, 1)).replace(".","")

# cache_on check -------------------------------------------------

if cache_on == 1:
    file_name = source_folder+ "\\latency_result.txt"
    dir_name = trace_type + "_" + num_gb + "GB_average_latency_results"
else:
    file_name = source_folder+ "\\latency_results_no_cache.txt"
    dir_name = trace_type + "_nocache_average_latency_results"

print("平均值來源檔案路徑: " + file_name)
print("資料夾名稱: " + dir_name)

# 讀取並計算latency -------------------------------------------------
with open(file_name, "r") as file:
    # 將每一行的數字讀取為列表並去除多餘空白格
    numbers = [float(line.strip()) for line in file if line.strip().isdigit()]

# 計算平均值 儲存在average變數中
if numbers:
    average = sum(numbers) / len(numbers)
    print(f"平均值是: {average} ns")
else:
    average = 0
    sys.exit("文件中沒有有效數字")

destination_folder = storage_folder + "\\" + dir_name

# 複製資料夾
copy_folder(source_folder, destination_folder)
# 建立平均值檔案
create_text_file(destination_folder + "\\" + dir_name + ".txt", str(average))