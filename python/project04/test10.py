# Python 점수와 Java 점수를 입력받으세요.
#
# 다음 조건을 모두 만족해야 통과입니다.
#
# - Python 60점 이상
# - Java 60점 이상
# - 두 과목 평균 70점 이상

p,j=int(input("파이썬점수:")),int(input("자바점수:"))
s = p+j/2
print("합격여부:", p>=60 and j>=60 and s>=70 )