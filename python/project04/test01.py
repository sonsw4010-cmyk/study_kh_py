# 현재 연도를 2026이라고 할 때 사용자의 출생 연도를 입력받아 나이를 출력하세요.
# (만나이 ㄴㄴ, 연나이 ㅇㅇ)

#쉬프트 f6동시에 누르면 같은변수이름 동시 변경 가능

y = int(input("현재년도를 입력하세요:"))
current_year = y
x = int(input("출생년도를 입력하세요:"))

r_age = current_year-x

print(f"{current_year}년 기준 당신의 나이는 {r_age}세 입니다.")
