'''
print("Hello,\nWorld!")

x = int(input())
if x<10 :
    print("small")
else:
    print()


x = int(input())
if x%7 ==0 :
    print("multiple")
else:
    print("not multiple")

x = int(input())
bmi = x
if bmi<=10 :
    print("정상")
elif bmi<=20 :
    print("과체중")
else :
    print("비만")


x = float(input())
if 50<=x<=60 :
    print("win")
else:
    print("lose")

x = float(input())
if 30<=x<=40 or 60<=x<=70 :
    print("win")
else:
    print("lose")

x = float(input())
if 50<=x<=70 or x%6 ==0 :
    print("win")
else:
    print("lose")


data = input()

birth = data[:6]
gender = data[-1]

birth_year = (1900 if gender in ('1', '2') else 2000) + int(birth[:2])

print(2012 -birth_year+1)


age = int(input())
year = 2012 - age + 1
short_year = year % 100

if year < 2000:
    code = 1
else:
    code = 3

print(short_year, code)

n = int(input())

if n%2 == 0 :
    print("even")
else :
    print("odd")


x = input().split()
a = int(x[0])
b = int(x[1])

if a > b:
    print(a - b)
else:
    print(b - a)


x = input().split()
a = int(x[0])
b = int(x[1])

if a > b:
    print(">")
elif a < b:
    print("<")
else:
    print("=")

x = int(input())

if x>=10 :
    print("big")
elif x<10 :
    print("small")


day = int(input())

if day==1 or day==3 or day==5 or day==7 :
    print("oh my god")
else :
    print("enjoy")

x = input().split()
a = int(x[0])
b = int(x[1])

if a%2 !=0 and b%2 !=0 :
    print("홀수+홀수=짝수")
elif a%2 !=0 and b%2 ==0:
    print("홀수+짝수=홀수")
elif a%2 ==0 and b%2 !=0 :
    print("짝수+홀수=홀수")
elif a%2 ==0 and b%2 ==0 :
    print("짝수+짝수=짝수")

x = input().split()
a = int(x[0])
b = int(x[1])
c = int(x[2])
z=a-b+c
if str(z)[-1] == '0':
    print("대박")
else:
    print("그럭저럭")

x = input().split()
a = int(x[0])
b = int(x[1])
c = int(x[2])
z = a + b + c

z = int(str(z)[-3])
if z % 2 == 0:
    print("대박")
else:
    print("그럭저럭")

x = input().split()
a = int(x[0])
b = int(x[1])
c = int(x[2])

if a > 170 and b > 170 and c > 170 :
    print("PASS")
else:
    print("CRASH")

x = input().split()
a = int(x[0])
b = int(x[1])
c = int(x[2])
z=170

if z>=a :
    print("CRASH",a)
elif z>=b :
    print("CRASH",b)
elif z>=c :
    print("CRASH",c)
else:
    print("PASS")

x = int(input())

if x>0 :
    print("양수")
elif x<0 :
    print("음수")
else :
    print("0")

x = input().split()
a = int(x[0])
b = int(x[1])

b = b - 30
if b < 0:
    b = b + 60
    a = a - 1
if a < 0:
    a = 23

print(a, b)

x = input().split()
a = int(x[0])
b = int(x[1])

if b%a==0 :           #a<b
    print(f"{a}*{b//a}={b}")
elif a%b==0 :
    print(f"{b}*{a//b}={a}")
else:
    print("none")

x = input().split()
a = int(x[0])
b = int(x[1])
c = int(x[2])

if a>=b and a>=c and a<b+c :
    print("yes")
elif b>=a and b>=c and b<a+c :
    print("yes")
elif c>=a and c>=b and c<b+a :
    print("yes")
else:
    print("no")
'''
# 윤년은 29일까지 아니면 28일임
x = input().split()
a = int(x[0])
b = int(x[1])

if b ==2 and a%400 == 0 or a%4 == 0 and a%100 != 0  :
    print("29")
else :
    if b == 1 or b == 3 or b == 5 or b == 7 or b ==8 or b == 10 or b == 12 :
        print("31")
    elif  b == 2 :
        print("28")
    else :
        print("30")