import numpy as np
import time


def quicksort(L=[]):
    if  len(L)<2: return L

    C = Partition(L, L[0])
    m1=quicksort(C[0])
    m2=quicksort(C[2])
    return m1+C[1]+m2
def Partition(arr,pivot):
    p1=[]
    p2=[]
    c=0
    for i in arr:
        if i < pivot:
            p1.append(i)
        elif i > pivot:
            p2.append(i)
        else:
            c+=1

    return (p1,([pivot]*c),p2)


def quicksort2(L=[],s=0,n=None):
    if  n-s<2: return L
    b = partition2(L,s,n)
    quicksort2(L,s,b)
    quicksort2(L,b+1,n)
    return L

def partition2(arr,s,n):
    # print(arr,s,n)
    pivot=arr[s]
    lh=s+1
    rh=n-1
    # cc=0
    while True:
        # print(lh,rh,arr[rh],pivot)
        while ((lh < rh) and (arr[rh]>=pivot)):

            rh-=1


        while ((lh < rh) & (arr[lh]<pivot)):
            lh+=1

        if lh==rh:
            break
        arr[lh],arr[rh]=arr[rh],arr[lh]
        # if cc==20: break
        # cc+=1
    if(arr[lh]<pivot):
        arr[s],arr[lh]=arr[lh],arr[s]
        return lh

    return lh-1







l=[np.random.randint(100) for i in range(1000)]
# print(Partition(l, l[0]))
print(time.time())
a=quicksort(l)

print(time.time())
c=quicksort2(l,0,len(l))
print(time.time())
b=sorted(l)

print(time.time())


# print(quicksort2(l,0,len(l)))
#
#
# print("*"*60)
