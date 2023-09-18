---
title: Spring常用注解
date: 2023-08-31 17:08:15
categories: 
    - java
    - spring
tags: 
    - java
    - spring
---

# **spring相关笔记**

## 常用依赖

```xml
<dependencies>
    <dependency>
        <groupId>org.springframework</groupId>
        <artifactId>spring-core</artifactId>
        <version>6.0.11</version>
    </dependency>
    <dependency>
        <groupId>org.springframework</groupId>
        <artifactId>spring-context</artifactId>
        <version>6.0.11</version>
    </dependency>
    <dependency>
        <groupId>org.junit.jupiter</groupId>
        <artifactId>junit-jupiter</artifactId>
        <version>RELEASE</version>
        <scope>test</scope>
    </dependency>
</dependencies>

```

## 常用xml文件中的spring约束

```xml
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:context="http://www.springframework.org/schema/context"
       xmlns:aop="http://www.springframework.org/schema/aop"
       xsi:schemaLocation="
       http://www.springframework.org/schema/beans
       http://www.springframework.org/schema/beans/spring-beans.xsd
       http://www.springframework.org/schema/context
       http://www.springframework.org/schema/context/spring-context.xsd
       http://www.springframework.org/schema/aop
       http://www.springframework.org/schema/aop/psring-aop.xsd
">

</beans>
```



## maven配置文件加载

```xml
    <build>
        <resources>
            <resource>
             <directory>src/main/resources</directory>
                <includes>
                    <include>**/*.properties</include>
                    <include>**/*.xml</include>
                </includes>
                <filtering>true</filtering>
            </resource>
            <resource>
                <directory>src/main/java</directory>
                <includes>
                    <include>**/*.properties</include>
                    <include>**/*.xml</include>
                </includes>
                <filtering>true</filtering>
            </resource>
        </resources>
    </build>
```





## 注解说明

1. **@Autowired**: 自动装配

   - 默认使用byType方式实现，找不到就使用byName方式，要求这个对象必须存在
   - 如果Autowired不能唯一装配上属性，则需要通过 @Qualifier(value = "xxx")限定是哪个id

2. **@Nullable**: 字段标记了这个注解，说明字段可以为null

3. **@Value**: 放在字段上面，属性注入值

4. **@Resource**: 自动装配，先byName，然后byType

5. **@Component**:

   - 组件，放在类上面，说明这个类被spring管理了，就是bean！相当于`<bean id="user" class="com.clb.POJO.User"/>`
   - 衍生了几个注解,但是功能是一样的，都是将某个类注册到spring中，然后装配bean:
     - @Repository dao层
     - @Service service层
     - @Controller controller层

6. **@Configuration**:

   - 表名当前类是一个配置类，想当于代替了原来的xml配置文件
   - 这个类也会被注册到spring容器中，因为本身也是一个@Component

7. **@ComponentScan**:放在配置类上面，扫描指定包下所有文件中含有@Component(及其衍生注解)注解的类，并将其注册为bean

8. **@Bean**:放在配置类的方法上面，注册一个bean，方法名作为id，返回值作为class

9. **@Import**:放在配置类上面，导入另外一个配置类的配置

10. **@Aspect**:标注这个类是一个切面

11. AOP切入点执行方法相关注解:

    - **@Before**:标注这个方法是切入点之前执行
    - **@After**:切入点之后执行
    - **@Around**:环绕，在方法中可以定义前后执行的语句

12. **@Param()注解:**

    1. 基本类型或者**String**类型需要加上
    2. **引用类型可以不加**
    3. *如果只有一个基本类型的话，可以不加，但是建议加上*
    4. 在注解中的**sql**语句中**{}**中的参数就是**@Param**注解中的属性名

    <img src="https://cdn.staticaly.com/gh/TankingCao/picx-images-hosting@master/redis-(1).1tezaf6khwqo.webp" alt="图片呢">

    **lombok相关注解**

    1. **@Data**:生成 无参构造、get、set、equals、hashcode、tostring方法

    2. **@NoArgsConstructor**：生成无参构造(声明了有参构造时使用)

    3. **@AllArgsConstructor**：生成有参构造

    4. 以及一些对应方法生成的注解

    ![](https://cdn.staticaly.com/gh/TankingCao/picx-images-hosting@master/redis-(2).4mrnuh38tmo0.webp)
