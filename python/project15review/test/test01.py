#반복문

x=0
while x < 10:
    print(x, end=" ")
    x +=1
    if x==10:
        break


for i in range(10,20,2):
    print(i, end=" ")

score_list = [100,90,85,100]
for x in score_list:
    print(x)