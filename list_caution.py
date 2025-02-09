#Python에서 리스트를 함수의 기본 인수로 사용하면 안 되는 이유
#✔ Python에서는 함수의 기본 인수 값이 함수 정의 시 한 번만 평가됨
#✔ 가변 객체(list, dict)를 기본 인수로 사용하면 참조가 유지되어 예기치 않은 동작 발생
#✔ 참조 전달(Reference Passing) 때문에 같은 리스트가 계속 사용됨

# 암묵적으로 비추천
def test_func(x, l=[]):
    l.append(x)
    return l
# 이렇게 쓰는것을 추천
def test_func(x, l=None):
    if l is None:
        l=[]
    l.append(x)
    return l


r = test_func(100)
print(r)

r = test_func(100)
print(r)