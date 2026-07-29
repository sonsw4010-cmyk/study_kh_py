# 3by3 행렬
arr =[]
row = 3
col = 3
for i in range(row):
    x = []
    for j in range(col):
        x.append(0)
    arr.append(x)

arr[0][0] =100
arr[0][1] =90
arr[0][2] =80
arr[1][0] =10
arr[1][1] =20
arr[1][2] =30
arr[2][0] =70
arr[2][1] =60
arr[2][2] =50
for n in arr:
    print(n)

#총점이 제일 높은학생 이름이랑 총점을 출력
name = ["철수","맹구","짱구"]
subjects = ["국어","영어","수학"]
total_list = []

for i in range(3):
    total = 0
    for score in arr[i]:
        total += score
    total_list.append(total)

print("토탈리스트 : ",total_list)
idx =-1
top = 0
for i in range(3):
    if top < total_list[i]:
        top = total_list[i]
        idx = i
print("최고점수:",top," idx:",idx," 이름:",name[idx])

#과목별 평균 출력
#수학 : 점 , 영어: 점, 과학: 점
subject_averages = []

for i in range(col):
  subject_total = 0
  for j in range(row):
    subject_total += arr[j][i]  # 각 학생(행)의 특정 과목(열) 점수를 더함
  avg = subject_total / row  # 평균 계산
  subject_averages.append(avg)

for i in subject_averages:
    print(i)

for i in range(col):
  print(f"{subjects[i]}: {subject_averages[i]}점")

# 학생별 총점과 평균
Stu_avg = []
Stu_total = []

for i in range(col):
    student_averages = 0
    student_total = 0
    for j in range(row):
        student_total += arr[i][j]
        avg = student_total / row
    Stu_avg.append(avg)
    Stu_total.append(student_total)

for i in range(row):
    print(f"{name[i]} 총점:{Stu_total[i]},평균:{Stu_avg[i]}")

# 과목별 최고 점수와 해당 학생 이름
'''
for sub in range(col):  # 가로(과목) 기준 3번 반복
  top_score = -1
  top_student = ""

  for stu in range(row):  # 세로(학생) 기준 3번 반복 (총 9번 연산)
    if arr[stu][sub] > top_score:
      top_score = arr[stu][sub]
      top_student = name[stu]

  print(f"{subjects[sub]} 최고 득점자: {top_student} ({top_score}점)")
  '''
top_list = []
top_idx_list = 0
for i in range(col):
  top = -1
  top_idx = -1
  for j in range(row):
      if top < arr[j][i]:
        top = arr[j][i]
        top_idx = j
top_list.append(top)
top_list.append(top_list)
print(top_list)
print(top_list)

# 총점 최고득점자와 최저득점자 이름
for j in range(row):
    student_total_list = []
    for i in range(col):
        std_score = arr[i]
        total= std_score[0] + std_score[1] + std_score[2]
        student_total_list.append(total)
print(student_total_list)

top = -1
top_idx = -1
bottom = 301
bottom_idx = 0
for i in range(col):
    if top < student_total_list[i]:
        top = student_total_list[i]
        top_idx = i
    elif bottom > student_total_list[i]:
        bottom = student_total_list[i]
        bottom_idx = i
print(f"최고점수는 {name[top_idx]}학생이 총점 {top}점을 기록하였습니다.\n"
      f"최저점수는 {name[bottom_idx]}학생이 총점 {bottom}점을 기록하였습니다.")

# 평균 미만 출력 (평균 60점 미만)
for i in range(col):
    if Stu_avg[i] < 60 :
        print(f"{name[i]}학생은 평균미만(60점)인 {Stu_avg[i]}점 입니다")
# 과락자 출력 (1과목이라도 40점 이하인 경우)
for i in range(col):
    for j in range(row):
        if arr[i][j] < 40:
            print(f"{name[i]}학생, 40점 이하인 {arr[i][j]}점이 있어 과락입니다.")
