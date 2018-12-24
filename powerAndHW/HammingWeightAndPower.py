#_*_ coding:utf-8 _*_
#不同汉明重量的数据所造成的能耗
#different power consumption correlated with different data.
import numpy as np
import matplotlib.pyplot as plt
import os
import time
import math
from openpyxl import Workbook#用来编辑Excel
from sklearn.decomposition import PCA#添加包含PCA的库

titlefont={'family': 'Times New Roman',#设置字体格式
           'color':  'black',
           'weight': 'normal',
           'size': 12,
        }
xylabelfont={'family': 'Times New Roman',
             'color': 'black',
             'weight': 'normal',
             'size': 12
        }
labelfont={'family': 'Times New Roman',
           'size': 12
        }

#测试模块
# fileOpen=fileOper()
# traceFile,textinFile=fileOpen.getFileName()
trace=np.load(r'./Hammingweight_data/traces/2018.08.04-20.45.09_traces.npy')#加载功耗痕迹
aaa=np.load(r'./Nooperation_data/traces/2018.08.04-20.05.07_traces.npy')

[traceRow,traceCol]=np.shape(trace)
averTrace=(np.sum(trace,axis=0)-np.sum(aaa,axis=0))/traceRow
#averTrace=np.sum(trace,axis=0)/traceRow
fig1=plt.figure(1,figsize=(4.5,3))
ax1=fig1.add_axes([0.12,0.15,0.8,0.75])
ax1.plot(averTrace,linewidth=0.5)
plt.xlabel("Sampling point",fontdict=xylabelfont)
plt.ylabel("Power consumption",fontdict=xylabelfont)
plt.savefig(r'./powerAndHW')
plt.show()


