'''
a=[1,2,3]
b=[4,5,6]
c=[7,8,9]

x =[[1,2,3],[4,5,6],[7,8,9]]

print(x[0])
print(x[1])
print(x[2])

for i in x:
    print(i)


x=[]
num = 0
for i in range(1,10):
    x.append(i)
print(x)
'''

value = 1
for j in range(3):
    x = []
    for i in range(1,4):
        x.append(i)
        value += 1

for temp in x:
    print(x)