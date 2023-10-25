from statistics import mean

import matplotlib.pyplot as plt

p = [0.625, 0.666666667, 0.5, 0.8, 0.466666667, 0.636363636, 0.4375, 0.888888889, 0.666666667, 0.625, 0.5, 0.777777778]
r = [0.555555556, 0.888888889, 0.714285714,0.8, 0.875, 0.777777778, 1, 0.627272727, 0.75, 0.625, 0.7, 0.777777778]
f1 = [0.588235294, 0.761904762, 0.588235294, 0.8, 0.608695652, 0.7, 0.8, 0.608695652,  0.705882353,
      0.625, 0.545454545, 0.777777778]
p2 = [0.636363636,
0.8,
0.571428571,
0.588235294,
0.7,
0.727272727,
0.615384615,
0.75,
0.666666667,
0.7,
0.538461538,
0.727272727
]
r2 =[
0.777777778,
0.888888889,
0.571428571,
    1,
0.875,
0.888888889,
1,
0.818181818,
0.75,
0.875,
0.7,
0.888888889
]
f12 = [
0.7,
0.842105263,
0.571428571,
0.740740741,
0.777777778,
0.8,
0.761904762,

0.782608696,
0.705882353,
0.823529412,
0.608695652,
0.8

]
data = [p, r, f1]
data2 = [p2, r2, f12]
# 创建箱型图对象
fig, ax = plt.subplots()

# 绘制两组数据的箱型图
boxplot1 = ax.boxplot(data, positions=[1, 2, 3], labels=['percision', 'recall', 'f1-score'], widths=0.4, patch_artist=True, boxprops=dict(facecolor='white', edgecolor='black'),
                      medianprops=dict(color='black'))
boxplot2 = ax.boxplot(data2, positions=[5, 6, 7], labels=['percision', 'recall', 'f1-score'], widths=0.4, patch_artist=True, boxprops=dict(facecolor='yellow', edgecolor='black'),
                      medianprops=dict(color='black'))

# 设置标题和标签
ax.set_xlabel('Metrics')
ax.set_ylabel('Values')

# 设置 y 轴范围从 0 开始
ax.set_ylim(0)
# 添加图例
legend = ax.legend([boxplot1["boxes"][0], boxplot2["boxes"][0]], ['Extraction 1st', 'Extraction 2nd'])
print(mean(p), mean(r), mean(f1))
print(mean(p2), mean(r2), mean(f12))
# 显示图像
plt.show()
