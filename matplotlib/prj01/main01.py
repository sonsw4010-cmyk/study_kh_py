import matplotlib.pyplot as plt
import numpy as np

fig,ax = plt.subplots(figsize=(6, 4)) #fig = 도화지// 도화지 안에 들어가는건 엑시"즈"

arr = np.linspace(0,10,10)
ax.plot(arr,arr,marker='^',label='y=x',linestyle='--')
ax.plot(arr,arr*2,marker='o',label='y=2x',linestyle=':')
ax.plot(arr,arr*3,marker='s',label='y=3x')
ax.legend()
ax.grid(alpha=0.3)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Scatter plot')

plt.savefig('test.png')
plt.show()