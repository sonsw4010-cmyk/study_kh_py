import matplotlib.pyplot as plt
import numpy as np

#한글 , 마이너스 기호 깨짐방지
plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

fig,ax =plt.subplots(figsize=(8,6))
labels = ["공부시간", "출석", "수면", "성적"]
data = np.array([[ 1.00,  0.65, -0.30,  0.80],
                 [ 0.65,  1.00, -0.10,  0.55],
                 [-0.30, -0.10,  1.00,  0.20],
                 [ 0.80,  0.55,  0.20,  1.00]])

ax.imshow(data,cmap="coolwarm",vmin=-1,vmax=1)
ax.set_xticks(range(4))
ax.set_xticklabels(labels)
ax.set_yticks(range(4))
ax.set_yticklabels(labels)

for i in range(4):
    for j in range(4):
        ax.text(i,j,f"{data[i, j]}",ha="center",va="center",fontsize=15,color="white"if data[i, j] > 0 else "black")

plt.show()