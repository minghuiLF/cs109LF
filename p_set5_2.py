import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


simulation=[]
for i in range(10000):
    x=stats.uniform.rvs(size=100)

    X=np.sum(x)
    # print(X)
    simulation.append(X)
ind=np.arange(30,61,1)
plt.hist(simulation,ind,edgecolor="black",alpha=0.5)

stats.norm.pdf(47,5,48.5)

x=np.arange(30, 61,0.01)

plt.fill_between(x,stats.norm.pdf(x,loc=50,scale=np.sqrt(100/12))*10000,color="green",alpha='0.7',edgecolor="red")






plt.show()
