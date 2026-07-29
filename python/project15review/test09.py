arr =[]
row = 3
col = 3
for i in range(row):
    x = []
    for j in range(col):
        x.append(0)
    arr.append(x)

arr[0][0] =100
arr[0][1] =90
arr[0][2] =80
arr[1][0] =10
arr[1][1] =20
arr[1][2] =30
arr[2][0] =70
arr[2][1] =60
arr[2][2] =50
for n in arr:
    print(n)

# 과목별 평균
# 학생별 총점과 평균
# 과목별 최고 점수와 해당 학생 이름
# 총점 최고득점자와 최저득점자 이름
# 평균 미만 출력 (평균 60점 미만)
# 과락자 출력 (1과목이라도 40점 이하인 경우)