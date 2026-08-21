import pandas as pd

data = {
    "이름":["김철수"],
    "나이":[29]
}
# 불러오기
# df = pd.read_csv('test.csv')
df = pd.DataFrame(data)
print(df.dtypes)