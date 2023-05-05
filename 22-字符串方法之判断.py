my_str = 'hello Python'

# 字符串是否以指定的字符开头，第二个参数表示开始的索引，第三个参数表示结束的索引
# withBool = my_str.startswith('hell')  # True

# withBool = my_str.startswith('ll', 2, 5)  # True

# 字符串是否以指定的字符结束，第二三个参数与 startswith 相同
# withBool = my_str.endswith('thon')  # True
# withBool = my_str.endswith('thons')  # Flase

# print(withBool)

# isalpha 字符串是否都由字母组成
print(my_str.isalpha())  # Flase
print(my_str.replace(' ', '').isalpha())  # True

# isdigit 字符串是否都由数字组成
print(my_str.isdigit())  # Flase
print(''.join(['11111']).isdigit())  # True

# isalnum 字符串是否都由字母或数字组成
print(my_str.isalnum())  # Flase
print('antelope92'.isalnum())  # True

# isspace 字符串是否都有空格组成
print(my_str.isspace())  # Flase
print(my_str[5:6].isspace())  # True
