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
conec
