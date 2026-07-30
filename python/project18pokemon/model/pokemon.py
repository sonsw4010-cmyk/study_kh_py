'''
class Pokomon():
    def __init__(self,name,atk,hp):
        self.name = name
        self.atk = atk
        self.hp = hp

    def attack(self, target):
        target.hp -= self.atk
        print(f'"{self.name}"가 "{target.name}"를 공격!')
        print(f"남은 체력 -> {target.name}: {target.hp}\n")

class Charmander(Pokomon):
    def __init__(self):
        super().__init__("파이리",100,1000)
class Bulbasaur(Pokomon):
    def __init__(self):
        super().__init__("이상해씨",100,1000)
class Squirtle(Pokomon):
    def __init__(self):
        super().__init__("꼬부기",100,1000)
'''
from abc import abstractmethod, ABC


class Pokemon(ABC):
    def __init__(self,name,max_hp,atk,arm):
        self.name = name
        self.max_hp = max_hp
        self.hp = self.max_hp
        self.atk = atk
        self.arm = arm
    def __str__(self):
        return f"{self.name}/,{self.max_hp}"
    def tackle(self,enemy):
        print(f"가랏 {self.name}!\n {enemy}에게 몸통박치기!")
        dmg = self.atk -enemy.arm
        if dmg < 1:
            print("효과가 없는것같다")
            dmg = 1
            enemy.hp -= dmg
        enemy.hp -= self.atk
    @abstractmethod
    def skill(self,enemy):
        pass

    def is_dead(self):
        return self.hp <= 0


class Pikachu(Pokemon):
    def __init__(self):
        super().__init__("피카츄",100,10,3)
    def skill(self,enemy):
        print(f"{self.name}, {enemy.name}한테 백만볼트!!")
        dmg = self.atk * 2
        enemy.hp -= dmg
class Lizard(Pokemon):
    def __init__(self):
        super().__init__("파이리",80,12,2)
    def skill(self,enemy):
        print(f"{self.name}, {enemy.name}한테 화염방사!!")
        dmg = self.atk * 3 - enemy.arm
        enemy.hp -= dmg

class Turtle(Pokemon):
    def __init__(self):
        super().__init__("꼬부기",110,4,10)
    def skill(self,enemy):
        print(f"{self.name}, {enemy.name}한테 물대포!!")
        dmg = self.atk * 2 - enemy.arm
        enemy.hp -= dmg
        self.hp = int(round(dmg* 0.3 , 0))