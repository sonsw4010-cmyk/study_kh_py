import numpy as np

x = np.array([100,50,80,30])
a = [
    [1,2],
    [3,4],
]
b = [[5,6],
    [7,8], ]
c =[[9,10],
    [11,12], ]
a = np.array(a)
b = np.array(b)
'''
#통계함수
result = np.sum(x)
#최댓값
result = np.max(x)
#최솟값
result = np.min(x)
#평균값
result = np.mean(x)
#중앙값(진짜 중앙에 있는 값나옴/ 만약 짝수여서 중앙값이 2개면 그 두개 더해서 나누기 2함)//(중위값이랑 같은말임)
result = np.median(x)
#표준편차
result = np.std(x)


# 집계,axis

#정렬 : np.sort()
print(np.sort(x))
#최댓값의 요소의 인덱스 번호
print(np.argmax(x))
#최솟값의 요소의 인덱스 번호
print(np.argmin(x))

#where
result = np.where(x > 60 ,"합격","불합격")

# random
g =np.random.default_rng(42) #<<<시드고정?
result = g.random(10) #<<< 10개 랜덤으로 뽑음
result = g.integers(1,7,size=3) # 정수형?
result = g.normal(0,100,size=3) # 플룻형으로 ㅈ대로 줌
'''

#행렬곱
result = a*b #<<이건 그냥 냅다 곱하기임 행렬곱 아님
result = a@b  #<< 이게 바로 행렬곱이시다

#역행렬
result = np.linalg.inv(a)

#그리고 행렬*역행렬은 단위행렬임

#파일
np.save("data.npy",x)
result = np.load("data.npy")
print(result)