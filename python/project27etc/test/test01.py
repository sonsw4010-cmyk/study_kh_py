#컴프리헨션

matrix = [[1,2],[3,4]]
#아차원배열 쫙 펴서 일차원 배열로 맹글어버라기~

'''
result = []
for row in matrix:
    for v in row:
        result.append(v)
print(result)
'''
result = [v for row in matrix for v in row]
print(result)

#일반적으로 하면 재미가 없으니까 제곱으로 출력
result = [v**2 for row in matrix for v in row]
print(result)