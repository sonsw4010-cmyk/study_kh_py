#1부터 10까지 3의배수의 합
sum = 0
x = 1
while x <= 10:
    if x%3 == 0:
        sum += x
    x += 1
print(sum)