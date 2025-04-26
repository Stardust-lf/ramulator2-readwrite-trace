import matplotlib.pyplot as plt
import numpy as np
from adjustText import adjust_text

plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.weight'] = 'bold'
plt.rcParams['font.size'] = 14

xtick_labels = [
    "gcc", "mcf", "omnetpp", "bwaves", "cactuBSSN",
    "parest", "lbm", "wrf", "fotonik3d", "roms",
    "bc road", "bc twitter", "bfs road", "bfs twitter",
    "cc road", "cc twitter", "pr road", "pr twitter",
    "tc road", "tc twitter",
    "SPEC_avg", "GAP_avg"
]
# === 第一个图的数据 ===
ideal = [100.0] * 22
half_rank = [
    67.0, 67.0, 67.0, 67.0, 67.0,
    66.0, 60.0, 58.0, 67.0, 61.0,
    52.0, 60.0, 66.0, 67.0, 68.0,
    63.0, 65.0, 61.0, 66.0, 64.0,
    0, 0
]
greenmem_1 = [
    92.0, 93.0, 93.0, 93.0, 93.0,
    95.0, 96.0, 97.0, 95.0, 96.0,
    88.0, 91.0, 92.0, 91.0, 90.0,
    87.0, 89.0, 91.0, 90.0, 91.0,
    0, 0
]
half_rank[-2] = np.mean(half_rank[:11])
half_rank[-1] = np.mean(half_rank[11:])
greenmem_1[-2] = np.mean(greenmem_1[:11])
greenmem_1[-1] = np.mean(greenmem_1[11:-2])

# === 第二个图的数据 ===
baseline_20 = [100.0] * 22
ganged_20 = [
    72.0, 59.0, 70.0, 58.0, 74.0,
    76.0, 68.0, 60.0, 67.0, 62.0,
    48.0, 47.0, 48.0, 49.0, 49.0,
    49.0, 48.0, 50.0, 51.0, 52.0,
    0, 0
]
greenmem_20 = [
    98.5, 98.7, 98.0, 97.0, 98.9,
    98.3, 99.2, 98.6, 98.4, 98.8,
    98.1, 98.9, 98.3, 99.0, 98.6,
    98.5, 99.3, 98.7, 99.1, 98.2,
    0, 0
]
ganged_20[-2] = np.mean(ganged_20[:11])
ganged_20[-1] = np.mean(ganged_20[11:])
greenmem_20[-2] = np.mean(greenmem_20[:11])
greenmem_20[-1] = np.mean(greenmem_20[11:-2])

# === 画图 ===
x = np.arange(len(xtick_labels))
width = 0.3

fig, axs = plt.subplots(2, 1, figsize=(10, 6), dpi=150, sharex=False)

# === 图一：GreenMem vs half-rank vs Ideal ===
# print(len(x))
axs[0].bar(x - width, ideal, width=width, label="Ideal", edgecolor='black', color='#FFA07A')
axs[0].bar(x, half_rank, width=width, label="half-rank", edgecolor='black', color='#CD3C14')
axs[0].bar(x + width, greenmem_1, width=width, label="SCREME-framewk", edgecolor='black', color='#87CEFA')
texts = []
for i in [-2, -1]:
    texts.append(axs[0].text(x[i] + width, greenmem_1[i] + 1, f"{greenmem_1[i]:.2f}%", ha='center', va='bottom',
                fontsize=12, color='purple', fontweight='bold'))
    # texts.append(axs[0].text(x[i] + width, half_rank[i] + 1, f"{half_rank[i]:.2f}%", ha='center', va='bottom',
    #             fontsize=9, color='purple', fontweight='bold'))
    adjust_text(texts, ax=axs[0])

axs[0].set_ylabel("Norm. exec. time", fontsize=14, fontweight='bold')
axs[0].set_yticks(np.arange(0, 110, 20))
axs[0].set_yticklabels([f"{i}%" for i in range(0, 110, 20)])
axs[0].grid(axis='y', linestyle='--', alpha=0.6)
axs[0].legend(loc='lower left', ncol=3)
# axs[0].set_title("(a) Normalized Performance: Ideal vs Half-Rank vs SCREME", fontsize=15, fontweight='bold')

# === 图二：GreenMem vs Ganged vs Baseline ===
axs[1].bar(x - width, baseline_20, width=width, edgecolor='black', label="Baseline", color='#FFA07A')
axs[1].bar(x, ganged_20, width=width, label="ganged-channel", edgecolor='black', color='#CD3C14')
axs[1].bar(x + width, greenmem_20, width=width, edgecolor='black', label="SCREME-framewk", color='#87CEFA')

texts = []
for i in [-2, -1]:
    # texts.append(axs[1].text(x[i] + width, ganged_20[i] + 1, f"{ganged_20[i]:.2f}%", ha='center', va='bottom',
    #             fontsize=9, color='purple', fontweight='bold'))
    texts.append(axs[1].text(x[i] + width, greenmem_20[i] + 1, f"{greenmem_20[i]:.2f}%", ha='center', va='bottom',
                fontsize=12, color='purple', fontweight='bold'))
    adjust_text(texts, ax=axs[1], arrowprops=dict(arrowstyle="-", color='black', lw=0))
    # axs[1].text(x[i], ganged_20[i] + 1, f"{ganged_20[i]:.2f}%", ha='center', va='bottom',
    #             fontsize=11, color='purple', fontweight='bold')

axs[1].set_ylabel("Norm. exec. time", fontsize=14, fontweight='bold')
axs[1].set_yticks(np.arange(0, 110, 20))
axs[1].set_yticklabels([f"{i}%" for i in range(0, 110, 20)])
axs[1].set_xticks(x)
axs[1].set_xticklabels(xtick_labels, rotation=30, ha='right', fontsize=13)
axs[0].set_xticks(x)
axs[0].set_xticklabels(xtick_labels, rotation=30, ha='right', fontsize=13)
axs[1].grid(axis='y', linestyle='--', alpha=0.6)
axs[1].legend(loc='lower left', ncol=3)
# axs[1].set_title("(b) Normalized Performance: Baseline vs Ganged vs SCREME", fontsize=15, fontweight='bold')
# axs[0].text(0.0, 1.0, "(a)", transform=axs[0].transAxes,
#             fontsize=16, fontweight='bold', va='top', ha='left')
# axs[1].text(0.0, 1.0, "(b)", transform=axs[1].transAxes,
#             fontsize=16, fontweight='bold', va='top', ha='left')
plt.tight_layout()
plt.savefig("8_1_3 resil design.png")
plt.show()
