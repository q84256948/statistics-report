# coding=utf-8
__author__ = 'Jay'

import pandas as pd
# 导入图表库以进行图表绘制
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.serif'] = ['SimHei']

plt.rcParams['axes.unicode_minus'] = False  # 用控制中文乱码
loandata = pd.DataFrame(pd.read_excel('loan_data.xlsx'))

# 创建箱线图，数据源为贷款来源，设置横向显示
plt.boxplot(loandata['loan_amnt'], 1, 'rs', vert=False)
# 添加x轴标题
plt.xlabel(u'贷款金额')
# 添加图表标题
plt.title(u'贷款金额分布')
# 设置背景网格线的颜色，样式，尺寸和透明度
plt.grid(color='#95a5a6', linestyle='--', linewidth=1, axis='both', alpha=0.4)
# 显示图表
plt.show()
