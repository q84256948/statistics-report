# coding=utf-8
__author__ = 'Jay'

import pandas as pd
#导入图表库以进行图表绘制
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.serif'] = ['SimHei']

plt.rcParams['axes.unicode_minus']=False #用控制中文乱码

loandata=pd.DataFrame(pd.read_excel('loan_data.xlsx'))

#创建直方图，数据源为贷款金额，将数据分为8等份显示，设置颜色和显示方式，透明度等
plt.hist(loandata['loan_amnt'],8,normed=1, histtype='stepfilled',facecolor='#99CC01', rwidth=0.9,alpha=0.6,edgecolor='white')
#添加x轴标题
plt.xlabel(u'贷款金额')
#添加y轴标题
plt.ylabel(u'概率')
#添加图表标题
plt.title(u'贷款金额概率密度')
#设置背景网格线的颜色，样式，尺寸和透明度
plt.grid(color='#95a5a6',linestyle='--', linewidth=1,axis='y',alpha=0.4)
#显示图表
plt.show()

