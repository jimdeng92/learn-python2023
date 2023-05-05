user_list = ['Tom', 'Rose', 'Jedi']

# 使用下标
# user_list[0] = 'Jim'  # ['Jim', 'Rose', 'Jedi']

# reverse
# user_list.reverse()  # ['Jedi', 'Rose', 'Tom']

# sort
user_list.sort()  # 默认升序 ['Jedi', 'Rose', 'Tom']

print(user_list)

num_list = [1, 2, 3, 4, 7, 5, 21]

# num_list.sort()  # [1, 2, 3, 4, 5, 7, 21]

num_list.sort(reverse=True)  # 降序排列 [21, 7, 5, 4, 3, 2, 1]

print(num_list)
