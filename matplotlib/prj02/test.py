import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


#한글 , 마이너스 기호 깨짐방지
plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False
'''
총 식사 금액
팁금액
일행인원수
성별
흡연여부
요일
시간대

0. 데이터 파악해보기
1. total_bill 히스토그램
2. 요일별 total_bill 박스플롯
3. total_bill 와 tip 산점도 차트
4. 요일별 주문 건수 막대그래프
'''

# CSV 데이터 로드
df = pd.read_csv("tips.csv")

# 1. 상위 5개 행 확인
print(df.head())
# 2. 데이터 구조 및 결측치 확인
print(df.info())
# 3. 기초 통계량 확인
print(df.describe())

# 2행 2열의 서브플롯 생성 (전체 크기 설정)
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(14, 10))

#1번 그래프: total_bill 히스토그램
axes[0,0].hist(df["total_bill"], bins=20, color="skyblue", edgecolor="black")
axes[0,0].set_title("total_bill 히스토그램")
axes[0,0].set_xlabel("Total Bill0")
axes[0,0].set_ylabel("Count")

#2번 그래프: 요일별 total_bill 박스플롯
days = ["Thur", "Fri", "Sat", "Sun"]
data_by_day = [df[df["day"] == d]["total_bill"] for d in days]
axes[0,1].boxplot(data_by_day, tick_labels=days)
axes[0,1].set_title("요일별 total_bill 박스플롯")
axes[0,1].set_xlabel("Day")
axes[0,1].set_ylabel("Total Bill")

#3번 그래프: Total Bill vs Tip 산점도
for name, group in df.groupby("sex"):
  axes[1, 0].scatter(
      group["total_bill"], group["tip"], label=name, alpha=0.7, s=50
  )
axes[1,0].set_title("Total Bill vs Tip")
axes[1,0].set_xlabel("Total Bill")
axes[1,0].set_ylabel("Tip ($)")
axes[1,0].legend(title="Sex")

#4번 그래프: 요일별 주문 건수 막대그래프
day_counts = df["day"].value_counts().reindex(["Thur", "Fri", "Sat", "Sun"])
axes[1,1].bar(
    day_counts.index, day_counts.values, color="lightcoral", width=0.6
)
axes[1,1].set_title("Order Count by Day")
axes[1,1].set_xlabel("Day")
axes[1,1].set_ylabel("Order Count")

# 그래프 간격 조절 및 출력
plt.tight_layout()
plt.show()