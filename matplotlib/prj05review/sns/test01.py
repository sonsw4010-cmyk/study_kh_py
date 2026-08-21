import  seaborn as sns
from matplotlib import pyplot as plt

titanic = sns.load_dataset("titanic")

print(titanic)
fig, axes = plt.subplots(2,3,figsize=(12,10))
sns.histplot(data=titanic,x="pclass",ax=axes[0,0])
sns.boxenplot(data=titanic,x="pclass", y="sex", ax=axes[0,1])
sns.scatterplot(data=titanic,x="fare", y="pclass", ax=axes[0,2])
sns.countplot(data=titanic,x="survived", ax=axes[1,0])
sns.heatmap(data=titanic[["pclass","survived","fare"]].corr(),ax=axes[1,1])
sns.pairplot(data=titanic)
plt.show()
