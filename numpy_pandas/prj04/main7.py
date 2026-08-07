import numpy as np

a =np.arange(6)
m = np.array([[1,2,3],[4,5,6],[3,7,1]])


a = a.reshape(2,3)


print(a)
print(m)
print(np.sum(m,axis=0))
print(np.max(m,axis=0))
print(np.min(m,axis=0))