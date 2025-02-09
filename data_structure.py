##############
###딕셔너리####
##############

data = {"name": "Alice", "age": 25, "city": "Seoul"}

#--키를 통해 값출력
print(data["name"])   # "Alice"
print(data.get("age"))  # 25 (key가 없을 경우 None 반환)

#--모든 키,값 가져오기기
print(data.keys())   # dict_keys(['name', 'age', 'city'])
print(data.values()) # dict_values(['Alice', 25, 'Seoul'])
print(data.items())  # dict_items([('name', 'Alice'), ('age', 25), ('city', 'Seoul')])


##############
###dict[str,list[str]]####
##############
# 딕셔너리 안에 리스트
my_dict_of_lists = {"numbers": [1, 2, 3], "letters": ["a", "b", "c"]}

# 특정 리스트의 요소에 접근
print(my_dict_of_lists["numbers"][0])  # 1


# for 루프를 이용해 모든 리스트와 요소 순회
for key, values in my_dict_of_lists.items():
    print(f"{key}: {values}")
    for value in values:
        print(value)


################
###list[dict[str,Any]]###
################

people = [
    {"name": "Alice", "age": 25, "city": "Seoul"},
    {"name": "Bob", "age": 30, "city": "Busan"},
    {"name": "Charlie", "age": 22, "city": "Incheon"}
]

print(people[0]["name"])  # "Alice"
print(people[1]["age"])   # 30

##############
###리스트####
##############

lst = ["Apple", "Banana", "Cherry"]

bananas = [item for item in lst if item == "Banana"]

print(lst[0])   # "Apple"
print(lst[-1])  # "Cherry" (뒤에서 첫 번째)

print(lst[0:2])  # ['Apple', 'Banana']
print(lst[:2])   # ['Apple', 'Banana'] (처음부터 2개)
print(lst[1:])   # ['Banana', 'Cherry'] (1번 인덱스부터 끝까지)




##############
####집합######
#집합은 hashable즉,immutable값만 넣을 수 있음
##############

s = {"Apple", "Banana", "Cherry"}

# 랜덤하게 하나 가져오면서 제거
item = s.pop()  
print(item)

#리스트로 반환하여 인덱싱으로가져오기
s_list = list(s)
print(s_list[0])

