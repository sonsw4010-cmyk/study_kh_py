import matplotlib.pyplot as plt
import numpy as np

# 1.한글 폰트 및 마이너스 깨짐 방지
plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

# 2.데이터 준비
month = ["1월", "2월", "3월", "4월", "5월", "6월"]
gangnam = [120, 135, 128, 150, 175, 210]  # 강남점
hongdae = [95, 110, 130, 125, 160, 185]   # 홍대점

# 3.평균 매출 계산 (두 지점 전체 평균)
total = gangnam + hongdae
total_avg = np.mean(gangnam + hongdae)
monthly_avg = [(g + h) / 2 for g, h in zip(gangnam, hongdae)]

# 4. 도화지준비
fig, ax = plt.subplots(figsize=(10, 6))

# 5. 꺾은선 그래프 그리기 (x축에 month, y축에 각각의 데이터 지정)
ax.plot(month, gangnam, marker='^', color='red', linewidth=2.5, label='강남점')
ax.plot(month, hongdae, marker='o', color='blue', linewidth=2.5, label='홍대점')

# 6. 평균선 추가
ax.plot(month, monthly_avg, marker='s', color='gray', linestyle='--', linewidth=1.5, label='월별 평균')

# 7. 최고 매출 지점 찾기 및 화살표 표시
# 강남점 6월이 210으로 가장 높다이
max_val = max(gangnam + hongdae)
max_month_idx = gangnam.index(max_val) # 5 (6월)
max_month = month[max_month_idx]

ax.annotate(f'최고 매출 {max_val}만원',  xy=(max_month_idx, max_val), xytext=(max_month_idx-2, max_val-10),arrowprops=dict(arrowstyle="->",color="red"),fontsize=13, fontweight='bold')

# 8. 제목, 축 이름 설정
ax.set_title(f"지점별 월별 매출 추이 (전체 평균: {total_avg:.1f}만원)", fontweight="bold",fontsize="20")
ax.set_xlabel("월", fontsize=12)
ax.set_ylabel("매출액 (만원)", fontsize=12)

# 9. y축 범위를 0부터 시작하도록 설정
ax.set_ylim(0)

# 10. 격자 표시
ax.grid(alpha=0.5)

# 11. 범례 표시
ax.legend()

# 12. 레이아웃 정리 및 이미지 파일로 저장
plt.tight_layout()
plt.savefig("result.png", dpi=300)

# 13. 화면에 출력
plt.show()