import seaborn as sns
import matplotlib.pyplot as plt


#인코딩
plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False


#데이터 준비
#total_bill,tip,sex,smoker,day,time,size
df = sns.load_dataset("tips")
#도화지 준비
fig, axes = plt.subplots(2,3,figsize=(12,8))

#hisplot
sns.histplot(data=df, x="total_bill", bins=20, kde=True, ax=axes[0,0]) #불편하잖어~

#boxplot
sns.boxenplot(data=df,x="day",y="total_bill",ax=axes[0,1])

#scatterplot
sns.scatterplot(data=df,x="total_bill",y="tip",hue="smoker",ax=axes[1,0])

#heatmap
c = df[["total_bill","tip","size"]].corr()
sns.heatmap(data=c, annot=True, cmap="coolwarm", fmt=".2f", ax=axes[1, 1])

#countplot 빈도수 쳌
sns.countplot(data=df,x="day",hue="sex",ax=axes[0,2])

#pairplot : 변수 쌍 전체 한번에
reslut = sns.pairplot(data=df)
reslut.savefig("reslut.png")
#결과확인
plt.show()
