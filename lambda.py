#------------------lambda
#lambda 매개변수: 표현식
add = lambda a, b: a + b
print(add(3, 5))  # 출력: 8

# 람다를 변수없이 집적출력
print((lambda x: x + 10)(5))  # 출력: 15


#리스트와 사용
squared_list = list(map(lambda x: x ** 2, numbers))
print(squared_list)  # 출력: [1, 4, 9, 16]


numbers = [1, 2, 3, 4]
squared = [(lambda x: x ** 2)(x) for x in numbers]
print(squared)  # 출력: [1, 4, 9, 16]
