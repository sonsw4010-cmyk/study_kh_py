# thread
import threading
import time

def f01():
    for i in range(10):
        print("kh")
        time.sleep(.1)

def f02():
    for i in range(10):
        print("hello")
        time.sleep(.1)

def f03():
    for i in range(10):
        print("world")
        time.sleep(.1)

t1 = threading.Thread(target=f01)
t2 = threading.Thread(target=f02)
t3 = threading.Thread(target=f03)

t1.start()
t2.start()
t3.start()
print("세카이노 오와리")