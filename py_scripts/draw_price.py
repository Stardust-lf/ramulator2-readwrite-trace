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
years = list(range(2015, 2027))
ddr_data = {
    'DDR':   [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'DDR2':  [75, 50, 25, 10, 5, 2, 1, 1, 1, 1, 1, 1],
    'DDR3':  [24, 45, 60, 75, 80, 80, 75, 60, 40, 20, 10, 5],
    'DDR4':  [0, 4, 15, 15, 15, 18, 20, 35, 45, 50, 55, 50],
    'DDR5':  [0, 0, 0, 0, 0, 0, 4, 10, 14, 29, 34, 44],
}
df_ddr = pd.DataFrame(ddr_data, index=years)[['DDR', 'DDR2', 'DDR3', 'DDR4', 'DDR5']]
colors_ddr = {
    'DDR': '#F7981D', 'DDR2': '#D8EC5D', 'DDR3': '#9A9A9A',
    'DDR4': '#547DBF', 'DDR5': '#1A3E7A'
}

# === Second plot: DRAM price data
data = [
    ["DDR4-2133", 2015, 6.25], ["DDR4-2133", 2016, 8.60], ["DDR4-2133", 2017, 11.70], ["DDR4-2133", 2018, 7.60], ["DDR4-2133", 2020, 3.75],
    ["DDR4-2400", 2016, 6.25], ["DDR4-2400", 2017, 10.00], ["DDR4-2400", 2018, 7.60], ["DDR4-2400", 2021, 3.06],
    ["DDR4-2666", 2017, 10.00], ["DDR4-2666", 2018, 8.50], ["DDR4-2666", 2019, 3.75], ["DDR4-2666", 2021, 2.65],
    ["DDR4-2933", 2018, 8.00], ["DDR4-2933", 2019, 6.50], ["DDR4-2933", 2020, 3.00],
    ["DDR4-3200", 2018, 12.00], ["DDR4-3200", 2019, 6.00], ["DDR4-3200", 2021, 3.30], ["DDR4-3200", 2023, 1.2], ["DDR4-3200", 2024, 1.5], ["DDR4-3200", 2025, 1.60],
    ["DDR4-3600", 2018, 12.00], ["DDR4-3600", 2020, 6.00], ["DDR4-3600", 2022, 4.50], ["DDR4-3600", 2025, 1.50],
    ["DDR4-4000", 2019, 18.00], ["DDR4-4000", 2020, 11.25], ["DDR4-4000", 2021, 7.50], ["DDR4-4000", 2022, 5.0], ["DDR4-4000", 2023, 2.5], ["DDR4-4000", 2024, 1.8], ["DDR4-4000", 2025, 2.00],
    ["DDR5-4800", 2021, 18.75], ["DDR5-4800", 2022, 4.44], ["DDR5-4800", 2023, 2.00], ["DDR5-4800", 2024, 1.9], ["DDR5-4800", 2025, 2.50],
    ["DDR5-5200", 2022, 11.00], ["DDR5-5200", 2023, 6.25], ["DDR5-5200", 2025, 1.56],
    ["DDR5-5600", 2022, 10.90], ["DDR5-5600", 2023, 6.25], ["DDR5-5600", 2024, 2.2], ["DDR5-5600", 2025, 1.88],
    # ["DDR5-6000", 2025, 2.42], ["DDR5-6400", 2025, 2.81],
]
df = pd.DataFrame(data, columns=["Frequency", "Year", "Price ($/GB)"])
group_map = {
    "DDR4-2133": "2014", "DDR4-2400": "2015", "DDR4-2666": "2017", "DDR4-2933": "2017",
    "DDR4-3200": "2018", "DDR4-3600": "2018", "DDR4-4000": "2019",
    "DDR5-4800": "2021", "DDR5-5200": "2021", "DDR5-5600": "2022",
    "DDR5-6000": "2025", "DDR5-6400": "2025"
}
df["ReleaseGroup"] = df["Frequency"].map(group_map)
df = df[df["Frequency"].str.extract(r"-(\d+)", expand=False).astype(float) >= 2400]
mean_df = df.groupby(["ReleaseGroup", "Year"])["Price ($/GB)"].mean().reset_index()

group_freqs = defaultdict(list)
for freq, group in group_map.items():
    group_freqs[group].append(freq)
def freq_key(f): return int(f.split("-")[1])
group_labels = {group: "\n".join(sorted(freqs, key=freq_key)) for group, freqs in group_freqs.items()}
mean_df["X Label"] = mean_df.apply(lambda row: f"{group_labels[row['ReleaseGroup']]}\n({row['ReleaseGroup']})", axis=1)

# === Plot side by side
fig, axes = plt.subplots(1, 2, figsize=(14, 6), dpi=100)

# Left subplot: DDR share
ax = axes[0]
xticks = list(df_ddr.index)
xticklabels = [str(y) if y < 2026 else "2026\n(forecast)" for y in xticks]
ax.set_xticks(xticks)
ax.set_xticklabels(xticklabels, rotation=30, fontsize=11)

bottom = np.zeros(len(df_ddr))
for col in df_ddr.columns:
    ax.bar(df_ddr.index, df_ddr[col], label=col, bottom=bottom, color=colors_ddr[col])
    bottom += df_ddr[col]
# ax.set_title("DDR Shipment Share")
ax.set_ylabel('% of bits shipped', fontweight="bold")
ax.set_ylim(0, 100)
ax.grid(axis='y', linestyle='--', alpha=0.5)
ax.text(-0.05, 1.05, "(a)", transform=ax.transAxes,
     fontweight='bold', va='top', ha='left')
ax.legend(title='DDR Gen.', loc='upper left', fontsize=12)

# Right subplot: DRAM price trend
ax = axes[1]
x_labels = mean_df["X Label"].unique()
years = sorted(mean_df["Year"].unique())
bar_width = 0.12
x = range(len(x_labels))
colors = pyplot.get_cmap("Paired", len(years)).colors
for i, year in enumerate(years):
    subset = mean_df[mean_df["Year"] == year]
    x_indices = [x_labels.tolist().index(label) + i * bar_width for label in subset["X Label"]]
    ax.bar(x_indices, subset["Price ($/GB)"], width=bar_width, label=str(year), color=colors[i])
mid_x = [i + (bar_width * (len(years) - 1)) / 2 for i in x]
# ax.set_title("DRAM Price by Released Frequency")
ax.set_xticks(mid_x)
ax.set_xticklabels(x_labels, rotation=30, fontsize=11)
ax.set_ylabel("Average Price (USD/GB)", fontweight="bold")
ax.grid(True, linestyle='--', linewidth=0.8, axis='y')
ax.legend(title="Year", fontsize=12, loc='upper left', ncol=2)

ax.text(-0.05, 1.05, "(b)", transform=ax.transAxes,
         fontweight='bold', va='top', ha='left')

plt.tight_layout()
plt.savefig("2_2 pricepred.png")
plt.show()
