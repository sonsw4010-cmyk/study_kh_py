#함수를 맹글어보자! 비밀번호 함수 기릿
#4개의 연속된값은 안됨. @ 또는 ! 를 포함해야함
from operator import contains
'''
def is_vaild_PW(pw) :
    if len(pw)<4 :
        return False
    elif len(pw) >12:
        return False
    elif pw[0] == pw[1] == pw[2] ==  pw[3] == pw[4]  :
        return False
    elif contains(pw,"!") or contains(pw,"@") :
        return False
    else :
        return True
'''

def is_vaild_PW(pw) :
    if len(pw)<4 :
        return False

    if len(pw) >12:
        return False

    if pw[0] == pw[1] == pw[2] ==  pw[3] :
        return False

    if not (contains(pw, "!") or contains(pw, "@")):
        return False

    return True