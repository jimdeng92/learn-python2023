user_list = ['TOM', 'Jerry', 'Jedi']

input_name = input('请填写您要注册的账号：')

if input_name in user_list:
    print(f'您输入的账号{input_name}已被注册，请重新输入')
else:
    print(f'恭喜您，用户名可用')
