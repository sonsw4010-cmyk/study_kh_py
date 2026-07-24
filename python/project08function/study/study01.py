
'''
def printSum():
    x = 10
    y = 20
    result = x + y
    print(result)
'''

# 매개변수 (파라미터/parameter) x,y
def getSum(x,y):
    result = x + y
    return result

   # print(result)

a = getSum(10, 20)
# print(result) << 이렇게는 안됨, 왜냐면 여기서 있는 result 는 def printSum안에서만 정의되는 함수임 근데 위에처럼  return을 사용하고 변수를 지정하면 값을 가져올수있음
#함수를 먼저 정의하고 그다음에 변수를 만들어야할듯
print(a)
getSum(20, 30)
getSum(30, 40)