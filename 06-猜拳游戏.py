import random

list1 = ['石头', '剪刀', '布']

player = int(input('请出拳'))
computer = random.randint(0, 2)

player_fist = list1[player]

computer_fit = list1[computer]

if player + 1 == computer:
    print(f'玩家出的是{player_fist}，电脑出的是{computer_fit}，玩家胜！')
elif player == computer:
    print(f'玩家和电脑出的都是{computer_fit}，平局！')
else:
    print(f'玩家出的是{player_fist}，电脑出的是{computer_fit}，电脑胜！')
