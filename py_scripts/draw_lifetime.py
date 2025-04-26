import numpy as np
import matplotlib.pyplot as plt

# === 通用设置 ===
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.weight'] = 'bold'
plt.rcParams['font.size'] = 12

# === 平滑函数（保留首尾，中间加权平均） ===
def smooth_counts(counts):
    smoothed = [counts[0]]
    for i in range(1, len(counts) - 1):
        val = 0.25 * counts[i - 1] + 0.5 * counts[i] + 0.25 * counts[i + 1]
        smoothed.append(val)
    smoothed.append(counts[-1])
    return smoothed

# === 第一组原始数据 ===
raw_data = {
    'AMD-chipkill': [0.0, 5.6e-05, 0.000188, 0.000362, 0.000656, 0.000914, 0.001342, 0.001702, 0.002116, 0.002684, 0.00319, 0.003538, 0.004066, 0.00493],
    'Green': [0.0, 2e-06, 2e-05, 5.2e-05, 0.000102, 0.000168, 0.000258, 0.000314, 0.000382, 0.00051, 0.00063, 0.000776, 0.000888, 0.001066],
    'Bamboo': [0.0, 5.8e-05, 0.00018, 0.000368, 0.000642, 0.00099, 0.001346, 0.001748, 0.002182, 0.002626, 0.003186, 0.003712, 0.004322, 0.004966],
    'Green-Bamboo': [0.0, 0.0, 6e-06, 1.8e-05, 3.2e-05, 4.4e-05, 6.4e-05, 7.8e-05, 9.8e-05, 0.000112, 0.00013, 0.000158, 0.000196, 0.00022]
}
smoothed_data = {k: smooth_counts(v) for k, v in raw_data.items()}
time_points = list(np.arange(1, 14))
smoothed_data = {k: v[1:] for k, v in smoothed_data.items()}

# === 第二组数据 ===
raw_data_2 = {
    'AMD-chipkill': [3e-7, 1e-6, 2e-6, 3e-6, 5e-6, 8e-6, 1e-5, 1.5e-5, 2e-5, 2.5e-5, 3e-5, 4e-5, 5e-5],
    'Green': [3e-9, 2e-8, 4e-8, 9e-8, 2e-7, 3e-7, 5e-7, 7e-7, 1e-6, 1.5e-6, 2e-6, 3e-6, 4e-6],
    'Bamboo': [5e-11, 1e-10, 3e-10, 6e-10, 1e-9, 2e-9, 3e-9, 5e-9, 7e-9, 1e-8, 1.3e-8, 1.8e-8, 2.5e-8],
    'Green-Bamboo': [0.0, 0.0, 0.0, 0.0, 1e-12, 5e-12, 1e-11, 3e-11, 5e-11, 1e-10, 2e-10, 3e-10, 5e-10]
}
smoothed_data_2 = {k: smooth_counts(v) for k, v in raw_data_2.items()}
time_2 = list(range(1, 14))

# === 第三组 DUE/SDC数据 ===
time = np.array([ 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0])
amd_due = np.array([ 0.089422, 0.170921, 0.245197, 0.312909, 0.374085, 0.430055, 0.480589, 0.527117, 0.56926, 0.607174, 0.642136, 0.673933, 0.702767])
amd_sdc = np.array([ 0.000256, 0.000504, 0.000725, 0.000918, 0.001109, 0.001277, 0.001445, 0.001601, 0.001729, 0.001839, 0.001944, 0.002039, 0.002124])
bamboo_due = np.array([ 0.000367, 0.001516, 0.003301, 0.005813, 0.008852, 0.012283, 0.01627, 0.020434, 0.025208, 0.030113, 0.035231, 0.04077, 0.046476])
bamboo_sdc = np.array([ 9e-06, 3.3e-05, 5.7e-05, 9.7e-05, 0.000157, 0.00021, 0.000274, 0.000339, 0.000431, 0.000505, 0.000583, 0.000665, 0.000762])

# === 创建2x2子图 ===
fig, axes = plt.subplots(1, 4, figsize=(8, 5), dpi=150,sharey=True)

