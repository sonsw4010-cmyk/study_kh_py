# bool 인덱싱
import numpy as np

score = np.array([100,50,70,30])

# score[score<60] = 0
print(score[(50<=score) & (score<80)])