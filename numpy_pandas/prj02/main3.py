#넘파이 사용할때 확인할것 목록

import numpy as np

a = np.array([[1.1,2.2,3,4],[5,6,7,8.5]],dtype=float) # dtype=int 이런식으로 플롯타입이여도 인트형으로 강제 형변환이 가능하다
print(a)
print(a.shape) #이건 앵간하면 확인해라 보통 이년때문에 에러남
print(a.ndim)#차원
print(a.size)#원소의 갯수
print(a.dtype) # 실수를 섞으면 인트형에서 플룻형으로 자동으로 바뀌더라

result = a.astype(int) #이걸로 타입을 int로 바꿈
print(result)