# (0,0) 第1幅：原始DUE数据
ax = axes[0]
ax.plot(time_points, smoothed_data['AMD-chipkill'],  linestyle='-', color='red', label='Chipkill', lw=1.5, ms=4)
ax.plot(time_points, smoothed_data['Green'],  linestyle='-', color='orange', label='SCREME', lw=1.5, ms=4)
ax.plot(time_points, smoothed_data['Bamboo'],  linestyle='-', color='green', label='En-ChipKill', lw=1.5, ms=4)
ax.plot(time_points, smoothed_data['Green-Bamboo'],  linestyle='-', color='dodgerblue', label='SCREME+En-ChipKill', lw=1.5, ms=4)
ax.set_yscale('log')
ax.set_xlabel('Time (Years)', fontweight="bold")
ax.set_ylabel('Failure probability(%)', fontweight="bold")
ax.grid(True, which="major", linestyle='--')
# ax.legend()
ax.text(0.0, 1.0, "(a)", transform=ax.transAxes, fontsize=16, fontweight='bold', va='top', ha='left')

# (0,1) 第2幅：新图DUE数据
ax = axes[1]
ax.plot(time_2, smoothed_data_2['AMD-chipkill'],  linestyle='-', color='red', label='Chipkill', lw=1.5, ms=4)
ax.plot(time_2, smoothed_data_2['Green'],  linestyle='-', color='orange', label='SCREME', lw=1.5, ms=4)
ax.plot(time_2, smoothed_data_2['Bamboo'],  linestyle='-', color='green', label='En-ChipKill', lw=1.5, ms=4)
ax.plot(time_2, smoothed_data_2['Green-Bamboo'],  linestyle='-', color='dodgerblue', label='SCREME+En-ChipKill', lw=1.5, ms=4)
ax.set_yscale('log')
ax.set_xlabel('Time (Years)', fontweight="bold")
ax.set_ylim([1e-12, 10])
ax.grid(True, which="major", linestyle='--')
ax.text(0.0, 1.0, "(b)", transform=ax.transAxes, fontsize=16, fontweight='bold', va='top', ha='left')

# (1,0) 第3幅：DUE概率
ax = axes[2]
ax.set_yscale('log')
ax.plot(time, amd_due, label='Chipkill',  linestyle='-', color='red', lw=1.5, ms=4)
ax.plot(time, smoothed_data['AMD-chipkill'], label='SCREME',  linestyle='-', color='orange', lw=1.5, ms=4)
ax.plot(time, bamboo_due, label='En-ChipKill',  linestyle='-', color='green',  lw=1.5, ms=4)
ax.plot(time, smoothed_data['Bamboo'], label='SCREME+En-ChipKill',  linestyle='-', color='dodgerblue',  lw=1.5, ms=4)
# ax.set_ylabel('Probability')
ax.set_xlabel('Time (Years)', fontweight="bold")
# ax.set_title('DUE Probability')
ax.grid(True, which='major', linestyle = '--')
# ax.legend()
ax.text(0.0, 1.0, "(c)", transform=ax.transAxes, fontsize=16, fontweight='bold', va='top', ha='left')

# (1,1) 第4幅：SDC概率
ax = axes[3]
ax.set_yscale('log')
ax.plot(time, amd_sdc, label='Chipkill',  linestyle='-', color='red', lw = 1.5, ms=4)
ax.plot(time, smoothed_data_2['AMD-chipkill'], label='SCREME',  linestyle='-', color='orange', lw=1.5, ms=4)
ax.plot(time, bamboo_sdc, label='En-ChipKill',  linestyle='-', color='green',  lw=1.5, ms=4)
ax.plot(time, smoothed_data_2['Bamboo'], label='SCREME+En-ChipKill',   linestyle='-', color='dodgerblue',  lw=1.5, ms=4)
# ax.set_ylabel('Probability')
ax.set_xlabel('Time (Years)', fontweight="bold")
# ax.set_title('SDC Probability')
ax.grid(True, which='major', linestyle = '--')
# ax.legend()
ax.text(0.0, 1.0, "(d)", transform=ax.transAxes, fontsize=16, fontweight='bold', va='top', ha='left')

handles, labels = ax.get_legend_handles_labels()
plt.tight_layout(rect=[0, 0.05, 1, 1]) 
fig.legend(handles, labels, loc='lower center', ncol=4, bbox_to_anchor=(0.5, 0), fontsize=12, frameon=False)

# plt.tight_layout()
plt.savefig("combined_lifetime.png")
plt.show()
