import numpy as np

a = np.array([1,2,3])
b = np.array([[4,5,6],[7,8,9]])
print(a)
print(b)

# x = np.zeros((5,5)) # 5by5 짜리 0으로 채워져있는 배열
# x = np.ones((3,2)) # 3 by 2 짜리 1로 꽉
# x = np.full((3,2),7) # 3 by 2 짜리 플롯타입말고 그냥 7로 꽉
x = np.eye(3) # 크기 3짜리 단위행렬 만들기 I 라고 쓰면 헷갈린다고 레전드 개발자 형님이 그냥 eye 이지랄로 해둠 ㄹㅈㄷ
print(x)