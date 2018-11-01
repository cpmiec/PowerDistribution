# Power Distribution

这个工程模拟了《能量分析攻击》一书中p53中的图4.4，实验平台为ChipWhisperer 1173开发板，其中包括有以下几个部分：

1. 纯数学仿真，能耗的均值方差均用书上p53数据（MatlabSimulation文件夹中）。![histogram](https://github.com/cpmiec/PowerDistribution/blob/master/MatlabSimulation/histogram.png)

2. 从电脑端接收一个16字节的数组，并且将数组的第一个字节赋值给一个变量，在赋值过程中收集能耗信息（XMEGAPowerDistributionCapturer）。

3. 将上述采集到的能耗信息进行分析，首先采用类似CPA攻击的方式，分析在哪个采样点和进行该赋值操作有关，之后对所有能耗信息的该采样点进行直方图统计，该数据为上一步从CW开发板处采集。![histogram](https://github.com/cpmiec/PowerDistribution/blob/master/XMEGAPowerDistributionAnalyzer/histogram.png)

