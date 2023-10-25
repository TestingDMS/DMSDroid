import matplotlib.pyplot as plt

# 两组示例数据
data1 = [25, 28, 30, 35, 40, 42, 45, 50, 55, 60, 70]
data2 = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 75]
data3 = [22, 26, 28, 32, 38, 42, 48, 52, 58, 62, 72]
data4 = [23, 24, 27, 31, 37, 41, 47, 53, 59, 63, 71]

# 创建箱型图对象
fig, ax = plt.subplots()

# 绘制两组数据的箱型图
boxplot1 = ax.boxplot([data1, data2], positions=[1, 2], labels=['D1', 'D2'], widths=0.3)
boxplot2 = ax.boxplot([data3, data4], positions=[4, 5], labels=['D1', 'D2'], widths=0.3)

# 调整两个组之间的间距
ax.set_xlim(0, 6)
ax.set_xticks([1.5, 4.5])

# 设置标题和标签
ax.set_title('Combined Box Plots')
ax.set_xlabel('Data Groups')
ax.set_ylabel('Values')

# 设置 y 轴范围从 0 开始
ax.set_ylim(0)

# 显示图像
plt.show()
