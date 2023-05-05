# 元组是不可修改的数据
t1 = (10, 20, 30)

print(type(t1))  # <class 'tuple'>

t2 = (10,)

# 定义长度为1的元组时，需要在后面添加逗号，否则小括号会被当成操作符解析
print(len(t2), type(t2))  # <class 'tuple'>

t3 = (10)

print(type(t3))  # <class 'int'>
