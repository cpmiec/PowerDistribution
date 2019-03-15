#_*_ coding:utf-8 _*_
#不同汉明重量的数据所造成的能耗
#different power consumption correlated with different data.
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties  # 

import os
import time
import math
from openpyxl import Workbook#用来编辑Excel
from sklearn.decomposition import PCA#添加包含PCA的库

xyAxisFont = FontProperties(fname=r"./simsun.ttc", size=12)  # 步骤二

#测试模块
# fileOpen=fileOper()
# traceFile,textinFile=fileOpen.getFileName()
trace=np.load(r'./Hammingweight_data/traces/2018.08.04-20.45.09_traces.npy')#加载功耗痕迹
noptrace=np.load(r'./Nooperation_data/traces/2018.08.04-20.05.07_traces.npy')

[traceRow,traceCol]=np.shape(trace)
averTrace=(np.sum(trace,axis=0)-np.sum(noptrace,axis=0))/traceRow
#averTrace=np.sum(trace,axis=0)/traceRow
fig1=plt.figure(1,figsize=(4.8,3))
ax1=fig1.add_axes([0.16,0.16,0.75,0.8])
ax1.plot(averTrace,linewidth=0.5)
plt.xlabel("采样点",fontproperties=xyAxisFont)
plt.ylabel("能耗",fontproperties=xyAxisFont)
plt.savefig(r'./powerAndHW.svg')
plt.show()


