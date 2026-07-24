#컴프리헨션
'''
x = [10,20,30,40,50]
y = []

for i in x:
    y.append(i+1)
print(y)
'''

x = [10,20,30,40,50]
y = [elem +1 for elem in x]
print(y)

x = [10,20,30,40,50]
y = [elem +1 for elem in x if elem <= 30]
print(y)