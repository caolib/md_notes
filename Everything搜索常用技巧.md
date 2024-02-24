---
title: Everything搜索常用技巧
date: 2024-02-18 15:18:12
tags:
  - everything
  - 搜索
categories:
  - tools
cover: https://dogefs.s3.ladydaily.com/~/source/wallhaven/full/d6/wallhaven-d6dvdl.png?w=2560&h=1440&fmt=webp
stick: 700
---

# 各种带条件搜索

## 1.指定文件后缀

搜索文件名，并且==要求后缀==，假设要搜索 名称包含`main`的所有`java`文件,可以搜索

> [!note] 
>
> `main ext:java `
>
> ext:java 就是指定后缀名，这个条件和main条件顺序随意，==注意中间要有一个空格==

## 2.指定文件路径

搜索文件，并且要求==该文件包含指定路径==，假设要搜索`base.css`文件，并且该文件路径中包含`typora`

> [!note]
>
> `base.css path:typora`
>
> 使用`path`指定文件包含的路径



更多用法见[voidtools](https://www.voidtools.com/zh-cn/)
