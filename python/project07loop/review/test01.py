# 숫자를 입력받고 홀짝인지 판단하는 프로그램 근데 이제 계속 판단해주는

n = int(input("숫자를 입력하세요:"))

while True :
    if n==0 :
        break
    elif n % 2 == 0 and n >0 :
        print("짝")
        n = int(input("숫자를 입력하세요:"))
    elif n % 2 != 0 and n > 0:
        print("홀")
        n = int(input("숫자를 입력하세요:"))
    else :
        n = int(input("자연수를 입력하세요:"))