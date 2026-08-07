#axis
import numpy as np

#2차원 배열맹긂
x = np.arange(1,13)
x = x.reshape(3,-1) # 3행으로 만들고싶고 나머진 맘대로 슛

#연산
# 행(0)끼리 or 열(1)끼리 더하기
print(x)
print(np.sum(x,axis=1))