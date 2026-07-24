#소수의 정의 : 1과 자기자신만을 약수로 가지는 수 ( 1,slef )
print("=========== prime ============")

num = int(input())
for i in range(2,num):
    if num % i == 0:
        print("not prime")
        break
else:
    print("prime")