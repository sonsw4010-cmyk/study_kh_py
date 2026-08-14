import matplotlib.pyplot as plt
import numpy as np

#한글 , 마이너스 기호 깨짐방지
plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

#data 준비
ratio = [25,2,2,4,7]
lang = ["pyton","c","cpp","java","rust"]

fig,ax =plt.subplots(figsize=(8,6))

#파이차트
ax.pie(ratio,labels=lang,autopct="%1.1f%%",startangle=90, counterclock=False) # %% 두개 쓰면 % 나옴 야미 / 스타트는 반시계방향으로 스따뚜//counterclock 쓰면 반전가능 정방향스따뚜
ax.set_title("pie chart")

plt.show()