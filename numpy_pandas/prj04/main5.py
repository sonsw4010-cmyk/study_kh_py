import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])

reslut = np.vstack((a,b)) # 두 배열 수직으로 합치기
print(reslut)
reslut = np.hstack([a,b]) # 두 배열 수평으로 합치기
print(reslut)