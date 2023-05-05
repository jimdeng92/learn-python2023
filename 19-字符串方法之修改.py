# replace/split/join
# replace(旧子串, 新子串[, 替换次数])
# split(子串[, 分割次数])
# join(列表)

mystr = 'python and antelope and itheima'

# replace
# 注意字符串的不可变性，旧字符并没有被修改
print(mystr.replace('and', 'or'))  # python or antelope or itheima 不填第三个参数表示全部替换
print(mystr.replace('and', 'or', 1))  # python or antelope and itheima

# split
print(mystr.split(' and '))  # ['python', 'antelope', 'itheima']
print(mystr.split(' and ', 1))  # ['python', 'antelope and itheima']

# join
# 注意 join 方法的使用方式与 JS 不同，它在 python 中是字符串的方法
print('...'.join(['a', 'b', 'c']))  # a...b...c
