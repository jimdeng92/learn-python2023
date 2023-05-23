# 创建一个 [0, 1, 2, ... , 8, 9] 的列表

# while 循环
list1 = []

i = 0
while i <= 9:
    list1.append(i)
    i += 1

print(list1)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# for 循环
list2 = []

for i in range(10):
    list2.append(i)

print(list2)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 列表推导式
list3 = [i for i in range(10)]

print(list3)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
