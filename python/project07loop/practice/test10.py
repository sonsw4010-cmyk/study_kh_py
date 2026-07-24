#자판기

'''
======= 자판기 =======
1. 콜라     1500원
2. 사이다   1300원
3. 커피     2000원
4. 잔액조회
0. 종료
======================
'''

print("======= 자판기 =======\n 1.콜라:1500원\n 2. 사이다:300원\n 3.커피:2000원\n 4.잔액조회\n 0.종료\n======================")
cash = 10000
while True:
    c = int(input("메뉴번호:"))
    if c == 1 :
        if cash < 1500 :
            print("잔액이 부족합니다.")
        cash -= 1500
        print("남은금액:",cash)
    elif c == 2:
        if cash < 1500 :
            print("잔액이 부족합니다.")
        cash -= 1300
        print("남은금액:", cash)
    elif c == 3:
        if cash < 1500 :
            print("잔액이 부족합니다.")
        cash -= 2000
        print("남은금액:", cash)
    elif c == 4:
        print("잔액조회",cash)
    elif c!=1 or c!=2 or c!=3 or c!=4 or c!=0:
        print("잘못 선택하셨습니다.")
    elif c == 0:
        print("종료합니다")
        break