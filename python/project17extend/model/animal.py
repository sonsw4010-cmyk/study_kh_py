class Animal:
    def __init__(self, name, category):
        self.name = name
        self.category = category


    def __str__(self):
        return f"{self.name} {self.category}"


class Dog(Animal):
    def __init__(self):
        super().__init__("강아지", "포유류")

    def bark(self):
        print("도그클래스 멍멍")


class Cat(Animal):
    def __init__(self):
        super().__init__("고양이", "포유류")

    def bark(self):
        print("캣클래스 야옹")


class Frog(Animal):
    def __init__(self):
        super().__init__("개구리", "양서류")

    def bark(self):
        print("프로그클래스 개굴")


class Dalamjwi(Animal):
    def __init__(self):
        super().__init__("다람쥐", "설치류")

    def bark(self):
        print("다람쥐클래스 찍찍스")
