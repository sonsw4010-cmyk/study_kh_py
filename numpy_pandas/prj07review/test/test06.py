import numpy as np

matrix = np.linspace(1,12,12).reshape(3,4).astype(int)   #와 원큐에 형변환! 샌즈!
print(matrix.shape)
print(matrix.ndim)
print(matrix.size)
print(matrix.dtype)
print(matrix)
print(matrix[1,2])
print(matrix[-1,-1])
print(matrix[1:3,1:3])