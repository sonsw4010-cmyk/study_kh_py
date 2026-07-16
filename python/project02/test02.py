#자료구조2
"""
list :
    - [ ]
    - 순서O, 수정O, 중복O
tuple :
    - ( ) //여기서 잠깐 , 가 없으면 튜플이 아니다잇
    - 순서O, 수정X, 중복O
dictionary :
    - {key:value}
    - 키-값 , 수정O
set :
    - { }
    - 순서X, 중복X
"""

x = (1,2,3) #() 빼도 됨
print(x)
print(type(x))


x = (1) #, 가 없어서 이건 그냥 1임
print(x)
print(type(x))


x = (1,) #, 가 있어서 튜플임
print(x)
print(type(x))

x = (100,200,300,"사과","바나나")
print(x)
print(x[0])
print(len(x))
print(type(x))
print("사과" in(x))