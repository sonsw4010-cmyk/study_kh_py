#파일 읽기
import csv

with open("sales.csv", "r",encoding="utf-8") as f:
    reader = csv.DictReader(f)
    data = list(reader)

#전체 매출
total = 0
for row in data:
    total += int(row["단가"])*int(row["수량"])

#메뉴별 판매금액
qty_by_menu = {}
for row in data:
    x = row["메뉴"]
    y = row["수량"]
    z = row["단가"]
    #qty_by_menu[x] +=y 는 x값이 없어버리면 안돌아간다 밑에처럼 지정해줘야 돌아감
    qty_by_menu[x] = qty_by_menu.get(x,0)+int(y)*int(z)

#카테고리별 매출 = 이거 메뉴별 하는거랑 똑같다고함
#베스트메뉴
best_menu = ""
max_value = -1
for k,v in qty_by_menu.items():
    if max_value < v:
        max_value = v
        best_menu = k
#베스트 카테고리


#월별 매출
sales_by_month = {}
for row in data:
    k = row["날짜"][0:7]
    result = int(row["수량"]) * int(row["단가"])
    sales_by_month[k] = sales_by_month.get(k,0) + result
#리포트파일 저장
with open("report.csv", "w",encoding="utf-8") as f:
    f.write("=====kh카페 매출 리포트(2025 1분기)=====\n\n")
    f.write(f"[전체매출]{total:,}원\n\n")
    for k,v in qty_by_menu.items():
        f.write(f"{k}:{v}원\n")