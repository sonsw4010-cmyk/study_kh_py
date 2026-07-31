from dog import Dog

age = int(input("나이 :"))
if age < 0:
    print("나이를 거꾸로 먹네")
    raise Dog("임마 이거 완전히 시간을 달리는 소녀네")
print(age)
