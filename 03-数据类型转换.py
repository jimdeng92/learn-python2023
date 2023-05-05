num1 = 1
num2 = 1.1
str1 = 'Python'
str2 = '22Python'
tuple1 = (1, 2, 3)
list1 = [1, 2, 3]

# 1 转为浮点数 1.0
print(type(float(num1)))
# 1.1 转为整型 1
print(int(num2))
print(type(int(num2)))

# 不是纯数字的字符串转为整型会报错
# print(int(str2))

# 元组与列表之间的相互转换
print(type(list(tuple1)))
print(type(tuple(list1)))
