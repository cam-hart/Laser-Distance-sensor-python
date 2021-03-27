# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 10:38:06 2021

@author: camer
"""
import math
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

distances=[]
x_pos=[]
y_pos=[]

position=0
delta_position=[0]
for i in range(len(distances)-1):
    x=x_pos[0]
    y=y_pos[0]
    x_delta=x_pos[(position+1)]
    y_delta=y_pos[(position+1)]
    delta=math.sqrt((abs(x_delta-x)**2)+(abs(y_delta-y)**2))
    delta_position.append(delta)
    position+=1

print(delta_position)
plt.plot(distances,delta_position)


def func(x,a,b,c):
    return (a*(np.log(x+b)))+c

x_range=np.arange(0.1,3,0.01)
opt_abc,other=curve_fit(func,distances,delta_position)
a,b,c=opt_abc
plt.plot(x_range,func(x_range,(a),(b+0.3),c))
plt.ylim([0,350])



