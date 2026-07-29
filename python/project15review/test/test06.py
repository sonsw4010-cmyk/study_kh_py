#단위행렬 만들기
N = int(input("만들 행렬의 크기 입력 : "))

row = N
col = N
arr = []
for i in range(N):
    x = []
    for j in range(N):
        if j ==i :
            x.append(1)
        else:
            x.append(0)
    arr.append(x)

for a in arr:
    print(a)