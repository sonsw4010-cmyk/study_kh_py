
'''
빈 배열에 이러면 오류남
x[0] = 10
x[1] = 20
x[2] = 30

#어펜드는 숫자말고도 물자열 튜플 리스트 등등 다양한걸 추가할수있음
x.append(10)
x.append(20)
x.append(30)

a = [10, 20, 30]
b = [40,50,60]
c = [70,80,90]
x.append(a)
x.append(b)
x.append(c)
'''
x = []
num = 10

for i in range(3):
    a = []
    for j in range(3):
        a.append(num)
        num += 10
    x.append(a)
print(x)
