import os
import string
from matplotlib.ticker import PercentFormatter
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch
from matplotlib.lines import Line2D

plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.weight'] = 'bold'
plt.rcParams['font.size'] = 9
colors = ['royalblue', 'orange', 'violet']
# plt.rcParams['font.style'] = 'italic'

# === 第一行：原始 violin plot 图 ===
input_dir = "./distribution"
data = []
for filename in os.listdir(input_dir):
    filepath = os.path.join(input_dir, filename)
    # print(filepath)
    with open(filepath, 'r') as f:
        for line in f:
            try:
                value = float(line.strip())
                data.append({"file": filename.split(".")[0], "ratio": value})
            except ValueError:
                continue

df = pd.DataFrame(data)

# === 第二行数据：你提供的 benchmark 数据 ===
bar_data = {
    "benchmark": [
        "bc road", "bc twitter", "bfs road", "bfs twitter", "cc road", "cc twitter",
        "pr road", "pr twitter", "tc road", "tc twitter", "fotonik3d", "lbm", "mcf",
        "bwaves", "roms", "parest", "wrf", "omnetpp", "gcc", "cactuBSSN"
    ],
    2800: [
        3.09989548, 1.4326216, 1.58546853, 1.50346327, 2.74425292, 1.84658098,
        0.705136299, 0.0203408357, 2.55799103, 2.86251879, 5.67411327, 9.27256775, 1.09889984,
        2.12974787, 2.51792049, 1.6363188, 5.2933445, 4.62275505, 2.35879564, 2.75383306
    ],
    3200: [
        1.49864459, 0.677859724, 0.80294174, 0.660776913, 1.23311341, 0.77966845,
        0.311788112, 0.0112541514, 1.33073807, 1.49561369, 2.41370463, 2.50061154, 0.470615029,
        0.909216523, 1.00893819, 0.665264308, 2.14170146, 2.78007245, 1.07671309, 1.25151551
    ],
    3600: [
        0.70393461, 0.300326824, 0.38822937, 0.313733131, 0.587373555, 0.325068384,
        0.145713314, 0.00551244989, 0.684278786, 0.811929226, 0.953546643, 0.864812076, 0.205219761,
        0.335178673, 0.402401805, 0.271243125, 0.814479351, 1.64947474, 0.491932184, 0.547068119
    ]
} 
benchmark_order = [
    "gcc", "mcf", "omnetpp",
    "bwaves", "cactuBSSN", "parest", "lbm", "wrf", "fotonik3d", "roms",
    "bc road", "bc twitter", "bfs road", "bfs twitter",
    "cc road", "cc twitter", "pr road", "pr twitter", "tc road", "tc twitter"
]

bar_df = pd.DataFrame(bar_data)
bar_df["benchmark"] = pd.Categorical(bar_df["benchmark"], categories=benchmark_order, ordered=True)
bar_df = bar_df.sort_values("benchmark")

# === 画图 ===
fig, axs = plt.subplots(2, 3, figsize=[16, 5], dpi=150, sharex=True)

# 第一行：violin 图（原样逻辑）
for idx, i in enumerate([2800, 3200, 3600]):
    sns.violinplot(
        x="file", y="ratio", data=df, inner="box", ax=axs[0][idx], linewidth=0.7,
        order=benchmark_order, color="gray", 
    )
    # axs[0][idx].set_yscale("log")
    axs[0][idx].grid(True, linestyle='--', linewidth=0.8, axis='y')
    axs[0][idx].set_ylim([0.1,1000])
    axs[0][idx].axhspan(0, 6400 / i - 1, linestyle='--', color=colors[idx],  alpha=0.2)
    axs[0][idx].axhline(6400 / i - 1, linestyle='--', color=colors[idx], lw=2, label="Performance loss threshold") 
    # axs[0][idx].set_title(f"Violin Plot @ {i}")
    axs[0][idx].tick_params(axis='x', labelrotation=45)
    axs[0][idx].set_ylabel("")
    axs[0][idx].set_ylim([0.5, 1.5])


# 第二行：bar 图（用你给的表格数据）


for idx, i in enumerate([2800, 3200, 3600]):
    # 计算柱子高度
    heights = 100 - bar_df[i].values
    labels = bar_df["benchmark"].values

    # 画图
    axs[1][idx].bar(labels, heights, color = colors[idx], edgecolor="black", label="Performance(%) ({}MT/s)".format(i))
    axs[1][idx].set_ylim([85, 100])
    axs[1][idx].grid(True, linestyle='--', linewidth=0.8, axis='y')
    axs[1][idx].set_xticklabels(labels, rotation=30, ha='right', fontsize=9)
    axs[1][idx].yaxis.set_major_formatter(PercentFormatter(xmax=100, decimals=0))

    top2_indices = np.argsort(heights)[:2]

    for j in top2_indices:
        axs[1][idx].text(
            j, heights[j],
            f"{heights[j]:.2f}%",
            ha="center", va="bottom",
            # color="green",
        )
        
legend_elements = [
    Patch(facecolor='gray', edgecolor='gray', label='Read frame length (relative)'),
    Line2D([0], [0], color='royalblue', lw=2, linestyle='--', label='Performance loss threshold'),
    Patch(facecolor='royalblue', edgecolor='black', label='Performance(%) (2800MT/s)'),
    Patch(facecolor='orange', edgecolor='black', label='Performance(%) (3200MT/s)'),
    Patch(facecolor='violet', edgecolor='black', label='Performance(%) (3600MT/s)'),
]

# 添加 legend 到底部
fig.legend(
    handles=legend_elements,
    loc='lower center',
    ncol=3,
    fontsize=10,
    frameon=False,
    bbox_to_anchor=(0.5, -0.01)
)
panel_labels = list(string.ascii_lowercase[:6])
for row in range(2):
    for col in range(3):
        axs[row][col].text(
            -0.05, 1.15, f"({panel_labels[row * 3 + col]})",
            transform=axs[row][col].transAxes,
            fontsize=11, fontweight='bold', va='top', ha='left'
        )
plt.tight_layout()
fig.subplots_adjust(bottom=0.2)
plt.savefig("8_1_1 perf loss.png")
plt.show()
