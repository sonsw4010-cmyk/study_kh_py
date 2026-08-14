import matplotlib.pyplot as plt
import numpy as np

#한글 , 마이너스 기호 깨짐방지
plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

rng = np.random.default_rng(42)
#data 준비
classA = rng.normal(60,15,100)
classB = rng.normal(70,10,100)
classC = rng.normal(80,5,100)

fig,ax =plt.subplots(figsize=(8,6))
ax.violinplot([classA,classB,classC],showmedians=True)
ax.set_xticks([1,2,3])
ax.set_xticklabels(["A","B","C"])
ax.set_ylabel("점수")

plt.show()