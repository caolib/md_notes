---
title: npm、yarn 包管理器
date: 2024-03-27 13:37:44
categories: 
    - 前端
    - nodejs
tags: npm
cover: https://img2.imgtp.com/2024/04/26/6Yu6WOXx.png
stick: 99
---

## npm

### 简介

npm 由三个独立的部分组成：

- 网站
- 注册表（registry）
- 命令行工具 (CLI)

[*网站*](https://npmjs.com/) 是开发者查找包（package）、设置参数以及管理 npm 使用体验的主要途径。

*注册表* 是一个巨大的数据库，保存了每个包（package）的信息。

[*CLI*](https://docs.npmjs.com/cli/npm) 通过命令行或终端运行。开发者通过 CLI 与 npm 打交道。

------



### 下载nodejs

[Node.js下载](https://nodejs.org/en/download/)

下载后查看版本

```sh
node -v
```

------

### 安装路径设置

先查看当前缓存和全局安装包路径，默认在C盘

```sh
npm config get prefix
npm config get cache
```

设置为其他路径,路径自定义

```sh
npm config set prefix D:\npm\node_global
npm config set cache D:\npm\node_cache
```

### [设置淘宝镜像](https://npmmirror.com/)

```sh
npm config set registry https://registry.npmmirror.com
```

设置完成后可以查看npm全局配置

```sh
npm config list -g
```

输出信息中有这样一条信息`"user" config from C:\Users\onebot\.npmrc`,这就是npm的全局配置文件，也可以直接修改配置文件来配置

------

### 常用命令

1. 安装命令

- 根据现有脚手架初始化项目,例初始化一个vue项目

  ```sh
  npm create vue@latest
  ```

- 安装项目中所有依赖(项目中有package.json文件)

  ```sh
  npm install
  ```

- **安装模块**

  ```sh
  npm install 模块名
  ```

  在使用npm安装模块时，参数的使用会影响模块的安装方式和位置，以及如何在`package.json`文件中记录这些模块。以下是各参数的区别：

  - **无参数**：当你运行`npm install module_name`而不加任何参数时，npm5开始，默认行为与`--save`相同，即模块会被安装在本地`node_modules`目录下，并且模块的条目会被添加到`package.json`文件的`dependencies`字段中。
  - **-g 或 --global**：这个参数用于全局安装模块。全局安装的模块不会被添加到当前项目的`node_modules`目录或`package.json`文件中，而是安装在系统范围内的位置，这样你可以在任何地方使用它们。
  - **-S 或 --save**：这个参数将模块添加到`package.json`文件的`dependencies`字段中。这些依赖项是在生产环境中需要的，即在实际运行应用程序时需要的模块。
  - **-D 或 --save-dev**：这个参数将模块添加到`package.json`文件的`devDependencies`字段中。`devDependencies`通常用于开发环境，比如编译工具或测试框架，这些模块不会在生产环境中使用。

  简而言之，无参安装会将模块添加到`dependencies`，`-g`用于全局安装，`-S`用于生产环境依赖，而`-D`用于开发环境依赖                

- 卸载模块

  ```sh
  npm uninstall 模块 
  npm uninstall 模块 -g 
  npm uninstall 模块 -s 
  npm uninstall 模块 -d
  ```

  当您使用`npm uninstall`命令卸载模块时，可以通过添加不同的参数来改变命令的行为。以下是各个参数的解释：

  - `npm uninstall 模块`：从项目的`node_modules`目录中卸载指定的模块，并且会从`package.json`文件的`dependencies`字段中移除该模块的条目
  - `npm uninstall 模块 -g`：添加`-g`参数表示全局卸载模块。这将从全局安装位置卸载模块，而不是从当前项目中卸载。
  - `npm uninstall 模块 -D`：添加`-D`或`--save-dev`参数时，卸载操作会从`package.json`文件的`devDependencies`字段中移除模块的条目。这通常用于开发依赖，即那些只在开发过程中需要的模块

- 更新模块

  ```sh
  npm update express  # 更新最新版本
  npm update express@2.1.0  # 更新到指定版本
  ```

## [yarn](https://www.yarnpkg.cn/getting-started)

### 简介

Yarn是一个现代的包管理工具，它是**为了解决一些npm的缺陷**而被创建的。它由Facebook、Google、Exponent（现在为Expo.dev）、Tilde（Ember.js背后的公司）共同开发。Yarn提供了速度快、安全性高和跨平台一致性等优势



### 安装

```sh
npm install -g yarn
```

2、安装成功后，查看版本号： 

```sh
yarn --version
```



### 常用命令

#### 显示所有配置

```sh
yarn config list # 显示所有配置项
```

#### 设置淘宝镜像

```sh
yarn config set registry https://registry.npmmirror.com # 添加淘宝源
```

#### **安装模块**

`yarn install` 和 `yarn add` 命令都是用于管理项目依赖的 Yarn 包管理工具的命令，但它们的用途和行为有所不同

`yarn install` 命令用于安装 `package.json` 文件中列出的所有依赖项。当你克隆一个项目或者需要更新/安装其他开发者添加的依赖时，通常会运行这个命令。如果项目中有 `yarn.lock` 文件，Yarn 会使用该文件中锁定的版本来确保依赖的一致性。

```sh
yarn install
```

`yarn add` 命令用于将新的包添加到项目的依赖中。当你想要添加一个新的库或工具到你的项目时，你会使用这个命令。它会更新 `package.json` 和 `yarn.lock` 文件，以包含新添加的依赖项。

```bash
yarn add <package>
```

例如，如果你想要添加 `lodash` 作为项目依赖，你可以运行：

```bash
yarn add lodash
```

如果你想将依赖项添加到开发依赖（`devDependencies`），可以使用 `--dev` 标志：

```bash
yarn add <package> --dev
```

> 总结一下，`yarn install` 是用来安装所有已经在 `package.json` 中声明的依赖项，而 `yarn add` 是用来添加新的依赖项到你的项目中，并更新 `package.json` 和 `yarn.lock` 文件

#### 移除模块

移除后,自动更新package.json和yarn.lock

```sh
yarn remove <packageName>
```

#### 运行脚本

用来执行在 package.json 中 scripts 属性下定义的脚本

```sh
yarn run 
```

#### 缓存

列出已缓存的每个包 

```sh
yarn cache list 
```

返回 全局缓存位置 

```sh
yarn cache dir 
```

清除缓存

```sh
yarn cache clean 
```



