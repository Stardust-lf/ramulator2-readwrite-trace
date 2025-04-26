# Re-import after reset
from matplotlib import pyplot
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib import cm
from collections import defaultdict

# === First plot: DDR shipment share data
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.weight'] = 'bold'
plt.rcParams['font.size'] = 14
years = list(range(2015, 2026))
ddr_data = {
    '200-400 MHz':  [1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    '400-800 MHz': [5.0, 4.0, 3.0, 2.0, 1.0, 1.0, 1.0, 1.1, 1.0, 1.0, 1.0],
    '800-1600 MHz': [75.0, 45.0, 20.0, 15.0, 10.0, 8.0, 7.0, 5.3, 5.0, 4.0, 3.0],
    '1600-3200 MHz': [19.0, 50.0, 76.0, 82.0, 89.0, 91.0, 88.0, 77.9, 40.0, 30.0, 20.0],
    '3200- MHz': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.0, 15.8, 54.0, 65.0, 76.0],
}

df_ddr = pd.DataFrame(ddr_data, index=years)[['200-400 MHz', '400-800 MHz', '800-1600 MHz', '1600-3200 MHz', '3200- MHz']]
# colors_ddr = {
#     '400+ MHz DDR2': '#D8EC5D', '800+ MHz DDR3': '#9A9A9A',
#     '1600+ MHz DDR4': '#547DBF', '3200+ MHz DDR5': '#1A3E7A'
# }

colors_ddr = pyplot.get_cmap("viridis", 5).colors
# === Second plot: DRAM price data
data = [
    # === DDR4 ===
    ["DDR4-2133", 2016, 8.60], ["DDR4-2133", 2018, 7.60], ["DDR4-2133", 2020, 3.75],

    ["DDR4-2400", 2016, 6.25], ["DDR4-2400", 2018, 7.60], ["DDR4-2400", 2020, 3.06],  # 2021 is odd but kept? Removing:
    # ["DDR4-2400", 2021, 3.06],

    ["DDR4-2666", 2018, 8.50], ["DDR4-2666", 2020, 2.65],  # 2021 removed
    # ["DDR4-2666", 2021, 2.65],

    ["DDR4-2933", 2018, 8.00], ["DDR4-2933", 2020, 3.00],["DDR4-2933", 2022, 2.10],

    ["DDR4-3200", 2018, 12.00],["DDR4-3200", 2020, 8.50],["DDR4-3200", 2022, 4.60], ["DDR4-3200", 2024, 1.5],

    ["DDR4-3600", 2018, 12.00], ["DDR4-3600", 2020, 6.00], ["DDR4-3600", 2022, 4.50], ["DDR4-3600", 2024, 3.50],["DDR4-3600", 2026, 1.50],["DDR4-3600", 2028, 1.30],

    ["DDR4-4000", 2020, 11.25], ["DDR4-4000", 2022, 5.0], ["DDR4-4000", 2024, 4.0],["DDR4-4000", 2026, 3.0],["DDR4-4000", 2028, 2.0],

    # === DDR5 ===
    ["DDR5-4800", 2022, 4.44], ["DDR5-4800", 2024, 3.9],["DDR5-4800", 2026, 3.4],["DDR5-4800", 2028, 3.0],

    ["DDR5-5200", 2022, 11.00], ["DDR5-5200", 2024, 8.00], ["DDR5-5200", 2026, 6.00], ["DDR5-5200", 2028, 5.00],

    ["DDR5-5600", 2022, 13.90], ["DDR5-5600", 2024, 8.5], ["DDR5-5600", 2026, 7.5], ["DDR5-5600", 2028, 6.5],

    ["DDR5-6000", 2026, 10], ["DDR5-6000", 2028, 7.5],

    ["DDR5-6400", 2026, 12], ["DDR5-6400", 2028, 9],

    ["DDR5-6800", 2026, 15], ["DDR5-6800", 2028, 11],

    ["DDR5-7200", 2026, 17], ["DDR5-7200", 2028, 14],

    
]
df = pd.DataFrame(data, columns=["Frequency", "Year", "Price ($/GB)"])
group_map = {
    "DDR4-2133": "2014", "DDR4-2400": "2015", "DDR4-2666": "2017", "DDR4-2933": "2017",
    "DDR4-3200": "2018", "DDR4-3600": "2018", "DDR4-4000": "2019",
    "DDR5-4800": "2021", "DDR5-5200": "2021", "DDR5-5600": "2022",
    "DDR5-6000": "2025", "DDR5-6400": "2025",
    "DDR5-6800": "2026", "DDR5-7200": "2026",
    "DDR5-7600": "2028", "DDR5-8000": "2028"
}
df["ReleaseGroup"] = df["Frequency"].map(group_map)
df = df[df["Frequency"].str.extract(r"-(\d+)", expand=False).astype(float) >= 2400]
mean_df = df.groupby(["ReleaseGroup", "Year"])["Price ($/GB)"].mean().reset_index()

