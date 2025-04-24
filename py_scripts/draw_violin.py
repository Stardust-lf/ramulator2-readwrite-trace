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
        "bwaves", "roms", "parest", "wrf", "omnetpp", "gcc", "cactusBSSN"
    ],
    3200: [
        5.60341597, 2.09849381, 4.58488989, 5.5955162, 8.99129868, 6.16509247,
        1.86069095, 0.0593739524, 12.9737082, 14.2487803, 10.8527851, 7.08946419, 1.49967003,
        2.49215436, 2.42841911, 4.72773647, 7.05549383, 2.69197011, 3.26250386, 7.27782249
    ],
    4000: [
        0.563748837, 0.217301369, 0.0741956979, 0.186456695, 0.520066023, 0.303307593,
        0.0805911273, 0.0065412866, 0.000028096154, 0, 1.29286957, 0.341492265, 0.155369833,
        0.0797408447, 0.304296196, 0.662876487, 0.668257475, 0.341964006, 0.377531677, 0.915132284
    ],
    4800: [
        0.117006913, 0.0464825891, 0.00953443348, 0.0354576372, 0.127684459, 0.0559027977,
        0.0200357307, 0, 0, 0, 0.250742346, 0.0210929401, 0.0488254204,
        0.00991197769, 0.152668521, 0.177604526, 0.150871187, 0.0959257931, 0.128390372, 0.304141283
    ]
}
benchmark_order = [
    "gcc", "mcf", "omnetpp",
    "bwaves", "cactusBSSN", "parest", "lbm", "wrf", "fotonik3d", "roms",
    "bc road", "bc twitter", "bfs road", "bfs twitter",
    "cc road", "cc twitter", "pr road", "pr twitter", "tc road", "tc twitter"
]

bar_df = pd.DataFrame(bar_data)
bar_df["benchmark"] = pd.Categorical(bar_df["benchmark"], categories=benchmark_order, ordered=True)
bar_df = bar_df.sort_values("benchmark")

# === 画图 ===
fig, axs = plt.subplots(2, 3, figsize=[16, 5], dpi=150, sharex=True)

# 第一行：violin 图（原样逻辑）
for idx, i in enumerate([3200, 4000, 4800]):
    sns.violinplot(
        x="file", y="ratio", data=df, inner="box", ax=axs[0][idx], linewidth=0.7,
        order=benchmark_order, color="gray"
    )
    axs[0][idx].set_yscale("log")
    axs[0][idx].grid(True, linestyle='--', linewidth=0.8, axis='y')
    axs[0][idx].set_ylim([0.1,1000])
    axs[0][idx].axhspan(0, 6400 / i - 1, linestyle='--', color=colors[idx],  alpha=0.2)
    axs[0][idx].axhline(6400 / i - 1, linestyle='--', color=colors[idx], lw=2, label="Performance loss threshold") 
    # axs[0][idx].set_title(f"Violin Plot @ {i}")
    axs[0][idx].tick_params(axis='x', labelrotation=45)
    axs[0][idx].set_ylabel("")


# 第二行：bar 图（用你给的表格数据）


for idx, i in enumerate([3200, 4000, 4800]):
    # 计算柱子高度
    heights = 100 - bar_df[i].values
    labels = bar_df["benchmark"].values

    # 画图
    axs[1][idx].bar(labels, heights, color = colors[idx], edgecolor="black", label="Performance(%) ({}MT/s)".format(i))
    axs[1][idx].set_ylim([85, 100])
    axs[1][idx].grid(True, linestyle='--', linewidth=0.8, axis='y')
    axs[1][idx].set_xticklabels(labels, rotation=30, ha='right', fontsize=7)
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
    Patch(facecolor='royalblue', edgecolor='black', label='Performance(%) (3200MT/s)'),
    Patch(facecolor='orange', edgecolor='black', label='Performance(%) (4000MT/s)'),
    Patch(facecolor='violet', edgecolor='black', label='Performance(%) (4800MT/s)'),
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
plt.savefig("combined_violin_bar_plot.png")
plt.show()
