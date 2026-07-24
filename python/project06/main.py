'''
num = 0
result = "+" if num >= 80 else "_" if num<0 else "0"
print(result)

x = "철수"
match x:
    case "철수" :
            print("남자")
    case "영희":
            print("여자")


# match

month = 0
match month :
    case 1 | 3 | 5 | 7 | 8 | 10 | 12 : print(31)
    case 4 | 6 | 9 | 11: print(30)
    case 2 : print(28)
    case _ : print("그런 달은 없습니다. 1~12 중 입력하세요")

x = input().split()
h = float(x[0])
kg = float(x[1])


kg1 = (h-100)*0.9
bmi = (kg-kg1)*100 / kg1

if bmi <= 10 :
    print("정상")
elif 10< bmi <= 20 :
    print("과체중")
elif 20< bmi :
    print("비만")
'''

x = input().split()
h = float(x[0])
kg = float(x[1])

if h <150 :
    kg1=h-100
elif 150 <= h <160 :
    kg1=(h-150)/2+50
elif 160 <= h  :
    kg1=(h-100)*0.9

bmi = (kg-kg1)*100 / kg1

if bmi <= 10 :
    print("정상")
elif 10< bmi <= 20 :
    print("과체중")
elif 20< bmi :
    print("비만")