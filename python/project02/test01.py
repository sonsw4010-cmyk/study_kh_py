#자료구조
"""
list :
    - [ ]
    - 순서O, 수정O, 중복O
tuple :
    - ( )
    - 순서O, 수정X, 중복O
dictionary :
    - {key:value}
    - 키-값 , 수정O
set :
    - { }
    - 순서X, 중복X
"""
'''
x = []

x.append(100)
x.append(3)
x.append(777)
x.append("사과")
x.append(True)
print(x)
'''
x = [100, 3, 777, '사과', True]
print(x)
print(x[0])
x.remove("사과")#제일 먼저있는게 없어지네
x.insert(4,"오미자")
print(x)

x = [1,2,3,4,5,6,7,8,9]
y = [10,11,12,13,14,15,16,17,18,19,20]
print(x + y)

print(x[0])

print(len(x))

print("바나나" in x)