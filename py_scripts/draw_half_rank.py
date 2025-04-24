import matplotlib.pyplot as plt
import numpy as np

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

ideal = [100.0] * 22
half_rank = [
    67.0, 67.0, 67.0, 67.0, 67.0,
    66.0, 60.0, 58.0, 67.0, 61.0,
    52.0, 60.0, 66.0, 67.0, 68.0,
    63.0, 65.0, 61.0, 66.0, 64.0,
    0, 0
]
greenmem = [
    92.0, 93.0, 93.0, 93.0, 93.0,
    95.0, 96.0, 97.0, 95.0, 96.0,
    88.0, 91.0, 92.0, 91.0, 90.0,
    87.0, 89.0, 91.0, 90.0, 91.0,
    0, 0
]

half_rank[-2] = np.mean(half_rank[:11])
half_rank[-1] = np.mean(half_rank[11:])
greenmem[-2] = np.mean(greenmem[:11])
greenmem[-1] = np.mean(greenmem[11:])

x = np.arange(len(xtick_labels))
width = 0.3

plt.figure(figsize=(10, 5), dpi=200)
plt.bar(x - width, ideal, width=width, label="Ideal", color='#FFA07A')
plt.bar(x, half_rank, width=width, label="half-rank", color='#CD3C14')
plt.bar(x + width, greenmem, width=width, label="SCREME-framework", color='#87CEFA')

for i in [-2, -1]:
    height = greenmem[i]
    plt.text(x[i] + width, height + 1, f"{height:.2f}%", ha='center', va='bottom',
             fontsize=11, color='green', fontweight='bold')
for i in [-2, -1]:
    height = half_rank[i]
    plt.text(x[i] + width, height + 1, f"{height:.2f}%", ha='center', va='bottom',
             fontsize=11, color='green', fontweight='bold')

plt.xticks(x, xtick_labels, rotation=30, ha='right', fontsize=13)
plt.yticks(np.arange(0, 110, 20), [f"{i}%" for i in range(0, 110, 20)])
plt.ylabel("Performance(%)", fontsize=14, fontweight='bold')
# plt.title("GreenMem Normalized Value Comparison (22 Benchmarks)", fontsize=14, fontweight='bold')
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.legend(loc='lower left', fontsize=12) 
plt.tight_layout()
plt.savefig("resilient_memory.png")
plt.show()
