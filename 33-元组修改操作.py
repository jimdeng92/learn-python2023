t1 = (10, 20, 30, [40, 50])

t1[3][0] = 4

print(t1)  # (10, 20, 30, [4, 50])

# t1[3] = [60]  # TypeError 不支持修改

# 元组里的一维数据不支持修改，但是里面包含了复杂数据类型是可以修改
# 但不建议修改
# 此现象类似于 JS 中使用 const 赋值引用类型，内存保存的只是引用
