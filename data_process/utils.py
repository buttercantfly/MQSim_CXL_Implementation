import os
import shutil
import xml.etree.ElementTree as ET

def extract_file_path(xml_file_path):
    """
    讀取 XML 文件並提取 File_Path 元素中的值。

    :param xml_file_path: XML 文件的路徑
    :return: File_Path 中的值（字串）
    """
    try:
        # 解析 XML 文件
        tree = ET.parse(xml_file_path)
        root = tree.getroot()

        # 找到 File_Path 元素
        file_path_element = root.find(".//File_Path")  # 搜索所有的 File_Path 元素

        if file_path_element is not None:
            return file_path_element.text
        else:
            raise ValueError("無法在 XML 文件中找到 File_Path 元素。")

    except Exception as e:
        print(f"解析 XML 文件時發生錯誤: {e}")
        return None

def copy_folder(src, dest):
    """
    將 src 資料夾的內容複製到 dest 位置。

    :param src: 原始資料夾路徑
    :param dest: 目標資料夾路徑
    """
    try:
        # 確保來源資料夾存在
        if not os.path.exists(src):
            raise FileNotFoundError(f"來源資料夾不存在: {src}")

        # 確保目標資料夾存在，若不存在則建立
        if not os.path.exists(dest):
            os.makedirs(dest)

        # 使用 shutil.copytree 如果希望複製整個資料夾結構，
        # 或 shutil.copy2 來逐個檔案複製。
        for item in os.listdir(src):
            src_path = os.path.join(src, item)
            dest_path = os.path.join(dest, item)

            if os.path.isdir(src_path):
                shutil.copytree(src_path, dest_path)
            else:
                shutil.copy2(src_path, dest_path)

        print(f"資料夾內容成功複製到 {dest}")
    except Exception as e:
        print(f"複製過程中發生錯誤: {e}")

def create_text_file(file_path, content):
    """
    建立一個 .txt 檔案，並寫入指定字串內容。

    :param file_path: 新檔案的完整路徑
    :param content: 要寫入檔案的字串
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"文字檔案已建立: {file_path}")
    except Exception as e:
        print(f"建立文字檔案時發生錯誤: {e}")

def extract_config_values(config_file_path):
    """
    讀取配置檔案並提取特定的參數值。

    :param config_file_path: 配置檔案的路徑
    :return: 一個字典，包含提取的參數和值
    """
    try:
        config_values = {}
        with open(config_file_path, 'r', encoding='utf-8') as file:
            for line in file:
                # 跳過空行和註解
                if line.strip() and not line.strip().startswith("#"):
                    key, value = line.strip().split(maxsplit=1)
                    config_values[key] = value

        # 提取特定參數
        dram_size = config_values.get("DRAM_size")
        has_cache = config_values.get("Has_cache")

        return {
            "DRAM_size": dram_size,
            "Has_cache": has_cache
        }
    except Exception as e:
        print(f"解析配置檔案時發生錯誤: {e}")
        return None

def copy_config_files(src, dest):
    """
    將 src 資料夾的內容複製到 dest 位置。

    :param src: 原始資料夾路徑()
    :param dest: 目標資料夾路徑(包含新資料夾名稱)
    """
    try:
        # 確保來源資料夾存在
        if not os.path.exists(src):
            raise FileNotFoundError(f"來源資料夾不存在: {src}")

        # 確保目標資料夾存在，若不存在則建立
        if not os.path.exists(dest):
            os.makedirs(dest)

        # 使用 shutil.copytree 如果希望複製整個資料夾結構，
        # 或 shutil.copy2 來逐個檔案複製。
        for item in os.listdir(src):
            src_path = os.path.join(src, item)
            dest_path = os.path.join(dest, item)

            if os.path.isdir(src_path):
                shutil.copytree(src_path, dest_path)
            else:
                shutil.copy2(src_path, dest_path)

        print(f"資料夾內容成功複製到 {dest}")
    except Exception as e:
        print(f"複製過程中發生錯誤: {e}")