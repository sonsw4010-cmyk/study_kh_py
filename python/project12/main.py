from model.animal import Animal
from model.animal import Bark
from model.food import  Food
from model.user import User
from model.musinsa_user import Musinsa_user


x1 = Animal("바둑이",1)
x2 = Animal("빙고",14)
x3 = Animal("뽀삐",12)
print(x1.name)
print(x2.name)
print(x3.name)
print(x1.age)
print(x2.age)
print(x3.age)
x1.bark()



y1 = Food("밥",1000,200)
y2 = Food("빵",3000,300)
y3 = Food("면",2000,500)
print(y1.name)
print(y2.name)
print(y3.name)
print(y1.price)
print(y2.price)
print(y3.price)
print(y1.calories)
print(y2.calories)
print(y3.calories)

z1 = User("홍",1234,"홍박사")
z2 = User("명",2341,"명박사")
z3 = User("보",3214,"보박사")
print(z1.username)
print(z2.username)
print(z3.username)
print(z1.password)
print(z2.password)
print(z3.password)
print(z1.nickname)
print(z2.nickname)
print(z3.nickname)

a1 = Musinsa_user("케로로",1234,"XL",170)
a2 = Musinsa_user("타마마",1234,"XL",170)
a3 = Musinsa_user("기로로",1234,"XL",170)
a4 = Musinsa_user("도로로",1234,"XL",170)
a5 = Musinsa_user("쿠루루",1234,"XL",170)



