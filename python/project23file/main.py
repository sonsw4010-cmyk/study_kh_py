# # try:
# #     f = open("data.txt", "a", encoding="utf-8")
# #     f.write("기존거 남았고 추가")
# # finally:
# #     f.close()
# from tokenize import endpats
# from unittest import case
from book import Book
import json

def write_to_file():
    with open("output.txt", "w", encoding="utf-8")as f:
        title = input("title: ")
        price = input("price: ")
        book = Book(title, price)
        json.dump(book.to_dict(), f, ensure_ascii=False, indent=2)


def read_from_file():
    with open("output.txt", "r", encoding="utf-8")as f:
        d = json.load(f)
        print(d)
        book = Book.from_dict(d)
        print(book.title)
        print(book.price)


# with open("data.txt", "r", encoding="utf-8") as f:
#     for x in f:
#         print(x.strip())
while True:
    print("0. exit\n1. write\n2.read")
    num = int(input("메뉴 번호"))
    match num:
        case "0":
            break
        case 1:
            write_to_file()
        case 2:
            read_from_file()

#json