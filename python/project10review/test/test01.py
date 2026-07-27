#조건문
#조건문 마스터한 요건 : 플러스 마이너스 제로 판단은 해야 기본빵은 되는거다.

n = int(input("양수 음수 판독기:"))

if n > 0 :
    print("양수")
elif n < 0 :
    print("음수")
elif n == 0 :
    print("0")