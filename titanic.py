import numpy as np
import pandas as pd
from pprint import pprint

cfname="titanic.csv"
def returnDataframlebyFliter(D,C={},S={}):
    constri=1
    for column_name,value in C.items():
        constri &= DS[column_name]==value
    for column_name,value in S.items():
        constri &= DS[column_name]<=value

    return D.loc[constri]
DS=pd.read_csv(cfname)
pprint(DS)
print(DS.loc[0])

for a in [1,2,3]:
    print(
    DS.loc[(DS['Sex']=='female')& (DS['Pclass']==a)&(DS['Survived']==1)].index.size/ \
    DS.loc[(DS['Sex']=='female')& (DS['Pclass']==a)].index.size
    )
for a in [1,2,3]:
    print( '%.2f' %
    (DS.loc[(DS['Sex']=='male')& (DS['Pclass']==a)&(DS['Survived']==1)].index.size/ \
    DS.loc[(DS['Sex']=='male')& (DS['Pclass']==a)].index.size)
    )

print('-'*50)
c=returnDataframlebyFliter(DS,{'Pclass':3},{'Age':10})
print(c.loc[c['Survived']==1].index.size)
print(c.loc[c['Survived']==0].index.size)

print('-'*50)



print('%.2f' %returnDataframlebyFliter(DS,{'Pclass':1})['Fare'].mean())
print('%.2f' %returnDataframlebyFliter(DS,{'Pclass':2})['Fare'].mean())
print('%.2f' %returnDataframlebyFliter(DS,{'Pclass':3})['Fare'].mean())
