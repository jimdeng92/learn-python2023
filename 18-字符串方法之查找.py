# index() find() count() rindex() rfind()

mystr = 'hello world and itcast and antelope'
# index()
# print(mystr.index('and'))  # 12
# print(mystr.index('ands'))  # 找不到直接报错
# print(mystr.index('and', 15, 30))  # 23 index(字串[，开始索引[，结束索引]])

# find()
# find 方法与 index 使用方法相同，但是 find 方法在找不到的情况下返回 -1
# print(mystr.find('and'))  # 12
# print(mystr.find('and', 15, 30))  # 23
# print(mystr.find('ands'))  # -1

# count()
# 统计出现的次数
# print(mystr.count('and'))  # 2
# print(mystr.count('ands'))  # 0 找不到返回 0

# rindex()
# 从右侧开始查找
# print(mystr.rindex('and'))  # 23
# print(mystr.rindex('and', 15))  # 23
# print(mystr.rindex('ands'))  # 报错

# rfind()
print(mystr.rfind('and'))  # 23
print(mystr.rfind('and', 15))  # 23
print(mystr.rfind('ands'))  # -1
