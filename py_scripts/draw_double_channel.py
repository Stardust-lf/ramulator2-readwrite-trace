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
    "tc road", "tc twitter", "SPEC_avg", "GAP_avg"
]

baseline_20 = [100.0] * 20
ganged_20 = [
    72.0, 59.0, 70.0, 58.0, 74.0,
    76.0, 68.0, 60.0, 67.0, 62.0,
    48.0, 47.0, 48.0, 49.0, 49.0,
    49.0, 48.0, 50.0, 51.0, 52.0
]
greenmem_20 = [
    98.5, 98.7, 98.0, 97.0, 98.9,
    98.3, 99.2, 98.6, 98.4, 98.8,
    98.1, 98.9, 98.3, 99.0, 98.6,
    98.5, 99.3, 98.7, 99.1, 98.2
]
def extend_with_avg(values):
    return values[:20] + [np.mean(values[:10]), np.mean(values[10:20])]

baseline = extend_with_avg(baseline_20)
ganged = extend_with_avg(ganged_20)
greenmem = extend_with_avg(greenmem_20)

x = np.arange(len(xtick_labels))
width = 0.3

plt.figure(figsize=(10, 5), dpi=200)
plt.bar(x - width, baseline, width=width, label="Baseline", color='#FFA07A')
plt.bar(x, ganged, width=width, label="ganged channel", color='#CD3C14')
plt.bar(x + width, greenmem, width=width, label="SCREME-framework", color='#87CEFA')

for i in [-2, -1]:  # SPEC_avg 和 GAP_avg
    height = ganged[i]
    plt.text(x[i], height + 1, f"{height:.2f}%", ha='center', va='bottom',
             fontsize=11, color='green', fontweight='bold')

plt.xticks(x, xtick_labels, rotation=30, ha='right', fontsize=13)
plt.yticks(np.arange(0, 110, 20), [f"{i}%" for i in range(0, 110, 20)])
plt.ylabel("Performance(%)", fontsize=14, fontweight='bold')
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.legend(loc='lower left', fontsize=12,)
plt.tight_layout()
plt.savefig("double_channel.png")
plt.show()
