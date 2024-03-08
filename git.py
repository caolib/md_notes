import os

def show():
    print('---------------------------------------------------------')
    print('enter ---> 状态')
    print('1     ---> 添加')
    print('2     ---> 提交')
    print('3     ---> 推送')
    print('4     ---> 拉取')
    print('5     ---> 添加、提交、推送')
    print('6     ---> 日志')
    print('7     ---> 远程仓库')
    print('else  ---> 退出')
    print('---------------------------------------------------------')

while True:
    try:
        show()
        choice = int(input('chioce: '))
        if choice == None:
            os.system('git status')
        elif choice == 1:
            os.system('git add .')
        elif choice == 2:
            message = input('Enter your message: ')
            os.system(f'git commit -m "{message}"')
            print(f'message:{message}')
        elif choice == 3:
            os.system('git push')
        elif choice == 4:
            os.system('git pull')
        elif choice == 5:
            message = input('Enter your message: ')
            os.system(f'git add .')
            os.system(f'git commit -m "{message}"')
            os.system(f'git push')
            print(f'message:{message}')
        elif choice == 6:
            os.system('git glog')
        elif choice == 7:
            os.system('git remote -v')
        else:
            exit()
    except Exception as e:
        if isinstance(e, ValueError):
            os.system('git status')
        print('Invalid choice')