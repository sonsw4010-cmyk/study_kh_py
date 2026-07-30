import random
from model.Squirtle import Squirtle
from model.Bulbasaur import Bulbasaur
from model.Charmander import Charmander

def battle(attacker,defender):
    print(f"\"{attacker.name}\"가 \"{defender.name}\"를 공격!")
    defender.hp -= attacker.atk
    print("공격한 포켓몬",attacker)
    print("맞은 포켓몬",defender)

p1 = Bulbasaur()
p2 = Squirtle()
p3 =  Charmander()

#스타팅 포켓몬 목록 출력
print("=======pokemon list=======")
print("1번",p1.name)
print("2번",p2.name)
print("3번",p3.name)
print()

#유저 포켓몬 선택
user = None
com = None

num = int(input("스타팅 포켓몬을 골라주세요! :"))
match num:
    case 1:
        user = p1
    case 2:
        user = p2
    case 3:
        user = p3

num = random.randint(1,3)
match num:
    case 1:
        com = Bulbasaur()
    case 2:
        com = Squirtle()
    case 3:
        com = Charmander()
'''
print(p)
print(p.name)
print(p.atk)
print(p.hp)

p.printInpo()

data = p.getInpo()
print(data)
'''
while True:
    #유저가 공격
    battle(user,com)
    if com.hp <= 0:
        break
    #컴퓨터가 공격
    battle(com,user)
    if user.hp <= 0:
        break

