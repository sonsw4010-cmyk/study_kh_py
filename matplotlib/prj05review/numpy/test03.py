# 인덱싱 , 연산
import numpy as np

x = [0,1,2,3,4]
x = np.array(x)

mask = [True, False, True, True, False]
result = x[mask]
print(result)

# 펜시 인덱싱
# 요소별 연산이 가능함
