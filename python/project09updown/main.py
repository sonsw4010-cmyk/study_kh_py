import random

from game.kh import judgeUpDown as abc  #(어디에 어떤파일에 뭐를 가져올거고 이름을 뭐로 바꾸겠다)

print("===== UP DOWN =====")

#1.정답 (랜덤) 숫자 준비하기
answer = random.randint(1,50)

while True:
    #2.유저한테 입력받기
    num =int(input("숫자: "))

    #3.판단하기 밑 결과출력
    result =abc(num,answer )  #빨간불에서 알트 엔터하면 해결책 추천됨(그리고 굵고 컨트롤 클릭하면 그함수 따라가짐 ㄹㅈㄷ)
    print(result)
    if result :
        break



