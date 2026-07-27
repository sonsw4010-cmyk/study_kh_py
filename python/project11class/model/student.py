#클래스 오브젝트는 대문자 스따뚜
class Student(object):
    def __init__(self, a, b):
        self.name = a
        self.score = b

    def __str__(self):
        return f'{self.name} 학생의 성적은 {self.score} 입니다.'