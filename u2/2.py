import sys
import random
from random import *
from math import floor
import time
sys.setrecursionlimit(1000000) # 10000 is an example, try with different values

def T(n):  
    if n == 1:
        return 1
    else:
        return T(n-1) + 1.0/n


#for i in range(2,8):
#    print("i = ", 10**i ,T(10**i))

def shuffle1(n):
    a = [i for i in range (n+1)]
    for i in range(0,n+1):
        j = random.randint(i,n)
        a[i],a[j] = a[j], a[i]
    return a

def shuffle2(n):
    a = [i for i in range (n+1)]
    for i in range(0,n+1):
        j = random.randint(0,n)
        a[i],a[j] = a[j], a[i]
    return a

def shuffle3(n):
    a = [i for i in range (n+1)]
    for i in range(0,n+1):
        j = random.randint(0,i)
        a[i],a[j] = a[j], a[i]
    return a

k=20
n=4
"""
print()
print("schuffle1:")
for i in range (0,k):  
    print(shuffle1(n))             

print()
print("schuffle2:")
for i in range (0,k):
    print(shuffle2(n))     
    

print()
print("schuffle3:")
for i in range (0,k):   
    print(shuffle3(n))     
    """


########################## u3















