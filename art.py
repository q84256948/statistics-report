# coding=utf-8
__author__ = 'Jay'

import pandas as pd
# 导入图表库以进行图表绘制
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.serif'] = ['SimHei']

plt.rcParams['axes.unicode_minus'] = False  # 用控制中文乱码

loandata = pd.DataFrame(pd.read_excel('loan_data.xlsx'))

# 按用户等级grade字段对贷款金额进行求和汇总
loan_grade = loandata.groupby('grade')['loan_amnt'].agg(sum)

# 设置饼图中每个数据分类的颜色
colors = ["#99CC01", "#FFFF01", "#0000FE", "#FE0000", "#A6A6A6", "#D9E021"]
# 设置饼图中每个数据分类的名称
name = [u'A级', u'B级', u'C级', u'D级', u'E级', u'F级']
# 创建饼图，设置分类标签，颜色和图表起始位置等，
# labels  (每一块)饼图外侧显示的说明文字
# loan_grade       (每一块)的比例，如果sum(x) > 1会使用sum(x)归一化
#  explode (每一块)离开中心距离
plt.pie(loan_grade, labels=name, colors=colors, explode=(0, 0, 0.1, 0, 0.1, 0), startangle=60, autopct='%1.1f%%')
# 添加图表标题
plt.title(u'不同用户等级的贷款金额占比')
# 添加图例，并设置显示位置
plt.legend(name, loc='upper left')
# 显示图表
plt.show()
