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

'''
students = [('김철수', 85), ('이영희', 92), ('박민수', 78)]

# 1) 모든 학생 이름과 점수를 출력
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

'''

'''
x = {1,2,3}
y = {2,3,4}

result = x|y  #합집합
print(result)

result = x&y #교집합
print(result)

result = x-y #차집합
print(result)'''


#예습인듯 예습아닌 시바꺼 이거 예습아니라 진도잖아 if문>> 조건식이란?? bool 타입이 값으로 나오는 거시에오 (T/F)
# 조건 맞는 실행문(들여쓰기가 되어있는) 을 전부 실행함

'''
if True:
    print("hello")  # 조건이 없어서 참 트루라 헬로
else:
    print("hi")

if False:
    print("hello")  # 이중부정은 긍정 하이요
else:
    print("hi")

x = True                   #x가 투르라 헬로우
if x:
    print("hello")
else:
    print("hi")
'''

n = int(input("밥알이 맻개고"))
result = 280<= n <= 320

if result:
    print("그래, 보통 초밥의 밥알은 320개가 적당하지만, 술안주로 낼 때는 손님이 배부르지 않도록 280개만 쥐어야 한다")
else:
    print("초밥이 얼굴로 날아온다")







