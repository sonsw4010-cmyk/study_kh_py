def getMemberName(x):
    if x == "에스파" :
        return ["카리나","윈터","닝닝"]
    elif x == "빅뱅" :
        return ["지디","태양","탑"]
    elif x == "프로미스나인" or "프미나" :
        return ["채영","지원","하영"]
    else :
        print("그런건 없습니다")

a = getMemberName(input())
print(a)
