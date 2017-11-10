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
    number[i]=np.max(np.shape(np.nonzero(conec==i+1)))
    print(i ,np.max(np.nonzero(conec==i+1)))
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
	pres_init=pres_init0*(L_0/L_t)**gam
	
rho_init=rho_init0*(pres_init/pres_init0)**(1/gam)
temp_init=pres_init/rho_init/gamm1/C_v
p_ext=0*pres_init0 #活塞左侧的压力
#设置初始速度与总的流体能量
u_init=0
e_init=pres_init/gamm1/rho_init+0.5*u_init**2

#初始化节点上的解
vsol =np.zeros((nnt,3))
vsol[:,0]=rho_init*np.ones((nnt,1))[:,0]
vsol[:,1]=rho_init*u_init*np.ones((nnt,1))[:,0]
vsol[:,2]=rho_init*e_init*np.ones((nnt,1))[:,0]

vtemp=temperature(C_v,vsol)
vpres=pressure(R,vtemp,vsol)
vcelerity=np.sqrt(gam*gamm1*C_v*vtemp)
cel_init=vcelerity[1]

vflux               = np.zeros((nnt,ndln))
wx                  = np.zeros((nnt,1))
presL2t = pres_init*np.array([1,1,1])
	


