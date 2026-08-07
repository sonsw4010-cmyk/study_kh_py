import numpy as np

x = np.arange(1,13)
x = x.reshape(3,-1) # 행은 주고 나머지 알아서 해달라는 뜻
x = x.flatten() # 1차원으로 펼치기
print(x)
print(x.shape)
print(x.ndim)