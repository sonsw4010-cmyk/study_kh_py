# for

'''
for 변수 in 반복가능한객체:
           실행할 코드 ~
'''

num_list = [10, 20, 30, 40, 50]

for n in num_list:
    print(n)

idx = 0
while idx < len(num_list):
    print(num_list[idx])
    idx += 1