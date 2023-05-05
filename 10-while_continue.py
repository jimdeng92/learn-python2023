i = 0

while i < 5:
    if i == 2:
        print(f'第{i + 1}个苹果吃出了半个虫子，不吃')
        i += 1
        continue
    print(f'吃了第{i + 1}个苹果')
    i += 1
