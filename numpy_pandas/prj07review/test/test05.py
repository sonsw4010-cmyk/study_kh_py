# shape 변환
import numpy as np

x = np.linspace(1,24,24)
x = x.astype(int)
x = x.reshape(2,3,4)    #3차원 배열(2개 묶음 × 3행 × 4열)
print(x)
print(x.ndim)
print(x.shape)
print(x.size)
print(x.dtype)