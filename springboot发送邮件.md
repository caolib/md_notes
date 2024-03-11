---
title: SpringBoot发送邮件
date: 2024年3月3日17:45:58
categories: 
    - java
    - spring
tags: 
  - 邮件
cover: https://dogefs.s3.ladydaily.com/~/source/wallhaven/full/kx/wallhaven-kxj3l1.jpg?w=2560&h=1440&fmt=webp
stick: 955
---

# SpringBoot发送邮件

## 导入依赖

```xml
<!-- 邮件依赖 -->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-mail</artifactId>
</dependency>
```

## 添加配置

```yml
spring:
  mail:
    # qq邮箱的host
    host: smtp.qq.com
    # 端口，固定的
    port: 465
    # 发件人的邮箱
    username: 1265****79@qq.com
    # qq邮箱服务的授权码
    password: etj*******afh
    test-connection: true
    properties:
      mail:
        smtp:
          ssl:
            enable: true
```

## 测试发送

```java
@SpringBootTest
class MailApplicationTests {
    @Autowired
    private JavaMailSender javaMailSender;

    @Test
    public void senderMail() {
        SimpleMailMessage message = new SimpleMailMessage();
        // 发件人 你的邮箱
        message.setFrom("12******9@qq.com");
        // 接收人 接收者邮箱
        message.setTo(new String[]{"tan*****@gmail.com"});
        //邮件主题
        message.setSubject("hello");
        //邮件内容
        message.setText("test");

        javaMailSender.send(message);
    }
}
```