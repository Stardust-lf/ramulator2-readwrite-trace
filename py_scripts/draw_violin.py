import os
import string
from matplotlib.ticker import PercentFormatter
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch
from matplotlib.lines import Line2D
from adjustText import adjust_text

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
    1600: [
        5.08910513, 2.26677728, 3.85827041, 5.88770485, 9.57246971, 6.3080492,
        1.51721191, 0.0276872963, 13.9734201, 14.5703211, 12.4606361, 31.7582455, 1.83277535,
        5.19484234, 5.97301197, 4.82758331, 14.3808746, 3.19970226, 5.19414997, 6.38748264
    ],
    2400: [
        0.831249356, 0.28821367, 0.0834114552, 0.350590765, 0.887942433, 0.517532945,
        0.108183451, 0.0, 0.000294829428, 0.0202805568, 2.04819226, 1.0542258, 0.131418735,
        0.564604104, 0.378228366, 0.943735123, 1.72408581, 0.161390141, 0.611027837, 0.999514759
    ],
    3200: [
        1.97509744e-05, 0.0, 0.00294787483, 0.00440246705, 0.0177935921, 0.000114556045,
        0.0, 0.0, 0.0, 0.0, 0.000870672578, 0.000247819873, 0.0,
        0.0002845946, 0.00748086022, 0.0562095419, 0.045802258, 0.00320680905, 0.0530476309, 0.0195941813
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
for idx, i in enumerate([1600, 2400, 3200]):
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
    axs[0][idx].set_ylim([0.5, 5])
    axs[0][idx].set_ylabel("")

axs[0][0].set_ylabel("Norm. read frame length", fontweight="bold")

# 第二行：bar 图（用你给的表格数据）


for idx, i in enumerate([1600, 2400, 3200]):
    # 计算柱子高度
    heights = 100 - bar_df[i].values
    labels = bar_df["benchmark"].values

    # 画图
    axs[1][idx].bar(labels, heights, color = colors[idx], edgecolor="gray", label="Performance(%) ({}MT/s)".format(i))
    axs[1][idx].set_ylim([85, 100])
    axs[1][idx].grid(True, linestyle='--', linewidth=0.8, axis='y')
    axs[1][idx].set_xticklabels(labels, rotation=30, ha='right', fontsize=9)
    axs[1][idx].yaxis.set_major_formatter(PercentFormatter(xmax=100, decimals=0))

    top2_indices = np.argsort(heights)[:2]

    # for j in top2_indices:
    #     axs[1][idx].text(
    #         j, heights[j],
    #         f"{heights[j]:.2f}%",
    #         ha="center", va="bottom",
    #         # color="green",
    #     )
for idx, i in enumerate([1600, 2400, 3200]):
    heights = 100 - bar_df[i].values
    labels = bar_df["benchmark"].values

    axs[1][idx].bar(labels, heights, color=colors[idx], edgecolor="black", label=f"Performance(%) ({i}MT/s)")
    axs[1][idx].set_ylim([85, 100])
    axs[1][idx].grid(True, linestyle='--', linewidth=0.8, axis='y')
    axs[1][idx].set_xticklabels(labels, rotation=30, ha='right', fontsize=9)
    axs[1][idx].yaxis.set_major_formatter(PercentFormatter(xmax=100, decimals=0))
    axs[1][0].set_ylabel("Norm. execution time", fontweight="bold")

    # === 添加文字标签并应用 adjust_text ===
    top2_indices = np.argsort(heights)[:2]
    texts = []
    for j in top2_indices:
        txt = axs[1][idx].text(
            j, heights[j],
            f"{heights[j]:.2f}%",
            ha="center", va="bottom"
        )
        texts.append(txt)
    adjust_text(texts, ax=axs[1][idx], arrowprops=dict(arrowstyle="-", color='black', lw=0.5))

        
legend_elements = [
    Patch(facecolor='gray', edgecolor='gray', label='Read frame length (distribution)'),
    Line2D([0], [0], color='royalblue', lw=2, linestyle='--', label='Performance loss threshold'),
    Patch(facecolor='royalblue', edgecolor='black', label='Performance(%) (1600MT/s)'),
    Patch(facecolor='orange', edgecolor='black', label='Performance(%) (2400MT/s)'),
    Patch(facecolor='violet', edgecolor='black', label='Performance(%) (3200MT/s)'),
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
