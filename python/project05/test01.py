#if

if True:
    print("hello world")


if False:
    print("hello world")


x= 10>3

if x:
    print("hello world")

if True:                   #실행됨
    print("hello")

print("world")             #따로나옴

if False:                  #실행안됨
    print("hello")

print("world")

if True:                   #둘다 나옴
    print("hello")
    print("world")