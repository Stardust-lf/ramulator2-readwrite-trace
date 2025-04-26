import matplotlib.pyplot as plt

# 设置字体
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.weight'] = 'bold'
plt.rcParams['font.size'] = 15

# 创建一个空白图
fig, ax = plt.subplots(figsize=(10,10))

# 在图中央写字
ax.text(0.5, 0.5, "SCREME-WO SPEC, SCREME-WO GAP, SCREME-framewk SPEC,SCREME-framewk GAP", ha='center', va='center', transform=ax.transAxes)
ax.text(0.5, 0.2, "0.96,1.25,1.01,2.08,2.41", ha='center', va='center', transform=ax.transAxes)

# 去掉坐标轴
ax.axis('off')

# 显示
plt.show()
