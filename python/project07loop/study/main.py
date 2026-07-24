#사실 조건문에  T F 는 1 0 무조건 이것만 와야하는게 아니라 공/백 같이 판단 가능한 영역이면 가능한듯

#구구단
'''
n = int(input("구구단 시뮬레이터:"))
x = [1,2,3,4,5,6,7,8,9]
for i in x:
    print(f"{n}*{i}={i*n}")
'''

'''
#시간출력
n = int(input("하루 시뮬레이터:"))
for i in range(0,24):
    for j in range(0,60):
        print(f"{i}:{j}")
'''

'''
n = int(input())

for i in range(1,n+1):
    if n % i == 0:
        print(i)
'''
'''
x, y = map(int, input().split())
sum = 0
for i in range(x,y+1):
    if i%2==0:
        sum = sum - i
    elif i%2!=0 :
        sum = sum + i
print(sum)
'''
'''
x, y = map(int, input().split())
sum = 0
sum1 =""
for i in range(x,y+1):
    if i%2==0:
        sum = sum - i
        sum1 = sum1 +f"-{i}"
    elif i%2!=0 :
        sum = sum + i
        sum1 = sum1 + f"+{i}"
print(f"{sum1}={sum}")
'''
'''
a, b = map(int, input().split())
sum = ""
sum1 = 0

for i in range(a, b + 1):
    if i % 2 == 1:
        if i == a:
            sum += f"{i}"
        else:
            sum += f"+{i}"
        sum1 += i
    else:
        sum += f"-{i}"
        sum1 -= i

print(f"{sum}={sum1}")
'''
'''
n = int(input())
total = 1
for i in range(1,n+1):
    total *= i
print(total)
'''
'''
n = int(input())
result = []

for i in range(2, n):
    if n % i == 0:
        result.append(i)
if len(result) == 2:
    if 4 in result:
        print("wrong number")
    else:
        print(*result)
else:
    print("wrong number")
'''
'''
n = int(input())
count = 0
for i in range(1,n+1):
    count += i

print("*"*i)
'''
'''
n = int(input())
x = list(map(int, input().split()))
print(x[0],x[n//2],x[n-1])
'''
'''
def isPrime(x):
    # 조건 1. 0과 1은 소수가 아님 (x < 2 -> 0, 1)
    if x < 2:
        return False
    # 조건 2. 2 이상인 경우
    else:
        # 2부터 x - 1까지 나누기 진행
        for i in range(2, x):
            # 나눠 떨어지는 수가 존재하면, 소수가 아님 (False)
            if x % i == 0:
                return False
        # for loop 동안 아무 숫자로도 나눠지지 않았다면, 소수 (True)
        else:
            return True

# 자연수 N 값 입력
n = int(input())

# 2부터(0, 1은 소수 아니므로) 자연수 N까지 확인(range는 ~이상, ~미만이므로 n+1)
for i in range(2, n+1):
    # i가 자연수 N의 약수인지 확인
    if n % i == 0 :
        # 두 숫자가 모두 소수인지 확인
        # isPrime(i)
        # => i가 소수라면 True
        # isPrime(n//i)
        # => 자연수 N을 i로 나눈 몫 = 나머지 한쪽 숫자
        # => 소수인지 검증해서(isPrime), 소수라면 True
        if isPrime(i) and isPrime(n//i):
            # 작은 수부터 반복 진행하므로, 자동 오름차순 출력
            print(i, n//i)
            # 반복하면 내림차순 값이 나오므로 break
            break
# for loop 동안 만족하지 못 했다면, 자연수 N은 어떤 두 소수의 곱이 아님.
else: print("wrong number")
'''
#1281
num_list = input().split()
a=int(num_list[0])
b=int(num_list[1])
sum = 0
for i in range(2,b+1):
    if a % 2 == 1 :
        if a == i :
            print(f"{a}", end=" ")
        else :
            print(f"+{a}", end=" ")
        print(f"{i}", end="")
        sum = sum + i
    else:
        print(f"-{a}", end=" ")
        sum = sum - i

print(f"={sum}", end= "")