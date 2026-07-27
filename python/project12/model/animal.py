class Animal:
    def __init__(self,x,y):
        self.name = x
        self.age = y
'''
    def __add__(self, other):                #magic 메서드 /Dunder함수
        return Animal()

    def __str__(self):                  #magic 메서드 /Dunder함수
        pass
    def __repr__(self):
        pass                         #magic 메서드 /Dunder함수
'''
class Bark:
    def __init__(self):
        print("멍멍")
