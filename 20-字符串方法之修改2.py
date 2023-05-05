mystr = 'hello world and itheima and Python'

# capitalize 将字符串的首个字符转为大写，其他均小写
# new_str = mystr.capitalize() # Hello world and itheima and python

# title 将字符串的每个单词的首字母大写
# new_str = mystr.title()  # Hello World And Itheima And Python

# upper 将字符串的所有字母均转化为大写
# new_str = mystr.upper()  # HELLO WORLD AND ITHEIMA AND PYTHON

# lower 将字符串的所有字母均转化为小写
# new_str = mystr.lower()  # hello world and itheima and python

# print(new_str)

mystr2 = ' my name is antelope '

# 删除左侧空白字符
# new_str2 = mystr2.lstrip() # ‘my name is antelope ’

# 删除右侧空白字符
# new_str2 = mystr2.rstrip()  # ‘ my name is antelope’

# 删除两侧的空白字符
new_str2 = mystr2.strip()  # ‘my name is antelope’
print(new_str2)
