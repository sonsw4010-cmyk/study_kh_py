#list,dictionary,set,tuple
''''''
def function01():
    a = [1,2,3,4,5]
    a.append(100)
    a.append(200)
    print (a)
    print (a[1])
    print (a[-1])
    print (a[:4])
    print (a[::2])
    a.insert(1,102)
    a[0] = 123
    print (a) #list >> remove ,pop,del,sort(원본을 건들임)>sorted(싫으면 이거쓰셈 새로 만듦),reverse
    #a.sort()
    result = sorted(a)
    print (a)
    print (result)


def function02():
    print("=====dick======")
    person = {"name":"hong","age":18,"blood":"A"}  #set 이랑  dictionary 이랑 둘다 {}여서 헷갈림, 둘의 차이는 :임 >> {:}
    print (person)
    print (person["name"])
    print (person["age"])
    print (person["blood"])
    #print (person["mbti"])   #<<<없어서 오류남
    print(person.get("mbti","음성"))
    print(person.keys())
    print(type(person.keys()))
    print(person.values())
    print(person.items())
    print("age" in person)
    print("hong" in person)


def function02_1():
    x = {
        "p1" : {"name":"철수","age":20} ,
        "p2":  {"name":"유리","age":21} ,
        "p3":  {"name":"짱구","age":5}
    }
    print (x)

def function03():
    print("======set=======")
    x = {1,2,3}
    print (x)
    print(type(x))
    x.add(100)
    x.add(10)
    x.add(112)
    print(x)  #set은 순서가 없음 꼭 맨뒤로 줄서서 들어가는거 아님

    x = {1,2,3,4}
    y = {4,5,6}
    print(x|y) #합집합
    print(x&y) #교집합
    print(x-y) #차집합

def function04():
    x =10,20,30
    x[0] =123
    print(x[0])

function04()


