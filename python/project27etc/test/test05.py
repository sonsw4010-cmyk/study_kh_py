#zip

a =["홍길동","엄홍길","호랑이"]
b = [100,200,300]
c = [146,125,167]

result = zip(a,b,c)
for n,s,h in result:
    print(n,s,h)
