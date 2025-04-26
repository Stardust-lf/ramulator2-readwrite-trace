import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.weight'] = 'bold'
plt.rcParams['font.size'] = 12

# 横坐标组名（每组代表一个场景）
group_labels = ['13579', '13579', '13579', '13579']
n_groups = len(group_labels)

# 每组有4根柱子
bar_width = 0.18
x = np.arange(n_groups)

# === 图 (a) 数据 ===
# 制造成本（每个方案）
manu_cost_a = [0.5, 0.5, 0.6, 0.6]

# 运行成本：Baseline SPEC, GreenMem-Recyc SPEC, Baseline GAP, GreenMem-Recyc GAP
baseline_spec = [0.52, 0.5, 0.52, 0.5]
greenmem_recyc_spec = [0.46, 0.5, 0.6, 0.65]
baseline_gap = [0.2, 0.25, 0.3, 0.4]
greenmem_recyc_gap = [0.4, 0.5, 0.55, 0.6]

# === 图 (b) 数据 ===
manu_cost_b = [1.0, 1.0, 1.1, 1.1]
baseline_spec_b = [0.1, 0.15, 0.3, 0.35]
baseline_gap_b = [0.2, 0.25, 0.35, 0.4]
greenmem_framewk_spec = [0.7, 0.8, 1.1, 1.3]
greenmem_framewk_gap = [0.9, 1.0, 1.2, 1.3]

# === 创建图像 ===
fig, axs = plt.subplots(1, 2, figsize=(13, 5))

# 位置偏移
offsets = [-1.5, -0.5, 0.5, 1.5]

# === 图 (a) ===
axs[0].bar(x + offsets[0]*bar_width, manu_cost_a, bar_width, color='lightblue', hatch='//')
axs[0].bar(x + offsets[0]*bar_width, baseline_spec, bar_width, bottom=manu_cost_a, color='lightblue', label='Baseline SPEC')

axs[0].bar(x + offsets[1]*bar_width, manu_cost_a, bar_width, color='salmon', hatch='//')
axs[0].bar(x + offsets[1]*bar_width, greenmem_recyc_spec, bar_width, bottom=manu_cost_a, color='salmon', label='GreenMem-Recyc SPEC')

axs[0].bar(x + offsets[2]*bar_width, manu_cost_a, bar_width, color='royalblue', hatch='//')
axs[0].bar(x + offsets[2]*bar_width, baseline_gap, bar_width, bottom=manu_cost_a, color='royalblue', label='Baseline GAP')

axs[0].bar(x + offsets[3]*bar_width, manu_cost_a, bar_width, color='tomato', hatch='//')
axs[0].bar(x + offsets[3]*bar_width, greenmem_recyc_gap, bar_width, bottom=manu_cost_a, color='tomato', label='GreenMem-Recyc GAP')

axs[0].text(x[1] + offsets[1]*bar_width, 0.96, "0.96", color='green', ha='center')
axs[0].text(x[2] + offsets[1]*bar_width, 1.25, "1.25", color='green', ha='center')
axs[0].text(x[3] + offsets[3]*bar_width, 1.01, "1.01", color='green', ha='center')

axs[0].set_ylabel("Energy Cost (GJ)")
axs[0].set_xticks(x)
axs[0].set_xticklabels(group_labels)
axs[0].set_title("(a)")

# === 图 (b) ===
axs[1].bar(x + offsets[0]*bar_width, manu_cost_b, bar_width, color='lightblue', hatch='//')
axs[1].bar(x + offsets[0]*bar_width, baseline_spec_b, bar_width, bottom=manu_cost_b, color='lightblue', label='Baseline SPEC')

axs[1].bar(x + offsets[1]*bar_width, manu_cost_b, bar_width, color='royalblue', hatch='//')
axs[1].bar(x + offsets[1]*bar_width, baseline_gap_b, bar_width, bottom=manu_cost_b, color='royalblue', label='Baseline GAP')

axs[1].bar(x + offsets[2]*bar_width, manu_cost_b, bar_width, color='salmon', hatch='//')
axs[1].bar(x + offsets[2]*bar_width, greenmem_framewk_spec, bar_width, bottom=manu_cost_b, color='salmon', label='GreenMem-Framewk SPEC')

axs[1].bar(x + offsets[3]*bar_width, manu_cost_b, bar_width, color='tomato', hatch='//')
axs[1].bar(x + offsets[3]*bar_width, greenmem_framewk_gap, bar_width, bottom=manu_cost_b, color='tomato', label='GreenMem-Framewk GAP')

axs[1].text(x[0] + offsets[2]*bar_width, 2.08, "2.08", color='green', ha='center')
axs[1].text(x[3] + offsets[3]*bar_width, 2.41, "2.41", color='green', ha='center')

axs[1].set_ylabel("Energy Cost (GJ)")
axs[1].set_xticks(x)
axs[1].set_xticklabels(group_labels)
axs[1].set_title("(b)")

# 图例
fig.legend(ncol=4, loc='lower center', bbox_to_anchor=(0.5, -0.05))
fig.tight_layout()
plt.show()
