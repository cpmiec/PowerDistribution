#_*_ coding:utf-8 _*_
#用来显示在处理随机数据时的能耗分布
import numpy as np
import matplotlib.pyplot as plt
import os
import time
import math
import seaborn as sns#用来画出直方图
from openpyxl import Workbook#用来编辑Excel
from sklearn.decomposition import PCA#添加包含PCA的库
from sklearn.neighbors import KernelDensity

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
realKey=[0x65,0xB1]#真实的轮密钥
startTime=time.clock()
class fileOper:
    '''获得当前目录下的功耗痕迹文件和明文文件名，并返回'''
    def getFileName(self):
        '''获得当前目录下功耗痕迹文件名和明文文件名，返回值：traceFile,textinFile'''
        curDir=os.getcwd()
        dataDir=[dir for dir in os.listdir(curDir) if os.path.isdir(dir) if dir.endswith('data')]

        if np.size(dataDir)!=1:
            print('请在当前目录存放一个数据文件')
            exit(1)
        else:
            dataDir=curDir+'\\'+dataDir[0]+'\\'+'traces'

            fileNameTemple=[filename for filename in os.listdir(dataDir) if filename.endswith ('traces.npy')]
            traceFile=dataDir+'\\'+fileNameTemple[0]

            fileNameTemple=[filename for filename in os.listdir(dataDir) if filename.endswith ('textin.npy')]
            textinFile=dataDir+'\\'+fileNameTemple[0]
            return traceFile,textinFile
    
class CPA:
    '''读取能耗和明文数据，并进行CPA攻击'''
    def __init__(self,traceIn,plaintextIn,):
        self.trace=traceIn#功耗
        self.plaintext=plaintextIn#明文
        self.traceNum=np.shape(self.trace)[0]#行数
        self.pointNum=np.shape(self.trace)[1]#列数

        self.HW = [bin(n).count("1") for n in range(0, 256)]  # 产生计算‘1’个数的查询表
        # self.hypPower=np.zeros((self.traceNum,1),dtype='int8')#针对第subKey个子密钥而生成的猜测能耗

    def calcCorrcoef(self,x, y=None, rowvar=True):
        '''计算相关系数'''
        c = np.cov(x, y,rowvar)
        try:
            d = np.diag(c)
        except ValueError:
            # scalar covariance
            # nan if incorrect value (nan, inf, 0), 1 otherwise
            return c / c
        stddev = np.sqrt(d)
    
        if (0 in stddev):
            c=np.array([[0,0],[0,0]])
        else:
            c /= stddev[:, None]
            c /= stddev[None, :]
        return c

        #绘制出加密一条明文所产生的能耗
    
    def plotTrace(self):
        '''绘制出加密一条明文所产生的能耗'''
        fig1=plt.figure(1,figsize=(4.5,3))
        ax1=fig1.add_axes([0.12,0.15,0.8,0.75])
        ax1.plot(self.trace[0,:]+0.5,linewidth=0.5)
        plt.xlabel("Sampling point",fontdict=xylabelfont)
        plt.ylabel("Power consumption",fontdict=xylabelfont)
        plt.xlim(0,self.pointNum)
        ax1.tick_params(labelsize=9)
        filename='UNPROTECTEDPowerConsumption.pdf'
        plt.savefig(filename)

    #进行CPA攻击
    def distribution(self):#攻击停止字节（因为攻击16个字节的密钥太耗费时间），和所用明文组数，funsel选择功能 0只进行攻击，1相关系数随采样点之间的关系，2相关性随明文组数之间的关系
        correlationTemp=np.zeros((self.pointNum))#用于存储keyGuess和能耗矩阵中每一列的相关系数
        hypPower=[self.HW[int(i)] for i in self.plaintext]
        for pointIndex in range(self.pointNum):
            correlationTemp[pointIndex]=np.absolute(self.calcCorrcoef(self.trace[0:int(self.traceNum),pointIndex],hypPower[0:int(self.traceNum)])[0][1])

        self.loc=np.argmax(correlationTemp)

        # self.aa=self.trace[:,self.loc]
        self.aa=self.trace[:,30]
        print(self.loc)
        delt=np.std(self.aa,ddof=1)
        aver=np.average(self.aa)
        
        plt.hist(self.aa,bins=100)
        plt.figure()
        sns.distplot(self.aa, rug=True, hist=True)
        plt.show()


#测试模块
fileOpen=fileOper()
traceFile,textinFile=fileOpen.getFileName()
trace=np.load(traceFile)#加载功耗痕迹
plaintext=np.load(textinFile)#加载明文

cpa=CPA(trace,plaintext)
cpa.distribution()

endTime=time.clock()
print('Runtime is %f seconds' %(endTime-startTime))
plt.show()
