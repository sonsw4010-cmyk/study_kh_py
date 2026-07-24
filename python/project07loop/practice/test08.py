# 업다운게임 만들기
#정답 숫자를 정함
import random

x=1
n = random.randint(1,50)

while True:
    z = int(input())
    if n == z and x != 1 :
        print(f"정답{x}번 만에 맞췄습니다!")
        break
    elif n == z and x == 1 :
        print("레전드상황발생..")
    elif n < z :
        print("다운")
        x= x + 1
    elif n > z :
        print("업")
        x = x + 1