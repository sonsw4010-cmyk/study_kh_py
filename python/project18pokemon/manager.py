import random

from model.pokemon import Pikachu, Lizard, Turtle

user = None
com = None

def print_pokemon_list():
    print("=========Pokemon list=========")
    print("1. :", Pikachu())
    print("2. :", Lizard())
    print("3. :", Turtle())
    print()

def select_user_pokemon():
    global user
    while True:
        num = int(input("원하는 포켓몬의 숫자를 입력하세요 :"))
        match num:
            case 1:
                user = Pikachu()
                break
            case 2:
                user = Lizard()
                break
            case 3:
                user = Turtle()
                break
            case _:
                print("잘못입력하셨습니다.")
                continue
        break


def select_com_pokemon():
    global com
    num = random.randint(1, 3)
    match num:
        case 1:
            com = Pikachu()
        case 2:
            com = Lizard()
        case 3:
            com = Turtle()

def battle_start():
   while True:
       # 사용자 입력/유저 턴
       print("======동작선택=======")
       print("1.몸통박치기")
       print("2.스낄")
       num = int(input("번호:"))

       is_finish = attack(user, com, num)
       if is_finish: break
       # 봇 턴
       num = random.randint(1, 2)
       is_finish = attack(com, user, num)
       if is_finish: break

def attack(attacker,defender,num):
    # 동작수행
    match num:
        case 1:
            attacker.tackle(defender)
        case 2:
            attacker.skill(defender)
    #정보 출력
    print("attacker:",attacker)
    print("defender:",defender)
    print(defender)
    # 결과판단
    result = defender.is_dead()
    if result:
        print(f"상대 포켓몬을 죽여버렸습니다. 이제 당신과 {attacker.name}은 살인자입니다...")
        return True





def play_game():
    print("Play game")







