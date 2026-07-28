#등록하기
from model.book import Book
book_list = []
def enroll_book():
    print("\n------도서등록-------")
    title = input("도서 제목 :")
    price = input("도서 가격 :")
    b = Book(title,price)
    book_list.append(b)
    print("등록 완료~")
#목록출력
def print_book_list():
    print("\n------도서목록-------")
    print("번호 | 제목")
    for idx,b in enumerate(book_list):    #enumerate >> 인덱스랑 같이 묶여있는 튜플 비스무리한 무언가로 나옴
        print(f"{idx} | {b.title}")
#조회
def print_book_one_by_number():
    print("\n------도서 조회-------")
    book_num = int(input("조회할 도서 번호 : "))
    b = book_list[book_num]
    print(b)
#삭제
def delete_book_two_by_number():
    print("\n------도서 삭제-------")
    book_num = int(input("삭제할 도서 번호 : "))
    del book_list[book_num]
    print("삭제 완료~")