import math

import pandas as pd

# def f01(x):
#     print("f01 called~",x)
#     if x >= 6000 :
#         return "개부자"
#     else :
#         return "개거지"

def check_grade(salary):
    if math.isnan(salary):
        return "결측치"
    elif salary > 6000 :
        return "개부자"
    else:
        return "개거지"

#데이터 준비
df = pd.read_csv("data/people.csv")
reslut = df["연봉"].map(check_grade)

print(reslut)


#f01함수의 리턴값이 행이되고 , 그 행을 가지고 시리즈가 만들어짐