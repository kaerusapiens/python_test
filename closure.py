def outer_function(outer_var):
    # 외부 함수의 변수
    def inner_function(inner_var):
        # 내부 함수
        print(f"Outer variable: {outer_var}, Inner variable: {inner_var}")

    return inner_function  # 내부 함수를 반환

# outer_function을 호출해서 반환된 inner_function을 closure로 사용
closure = outer_function("Hello")
closure("World")  # 출력: Outer variable: Hello, Inner variable: World

# 크로저의 주요 특징은 내부 함수가 외부 함수의 변수에 접근하고 그 값을 기억한다는 점입니다. 이를 통해 상태를 유지하거, 특정 환경에 맞춘 동작을 할 수 있습니다.
# 크로저는 주로 함수형 프로그래밍에서 많이 사용되며, 상태를 유지하면서, 함수가 외부와 격리된 환경을 가질 수 있게 합니다.