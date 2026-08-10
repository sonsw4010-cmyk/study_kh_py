# Boolean Indexing
import pandas as pd

df = pd.read_csv("data/people.csv")

print(df[df["나이"] > 30])

print(df[df["도시"] == "서울"])

print(df[ (df["나이"] >=40) & (df["연봉"] >= 5000) ])

print(df[(df["도시"] == "서울") | (df["도시"] == "부산")])
print(df[df["도시"].isin(["서울","부산"])]) # 위에랑 똑같이 동작함 레전드

print(df[ (df["나이"] >=30) & (df["나이"] <40) ])
print( df[ df["나이"].between(30,39) ] ) # 위에랑 똑같이 동작함 레전드