# row (행), col(열) 받아서 2차원 배열 생성하기 (1부터 시작해서 1씩 증가하도록)
#2차원 배열 생성하기

row = int(input("행 :"))
col = int(input("열 :"))
value = 1
arr =[]
for i in range(row):
    x = []
    for j in range(col):
        x.append(value)
        value += 1
    arr.append(x)
for n in arr:
    print(n)


