# loc , iloc

import pandas as pd

df = pd.read_csv("data/people.csv")
# print(df[["이름","연봉"]])
# print(type(df[["이름","연봉"]]))

reslut = df.set_index("이름")
print(reslut.loc["가영"]) #문자열로 검색할때
print(reslut.iloc[0]) #숫자로 검색할때