# coding=utf-8
# LOCALTION = [3, 4, 5, 6, 7, 8]
__author__ = 'Jay'

import numpy as np
import pandas as pd

# 导入图表库以进行图表绘制
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.serif'] = ['SimHei']

plt.rcParams['axes.unicode_minus'] = False  # 用控制中文乱码

loandata = pd.DataFrame(pd.read_excel('loan_data.xlsx'))

# 按用户等级grade字段对贷款金额进行求和汇总
loan_grade = loandata.groupby('grade')['loan_amnt'].agg(sum)
# 定义数据分类名称
LOCALTIONS = [u'A级', u'B级', u'C级', u'D级', u'E级', u'F级']
# 创建一个一维数组赋值给LOCALTION
LOCALTION = np.arange(len(LOCALTIONS))
# 设置饼图中每个数据分类的颜色
colors = ["#99CC01", "#FFFF01", "#0000FE", "#FE0000", "#A6A6A6", "#D9E021"]
# a=np.array(LOCALTION)
# 创建柱状图，数据源为按用户等级汇总的贷款金额，设置颜色，透明度和外边框颜色
plt.barh(LOCALTION, loan_grade, color=colors, alpha=0.8, align='center', edgecolor='white')
# 设置x轴标签
plt.ylabel(u'用户等级')
# 设置y周标签
plt.xlabel(u'贷款金额')
# 设置图表标题
plt.title(u'不同用户等级的贷款金额分布')
# 设置图例的文字和在图表中的位置
plt.legend([u'贷款金额'], loc='upper right')
# 设置背景网格线的颜色，样式，尺寸和透明度
plt.grid(color='#95a5a6', linestyle='--', linewidth=1, axis='y', alpha=0.4)
# 设置数据分类名称
plt.yticks(LOCALTION + 0.4, LOCALTIONS)
# 显示图表
plt.show()
