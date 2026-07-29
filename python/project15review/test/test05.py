#N*N행렬 만들기 (입력받아서)

N = int(input("만들 행렬의 크기 입력 : "))

row = N
col = N
conut = 1
arr = []
for i in range(N):
    x = []
    for j in range(N):
        x.append(conut)
        conut += 1
    arr.append(x)
for a in arr:
    print(a)