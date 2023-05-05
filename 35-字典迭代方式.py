person = {'name': 'Jim', 'age': 22, 'gender': '男'}

# 【key]
print(person['name'])

# get()
print(person.get('name'))
# is和==的区别 https://blog.csdn.net/liuweiyuxiang/article/details/89333878
print(person.get('id') is None)  # True
print(type(person.get('id')))  # <class 'NoneType'>

# keys()
print(person.keys())  # 一个可迭代的对象 dict_keys(['name', 'age', 'gender'])
print(type(person.keys()))  # <class 'dict_keys'>

for key in person.keys():
    print('key:', key)

# value()
print(person.values())  # 一个可迭代的对象 dict_values(['Jim', 22, '男'])
print(type(person.values()))  # <class 'dict_values'>

# items()
print(person.items())  # 一个可迭代的对象 dict_items([('name', 'Jim'), ('age', 22), ('gender', '男')])
print(type(person.items()))  # <class 'dict_items'>

for item in person.items():
    print(item)  # 一个由key和value组成的元组
