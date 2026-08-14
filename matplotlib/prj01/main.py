# import 및 글자 깨짐 처리
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

#데이터준비 (x,y 좌표세트)
x = np.linspace(1,2,10)
y = x*2

#도화지,차트 준비
fig,ax = plt.subplots(figsize=(8, 6))


#차트 꾸
ax.plot(x, y, marker='o', markersize=15, color='red', linewidth="15",alpha = 0.5)
ax.set_title("차트 쿠쿠",fontweight="bold",fontsize="20")
ax.set_xlabel("x")
ax.set_ylabel("y")
plt.show()