'''
list1 = [1,2,3,4,5,6]
print(list1)

list2 = [7,8,9,10,11,12]
print(list2)

x= list1 + list2
print(x)

x.append(13)
print(x)

x.insert(0,0)
print(x)'''
from os import remove

'''
name = input("이름")
age = int(input("나이"))

print(f"제 이름은 {name}이고,\n"
      f"나이는 {age}살 입니다. \n"
      f"내년에는 {age+1}살이 됩니다.")'''

#연산자 테스트

#산술 +,-,*,/,//,%
'''
print(3+4)
print(3//4)
print(3%4)

#비교 <,>,<=,>=,==,!=
print(3<4)

#논리 and,or,not
print(True and True)
print(True or False)
print(not True)
print(not False)
print(not False and True) #앤드가 먼저임 ㅅㄱ
'''
#자료구조 (리스트)
'''
score01 = 100
score02 = 90
score03 = 95

print(score01)
print(score02)
print(score03)

x = int(input("학생성적:"))
y = int(input("학생성적:"))
z = int(input("학생성적:"))

score01 = x
score02 = y
score03 = z

print(score01)
print(score02)
print(score03)

score_list =[]
score_list.append(int(input("학생성적:"))+5)
score_list.append(int(input("학생성적:"))+5)
score_list.append(int(input("학생성적:"))+5)

print(score_list) # 이거는 좀 그렇긴해
'''

# 문제1
# 첫번째요소 , 마지막요소 출력
fruits = ["사과", "바나나", "포도", "귤", "감"]

print(fruits[0],fruits[-1])

# 문제2
# 리스트 [10, 20, 30]에 다음을 순서대로 적용
# 1. 맨 끝에 40 추가
# 2. 맨 앞에 5 삽입
# 3. 20 삭제
# 최종 결과 출력 (기대값: [5, 10, 30, 40])
list = [10,20,30]
list.append(40)
list.insert(0,5)
list.remove(20)
print(list)

# 문제3
# 리스트 ["김", "이", "박", "이", "최"]에서
# "이"가 몇 번 나오는지 출력하고, "박" 의 위치(인덱스) 출력

x = ["김", "이", "박", "이", "최"]
cnt = x.count("이")  #얼마나 들어있나 췤
print(cnt)
z = x.index("박")
print(z)

# 문제4
# 리스트 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]에서 슬라이싱만 사용해 아래를 각각 출력하세요.
# 1. 앞 3개 → [1, 2, 3]
# 2. 뒤 3개 → [8, 9, 10]
# 3. 짝수 인덱스 값만 → [1, 3, 5, 7, 9]
# 4. 전체 역순 → [10, 9, 8, ..., 1]

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(a[0:3])
print(a[7:10])
print(a[0: :2])
a.reverse()
print(a)

