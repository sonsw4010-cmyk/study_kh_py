#인덱싱 , 연산
import numpy as np
a1 = np.array([10,20,30,40,50])
a2  = np.array([[1,2,3],
               [4,5,6],
               [7,8,9]])
# print(a[2,0])
# print(a.shape)
# print(a.ndim)
# print(a.size)
# print(a.dtype)

# 1차원 배열 슬라이싱
# print(a1[1:4]) #1이상 4미만
# print(a1[:3]) #처음 ~ 3미만
# print(a1[3:]) #3이상 ~ 끝까지
# print(a1[0::2]) # 처음부터~ 끝까지 2칸씩 건너뜀


# 2차원배열 슬라이싱
# print(a2)
# print(a2[1:3,0:2]) #1이상 3미만까지 (렬) / 0부터 2번 칼럼까지 (행)

print(a2[:,1:2])
print(a2[-1,:])
