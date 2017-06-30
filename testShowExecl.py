# coding=utf-8
__author__ = 'Jay'

import numpy as np
import pandas as pd
#导入图表库以进行图表绘制
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.serif'] = ['SimHei']

plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

loandata=pd.DataFrame(pd.read_excel('loan_data.xlsx'))

loandata.set_index('issue_d')
#按月对贷款金额loan_amnt求均值
loan_plot=loandata['loan_amnt']

#创建一个一维数组赋值给a
a=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
#创建折线图，数据源为按月贷款均值，标记点，标记线样式，线条宽度，标记点颜色和透明度
plt.plot(loan_plot,'g^',loan_plot,'g-',color='#99CC01',linewidth=3,markeredgewidth=3,markeredgecolor='#99CC01',alpha=0.8)
#添加x轴标签
plt.xlabel(u'月份')
#添加y周标签
plt.ylabel(u'贷款金额')
#添加图表标题
plt.title(u'分月贷款金额分布')
#添加图表网格线，设置网格线颜色，线形，宽度和透明度
plt.grid( color='#95a5a6',linestyle='--', linewidth=1 ,axis='y',alpha=0.4)
#设置数据分类名称
plt.xticks(a, (u'1月',u'2月',u'3月',u'4月',u'5月',u'6月',u'7月',u'8月',u'9月',u'10月',u'11月',u'12月') )
#输出图表
plt.show()

