# 가위바위보 게임 만들기
'''
import random

c = ["가위","바위","보"]

while True :
    C_c = random.choice(c)
    P_c = input("가위 바위 보:")
    print("컴퓨터:",C_c)
    if P_c == C_c:
        print("비겼습니다.")
    elif (P_c == "가위" and C_c == "보") or (P_c == "바위" and C_c == "가위") or (P_c == "보" and C_c == "바위") :
        print("WIN")
        break
    elif P_c not in c  :
        print("다시골라주세요")
    else:
        print("Loser")
        break
'''
# 야구게임

import random

n1 = random.randint(0,9)
n2 = random.randint(0,9)
n3 = random.randint(0,9)
y = [n1,n2,n3]
count = 0
print("숫자 야구 게임 (1~9까지의 정수, 중복 가능)")
print(*y)
while True :
    user_input = input("3자리 숫자를 입력하세요 (예: 122): ")
    if len(user_input) != 3 or not user_input.isdigit():
        print( "정확히 3자리의 숫자를 입력해 주세요.")
        continue

    user_list = []

    for i in user_input:
        user_list.append(int(i))

    count += 1
    strike = 0
    ball = 0

    if user_list[0] == y[0]:
        strike += 1
    elif user_list[0] in y:
        ball += 1
    if user_list[1] == y[1]:
        strike += 1
    elif user_list[1] in y:
        ball += 1
    if user_list[2] == y[2]:
        strike += 1
    elif user_list[2] in y:
        ball += 1

    if strike == 3:
        print(f"스트라이크입니다! {count}번 만에 맞추셨습니다.")
        break
    elif strike == 0 and ball == 0:
        print("아웃입니다!")
    else:
        print(f"{strike} 스트라이크 | {ball} 볼")