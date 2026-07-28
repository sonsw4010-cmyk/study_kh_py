class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def __str__(self):
        print("str함수가 호출됨")
        return f"[책] 제목: {self.title}, 가격: {self.price}"


    def __repr__(self):
        print("repr함수가 호출됨")
        return f"[책] 제목: {self.title}, 가격: {self.price}"
