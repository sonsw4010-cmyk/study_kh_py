import pandas as pd
sr = pd.Series([10, 20, 30], index=["x", "y", "z"])
df = pd.DataFrame({"도시": ["서울","부산","대구"], "인구": [970,340,240]})

print(sr)
print(df)
print(df.shape)
print(type(df["인구"]))
print(df["인구"])
print(df.columns)