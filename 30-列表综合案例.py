import random

teachers = ['1', '2', '3', '4', '5', '6', '7', '8']

classes = [[], [], []]

teacherNum = len(teachers)
classNum = len(classes)

while teacherNum > 0:
    num = random.randint(0, classNum - 1)  # 随机班级
    current = teachers.pop(0)  # 当前老师

    classes[num].append(current)  # 添加到当前班级

    teacherNum -= 1

print(classes)
