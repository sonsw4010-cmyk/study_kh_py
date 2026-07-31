from model.book import Book

book_list = []

def print_menu():
    print("-------menu----------")
    print("0. 프로그램 종료")
    print("1.도서등록")
    print("2.도서목록")
    print("3.도서조회")
    print("4.도서삭제")

def scan_user_input():
    return int(input("메뉴번호:"))


def process(num):
    match num:
        case 0:
            pass
        case 1:
            enroll_book()
        case 2:
            select_book_list()
        case 3:
            select_book_one()
        case 4:
            remove_book()

def enroll_book():
    print("도서 등록 시작!")
    t = input("title :")
    a = input("author :")
    book = Book(t,a)
    book_list.append(book)
    print("도서 등록 완료!")

def select_book_list():
    print("--------도서목록 조회---------")
    for idx,book in enumerate(book_list):
        print(f"{idx}. {book.title}")

def select_book_one():
    print("--------도서목록 상세조회---------")
    num = int(input("num :"))
    book = book_list[num]
    print(book)
def remove_book():
    print("--------도서삭제---------")
    num = int(input("num :"))
    del book_list[num]
    print("삭제완료!")