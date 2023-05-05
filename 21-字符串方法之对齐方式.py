my_str = 'antelope'

# ljust 字符串左对齐，剩余字符使用 . 填充
# new_str = my_str.ljust(12, '.')  # antelope....

# rjust 字符串右对齐
# new_str = my_str.rjust(12, ',')  # ,,,,antelope

# center 字符串居中对齐
new_str = my_str.center(12, '\\')  # \\antelope\\

print(new_str)
