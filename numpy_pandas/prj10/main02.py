import pandas as pd

# 데이터 준비
df = pd.read_csv('data/emp.csv')

# 피벗 테이블 생성
result = df.pivot_table(index='부서', columns='직급', values='급여', aggfunc="mean")

# 결측치를 0으로 채운 후 정수형(int)으로 변환
result_int = result.fillna(0).astype(int)

print(result_int)