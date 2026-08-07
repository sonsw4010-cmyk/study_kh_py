import numpy as np

scores = [70,80,50,90]
np_scores = np.array(scores)

print(scores) # 여기는 배열로 출력
print(np_scores) # 넘파이특 컴마 없이 출력됨

print(np_scores+5) # 와 이게 그냥 한방에 된다. 기가..메키노