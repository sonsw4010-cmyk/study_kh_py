import numpy as np

x = np.linspace(1,24,24)
print(x)
#차원 변경
# x = x.reshape(3,4) # 3,4 행렬로 재구성
# x = x.reshape(2, 3,2,2)
# print(x)
# print(x.shape)
x = np.full((2,3),5)
print(x)