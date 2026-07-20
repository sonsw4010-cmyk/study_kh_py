# 자료구조 // 인덱스는 데이터주소의 시작지점을 가르킴
from multiprocessing import context

#list : 순서있음 , 변경가능 , 중복허용 , 다양한타입가능


x= [1,4.1,True,"사과"]
print(x)
print(x[3])
x[3] = "과일"
print(x[0:3])  #0부터 n미만까지 / 처음부터 끝까지는 그냥 : 만 쓰면됨
print(x[3:0:-1]) # begin : end : step
x[1:3] = ["포도","1.11"] #슬라이싱을 이용한 수정
print(x)
x[1:3] = [] #슬라이싱을 이용한 삭제
print(x)

x.append(777) #맨뒤에 추가
print(x)

x.insert(2,"콩진호") #원하는 인덱스 위치에 추가
print(x)

x.remove("콩진호") #삭제
print(x)

'''
x.clear()  #어젯밤에.. 내 리스트가 무너졌어,,
print(x)
'''
y = ["강동연","지혜성","김석범"] #오우 리스트 안에 리스트가 추가됨 / 하지만 이게 아니지
x.append(y)
print(x)
x.remove(y)
x.extend(y) #이거는 요소가 추가됨 야미 / 근데 이거는 꼭 extend 안쓰고 print(x+y) 해도 됨 수고용
print(x)

i = x.index("강동연")  #3인덱스 자리에 있다 이거야
print(i)

cnt = x.count("강동연")  #얼마나 들어있나 췤
print(cnt)

x.reverse() #리스트 안에있는 요소들 뒤집기 라잌 천지개벽 // 그리고 보면 따로 변수등록을 안해도 단독으로 쓸수있는거임
print(x)

x2 = x # 이러면둘다 바뀜
print(x2)
print()

x[0] = "한요한"
print(x)
print(x2)

x2 = x.copy()
print(x2)
'''
x = "hello"
print(x)
X = list("hello") # ["hello"]  도 똑같이 작동함 내가해봄 ㅇㅇ
print(x)
print(x[0])
print(x[2])
print(x[4])
'''

#tuple
# dictionary
# set



















































































