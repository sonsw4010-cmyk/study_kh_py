class Pokomon():
    def __init__(self,name,atk,hp):
        self.name = name
        self.atk = atk
        self.hp = hp

    def __str__(self):
        return f"{self.name} {self.atk} {self.hp}"  #원래 리턴값은 무조건 하나만 가능한데 이거는 튜플로 묶어서 하나로 만든거임 그래서 됨 ㅅㄱㅇ
'''
    def printInpo(self):
        data = self.getInpo()
        print(data)
'''


