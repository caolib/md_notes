---
title: SpringBoot相关配置
date: 2024-01-07 13:10:42
categories: 
    - spring
    - java
tags: 
  - spring
cover: https://dogefs.s3.ladydaily.com/~/source/wallhaven/full/5g/wallhaven-5gr5m7.jpg?w=2560&h=1440&fmt=webp
stick: 955
---

# SpringBoot相关配置

## 1.[自定义项目LOGO](https://docs.spring.io/spring-boot/docs/current/reference/html/features.html#features.spring-application.banner)

在`resources`文件夹下新建一个`banner.txt`文件，加入相关内容即可，[艺术字生成网站](https://www.bootschool.net/ascii-art)

```txt
---------------+---------------
          ___ /^^[___              _
         /|^+----+   |#___________//
       ( -+ |____|    ______-----+/
        ==_________--'            \
          ~_|___|__
```

## 2. 跨域请求

添加此配置到`WebMvc`配置类中(推荐)，也可以在每个`Controller`类上添加注解`@CrossOrigin`

```java
@Configuration
public class WebMvcConfig implements WebMvcConfigurer {
    //允许所有跨域请求
    @Override
    public void addCorsMappings(CorsRegistry registry) {
        registry.addMapping("/**")
                .allowedOriginPatterns("*")
                .allowedMethods("*")
                .allowedHeaders("*")
                .allowCredentials(true);
    }
}
```

## 3. application配置文件

`application.yml`

```yaml
server:
  port: 8080

spring:
  profiles:
    active: dev
  main:
    allow-circular-references: true
  devtools:
    restart:
      enabled: true
      # 设置重启的目录
      additional-paths: src/main/java

# mybatis-plus配置
mybatis-plus:
  configuration:
    map-underscore-to-camel-case: true    #开启下划线自动转驼峰命名
  type-aliases-package: com.clb.pojo  #别名扫描
  mapper-locations: classpath:mapper/*.xml  #注册mapper
  global-config:
    banner: false
    db-config:
      id-type: auto

logging:
  level:
    com.clb: debug
  pattern:
    dateformat: MM-dd HH:mm:ss.SSS
```

`application-dev.yml`

```yaml
spring:
  config:
    activate:
      on-profile: dev
  datasource:
    driver-class-name: com.mysql.cj.jdbc.Driver
    url: jdbc:mysql://localhost:3306/mybatis?rewriteBatchedStatements=true
    username: root
    password: 123456
  data:
    redis:
      host: 192.168.0.88
      password: 123456
      port: 6379
      database: 0
```