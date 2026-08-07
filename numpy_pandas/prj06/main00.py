import numpy as np

scores = np.array([[85,90,100], [70, 60, 50], [95, 88, 92],[40,55,65],[100,100,80]])
names = ["가","나","다","라","마"]
'''
#학생별 총점
reslut01 = np.sum(scores, axis=1)
print(reslut01)

#과목별 총점
reslut02 = np.sum(scores, axis=0)
print(reslut02)

#과목별 평균
reslut03 = np.mean(scores, axis=0)
print(reslut03)

#1등찾기 ( 총점이 제일 높은 학생 이름)
reslut04 = names[np.argmax(np.sum(scores, axis=1))]
print(reslut04)
'''
#60점 미만인 친구찾기
reslut05 = names[np.argmin(np.sum(scores, axis=1))]
print(reslut05)

