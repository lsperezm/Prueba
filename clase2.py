# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 11:06:34 2023

@author: lsper
"""
import numpy as np
import matplotlib.pyplot as plt

x=2
n=10
func = np.zeros(n)

func[0]=x

def update (f,x):
    f=(x/f +f)/2
    
    return f



for i in range (1,n):
    func[i]=update(func[i-1],x)

k=np.arange(0,n,1)

plt.scatter(k,func,marker='*', s=70)
plt.xlabel(r'$n$',fontsize=15)
plt.ylabel(r'$f_{n}(x)$',fontsize=15)
plt.axhline(y=np.sqrt(x),color='r',ls='--')

a=np.array([1,0])
b=np.array([0,1])

def get_cross_product(a,b):
    c=np.zeros(3)
    c[2]=a[0]*b[1] - a[1]*b[0]
    
    return c

c=get_cross_product(b,a)

def get_area(c):
    
    resp= np.sqrt(np.sum(c**2))
    
    return resp

area=get_area(c)


def transform(a):
    
    m=np.zeros( (2,2) )
    m[0,:]=[4,2]
    m[1,:]=[1,2]
    
    at=np.zeros_like(a)
    
    for i in range(len(a)):
        at[i]=np.sum([m[i,:]*a[:]])
        
        

    return at

at=transform(a)
bt=transform(b)

print(at,bt)

fig=plt.figure(figsize=(10,5))
ax1=fig.add_subplot(121)
ax2=fig.add_subplot(122)

ax1.arrow(0,0,a[0],a[1],head_width=0.5)
ax1.arrow(0,0,b[0],b[1],head_width=0.5)

ax2.arrow(0,0,at[0],at[1],head_width=0.5)
ax2.arrow(0,0,bt[0],bt[1],head_width=0.5)








