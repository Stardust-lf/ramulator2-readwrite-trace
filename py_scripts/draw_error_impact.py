import numpy as np
import matplotlib.pyplot as plt

# Matplotlib 全局设置
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.weight'] = 'bold'
plt.rcParams['font.size'] = 14

# Benchmarks 名单
benchmarks = [
    "gcc", "mcf", "omnetpp", "bwaves", "cactuBSSN",
    "parest", "lbm", "wrf", "fotonik3d", "roms",
    "bc road", "bc twitter", "bfs road", "bfs twitter",
    "cc road", "cc twitter", "pr road", "pr twitter",
    "tc road", "tc twitter",
    "SPEC_avg", "GAP_avg"
]

# Epsilon 噪声等级
epsilons = ["0", "1e-5", "1e-4", "1e-3", "1e-2"]
colors = ["#fddbb0", "#f4a582", "#d6604d", "#b2182b", "#67001f"]

# 初步数据
data_refined = {
    "0": [
        99.5, 99.5, 99.5, 99.5, 99.5,
        99.5, 99.5, 99.5, 99.5, 99.5,
        99.5, 99.5, 99.5, 99.5, 99.5,
        99.5, 99.5, 99.5, 99.5, 99.5,
        99.5, 99.5,
    ],
    "1e-5": [
        99.2, 99.3, 99.3, 99.2, 99.3,
        99.3, 99.3, 99.2, 99.2, 99.3,
        99.2, 99.2, 99.2, 99.3, 99.2,
        99.3, 99.2, 99.2, 99.2, 99.2,
        99.3, 99.3,
    ],
    "1e-4": [
        98.8, 98.8, 98.9, 98.9, 98.8,
        98.9, 98.9, 98.8, 98.7, 98.8,
        98.8, 98.7, 98.8, 98.9, 98.7,
        98.9, 98.8, 98.8, 98.8, 98.7,
        98.9, 98.9,
    ],
    "1e-3": [
        98.6024, 98.6024, 98.7022, 98.7022, 98.6024,
        98.7022, 98.7022, 98.6024, 98.5026, 98.6024,
        98.6024, 98.5026, 98.6024, 98.7022, 98.5026,
        98.7022, 98.6024, 98.6024, 98.6024, 98.5026,
        98.7022, 98.7022,
    ],
    "1e-2": [
        85.08, 84.95, 84.82, 85.12, 84.82,
        84.39, 84.24, 84.16, 83.91, 83.99,
        86.65, 83.80, 83.97, 84.05, 83.86,
        84.07, 83.42, 83.46, 83.73, 83.21,
        84.08, 84.05,
    ],
}

# === 重点：调整 SPEC_avg 和 GAP_avg ===
for eps in epsilons:
    group = data_refined[eps]
    avg_spec = round(np.mean(group[:10]), 2)   # 前10个
    avg_gap = round(np.mean(group[10:20]), 2)   # 中间10个
    data_refined[eps][-2] = avg_spec  # SPEC_avg
    data_refined[eps][-1] = avg_gap   # GAP_avg

# === 绘图 ===
x = np.arange(len(benchmarks))
bar_width = 0.15
fig, ax = plt.subplots(figsize=(10, 3), dpi=150)

for i, eps in enumerate(epsilons):
    heights = data_refined[eps]
    ax.bar(
        x + i * bar_width,
        heights,
        width=bar_width,
        label=eps,
        color=colors[i],
        edgecolor="black",
    )

# 坐标轴设定
ax.set_xticks(x + bar_width * 2)
ax.set_xticklabels(benchmarks, rotation=30, ha="right", fontsize=14)
ax.set_ylim(80, 100)
ax.set_yticks(np.arange(80, 101, 5))
ax.set_ylabel("Norm. exec. time", fontweight="bold")
ax.set_yticklabels([f"{v}%" for v in np.arange(80, 101, 5)])

# 图例
legend_labels = ["0", "10⁻⁵", "10⁻⁴", "10⁻³", "10⁻²"]

ax.legend(
    legend_labels,
    # title="Error prob.",
    loc="lower left",
    # bbox_to_anchor=(0.5, -0.35),
    ncol=2,
    # framealpha=0.8
)
# 网格、布局
ax.grid(True, axis="y", linestyle="--", linewidth=0.5)
plt.tight_layout()
plt.savefig("8_1_2 correction impact.png")
plt.show()
