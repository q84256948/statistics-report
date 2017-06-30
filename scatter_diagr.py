# coding=utf-8
__author__ = 'Jay'


import pandas as pd
#导入图表库以进行图表绘制
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.serif'] = ['SimHei']

plt.rcParams['axes.unicode_minus']=False #用控制中文乱码

loandata=pd.DataFrame(pd.read_excel('loan_data.xlsx'))

#按月汇总贷款金额，以0填充空值
loan_x=loandata['loan_amnt']
#按月汇总利息金额，以0填充空值
loan_y=loandata['total_rec_int']

#创建散点图，贷款金额为x，利息金额为y，设置颜色，标记点样式和透明度等
plt.scatter(loan_x,loan_y,60,color='white',marker='*',edgecolors='#0D8ECF',linewidth=3,alpha=0.8)
#添加x轴标题
plt.xlabel(u'贷款金额')
#添加y轴标题
plt.ylabel(u'利息收入')
#添加图表标题
plt.title(u'贷款金额与利息收入')
#设置背景网格线的颜色，样式，尺寸和透明度
plt.grid(color='#95a5a6',linestyle='--', linewidth=1,axis='both',alpha=0.4)
#显示图表
plt.show()

