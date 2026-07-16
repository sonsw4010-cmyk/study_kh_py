from unittest import result

a = ["손흥민","봉준호","지혜성","이강인","나얼","카리나"]
b = ("손흥민","봉준호","지혜성","이강인","나얼","카리나")


'''
print(a)
print(type(a))

print()

print(b)
print(type(b))

a[0] = "강동원"
print(a)
print(b)#a는 리스트라 a만 바뀜 b(튜플)는 못바꿈'''

'''
print(len(a))
print(len(b))

print(a[0])
print(a[4])

print(a[3:5])# 3부터 5전까지 [a:b] >> b-a개
print(a[3:])# 3부터 젠부
print(a[:5])#0부터 5까지
#>> 리스트로만 했지만 튜플도 동일하게 가능함
'''

'''
print(type( tuple(a) ))
a = tuple( a )
a[1] = "튜플이라 안바뀌쥬?"
print(a)
'''

'''
result = b + ("이강인",) # 튜플에 추가하고싶을때는 리스트로 바꾸던지 아니면 튜플끼리 더하자 그리고 튜플은 () 보다 ,가 중요하다
print(result)'''


'''
x = a[0]
y = a[1]
z = a[2]

print(x)
print(y)
print(z)
'''

'''
#이거는 값이 3개일때만 됨 4개부터 안됨 , 변수 갯수랑 맞춰라 / 근데 *을 박으면 다 넣을수있음 > 근데 무조건 리스트로 바뀜 튜플로해도 마찬가지
*x,y,z = a
print(x)
print(y)
print(z)
'''


students = [('김철수', 85), ('이영희', 92), ('박민수', 78)]

# 1) 모든 학생 이름과 점수를 언패킹으로 출력
print(students[0])
print(students[1])
print(students[2])
# 2) 이름만
print(students[0][0])
print(students[1][0])
print(students[2][0])
# 3) 점수만
print(students[0][1])
print(students[1][1])
print(students[2][1])
