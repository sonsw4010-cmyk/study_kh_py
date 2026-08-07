#data.csv 파일연결 (쓰기모드)
import csv
def f01()->None:
    #,newline='' 이거는 , end='' 같은거임
    with open("data.csv","w",encoding="utf-8",newline='') as f:
        writer = csv.writer(f)
        '''
        writer.writerow([111,222])
        writer.writerow([333, 444])
        writer.writerow([555, 666])
        '''
        #writer.writerow()대신 s 붙여서 writer.writerows()를 사용하면 2차원 배열을 만들수가 있슴메
        writer.writerows([["name","age","city"],
                          ["홀길동",20,"서울"],
                          ["심청이",15,"부산"]])

# w:쓰기모드 r:읽기모드
def f02()->None:
    with open("data.csv","r",encoding="utf-8") as f:
        '''
        #한줄 읽어오기
        content = f.readlines()
        print(content)

        print(f.read())
        '''
        #한 행씩 데이터 출력하기
        x = csv.reader(f)
        for row in x:
            print(row)
#dict 기반 쓰기
def f03()->None:
    data = [
        {"name":"홍길동","age":20,"city":"서울"},
        {"name":"심청이","age":15,"city":"부산"},
            ]
    with open("data.csv","w",encoding="utf-8",newline="") as f:
        writer = csv.DictWriter(f,fieldnames=["name","age","city"]) #이거는
        '''
        이렇게 써도 됨 똑같은 것 , 취차
        fieldnames = ["name","age","city"]
        writer = csv.DictWriter(f,fieldnames=fieldnames)
        '''
        writer.writeheader()
        writer.writerows(data)
        print(writer)

#dict 기반 읽기
def f04()->None:
    with open("data.csv","r",encoding="utf-8")as f:
        x = csv.DictReader(f)
        for row in x:
            print(row)


f03()
