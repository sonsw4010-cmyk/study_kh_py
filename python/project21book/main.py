#도서 관리
from book_manager import print_menu, scan_user_input,process

#등록
#목록조회
#상세조회
#삭제

print("======도서관리 프로그램=======")
while True:
    try:
        print_menu()
        num = scan_user_input()
        process(num)
    except Exception as e:
        print(e)



