#sort
#argsort
#argmax
#where (조건,참값,거짓값)
import numpy as np

# x = np.array([1,2,3,4,5])
# print(np.where(np.isin(x,[3,5]),"굿","노굿"))

rng = np.random.default_rng(42)
# result = reg.random(3) # 0~1
# result = rng.integers(1, 46, size=6) # 1~6
result = rng.normal(60,10)
print(result)