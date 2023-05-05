# 创建字典
# my_dict_1 = {'name': 'Jim', 'age': 30, 'gender': '男'}
# print(my_dict_1)

# 创建空字典的两种方式
# my_dict_2 = {}
# print(my_dict_2)
#
# my_dict_3 = dict()
# print(my_dict_3)

# 字典操作方法
# new_dict = {'name': '三年一班', 'students': 55, 'teacher': 'Tang'}
# new_dict['floor'] = 3
#
# print(new_dict)
#
# new_dict['teacher'] = 'Li'
#
# print(new_dict)

# 字典的删除方法
del_dict = {'name': 'Jim', 'age': 18}
# del del_dict # 直接删除变量，变量在后续代码中不再存在

# del del_dict['name']
# print(del_dict)  # {'age': 18} 删除字典的属性

# del_dict.clear()
# print(del_dict)  # {} 清空字典

# del_dict = {}
# print(del_dict)  # {} 重新赋值，但不建议这样使用

# del_dict = 1
# print(del_dict)  # 1 可以重新赋值为任何类型
