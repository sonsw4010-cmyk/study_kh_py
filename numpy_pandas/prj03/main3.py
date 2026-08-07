import numpy as np

# x = np.array([1,2,3,4,5])
# y = np.array([10,20,30,40,50])
# reslut = x+y
# print(reslut) # 오 이러면 같은 자리에 있는 애들끼리 더해짐

x = np.array([[1,2,3],[4,5,6]])
y = x*10
print(x)
print(y) # 그냥 *10 때려 박았는데 됨 ㄷㄷ
print(x+y) # 아니 더하기도 된다고