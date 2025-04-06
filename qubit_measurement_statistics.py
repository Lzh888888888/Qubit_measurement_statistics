from qiskit import QuantumCircuit
from qiskit_aer import Aer
import matplotlib.pyplot as plt 

# 設定實驗參數
num_experiments = 10  # 重複運行 10 次
shots_per_experiment = 1000  # 每次實驗的測量次數

# 初始化統計
total_counts = {'0': 0, '1': 0}

# 建立量子電路
qc = QuantumCircuit(1, 1)
qc.h(0)
qc.measure(0, 0)

# 選擇模擬器
backend = Aer.get_backend('qasm_simulator')

# 開始重複實驗
for i in range(num_experiments):
    job = backend.run(qc, shots=shots_per_experiment)
    result = job.result()
    counts = result.get_counts()
    
    # 累加結果到總統計
    for bit, count in counts.items():
        total_counts[bit] += count
    
    # 打印單次實驗結果（可選）
    print(f"實驗 {i+1}/{num_experiments} 結果:", counts)

# 計算總比例
total_shots = num_experiments * shots_per_experiment
prob_0 = total_counts['0'] / total_shots * 100
prob_1 = total_counts['1'] / total_shots * 100

# 打印統整結果
print("\n===== 最終統計結果 =====")
print(f"總運行次數: {total_shots} ( {num_experiments} 次實驗 x {shots_per_experiment} shots )")
print(f"0 出現次數: {total_counts['0']} ({prob_0:.2f}%)")
print(f"1 出現次數: {total_counts['1']} ({prob_1:.2f}%)")

#繪製長條圖
plt.bar(['0', '1'], [prob_0, prob_1], color=['blue', 'orange'])
plt.title('Statistics of qubit measurement results')
plt.ylabel('Proportion (%)')
plt.show()