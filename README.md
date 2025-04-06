# 量子測量統計實驗（使用 Qiskit）

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![Qiskit](https://img.shields.io/badge/Qiskit-1.0%2B-purple)
![授權條款](https://img.shields.io/badge/License-MIT-green)

一個使用 Qiskit 重複運行量子電路並分析測量結果的 Python 腳本。

## 📌 專案概述

本專案實現：
- 創建包含 1 個量子位元和哈達瑪門（Hadamard gate）的基本量子電路
- 通過多次實驗收集測量統計數據
- 分析 |0⟩ 和 |1⟩ 狀態的機率分佈
- 使用 matplotlib 可視化實驗結果

## ⚙️ 環境需求

- Python 3.7 或更新版本
- 必要套件：
  ```bash
  pip install qiskit qiskit-aer matplotlib
  ```

## 🚀 執行方式

1. 複製本專案：
   ```bash
   git clone https://github.com/Lzh888888888/Qubit_measurement_statistics.git
   ```
2. 安裝依賴套件：
   ```bash
   pip install -r requirements.txt
   ```
3. 運行主程式：
   ```bash
   python quantum_measurement.py
   ```

## 📊 預期輸出

程式將會：
1. 顯示每次實驗的獨立結果
2. 輸出統整統計數據：
   ```
   ===== 最終統計結果 =====
   總運行次數: 10000 (10 次實驗 x 1000 次測量)
   0 出現次數: 5023 (50.23%)
   1 出現次數: 4977 (49.77%)
   ```
3. 顯示長條圖視覺化結果

## 🧮 技術細節

- **量子電路設計**：
  ```python
  qc = QuantumCircuit(1, 1)
  qc.h(0)  # 施加哈達瑪門
  qc.measure(0, 0)
  ```
- **模擬器**：使用 Qiskit Aer 的 `qasm_simulator`
- **實驗設定**：可調整實驗次數與每次測量次數

## 📈 理論背景

哈達瑪門會創建量子疊加態：
```
H|0⟩ = (|0⟩ + |1⟩)/√2
```
在理想情況下，測量結果應呈現 50% |0⟩ 和 50% |1⟩ 的分佈。

## 📂 專案結構

```
quantum_measurement/
├── quantum_measurement.py  # 主程式
├── README.md               # 本文件
└── requirements.txt        # 套件需求
```

## 📜 授權條款

MIT 授權 - 可自由用於教育與研究用途

## ✉️ 聯絡方式

如有問題或建議，請在本專案提交 issue。
```

---

### 補充說明：
1. 若需 `requirements.txt` 文件，內容建議如下：
   ```
   qiskit>=1.0
   qiskit-aer>=0.12
   matplotlib>=3.5
   ```

2. 進階建議：
   - 上傳至 GitHub 時可添加標籤 `quantum-computing` 和 `qiskit`
   - 可加入 `.gitignore` 文件過濾 Python 暫存檔
   - 進階版本可附加 Jupyter Notebook 範例

此 README 提供完整的繁體中文說明，包含理論基礎、技術細節與執行方法，非常適合教學分享或協作開發。