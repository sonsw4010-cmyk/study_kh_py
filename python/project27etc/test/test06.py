# str

s  = "  Hello, World~!  "
print(s)
# print(s.strip()) #공백제거
# print(s.lstrip())#왼쪽 공백제거
# print(s.rstrip())#오른쪽 공백제거
# print(s.lower())#소문자 변환
# print(s.upper())#대문자 변환
# print(s.replace("Hello", "python")) #치환 a를 b로
print(s.strip().startswith("H")) #.startswith >>> "뭐시기"로 시작하는지 확인하는 코드 0