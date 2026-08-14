import  pandas as pd
#데이터 준비
df = pd.read_csv('data/emp.csv')

# #결측치 삭제
# print("결측치 처리 전 :\n",df.isna().sum())
# df = df.dropna()

# # 결측치 확인
# print("결측치 처리 후 :\n",df.isna().sum())

# #결측치 채우기(나이 중위값으로 채우기)
# df = df.dropna()
# df['나이'] = df['나이'].fillna(df['나이'].median())
# print("결측치 처리 후 :\n",df.head())

#결측치 도시 최빈값으로 채우기
df['도시'] = df['도시'].fillna(df['도시'].mode()[0])
print("결측치 처리 후 :\n",df)

#중복제거
print(df.duplicated())
df = df.drop_duplicates(subset=["이름"])
print(df)

#연봉이 결측치인 행 지우기
df = df.dropna(subset=["연봉","이름","나이"])
print(df)

# 칼럼 이름변경하기
df = df.rename(columns={"도시": "지역"})

# 값 치환 // 서울을 한양으로
df["지역"] = df["지역"].replace("서울", "한양")
print(df)

# 칼럼삭제(이름칼럼)
df = df.drop("이름", axis=1)
# df.drop(columns=["이름"],inplace=True) 이것도 가능


# 칼럼 타입변경
#타입변환 : ( astype(int)<<<< int형으로 타입변환 )// 근데 데이터중에 int가 아닌거(Nan) 같은게 있으면 형변환이 안됨, 그러니까 결측치를 항상 먼저 처리해야함
df["나이"] = df["나이"].astype("int")
df["연봉"] = df["연봉"].astype("int")
print(df)

#새로운 칼럼 만들기
df["월급"] = df["연봉"] / 12
print(df)

#정렬(월급칼럼가지고 내림차순정렬)
df = df.sort_values(by="월급", ascending=False)
print(df)

#정렬(인덱스 기준으로)
# df = df.sort_index()
# print(df)