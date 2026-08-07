#컴프리헨션
#0,1,2,3,4,5,6,7,8,9 에 대하여 홀짝판단하여 리스트에 추가하는것
result = []
for x in range(10):
    if(x%2 == 0):
        result.append("짝")
    else:
        result.append("홀")
print(result)

result = ["짝" if n%2==0 else "홀" for n in range(10)]
print(result)