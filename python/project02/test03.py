#dictionary 딕셔너리 // 중괄호로 구성, 키밸류값 중요

x = {}
'''
x["name"] = "지혜성"
x["age"] = 24 <<<중간에 추가도 가능
'''


x = {"name":"지혜성","age":24,"MBTI":"SEXY"} # 미리 넣기도 당연히 가능// 키값 매칭반드시

print(x)
print(type(x))
print(x["name"])
print(x["age"])

x["age"] = 5
print(x["age"]) # 값 변경하기
'''
del x["age"]
print(x)
print("age" in x) //위에서 삭제해서 거짓임
print(x["age"]) # 값 삭제하기 / 그러면 안뜸 에러남 수구요

'''