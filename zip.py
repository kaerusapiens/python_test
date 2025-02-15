

w = ["mon", "tue", "wed"]
f = ["coffee", "milk", "water"]

d= {x:y for x,y in zip(w,f)}
print(d)


# listのdict化
keys = ["名前", "年齢", "出身地"]
values = ["太郎", 30, "東京"]

person = dict(zip(keys, values))
print(person)  
# {'名前': '太郎', '年齢': 30, '出身地': '東京'}


#unpakcing
pairs = [('太郎', 30), ('花子', 25), ('健一', 35)]

names, ages = zip(*pairs)
print(names)  # ('太郎', '花子', '健一')
print(ages)   # (30, 25, 35)