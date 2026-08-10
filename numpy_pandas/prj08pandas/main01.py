import pandas as pd

# Series 는 numpy 에다가 이름(label)붙여둔거임 (1차원)
sr = pd.Series([80,90,100],index=["a","b","c"])
# print(sr.values) #넘파이 배열 그대로
# print(sr.index) #label
# print(sr+5) #vector 연산 가능