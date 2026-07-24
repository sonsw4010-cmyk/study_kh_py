# 홀짝 판단하고 출력하기 사용자가 입력
from unittest import result


def num(x):
    if x%2 == 0:
        return "짝수"
    elif x%2 != 0:
        return "홀수"


x =int(input("숫자를 입력하세요:"))
result = num(x)
print(result)