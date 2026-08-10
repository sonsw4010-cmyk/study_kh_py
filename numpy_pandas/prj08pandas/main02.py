#DataFrame : 시리즈가 여러개 있는거 (이차원 배열, 라잌 엑셀)//시리즈의 집합
import pandas as pd

dx = pd.DataFrame({
    "이름":["가","나","다"],
    "국어":[70,80,90],
    "영어":[100,50,60],
    "수학":[30,100,80],
              })

print(dx)
print(dx.columns)
print(dx.index)
print(dx.shape)
print(dx.head()) #앞에서부터 (n) 안에 보고싶은갯수 넣어도 됨 / 기본은 5개임
print(dx.tail()) #뒤에서부터 (n) 안에 보고싶은갯수 넣어도 됨 / 기본은 5개임
print(dx.sample()) #데이터를 무작위로 가져옴 (n) 안에 가져오고싶은갯수 넣어도 됨 