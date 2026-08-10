# load

import pandas as pd

df = pd.read_csv("data/people.csv")

#만든데이터 저장하는법~
df.to_csv("data/result.csv", index = False,encoding="utf-8-sig")
print(df)