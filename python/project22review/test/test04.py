# class,instance,attribute,method
# 상속

class Snack:  # [클래스] 붕어빵 틀(설계도) 역할
    def __init__(self):  # [메서드] 객체가 만들어질 때 자동으로 실행되는 생성자 함수
        self.a = 3  # [어트리뷰트] 이 객체가 가지는 데이터(변수 'a'에 3 저장)

    def hello(self):  # [메서드] 이 객체가 수행할 수 있는 동작(함수)
        pass

obj = Snack()  # [인스턴스] 설계도(Snack)를 바탕으로 메모리에 만들어진 실제 객체(obj)
print(obj.a)  # [어트리뷰트 접근] 객체(obj)가 가진 속성 'a'의 값을 가져와 출력 (결과: 3)