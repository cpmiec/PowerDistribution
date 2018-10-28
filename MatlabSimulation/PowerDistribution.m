A=[];
for i=0:8
    num=nchoosek(8,i)*100;%汉明重量为i的数的个数
    A=[A,normrnd(159.6-5.5*i,1.63,[1,num])];%对应汉明重量为i的随机变量的分布为
end
histogram(A,100)