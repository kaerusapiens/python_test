#---------------------map(함수, 반복 가능한 객체)

numbers = [1, 2, 3, 4]

# 일반적인 함수 사용
def square(x):
    return x ** 2

squared_list = list(map(square, numbers))  # [1, 4, 9, 16]
print(squared_list)

#---------------------filter(조건을 정의하는 함수, iterable 객체)
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # 출력: [2, 4, 6]


#--------------------sorted함수
# sorted(iterable, key=None, reverse=False)
#   iterable: 정렬할 대상이 되는 순회 가능한 객체(리스트, 튜플, 문자열 등).
#   key: 각 요소를 정렬하기 전에 적용할 함수입니다. 이 함수는 각 요소에 대해 값을 반환하고, 이 반환된 값이 정렬 기준이 됩니다. 기본값은 None입니다.
#   reverse: True이면 내림차순으로 정렬하고, 기본값은 False로 오름차순 정렬입니다.
students = [("철수", 90), ("영희", 85), ("민수", 95)]
students_sorted = sorted(students, key=lambda x: x[1])  # 점수 기준 정렬
print(students_sorted)
# 출력: [('영희', 85), ('철수', 90), ('민수', 95)]

numbers = [4, 2, 3, 1]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # 출력: [1, 2, 3, 4]


#---------------------

squared_list = [x ** 2 for x in numbers]
print(squared_list)  # [1, 4, 9, 16]




