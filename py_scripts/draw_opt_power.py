import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.weight'] = 'bold'
plt.rcParams['font.size'] = 14


xtick_labels = [
    "gcc", "mcf", "omnetpp", "bwaves", "cactuBSSN", "parest", "lbm", "wrf", "fotonik3d", "roms",
    "bc road", "bc twitter", "bfs road", "bfs twitter", "cc road", "cc twitter",
    "pr road", "pr twitter", "tc road", "tc twitter", "SPEC_avg", "GAP_avg"
]

baseline_a = [13.8, 11.2, 9.4, 10.2, 8.4, 8.8, 8.8, 9.0, 9.6, 10.8,
              13.8, 14.6, 12.2, 12.6, 10.8, 11.2, 10.2, 10.8, 11.2, 11.5, 0, 0]
greenmem_a = [12.6, 9.8, 8.2, 8.6, 8.0, 8.6, 8.6, 8.4, 8.8, 9.4,
              12.6, 13.6, 11.2, 11.2, 9.4, 10.0, 9.2, 9.8, 10.0, 10.4, 0, 0]

baseline_b = [26, 21, 18, 19, 15, 17, 17, 18, 20, 21,
              25, 26, 22, 23, 21, 23, 21, 22, 23, 22, 0, 0]
greenmem_b = [14, 12, 10, 9, 8, 9, 9, 10, 11, 12,
              14, 15, 13, 13, 12, 13, 11, 12, 13, 13, 0, 0]

baseline_a[20] = np.mean(baseline_a[:10])
greenmem_a[20] = np.mean(greenmem_a[:10])
baseline_a[21] = np.mean(baseline_a[10:20])
greenmem_a[21] = np.mean(greenmem_a[10:20])

baseline_b[20] = np.mean(baseline_b[:10])
greenmem_b[20] = np.mean(greenmem_b[:10])
baseline_b[21] = np.mean(baseline_b[10:20])
greenmem_b[21] = np.mean(greenmem_b[10:20])

x = np.arange(len(xtick_labels))
width = 0.35

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10), sharex=True, dpi=150)

ax1.bar(x - width/2, baseline_a, width, label='Baseline', color='#FFA07A')
ax1.bar(x + width/2, greenmem_a, width, label='SCREME-Recyc', color='#87CEFA')
ax1.set_ylabel('Operational Power (W)', fontweight="bold")
# ax1.set_title('(a)')
ax1.legend(loc="upper left")
ax1.grid(axis='y', linestyle='--', alpha=0.6)

for i in [20, 21]:
    ax1.text(i - width/2, baseline_a[i] + 0.3, f'{baseline_a[i]:.1f}', ha='center', color="green", va='bottom', fontsize=11, fontweight='bold')
    ax1.text(i + width/2, greenmem_a[i] + 0.3, f'{greenmem_a[i]:.1f}', ha='center', color="green", va='bottom', fontsize=11, fontweight='bold')

ax2.bar(x - width/2, baseline_b, width, label='Baseline', color='#FFA07A')
ax2.bar(x + width/2, greenmem_b, width, label='SCREME-Framewk', color='#87CEFA')
ax2.set_ylabel('Operational Power (W)', fontweight="bold")
# ax2.set_title('(b)')
ax2.legend()
ax2.grid(axis='y', linestyle='--', alpha=0.6)
ax2.set_xticks(x)
ax2.set_xticklabels(xtick_labels, rotation=30, ha='right')

for i in [20, 21]:
    ax2.text(i - width/2, baseline_b[i] + 0.6, f'{baseline_b[i]:.1f}', ha='center', color = "green", va='bottom', fontsize=11, fontweight='bold')
    ax2.text(i + width/2, greenmem_b[i] + 0.6, f'{greenmem_b[i]:.1f}', ha='center', color = "green", va='bottom', fontsize=11, fontweight='bold')

ax1.text(-0.05, 1.05, "(a)", transform=ax1.transAxes,
     fontsize=16, fontweight='bold', va='top', ha='left')

ax2.text(-0.05, 1.05, "(b)", transform=ax2.transAxes,
         fontsize=16, fontweight='bold', va='top', ha='left')

plt.tight_layout()
plt.savefig("8_2_1 opt power")
plt.show()
