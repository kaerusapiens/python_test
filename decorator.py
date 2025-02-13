def my_decorator(func):
    def wrapper(*args, **kwargs):  # 함수의 모든 인자를 받을 수 있도록 설정
        print(f"함수 실행 전! 인자: {args}, {kwargs}")
        func(*args, **kwargs)  # 원래 함수 실행
        print("함수 실행 후!")  # 원래 함수의 반환값 유지
    return wrapper

@my_decorator
def add(a, b):
    print(a + b)

add(3, 5)  # add(3, 5)를 호출하면 wrapper(3, 5)로 실행됨