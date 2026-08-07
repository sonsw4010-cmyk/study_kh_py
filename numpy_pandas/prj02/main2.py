import numpy as np
#규칙이 있는 배열

# arange : 간격을 정할때 사용
a =np.arange(10)
a =np.arange(2,20,3) # 2부터 20까지 3칸씩 뛰면서 만들겠다
print(a)
# print(a.shape)
# print(a.ndim)
# print(a.size)

# linspace : 갯수를 정할때 사용
b = np.linspace(0,1,5) #0부터 1까지 5개 만들겠다 // 일정한 간격으로 만들어줌
print(b)
