import json
from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int

json_data = '{"name": "Alice", "age": 25}'
data_dict = json.loads(json_data)  # JSONを辞書に変換
user = User(**data_dict)  # 辞書を展開してUserオブジェクトに変換
print(user)  # User(name='Alice', age=25)
print(user.name)
print(user.age)