---
title: git版本控制系统
date: 2024-3-25 21:45:03
categories: 
    - tools
tags: git
cover: https://dogefs.s3.ladydaily.com/~/source/wallhaven/full/3l/wallhaven-3lgrr3.jpg?w=2560&h=1440&fmt=webp
stick: 9999
---

# [Git](https://git-scm.com/)

## 介绍

> Git是一个开源的**分布式版本控制系统**，用于高效地处理从小到大的项目。Git由Linus Torvalds创建，用于管理Linux内核开发。与集中式版本控制系统不同，如CVS或Subversion，Git采用分布式版本库的方式，不需要服务器端软件支持。这使得源代码的发布和交流变得非常方便。Git的速度很快，特别适合大型项目的版本管理。

## 常用命令

Git的常用命令包括但不限于以下几个：

- `git init`：初始化一个Git仓库。
- `git clone [url]`：克隆一个仓库到本地。
- `git add [file]`：添加文件到暂存区。
- `git commit -m "[message]"`：提交更新，并附加一条提交信息。
- `git status`：查看仓库当前的状态，显示有变更的文件。
- `git push [alias] [branch]`：将本地分支的更新推送到远程仓库。
- `git pull [alias] [branch]`：从远程仓库拉取更新并合并到本地。
- `git branch`：列出所有本地分支。
- `git checkout [branch-name]`：切换到指定分支。
- `git merge [branch]`：合并指定分支到当前分支。

工作流程图

![image-20240325220023918](https://gitee.com/clibin/image-bed/raw/master/image-20240325220023918.png)

## 分支

 Git分支是一个非常强大的功能，它允许你在不同的开发线路上独立工作，而不会影响主线（通常是master分支）。这样，你可以在一个分支上开发新功能，而在另一个分支上修复bug，然后再将它们合并回主线。分支的用途包括：

- **功能开发和并行开发**：你可以在不同的分支上同时开发多个功能。
- **Bug修复和紧急修复**：为了不干扰主要开发，可以在单独的分支上进行bug修复。
- **版本发布和稳定的主分支**：保持主分支稳定，只有完全测试通过的代码才能合并。
- **实验性开发和试验性分支**：尝试新想法而不影响主分支。
- **多人协作和团队开发**：团队成员可以在各自的分支上工作，然后合并他们的更改。

假设你正在开发一个新功能，我们将其称为“feature-x”。你不希望这些更改影响主分支，因此你可以创建一个新分支并在其中工作。以下是步骤：

1. **创建新分支**：

   ```bash
   git branch feature-x
   ```

   这将创建一个名为`feature-x`的新分支。

2. **切换到新分支**：

   ```bash
   git checkout feature-x
   ```

   现在你在`feature-x`分支上工作。

3. **添加更改**： 在`feature-x`分支上进行更改后，使用以下命令将它们添加到暂存区：

   ```bash
   git add .
   ```

4. **提交更改**： 提交你的更改，并附加一条提交信息：

   ```bash
   git commit -m "Add new feature x"
   ```

5. **切换回主分支**： 完成开发后，切换回主分支：

   ```bash
   git checkout master
   ```

6. **合并分支**： 将`feature-x`分支的更改合并到主分支：

   ```bash
   git merge feature-x
   ```

7. **推送更改**： 如果你想将更改推送到远程仓库，使用：

   ```bash
   git push origin master
   ```

## 简化使用

将下面代码保存为py文件，就能直接运行python执行一些常用操作，注意`git glog`是我自定义的一个命令

```python
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
```

