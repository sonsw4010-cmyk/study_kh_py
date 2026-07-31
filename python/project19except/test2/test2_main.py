def f01():
    print("f01")
    try:
        f02()
    except Exception as e:
        print(e)
    print("1끝")

def f02():
    print("f02")
    raise Exception(f03())
    f03()
    print("2끝")

def f03():
    print("f03")
    try:
        f01()
    except Exception as e:
        print(e)
    print("3끝")


f01()
