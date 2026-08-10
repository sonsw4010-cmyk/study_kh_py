# 전처리
import pandas as pd

#데이터 준비
df = pd.read_csv("data/people.csv")

#결측치 처리
# df = df.dropna()
# df["나이"] = df["나이"].fillna(df["나이"].mean())
# df["도시"] = df["도시"].fillna("커닝시티")
# df["연봉"] = df["연봉"].fillna(df["연봉"].mean())
# print(df.isna().sum())
print(df.head())

#중복제거
df = df.drop_duplicates()
print(df.head())