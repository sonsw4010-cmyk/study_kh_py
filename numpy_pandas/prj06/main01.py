#일주일 기온 통계
import numpy as np

temps = np.array([12, 15, 18, 14, 20, 22, 17])  # 월~일 기온(℃)

# 1. 평균 기온
reslut = np.mean(temps)
print("평균기온 :" ,reslut)
# 2. 가장 더운 날과 추운 날의 기온
reslut1 = np.max(temps)
reslut2 = np.min(temps)
print("가장더운날: ",reslut1,"C","가장 추운날 :","C",reslut2)
# 3. 기온의 표준편차
reslut3 = np.std(temps)
print("표준편차 :",reslut3)
# 4. 중앙값
reslut4 = np.median(temps)
print(reslut4)
# 5. 평균보다 더운 날은 몇번 있었나?
reslut5 = temps[temps > reslut]
print(len(reslut5),"번")