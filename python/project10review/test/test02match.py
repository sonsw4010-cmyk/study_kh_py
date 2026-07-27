# match
#1월부터 12월의 말일 출력하기(윤년제외)

n = int(input("month: "))

match n :
    case 1 | 3 | 5 | 7 | 8 | 10 |12:
        print(31)
    case 2 :
        print(28)
    case 4 | 6 | 9 | 11 :
        print(30)
    case _:
        print("그런달은 없습니다.")