#(*)를 붙이면 개수가 정해지지 않은 여러 개의 값을 튜플 형태로 한 번에 받을 수 있습니다.
#(**)를 붙이면 키워드 인자들을 딕셔너리(dictionary) 형태로 한 번에 받습니다.
def f01(a,b,*c,**d):
    print("f01슛")
    print(a)
    print(b)
    print(c)
    print(d)


f01("에이","비","씨","디","ㅋㅋㅋ",age=20,height=183)

#함수 힌트(+변수에도 가능함)
#매매변수,리턴타입,(+일반 변수에도 가능)
#def 함수이름(매개변수 : 타입힌트) -> 리턴타입힌트
# x: 타입힌트 =10 이렇게도 가능
'''
def f01(a:int,b:float,c:str,d:bool)->float :
    return "hi"

def f01(a:list,b:dict,c:tuple,d:set):
    return "hi"

def f01(a:list[int],b:dict[str,int],c:tuple[int,int],d:set[str]):
    return "hi"

#여러타입 힌트가능
def f01(a:int|str):
    return "hi"

#값이 없을수도 있음
def f01(x:None)->str|None:
    return "hi"
'''
#기본값
def f01(x="apple"):
    return "hi"
#변수에 함수를 담을수있다
def f01():
    return "hi"
x = f01 #괄호 없어야함 ,있으면 그냥 호출하는거임

#가변인자(*은 여러값을 받을수있고,**는 딕셔너리 형태로 받을수있음/매개변수 지정시에 순서를 조심해서 사용)
def f01(*x,**y):
    return "hi"