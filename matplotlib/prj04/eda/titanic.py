import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

# 폰트 깨짐 방지
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

#데이터 로드
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url, index_col="PassengerId")
#데이터 파악
print(df.isna().sum())
#결측치 처리(Age,Cabin,Embarked)
df["Age"]=df["Age"].fillna(df["Age"].median())
df = df.drop(columns=["Cabin"])
df["Embarked"]=df["Embarked"].fillna(df["Embarked"].mode()[0])
#단변량 분석
# 생존/사망자 비율
# print(df["Survived"].value_counts(normalize=True)*100)
# 범주형 시각화
# fig, axes = plt.subplots(1,3,figsize=(15,5))
# axes[0].set_title("생존 여부")
# sns.countplot(x="Survived", data=df, ax=axes[0])
# axes[1].set_title("성별")
# sns.countplot(x="Sex", data=df, ax=axes[1])
# axes[2].set_title("객실 등급")
# sns.countplot(x="Pclass", data=df, ax=axes[2])

# 나이 시각화
# plt.figure(figsize=(5,5))
# sns.histplot(df["Age"],bins=30,kde=True)
# plt.title("나이")
# plt.show()

#이변량 분석 (성별에 따른 생존률 파악)
# fig, axes = plt.subplots(2,2,figsize=(12,10))
# axes[0,0].set_title("성별")
# sns.barplot(x="Sex", y="Survived", data=df,ax=axes[0,0])
# axes[0,1].set_title("객실 등급")
# sns.barplot(x="Pclass", y="Survived", data=df,ax=axes[0,1])
# df["AgeBand"]=pd.cut(df["Age"], bins=[0,12,18,40,60,100], labels=["아동","청소년","청년","중년","노년"])
# sns.barplot(x="AgeBand", y="Survived", data=df, ax=axes[1,0])

# 가족숫자에 따른 생존률 파악
# df["FamilySize"] = df["SibSp"] + df["Parch"] + 1
# df["FamilyBand"] = pd.cut(
#     df["FamilySize"],
#     bins=[0, 1, 4, 10],
#     labels=["1인가구", "소가족", "대가족"],
# )
# sns.barplot(x="FamilyBand", y="Survived", data=df, ax=axes[1,1])
# plt.show()
#상관관계
# print(df.info())
# cols = ["Survived", "Pclass","Age","SibSp","Parch","Fare"]
# cor = df[cols].corr()
# plt.figure(figsize=(10,8))
# sns.heatmap(cor, cmap="coolwarm", annot=True, fmt=".2f")
# plt.show()
#인사이트
'''
여성의 생존률이 남성보다 높다
객실 등급이 높을수록(숫자가 작을수록) 생존률이 높다
나이가 어린 아동의 경우 생존률이 높다
가속규모가 2~4 일 때 생존률이 높다
'''

#성별 + 객실등급에 따른 생존률 파악
# fig, axes = plt.subplots(2,2,figsize=(12,10))
# sns.barplot(x="Pclass", y="Survived", hue="Sex", data=df,ax=axes[0,0])
# plt.title("성별 + 객실등급에 따른 생존률 파악")

# result = df.groupby(["Sex","Pclass"])["Survived"].mean().unstack()
# plt.figure(figsize=[6,4])
# sns.heatmap(result,annot=True,cmap="YlGnBu",fmt=".2f")
# plt.title("성별 + 객실등급에 따른 생존률 파악")
# plt.show()

#탑승 항구에 따른 생존률 파악
# sns.barplot(x="Embarked", y="Survived", data=df,ax=axes[0,1])
# plt.title("탑승 항구에 따른 생존률 파악")

# result = df.groupby("Embarked")["Survived"].mean()
# plt.figure(figsize=(6,4))
# sns.barplot(data=df, x="Embarked", y="Survived",order=["C","Q","S"])
# plt.title("탑승 항구에 따른 생존률 파악")
# plt.show()
#
# result = pd.crosstab(df["Embarked"], df["Sex"])

#이름에 따른 생존률 파악
# df["Title"] = df["Name"].str.extract(" ([A-Za-z]+)\\.", expand=False)
#
# rare_titles = [
#     "Lady",
#     "Countess",
#     "Capt",
#     "Col",
#     "Don",
#     "Dr",
#     "Major",
#     "Rev",
#     "Sir",
#     "Jonkheer",
#     "Dona",
# ]
# df["Title"] = df["Title"].replace(rare_titles, "Rare")
# df["Title"] = df["Title"].replace(
#     {"Mlle": "Miss", "Ms": "Miss", "Mme": "Mrs"}
# )
#
# sns.barplot(x="Title", y="Survived", data=df, ax=axes[1, 0])
# axes[1, 0].set_title("이름에 따른 생존률 파악")

df["Title"]=df["Name"].str.extract(r",\s*([^\.]+)\.")
x = ["Ms","Miss","Mrs","Master"]
df["Title"].where(df["Title"].isin(x),"Rare")
result = df.groupby(["Title"])["Survived"].mean()
print(result)

#운임에 따른 생존률 파악
# df["FareBand"] = pd.qcut(
#     df["Fare"], q=4, labels=["매우저렴", "저렴", "비쌈", "매우비쌈"]
# )
# sns.barplot(x="FareBand", y="Survived", data=df,ax=axes[1,1])
# plt.title("운임에 따른 생존률 파악")
# plt.show()

# df["FareBand"] = pd.qcut(df["Fare"], q=3, labels=["저가", "중가", "고가"])
# result = df.groupby("FareBand")["Survived"].mean()
# print(result)
