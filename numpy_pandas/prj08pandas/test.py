import pandas as pd

df = pd.read_csv("data/employees.csv")
'''
print(df.head())
print(df.shape)
print(df.info())

result = df[['나이', '연봉']].agg(['mean', 'min', 'max'])
print(result,df[['나이', '연봉']].describe())

result = df.groupby("부서코드").size()
print(result)

# 1. 데이터 불러오기
df = pd.read_csv("data/orders.csv")
# 2. '카테고리' 열의 항목별 개수 세기
df = df["카테고리"].value_counts()
print(df)
'''
##################################################################################
'''
print(df[["이름","연봉"]])

print((df["연봉"] >= 5000).sum(),"명")

print(df[(df["부서코드"] == "D01") & (df["나이"] < 30)])

print(f"{(df["연봉"] >= 5000).sum()}명")

print(df[(df["부서코드"] == "D01") & (df["나이"] < 30)])

print(df.sort_values(by="연봉", ascending=False).head()[["이름", "연봉"]])

print(df.iloc[5:10])

print(df[df["연봉"].isna()][["사번", "이름", "부서코드"]])
'''
###############################################################################

print(df.isnull().sum())