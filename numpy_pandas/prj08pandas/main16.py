import pandas as pd

# 직원 데이터
emp = pd.DataFrame({
    "이름": ["가영", "나은", "다희", "라온", "마루", "바다", "사랑"],
    "부서코드": ["D01", "D02", "D01", "D03", "D02", "D05", "D01"]
})

# 부서 데이터
dept = pd.DataFrame({
    "부서코드": ["D01", "D02", "D03", "D04"],
    "부서명": ["개발팀", "영업팀", "인사팀", "총무팀"]
})

reslut = pd.merge(emp, dept,on="부서코드",how="outer") #merge 서로다른 데이터테이블 2개를 병합하잇 / on을 쓰면 쓴걸로 찾아주고 없으면 알아서 같은걸로 찾아줌
print(reslut)