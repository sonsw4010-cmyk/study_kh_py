import matplotlib.pyplot as plt
import numpy as np

#한글 , 마이너스 기호 깨짐방지
plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

# 박스플롯
    #data 준비
rng = np.random.default_rng(42)
classA = rng.normal(60,15,100)
classB = rng.normal(70,10,100)
classC = rng.normal(80,5,100)

fig,ax =plt.subplots(figsize=(8,6))
ax.boxplot([classA,classB,classC],tick_labels=["A","B","C"])
plt.show()