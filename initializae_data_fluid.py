# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 10:48:19 2017

@author: ivan
"""
####
import numpy as np
######
nelt=70;
nnt=nelt+1;
nnel=2;
ndln=3;
ndle=ndln*nnel;
ndlt=nnt*ndln;
###########################
L_0=1;
A=1;
############################
U0=0.2;
L_t=L_0+U0;
###################################
#x为行向量
x=np.linspace(0,L_t,nnt)
#print(x)
#y=x.size
#print(y)

# ###
vcor=x.T
#print(vcor)
vcor0=vcor
vcor_n=vcor
vcor_np1=vcor
###################################
#the conncetivity table
conec=np.ones((nnt-1,2))
conec1=np.linspace(1,nnt-1,nnt-1)
#print(conec1)
conec2=np.linspace(2,nnt,nnt-1)
#print(conec2)
conec[:,0]=conec1
conec[:,1]=conec2
#print(conec)
################################################
#值不对需要修改
number=np.zeros((nnt,1))
for i in range(0,nnt-1,1):
	number[i]=np.size(np.nonzero(conec==i))
print(number)	
#####################################################
iopen1=0   #节点1在腔的左侧
####################################################
#physical properties of the flow
gam=1.4 #特定的气体热比
gamm1=gam-1
R=287	#单独的气体常数
C_v=R/gamm1 #特定的气体比热容

pres_init0=1E5
#print(pres_init0)
temp_init0=300#初始温度
rho_init0=pres_init0/gamm1/C_v/temp_init0 
#
#我们计算初始压强
#我们设定外部压力
if(iopen1==0):
	


