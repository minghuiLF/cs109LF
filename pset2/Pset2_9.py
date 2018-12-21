import numpy as np

pfname="prior.csv"
cfname="conditional.csv"
def loadCsvData(file_name):
    return np.genfromtxt(file_name,delimiter=',')



prior=loadCsvData(pfname)
conditional=loadCsvData(cfname)

print(prior)
print(conditional)
postrior=(prior*conditional)/(prior*conditional).sum()
print(postrior)
