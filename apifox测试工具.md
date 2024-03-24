---
title: apifox测试工具
date: 2024-03-18 22:20:23
categories: 测试
tags: 
    - apifox
    - 测试
cover: https://dogefs.s3.ladydaily.com/~/source/wallhaven/full/2y/wallhaven-2y2q7y.jpg?w=2560&h=1440&fmt=webp
stick: 887
---

# [Apifox](https://blog.csdn.net/qq_63241030/article/details/136098717?spm=1001.2014.3001.5501)

## 登录自动更新token

> 问题：使用apifox测试接口时，令牌过期后，需要重新登录，然后复制粘贴替换全局变量的token，有点麻烦，而且不注意可能会复制错误，怎么实现运行登录接口后自动将返回数据中的token值更新，然后其他请求自动携带全新的token呢

### 1.给登录接口添加后置操作

> **1.1 打开项目的登录接口，添加该接口的后置操作**

![1](https://gitee.com/clibin/image-bed/raw/master/CopyQ.guHvRu.png)

> **1.2 随便设置一个变量名字，然后点击小箭头**

![2](https://gitee.com/clibin/image-bed/raw/master/edd94cadbfb44edbbdca3274e146e06a.png)

> **1.3 左边是返回结果的结构，书写jsonpath表达式 ，代表左边的json对象，然后就像访问对象属性一样写就可以了，最后看看提取结果和左边是不是对上了，最后点击确定保存，我的token是data中的token，所以是 `$.data.token`**

![img](https://gitee.com/clibin/image-bed/raw/master/bed066a49bd940879263f93412173baa.png)![点击并拖拽以移动](data:image/gif;base64,R0lGODlhAQABAPABAP///wAAACH5BAEKAAAALAAAAAABAAEAAAICRAEAOw==)

> **1.4 保存接口文档后测试接口**

![img](https://gitee.com/clibin/image-bed/raw/master/1ad4210461e440beaac3b0a749768d08.png)![点击并拖拽以移动](data:image/gif;base64,R0lGODlhAQABAPABAP///wAAACH5BAEKAAAALAAAAAABAAEAAAICRAEAOw==)

> **1.5 如果上面操作无误，点击右上角按钮可以看到在本地环境多了一个变量值token，并且值就是返回结果的token**

![img](https://gitee.com/clibin/image-bed/raw/master/63a8edb4bde94b9bb9954e05b32cb14a.png)![点击并拖拽以移动](data:image/gif;base64,R0lGODlhAQABAPABAP///wAAACH5BAEKAAAALAAAAAABAAEAAAICRAEAOw==)

### 2.设置项目所有接口的auth认证

> **2.1 如图依次点击，key的名字根据自己需要设置，value的值从环境变量读取**

![img](https://gitee.com/clibin/image-bed/raw/master/ffd06d59868d424f951575480b1c795d.png)![点击并拖拽以移动](data:image/gif;base64,R0lGODlhAQABAPABAP///wAAACH5BAEKAAAALAAAAAABAAEAAAICRAEAOw==)

> **2.2 读取变量选择之前设置的变量，确定后保存接口的修改**

![img](https://gitee.com/clibin/image-bed/raw/master/92030ead665042709df2f6533d8c25b3.png)![点击并拖拽以移动](data:image/gif;base64,R0lGODlhAQABAPABAP///wAAACH5BAEKAAAALAAAAAABAAEAAAICRAEAOw==)

> **3. 测试执行登录接口是否会自动设置token，可以执行登录接口后直接执行其他接口**

![img](https://gitee.com/clibin/image-bed/raw/master/906528f23ce64f4e967053adbe2be91c.png)![点击并拖拽以移动](data:image/gif;base64,R0lGODlhAQABAPABAP///wAAACH5BAEKAAAALAAAAAABAAEAAAICRAEAOw==)

每次修改完成后记得保存再运行，这样就能简单完成token的自动更换
