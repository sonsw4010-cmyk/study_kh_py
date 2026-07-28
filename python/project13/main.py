'''
from model.book import Book


b1 = Book("긴키지방에 어느 장소에 관하여", "20000")
b2 = Book("학교괴담", "120000")
b3 = Book("조선왕조실록","50000")


print(b1.title)
print(b1.price)
print(b2.title)
print(b2.price)

print(b1)
info = b1.__str__()
print(info)


book_list = []
for book in range(3):
    title =input("title :")
    price =input("price :")
    b1 = Book(title,price)
    book_list.append(b1)



for book in book_list:
    print(book)


print(book_list[0])
print(book_list[1])
print(book_list[2])
print(book_list)
'''
#컨트롤 + 알트 + L 누르면 정렬됨 ㄹㅈㄷ
#도서관리 프로그램: 도서 등록,목록출력,상세조회(도서번호를 이용하여 조회),삭제 기능(도서번호를 이용하여 삭제)이 있는 도서관리 프로그램 작성
from view.book_view import print_menu, scan_menu_num, process

print("=======도서관리 프로그램=========")
while True:
    print_menu()
    x = scan_menu_num()
    is_exit = process(x)
    if is_exit :
        break