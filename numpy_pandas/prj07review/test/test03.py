#배열 생성 및 속성
import numpy as np
 # 넘파이 기본 자료형은 플룻형태임. ( 1.  이나 0. 이런거)


# 단위행렬 만들기~!
shape = (100,100)
v = 123
reslut = np.zeros(shape) # 0으로 배열 먕긂
reslut = np.ones(shape) # 1으로 배열 먕긂
reslut = np.full(shape,v) # 255으로 배열 먕긂
reslut = np.eye(2)


print(reslut.ndim)
print(reslut.shape)
print(reslut)