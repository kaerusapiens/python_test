#데코레이터 자체도 인자를 받는 경우


def repeat(n):  # 데코레이터의 설정값 (반복 횟수)
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(n):  # n번 반복
                print(f"({i+1}/{n}) 실행")
                result = func(*args, **kwargs)
            #return result  # 마지막 실행 결과 반환
        return wrapper
    return decorator

@repeat(3)  # 데코레이터에 직접 3을 전달!
def greet(name):
    print(f"안녕하세요, {name}님!")

greet("철수")