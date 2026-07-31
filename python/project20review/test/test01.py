#중첩 반복문
'''
#1부터 6까지 출력
for i in range(1,7):
    print(i,end=" ")


#주사위를 2개 던져서 나올수있는 모든 경우의수
for i in range(1,7):
    for j in range(1,7):
        print(i,j)
    print()
'''
#시간마다 분,초 출력
for i in range(0,24):
  for j in range(0,60):
      for k in range(0,60):
          print(f"{i}:{j}:{k}")
  print()

