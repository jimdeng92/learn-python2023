set1 = {10, 20, 30, 40, 100}
# add 只能添加单一数据，并且无法重复添加
set1.add(200)
set1.add(100)

print(set1)  # {100, 20, 40, 10, 30, 200}

# update 可以批量添加数据，同样无法重复添加
set2 = {10, 20, 40, 90, 200}

set2.update([100, 200])  # {20, 90, 100, 40, 10, 200}

print(set2)

# in
set3 = {10, 20, 40, 90, 200}
print(10 in set3)  # True
print(10 not in set3)  # False
