---
title: nacos从入门到入土
date: 2024-03-16 18:42:42
categories: 后端
tags: 
  - springcloud
  - nacos
cover: https://dogefs.s3.ladydaily.com/~/source/wallhaven/full/l8/wallhaven-l8gg1r.jpg?w=2560&h=1440&fmt=webp
stick: 478
---

# quickstart

## 下载

[Nacos Server 下载 | Nacos](https://nacos.io/download/nacos-server/#稳定版本)

## 启动

解压缩后在`bin`目录下有几个脚本，`startup`就是启动脚本,默认都是集群`cluster`方式启动,也可以使用单机`standalone`模式启动

1. 第一种方法，添加启动参数，打开控制台，输入：

   ```sh
   startup -m standalone
   ```

2. 第二种方法，复制一份`startup.cmd`文件，修改启动模式

   ```sh
   export MODE="standalone"
   ```

3. 我表示：在`terminal`中添加一个powershell的配置，设置启动目录为nacos的bin目录，修改startup为nacos

   ![image-20240316202535951](https://raw.githubusercontent.com/TankingCao/picx-images-hosting/master/image-20240316202535951.png)

启动后默认端口为`8848`，可以在`conf/application.properties`文件中修改`server.port`

```properties
server.port=8888
```

浏览器打开`http://localhost:8848/nacos`即可看到nacos界面

![image-20240316203105872](https://s2.loli.net/2024/03/16/Q3jGhpuLe7iU4Kg.png)

## 导入依赖

```xml
<!--nacos-->
<dependency>
    <groupId>com.alibaba.cloud</groupId>
    <artifactId>spring-cloud-starter-alibaba-nacos-discovery</artifactId>
    <version>2.2.5.RELEASE</version>
</dependency>
```

## 添加配置

添加nacos地址与当前项目的应用名称，默认是单机模式

```yml
spring:  
  cloud:
    nacos:
      server-addr: localhost:8848
  application:
    name: book-service
```

## 注册服务

启动项目，可以看到当前项目服务已经注册到nacos

![image-20240316204044294](https://s2.loli.net/2024/03/16/uUS8oGh4OliKAVF.png)



> to be continued……
