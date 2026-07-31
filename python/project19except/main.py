#예외 처리
try:
    x = int(input("x :"))
    y = int(input("y :"))
    result = x/y
    print(result)
except Exception as e:
    print("아 몰라 에러임")
    print(e)
    print(type(e))
else:
    print("이게 에러가 안뜨네")
finally:
    print("결과는 알빠노고, 반드시 실행됨")
print("수구바위")


'''
except ZeroDivisionError:
    print("되겠냐?")
except ValueError:
    print("숫자만 쓰라고")
    이렇게 except 조건부로 여러게 써도 되는데
    except Exception: 처럼 부모클래스로 퉁치자
    
    except Exception as e: print(e) 이거는 에러 내용을 알수있음
    
'''