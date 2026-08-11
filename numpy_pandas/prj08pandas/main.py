import numpy as np
import pandas as pd

'''
#파이썬 순수 리스트
x = [10,20,30]
# numpy 리스트
np.array(x)
# 시리즈 리스트
z = pd.Series(x)


a = pd.Series([10,20,30],index=["math","kor","eng"])
b = pd.Series([40,50,60],index=["math","eng","kor"])

print(a["math"]) #문자열로 접근
print(b.iloc[0]) #숫자로 접근

print(a+b) # 위에 인덱스 순서를 바꿔도 같은 이름의 인덱스끼리만 계산됨



sr01 = pd.Series(["가영","나영","다영"],index= ["1번학생","2번학생","3번학생"])
sr02 = pd.Series([100,90,80],index= ["1번학생","2번학생","3번학생"])

sr03 = pd.Series(["홍길동","안철수"],index= ["4번 학생","5번학생"])
sr04 = pd.Series([50,60],index= ["4번학생","5번학생"])

sr_names = pd.concat([sr01,sr03])
sr_scores = pd.concat([sr02,sr04])

df = pd.DataFrame({
    "이름":sr_names,
    "성적":sr_scores,
})
print(df.iloc[0])
'''
df = pd.read_csv("data/people.csv")
print(df.loc[0:3,"이름"])
df  = df.dropna()
df = df.drop_duplicates()
print(df.head())
# print(x)
# print(x.max)

# sr = df["나이"]
# print(sr.max())
# print(sr.min())
# print(sr.mean())

# print(pd.info())
# print(pd.describe())
# print(pd.isna().sum())
# print(pd.sample(5))

df.to_csv("data/result.csv",index=False,encoding="utf-8-sig")
