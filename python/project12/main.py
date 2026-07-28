from model.animal import Animal
from model.food import  Food
from model.user import User
from model.musinsa_user import Musinsa_user
from model.duo_user import User as Duo_user


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
x2.bark()
x3.bark()



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

w1 = Duo_user()
w2 = Duo_user()
w3 = Duo_user()
w4 = Duo_user()

a1 = Musinsa_user("케로로",1234,"XL",170)
a2 = Musinsa_user("타마마",1234,"XL",175)
a3 = Musinsa_user("기로로",1234,"XL",160)
a4 = Musinsa_user("도로로",1234,"XL",180)
a5 = Musinsa_user("쿠루루",1234,"XL",170)
print(a1.username)
print(a2.username)
print(a3.username)
print(a4.username)
print(a5.username)
print(a1.password)
print(a2.password)
print(a3.password)
print(a4.password)
print(a5.password)
print(a1.size)
print(a2.size)
print(a3.size)
print(a4.size)
print(a5.size)
print(a1.cm)
print(a2.cm)
print(a3.cm)
print(a4.cm)
print(a5.cm)



