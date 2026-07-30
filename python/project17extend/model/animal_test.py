from model.animal import Dog, Frog, Cat, Animal, Dalamjwi  # 컨트롤 스페이스 해서 임포트 쉽게 가능

print("=====Animal=====")

a1 = Dog()
a2 = Cat()
a3 = Frog()
a4 = Dalamjwi()
print(a1)
print(a2)
print(a3)
print(a4)

a1.bark()  #부모 자식 둘다 같은 함수가 있으면 자식께 먼저 쓰임>>> 오버라이드(override)
a2.bark()
a3.bark()
a4.bark()