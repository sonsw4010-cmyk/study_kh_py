import numpy as np
# 규칙이 있는 배열
#간격을 알때
# reslut = np.arange(1,10,2)  #(시작,끝,간격) 임 스텝 안쓰면 기본빵 1로 됨, 시작값도 안쓰면 기본빵 0부터임
# print(reslut)
#요소들의 갯수를 알때
reslut = np.linspace(0,1,5) #(시작값,끝값,사이갯수)
reslut = reslut.astype(int)
print(reslut.shape)
print(reslut.ndim)
print(reslut.shape)
print(reslut.dtype)
print(reslut)
