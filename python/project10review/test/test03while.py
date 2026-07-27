#while
n = 0

while n < 10 :
    n = n + 1
    if n%2 == 0 :
        print("짝수")
        continue  #반복문의 처음으로 돌아감  #컨티뉴 때문에 밑에 코드 실행이 안됨 그래서 보통 이프문 안에 들어감
    