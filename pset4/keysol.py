import numpy as np
import pandas as pd
from pprint import pprint
from math import sqrt,exp,pi
def readfile(filename):
    with open(filename) as F:
        data = F.read()

    return data


file1="personKeyTimingA.txt"
file2="personKeyTimingB.txt"
file_email="email.txt"
p1=readfile(file1)
p2=readfile(file2)



# pprint(p2)
# pprint(p1)

pp=np.genfromtxt(file1,delimiter=",")[:,:1]

data1=pp[1:]-pp[:-1]
n1=len(data1)
sample_mean1=data1.mean()
var1=data1.var()
sample_var1=((n1)/(n1-1))*var1

print(sample_mean1,sample_var1+((sample_mean1)**2))
print(sample_mean1,sample_var1)


pp=np.genfromtxt(file2,delimiter=",")[:,:1]

data2=pp[1:]-pp[:-1]

n2=len(data2)
sample_mean2=data2.mean()
var2=data2.var()
sample_var2=((n2)/(n2-1))*var2


print(sample_mean2,sample_var2+((sample_mean2)**2))
print(sample_mean2,sample_var2)




def caculateNormal(u,sigm2,x):

    c=1/sqrt(sigm2)
    # print(c,"c----------")
    d=-((x-u)**2)/(2*sigm2)
    # print(d)
    # print(c*(exp(d)))
    # print("-"*20)
    return c*(exp(d))



pp=np.genfromtxt(file_email,delimiter=",")[:,:1]

email_key=pp[1:]-pp[:-1]
email_key=np.append(pp[:1],email_key)
print(email_key)
a=[]
b=[]
for x in email_key:
    # print(a,b)
    a.append(caculateNormal(7.4, 3.98, x))
    b.append(caculateNormal(8.0, 3.68, x))

aa=1
bb=1
for x in email_key:
    # print(a,b)
    aa*=caculateNormal(sample_mean1, sample_var1, x)
    bb*=caculateNormal(sample_mean2, sample_var2, x)

a=np.array(a)
b=np.array(b)
print(aa,bb)
print(aa/bb)
print(np.cumproduct(a)[-1]/np.cumproduct(b)[-1])

# print(caculateNormal(sample_mean1, sample_var1, sample_mean1),1/sqrt(sample_var1))
