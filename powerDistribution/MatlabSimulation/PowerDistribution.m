A=[];
for i=0:8
    num=nchoosek(8,i)*100;%��������Ϊi�����ĸ���
    A=[A,normrnd(159.6-5.5*i,1.63,[1,num])];%��Ӧ��������Ϊi����������ķֲ�Ϊ
end
histogram(A,100)