## MQSim_CXL_Implementation

This project serves as the final report for the Emerging Memory course (NCU 113-1) at National Central University. The primary objective of this project is to replicate the experiments described in the MQSim_CXL research paper.

### Background Technology

The main experimental tools utilized in this study are part of the CXL-flash Design Tools suite, comprising two primary components: the Trace Generator and MQSim CXL. The Trace Generator captures both virtual and physical addresses accessed by the program, while MQSim CXL conducts simulations based on the parameters configured and the trace files produced by the Trace Generator.

The MQSim CXL tool can be accessed via its GitHub repository at: https://github.com/spypaul/MQSim_CXL

### Implementation

The project encompasses the following activities:
- Implementation of the Trace Generator and MQSim CXL.
- Reproduction of selected experiments outlined in the original paper.
- Exploratory experiments examining the characteristics of CXL Memory.

Within the repository, the `data_process` directory contains scripts utilized for post-simulation data processing. The `results` directory contains all experimental outcomes, excluding the latency files, with summarized experimental data available within the `plots` subdirectory. For an in-depth report, please refer to the PDF file titled "CXL Design Tool Experiment Presentation Group 2."

It is important to note that the experiments cannot be entirely replicated using the instructions provided in the original paper's readme file. Additional steps are required to set up the Trace Generator, details of which can be referenced at: https://hackmd.io/@buttercantfly/Hyk2qy1S1x

Furthermore, the developed data-processing scripts include the following functionalities:

- `calculate_avg_latency.py` along with `utils.py`: These scripts facilitate copying simulation results based on the provided result directory paths, organizing data according to configuration settings, and calculating the average latency values found in `latency_result.txt` (or `latency_results_nocache.txt`).
- `ms_ratio.py`: This script automatically extracts data from all `latency_result.txt` files within a directory, computes the ms ratio (the ratio of accesses with latency under 1ms), and stores the results in `ms_ratio.txt`. For visualization purposes, the data must be manually transferred to Excel.
- `latency_result.py`: Similar to `ms_ratio.py`, this script computes the average latency of simulation results, with results also requiring manual transfer to Excel for visualization.

Please be aware that these scripts are relatively simple, and modifications to file paths are required when used.

Lastly, the files contained in the `results` directory are not complete "Result" files, as the latency data (`latency_result.txt`) has not been uploaded due to its considerable size. However, summary data and other simulation results can be accessed in corresponding subdirectories and within the `overall.txt` file.

---

## MQSim_CXL_Implementation

此專案為國立中央大學 NCU 113-1 新興記憶體課程期末報告，主要在重現 MQSim_CXL 論文中的實驗。

### 背景技術

本實驗主要使用的 CXL-flash Design Tools 包含兩個主要工具：
Trace generator 與 MQSim CXL，Trace generator 可追蹤程式的虛擬與實體地址，MQSim CXL 則是能依照設置參數與 trace genertaor 所產生的 trace 檔案進行模擬。

MQSim CXL Github網址：https://github.com/spypaul/MQSim_CXL

### 實驗實作

整體實驗內容包含：
1. 實作 Trace Generator 與 MQSim CXL
2. 重現論文中之部分實驗
3. 進行嘗試性實驗探討 CXL Memory 的向性

Repository 中 data_process 為完成模擬後的數據處理腳本，results 為不包含 latency files 的所有實驗的結果，並於 plots 子資料夾中有實驗結果整理，更為詳細的專案報告請參考 CXL Design Tool Experiment Presentation Group 2 pdf 檔。

須注意實驗過程中不能全依照原論文之 readme 進行，建立 trace generator 皆需要多一些額外操作，可參考 https://hackmd.io/@buttercantfly/Hyk2qy1S1x

此外，我所建立的數據處理腳本的功能入下：
1. calculate_avg_latency.py + utils.py: 可根據輸入的 Result 目錄路徑來複製模擬結果，並且根據 configuration 設定管理資料，同時計算 latency_result.txt (or latency_results_nocache.txt)內的平均值
2. ms_ratio.py: 可自動將目錄內的所有 latency_result.txt 檔案資料抓出，並計算其 ms ratio (延遲低於1ms的 access ratio)儲存在 ms_ratio.txt 中，在實驗中我們手動將其內的資料轉到 excel 檔案內作圖
3. latency_result.py: 與 ms_ratio.py 類似，不過是計算結果的 average latency ，並同樣需要手動將資料轉到 excel 內作圖

須注意腳本功能皆較為陽春，在使用上需注意路徑的修改。

最後，在 results 中並非完整的 "Result"，由於其大小過於龐大，因此我並沒有上傳其中的 latency_result.txt 檔案，不過可於各個子資料夾中見到對應的數據整理以及 overall.txt 內的其他模擬結果。
