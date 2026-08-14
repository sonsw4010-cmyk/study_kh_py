import pandas as pd

df = pd.read_csv('data/emp.csv')

# 전 직원 평균급여
reslut = df["급여"].mean()

# 부서별 평균 급여
# reslut = df.groupby("부서")["급여"].mean()

#부서별 인원수 확인
# reslut = df.groupby("부서").size()

#부서별 여러개의 통계를 한번에 출력 (최대 ,최소,평균) // .agg()
# reslut = df.groupby("부서")["급여"].agg(["max", "min", "mean"])

#칼럼으로 묶기 (부서+직급)
# reslut = df.groupby(["부서", "직급"])["급여"].max()

#칼럼별로 다른 집계 // 급여는 평균 , 나이는 최댓값, 평가점수는 최솟값
# reslut = df.groupby("부서").agg({"나이":"max", "평가점수":"min", "급여":"mean"})

'''
# map() 사용 (콜백함수를 잘 이해했으면 이지)
def f01(x):
    if pd.isna(x):
        return None
    if x >= 90 :
        return "A"
    elif x >= 80 :
        return "B"
    elif x >= 70 :
        return "C"
    else :
        return "D"

df['평가등급'] = df['평가점수'].map(f01)
'''
def create_score(r):
    return (r["근속연수"] * r["평가점수"])

df["종합점수"] = df.apply(lambda r : r["근속연수"] * r["평가점수"],axis=1)
# df["종합점수"] = df.apply(create_score, axis=1) # 0이면 칼럼(열) 1이면 행 // 여기서는 반대임
# 결과 확인
print(df)