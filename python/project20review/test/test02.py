#이차원 배열
'''
table = []
num = 10
for i in range(3):
    x = []
    for j in range(3):
        x.append(num)
        num = num + 10
    table.append(x)

for i in table:
    print(i)
'''
'''
table = [
    [10, 20, 30],
    [40, 50, None],
    [70, 80, 90]
]
found = False
for i in range(3):
    for j in range(3):
        if table[i][j] is None:
            del table[i]
            found = True
            break
    if found == True:
        break
print("--- 삭제 후 2차원 리스트 ---")
for row in table:
    print(row)
'''
'''
table = [
    [None, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

new_table = []

for row in table:
    if None not in row:
        new_table.append(row) 


print(new_table)
'''
table = [
    [10, 20, 30],
    [40, 50, None],
    [70, 80, 90]
]

for i in range(3):
    if None in table[i]:
        del table[i]
        break
print(table)