group_freqs = defaultdict(list)
for freq, group in group_map.items():
    group_freqs[group].append(freq)
def freq_key(f): return int(f.split("-")[1])
def strip_prefix(freq):
    return freq.split("-")[1]  # e.g., "DDR4-3200" → "3200"

group_labels = {
    group: "\n".join([strip_prefix(f) for f in sorted(freqs, key=freq_key)])
    for group, freqs in group_freqs.items()
}
mean_df["X Label"] = mean_df.apply(lambda row: f"{group_labels[row['ReleaseGroup']]}\n({row['ReleaseGroup']})", axis=1)

# === Plot side by side
fig, axes = plt.subplots(1, 2, figsize=(10, 4), dpi=100)

# Left subplot: DDR share
ax = axes[0]
xticks = list(df_ddr.index)
xticklabels = [str(y) if y < 2026 else "2026\n(forecast)" for y in xticks]
ax.set_xticks(xticks)
ax.set_xticklabels(xticklabels, rotation=30, fontsize=10)
ax.set_ylim([0,100])

bottom = np.zeros(len(df_ddr))
for i, col in enumerate(df_ddr.columns):
    ax.bar(df_ddr.index, df_ddr[col], label=col, bottom=bottom,edgecolor="black", color=colors_ddr[i])
    bottom += df_ddr[col]
# ax.set_title("DDR Shipment Share")
ax.set_ylabel('% of bits shipped', fontweight="bold")
ax.set_ylim(0, 100)
ax.grid(axis='y', linestyle='--', alpha=0.5)
ax.text(-0.05, 1.15, "(a)", transform=ax.transAxes,
     fontweight='bold', va='top', ha='left', fontsize=20)
ax.legend(loc='upper left', fontsize=10)

# Right subplot: DRAM price trend
ax = axes[1]
x_labels = mean_df["X Label"].unique()
years = sorted(mean_df["Year"].unique())
bar_width = 0.19
x = range(len(x_labels))
colors = pyplot.get_cmap("viridis", len(years)).colors
for i, year in enumerate(years):
    subset = mean_df[mean_df["Year"] == year]
    x_indices = [x_labels.tolist().index(label) + i * bar_width for label in subset["X Label"]]
    bar = ax.bar(x_indices, subset["Price ($/GB)"], width=bar_width, edgecolor="black", label=str(year), color=colors[i])
    if year > 2024:
        for rect in bar:
            rect.set_linestyle((0, (5, 5)))
mid_x = [i + (bar_width * (len(years) - 1)) / 2 for i in x]
# ax.set_title("DRAM Price by Released Frequency")
# 去掉括号部分，仅显示频率数字作为 xtick
xtick_freqs = [label.split("\n(")[0] for label in x_labels]
ax.set_xticks(mid_x)
ax.set_xticklabels(xtick_freqs, fontsize=10, fontweight="bold")

# 再人为在下方添加年份（用灰色斜体小字）

# for i, label in enumerate(x_labels):
#     raw_year = label.split("(")[-1].rstrip(")")
#     y_base = -2.6  # y 轴起始位置

#     # 显示年份
#     ax.text(mid_x[i], y_base, raw_year,
#             ha='center', va='top',
#             fontsize=9, fontstyle='italic', color='gray',
#             transform=ax.transData, clip_on=False)

#     # 若是 2026 或之后，加 forecast 作为下一行
#     if int(raw_year) >= 2026:
#         ax.text(mid_x[i], y_base - 0.8, "(forecast)",
#                 ha='center', va='top',
#                 fontsize=7, fontstyle='italic', color='gray',
#                 transform=ax.transData, clip_on=False)
ax.set_ylabel("Average price (USD/GB)", fontweight="bold")
ax.grid(True, linestyle='--', linewidth=0.8, axis='y')
ax.legend(fontsize=10, loc='upper left', ncol=2)

ax.text(-0.05, 1.15, "(b)", transform=ax.transAxes,
         fontweight='bold', va='top', ha='left', fontsize=20)

plt.tight_layout()
plt.savefig("2_2 pricepred.png")
plt.show()
