from matplotlib import pyplot as plt
from random import random
from math import factorial,exp
from pprint import pprint
import numpy as np
from collections import defaultdict

#
#X ~Bin()simulator
#
def simulateBin(n=20,p=0.4):
    nSuccesses=0
    for i in range(n):
        if random()<p:
            nSuccesses+=1
    return nSuccesses


def Bin(n=20,p=0.4):
    Binfunc={x:0 for x in range(21)}
    for i in range(21):
        c=factorial(n)/(factorial(i)*factorial(n-i))
        success=p**i
        faill=(1-p)**(n-i)
        Binfunc[i]=c*success*faill*10000



    plt.bar(Binfunc.keys(),Binfunc.values())
    plt.show()

def exprienceBin(N=10000):
    statistic={x:0 for x in range(21)}
    for i in range(N):
        statistic[simulateBin()]+=1



    plt.bar(statistic.keys(),statistic.values())
    plt.show()
# Bin()
# exprienceBin()


#
#X ~Geo()simulator
#
def simulateGeo(p=0.05):
    i=1
    while i <210:
        if random()<p:
            return i

        i+=1
    return None
def Geo(p=0.03):
    Geofunc={x:0 for x in range(1,210)}
    for x in Geofunc.keys():
        faill=(1-p)**(x-1)
        Geofunc[x]=faill*p
    plt.bar(Geofunc.keys(),Geofunc.values())
    plt.show()


def exprienceGeo(N=10000):
    statistic={x:0 for x in range(1,210)}
    statistic[None]=0
    for i in range(N):
        statistic[simulateGeo()]+=1



    plt.bar(list(statistic.keys())[:-1],list(statistic.values())[:-1])
    plt.show()

# Geo()
# exprienceGeo()

#
#X ~HypGeo()simulator
#

def HypGeo(k=5,p=0.03):
    func={x:0 for x in range(5,210)}
    for i in range(5,210):
        c=factorial(i-1)/(factorial(k-1)*factorial(i-k))
        success=p**k
        faill=(1-p)**(i-k)
        func[i]=c*success*faill*10000



    plt.bar(func.keys(),func.values())
    plt.show()

def simulateHypGeo(k=5,p=0.03):

    i=0
    x=0
    while x<210-1:
        if random()<p:
            i+=1
        if i==k:
            return x+1
        x+=1
    return None
def exprienceHypGeo(N=10000):
    statistic={x:0 for x in range(5,210)}
    statistic[None]=0
    for i in range(N):
        statistic[simulateHypGeo()]+=1



    plt.bar(list(statistic.keys())[:-1],list(statistic.values())[:-1])
    plt.show()

# HypGeo()
# exprienceHypGeo()

#
#X ~Poi()simulator
#

def Poi(lmd=3.1):
    data={x:0 for x in range(20)}

    for x in range(20):
        data[x]=((lmd**x)*exp(lmd))/factorial(x)

    plt.bar(data.keys(),data.values())
    plt.show()

def expriencePoi(N=10000,lmd=3.1):
    statistic={x:0 for x in range(21)}
    for i in range(N):
        statistic[simulateBin(n=60000,p=3.1/60000)]+=1



    plt.bar(statistic.keys(),statistic.values())
    plt.show()




# Poi()
# expriencePoi()

#
#X ~Exp()simulator
#

def Exp(lmd=1):
    data={x:0 for x in np.arange(0,6,0.0001)}
    for x in np.arange(0,6,0.0001):
        data[x]=lmd*exp(-lmd*x)

    plt.plot(data.keys(),data.values())
    plt.show()

def simulateExp(lmd=3.1):
    n=6000
    p=lmd/n
    i=1
    while i<18000:
        if random()<p:
            return i

        i+=1



def exprienceExp(N=18000):
    statistic=defaultdict(int)
    i=0
    while i<N:
        X=simulateExp(3.1)
        if X!=None:
            statistic[X]+=1
        i+=1
    # for x,y in statistic.items():
    #     plt.bar(x,y)
    # pprint(statistic.keys())
    # pprint(statistic.values())
    plt.bar(statistic.keys(),statistic.values())
    plt.show()




# Exp()
exprienceExp()
