# 변수
'''
룰
1. 문자나 숫자 혹은 _
2. 숫자로 시작하면 안됨
3.대소문자로 구분됨
4.이미 파이썬이 쓰려고 예약한 문자는 안됨 (ex) if,True,class
5. 가능하면 변수명은 느자구없이 짓지말자.
6. snake_case 혹은 camelCase 를 이용해서 적자 (ex) total price >>띄어쓰기하면 병신 // total_price나 totalPrice 로 하렴
7.상수는 대문자로 적어라 TOTAL_PRICE
/변수에는 정수, 실수, 논리, 문자열등 다양한 형태위 변수가 있다.
'''
x = 10
print(x)

x,y = 30,"100"
print(x,y)

print(type(x))
print(type(y))

y = int(y)
print(type(y))

'''
print(x)
del x
print(x) < x가 삭제되어서 에러남
'''