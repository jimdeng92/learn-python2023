i = 1

# else 表示 while 循环正常结束之后要执行的代码
# while i <= 5:
#     print('媳妇儿，我错了')
#     i += 1
# else:
#     print('媳妇儿原谅我了')

# break 不属于正常结束循环，else中的代码不会被执行
# while i <= 5:
#     if i == 3:
#         break;
#     print('媳妇儿，我错了')
#     i += 1
# else:
#     print('媳妇儿原谅我了') # break 退出循环 else 不执行

# continue 正常结束循环可以执行else的代码
while i <= 5:
    if i == 5:
        print('这遍说的不够真诚')
        i += 1 # 注意continue也需要自增1
        continue
    print('媳妇儿，我错了')
    i += 1
else:
    print('媳妇儿原谅我了') # break 退出循环 else 不执行
