'''
x = {"철수":100,"유리":95,"짱구":5}

print(x)
'''


s1name = "철수"
s1score = 100

s2name = "유리"
s2score = 95

s3name = "짱구"
s3score = 5

print(f"{s1name}학생의 점수는 {s1score}점 입니다")
print(f"{s2name}학생의 점수는 {s2score}점 입니다")
print(f"{s3name}학생의 점수는 {s3score}점 입니다")


std_name_list = ["홍","박","사"]
std_num_list = [100,100,91]

for i in range(0,3):
    print(f"{std_name_list[i]}학생의 점수는 {std_num_list[i]}점 입니다")


std01={"name":"손","score":100}
std02={"name":"흥","score":200}
std03={"name":"민","score":300}
print(f"{std01["name"]}학생의 점수는 {std01["score"]}점 입니다")
print(f"{std02["name"]}학생의 점수는 {std02["score"]}점 입니다")
print(f"{std03["name"]}학생의 점수는 {std03["score"]}점 입니다")

std_list = [
    {"name":"박","score":100},
{"name":"지","score":200},
{"name":"성","score":300}
]

for std_info in std_list:
    print(f"{std_info["name"]}학생의 점수는 {std_info["score"]}점 입니다")