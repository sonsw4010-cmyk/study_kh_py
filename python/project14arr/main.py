'''
a = list(range(3))
b = list(range(3))
c = list(range(3))
x = [a,b,c]

x[0]="하나"
x[1]="둘"
x[2]="셋"
'''
a = [10,20,30]
b = [40,50,60]
c = [70,80,90]
x = [a,b,c]

value = 10
i = 0

while i < 3:
    x[0][i] = value
    i += 1
    value += 10

value = 10
for i in range(3):
    for j in range(3):
        x[i][j] = value
        value += 10

print(x)

