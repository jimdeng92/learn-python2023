t1 = (10, 20, 30)

# 索引查找
print(t1[2])  # 30

# index 查找，找到对应元素返回索引，没找到就报错
print(t1.index(20))  # 1
# print(t1.index('20'))  # ValueError

# count 统计元素在元组中出现的次数
print(t1.count(10))  # 1

# len 公共方法，返回元组的长度
print(len(t1))  # 3
