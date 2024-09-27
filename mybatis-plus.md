---
title: mybatis-plus
date: 2023-08-31 17:13:56
tags:
  - mysql
  - mybatis
  - java
categories: 后端
cover: https://s2.loli.net/2024/06/09/ZuWeizVmJ3DNOgq.webp
stick: 996
---

# mybatis-plus

## 简介

> [MyBatis-Plus](https://github.com/baomidou/mybatis-plus)（简称 MP）是一个 [MyBatis](https://www.mybatis.org/mybatis-3/)的增强工具，在 MyBatis 的基础上==只做增强不做改变==，为简化开发、提高效率而生。(先了解[[mybatis]]框架)


![](https://img2.imgtp.com/2024/04/04/zV34uOPj.png)

## 1.快速开始

### 1.1 导入依赖

> 导入mybatis-plus依赖,包含了mybatis，==不用额外再导入mybatis依赖==

```xml
<dependency>
    <groupId>com.baomidou</groupId>
    <artifactId>mybatis-plus-boot-starter</artifactId>
    <version>3.5.3.1</version>
</dependency>
```

### 1.2 创建Mapper

>为了简化单表CRUD，mp已经提供了对于单表的CRUD操作的接口`BaseMapper`,直接继承BaseMapper接口即可直接使用

![](https://img2.imgtp.com/2024/04/04/WiwPW9IW.png)

### 1.3 测试CRUD

> 测试BaseMapper中对单表CRUD操作

```java
@Test
public void testInsert() {
    User user = new User();
    //user.setId(5L);
    user.setUsername("ikun23");
    user.setPassword("123");
    user.setPhone("18688990011");
    user.setBalance(200);
    user.setInfo(UserInfo.of(24,"英语老师","female"));
    user.setCreateTime(LocalDateTime.now());
    user.setUpdateTime(LocalDateTime.now());
    userMapper.insert(user);
}

@Test
public void testSelectById() {
    User user = userMapper.selectById(4L);
    System.out.println(user);
}

@Test
public void testSelectByIds() {
    List<User> users = userMapper.selectBatchIds(List.of(1, 2, 3));
    users.forEach(System.out::println);
}

@Test
public void testUpdate() {
    User user = new User();
    user.setId(5L);
    user.setBalance(3);
    user.setInfo(UserInfo.of(24,"英语老师","female"));
    user.setCreateTime(LocalDateTime.now());
    user.setUpdateTime(LocalDateTime.now());

    userMapper.updateById(user);
}

@Test
public void testDelete() {
    System.out.println(userMapper.deleteById(5L));
}
```

> 总结：只要继承了`BaseMapper`，就能直接对单表进行CRUD操作！

## 2.常见注解

> **问题**：在刚刚的测试中，我们直接调用BaseMapper中的方法就能对表增删改查，在继承`BaseMapper`的时候我们只是指定了一个泛型`<User>`,并没有指定是哪张表，那么==mybatis-plus怎么知道我们要操作的是user表呢？它又是怎么知道这张表中的所有字段名呢？==
>
> 解答：其实mp遵从==约定大于配置==的思想,mp从`User`类推导出数据库中表名为`user`，然后根据User类中的所有变量名从==驼峰命名==转成==下划线==作为数据库的字段名，从而在调用方法时可以自动生成正确的sql语句。
>
> 如果我们在创建User类和user表的时候遵从驼峰命名和下划线命名，那么我们不需要做额外的配置，如果类名和表名、属性名和字段名直接不是简单的转换，那么我们就不得不使用一些相应的注解来声明表的信息

### 2.1 [@TableName](https://www.baomidou.com/pages/223848/#tablename)

- 描述：表名注解，标识实体类对应的表
- 使用位置：实体类

```java
@TableName("sys_user")
public class User {
    private Long id;
    private String name;
    private Integer age;
    private String email;
}
```

### 2.2 [ @TableId](https://github.com/baomidou/mybatis-plus/blob/3.0/mybatis-plus-annotation/src/main/java/com/baomidou/mybatisplus/annotation/TableId.java)

- 描述：主键注解
- 使用位置：实体类主键字段

```java
@TableName("sys_user")
public class User {
    @TableId
    private Long id;
    private String name;
    private Integer age;
    private String email;
}
```

| **属性** | **类型** | **必须指定** | **默认值**      | **描述**     |
| -------- | -------- | ------------ | --------------- | ------------ |
| value    | String   | 否           | ""              | 主键字段名   |
| type     | Enum     | 否           | ==IdType.NONE== | 指定主键类型 |

`IdType`支持的类型有：

| **值**            | **描述**                                                     |
| ----------------- | ------------------------------------------------------------ |
| AUTO              | 数据库 ID 自增                                               |
| NONE              | 无状态，该类型为未设置主键类型（注解里等于跟随全局，全局里约等于 INPUT） |
| INPUT             | insert 前自行 set 主键值                                     |
| ASSIGN_ID         | 分配 ID(主键类型为 Number(Long 和 Integer)或 String)(since 3.3.0),使用接口IdentifierGenerator的方法nextId(默认实现类为DefaultIdentifierGenerator雪花算法) |
| ASSIGN_UUID       | 分配 UUID,主键类型为 String(since 3.3.0),使用接口IdentifierGenerator的方法nextUUID(默认 default 方法) |
| ~~ID_WORKER~~     | 分布式全局唯一 ID 长整型类型(please use ASSIGN_ID)           |
| ~~UUID~~          | 32 位 UUID 字符串(please use ASSIGN_UUID)                    |
| ~~ID_WORKER_STR~~ | 分布式全局唯一 ID 字符串类型(please use ASSIGN_ID)           |

这里比较常见的有三种：

- `AUTO`：利用数据库的id自增长
- `INPUT`：手动生成id
- `ASSIGN_ID`：雪花算法生成`Long`类型的全局唯一id，这是默认的ID策略

### 2.3 [@TableField](https://www.baomidou.com/pages/223848/#tablefield)

- 描述：字段注解（非主键）

```java
@TableName("sys_user")
public class User {
    @TableId
    private Long id;
    @TableField("nickname")
    private String name;
    private Integer age;
    private String email;
}
```

## 3.常见配置

MybatisPlus也支持基于yaml文件的自定义配置，详见官方文档：
[使用配置 | MyBatis-Plus](https://www.baomidou.com/pages/56bac0/#%E5%9F%BA%E6%9C%AC%E9%85%8D%E7%BD%AE)

大多数的配置都有默认值，因此我们都无需配置。但还有一些是没有默认值的，例如:

- 实体类的别名扫描包
- 全局id类型

```yaml
mybatis-plus:
  type-aliases-package: com.itheima.mp.domain.po	#别名扫描包
  global-config:
    db-config:
      id-type: auto # 全局id类型为自增长
```

需要注意的是，MyBatisPlus也支持手写SQL的，而mapper文件的读取地址可以自己配置：

```yaml
mybatis-plus:
  mapper-locations: "classpath*:/mapper/**/*.xml" # Mapper.xml文件地址，当前这个是默认值。
```

可以看到默认值是`classpath*:/mapper/**/*.xml`，也就是说我们只要把mapper.xml文件放置这个目录下就一定会被加载。

使用`@MapperScan`注解标识mapper类所在目录

```java
@SpringBootApplication
@MapperScan("com.clb.mapper")
public class App {
    public static void main(String[] args) {
        SpringApplication.run(App.class, args);
    }
}

```

> 配置了==@MapperScan==注解后，mapper类中无需添加==@Mapper==注解

---

## **==4.核心功能==**

### 4.1 条件构造器

除了新增以外，修改、删除、查询的SQL语句都需要指定where条件。因此BaseMapper中提供的相关方法除了以`id`作为`where`条件以外，还支持更加复杂的`where`条件。
![image.png](https://img2.imgtp.com/2024/04/04/EYycmHcF.png)
参数中的`Wrapper`就是条件构造的抽象类，其下有很多默认实现，继承关系如图：
![image.png](https://img2.imgtp.com/2024/04/04/yBBlOx4P.png)

`Wrapper`的子类`AbstractWrapper`提供了where中包含的所有条件构造方法：
![image.png](https://img2.imgtp.com/2024/04/04/mdBy9WoL.png)
而QueryWrapper在AbstractWrapper的基础上拓展了一个select方法，允许指定查询字段：
![image.png](https://img2.imgtp.com/2024/04/04/hpyUpWuQ.png)
而UpdateWrapper在AbstractWrapper的基础上拓展了一个set方法，允许指定SQL中的SET部分：
![image.png](https://img2.imgtp.com/2024/04/04/73APzR7R.png)

接下来，我们就来看看如何利用`Wrapper`实现复杂查询。

#### 4.1.1 QueryWrapper

修改、删除、查询都可以使用QueryWrapper构建查询条件

**查询：**查询名字带有o，且存款大于等于1000的人

```mysql
select id,username,info,balance 
from user
where username like %o% and balance >= 1000;
```

```java
@Test
public void test02() {
    QueryWrapper<User> wrapper = new QueryWrapper<>();
    //构建查询条件
    wrapper.select("id", "username", "info", "balance")
        .like("username", "o")
        .ge("balance", 1000);
    //查询数据
    List<User> users = userMapper.selectList(wrapper);
    users.forEach(System.out::println);
}
```

#### 4.1.2 UpdateWrapper

基于BaseMapper中的update方法更新时只能直接赋值，对于一些复杂的需求就难以实现。
例如：更新id为`1,2,4`的用户的余额，扣200，对于的SQL应该是：

```sql
UPDATE user SET balance = balance - 200 WHERE id in (1, 2, 4)
```

SET的赋值结果是基于字段现有值的，这个时候就要利用UpdateWrapper中的setSql功能了：

```java
@Test
void testUpdateWrapper() {
    List<Long> ids = List.of(1L, 2L, 4L);
    // 1.生成SQL
    UpdateWrapper<User> wrapper = new UpdateWrapper<User>()
            .setSql("balance = balance - 200") // SET balance = balance - 200
            .in("id", ids); // WHERE id in (1, 2, 4)
	// 2.更新，注意第一个参数可以给null，也就是不填更新字段和数据，
    // 而是基于UpdateWrapper中的setSQL来更新
    userMapper.update(null, wrapper);
}
```

#### 4.1.3 LambdaQueryWrapper

无论是QueryWrapper还是UpdateWrapper在构造条件的时候都需要写死字段名称，可能会出现字符串写错的现象，因此MybatisPlus又提供了一套基于Lambda的Wrapper，包含两个：

- `LambdaQueryWrapper`
- `LambdaUpdateWrapper`

分别对应`QueryWrapper`和`UpdateWrapper`

```mysql
select id,username,info,balance 
from user
where username like %o% and balance >= 1000;
```

```java
@Test
public void test02() {
    LambdaQueryWrapper<User> wrapper = new LambdaQueryWrapper<>();
    //构建查询条件
    //由原来的字符串变成getter函数对象获取类属性
    wrapper.select(User::getId, User::getUsername, User::getInfo, User::getBalance)
        .like(User::getUsername, "o")
        .ge(User::getBalance, 1000);
    userMapper.selectList(wrapper);
}
```

```mysql
UPDATE user SET balance = balance - 200 WHERE id in (1, 2, 4);
```

### 4.2 自定义SQL

#### 4.2.1 基本使用

在演示`UpdateWrapper`的案例中，我们在代码中编写了更新的SQL语句：
![image.png](https://img2.imgtp.com/2024/04/04/kpX6ZbUO.png)
这种写法在某些企业也是不允许的，因为SQL语句最好都维护在持久层，而不是业务层。就当前案例来说，由于条件是in语句，只能将SQL写在Mapper.xml文件，利用foreach来生成动态SQL。
这实在是太麻烦了。假如查询条件更复杂，动态SQL的编写也会更加复杂。

所以，MybatisPlus提供了自定义SQL功能，可以让我们利用Wrapper生成查询条件，再结合Mapper.xml或注解编写SQL

```mysql
UPDATE user SET balance = balance - 200 WHERE id in (1, 2, 4)
```

`update user set balance = balance - 200`使用注解完成

```java
//将wrapper作为ew，并使用ew.customSqlSegment取出条件是固定写法
@Update("update tb_user set balance = balance - #{amount} ${ew.customSqlSegment}")
void updateBalanceByWrapper(@Param("amount") int amount, @Param("ew") LambdaQueryWrapper<User> wrapper);
```

`where id in(1,2,4)` 使用自定义sql完成,将wrapper作为参数传入自定义的方法中`${ew.customSqlSegment}` ==>` where id in (1,2,4)`

```java
    @Test
    public void testCustomSql() {
        int amount = 200;
        LambdaQueryWrapper<User> wrapper = new LambdaQueryWrapper<>();
        wrapper.in(User::getId, 1, 2, 4);
        userMapper.updateBalanceByWrapper(amount, wrapper);
    }
```

#### 4.2.2 多表联查

理论上来将MyBatisPlus是不支持多表查询的，不过我们可以利用Wrapper中自定义条件结合自定义SQL来实现多表查询的效果。
例如，我们要查询出所有收货地址在北京的并且用户id在1、2、4之中的用户
要是自己基于mybatis实现SQL，大概是这样的：

```xml
  <select id="queryUserByIdAndAddr" resultType="com.itheima.mp.domain.po.User">
      SELECT *
      FROM user u
      INNER JOIN address a ON u.id = a.user_id
      WHERE u.id
      <foreach collection="ids" separator="," item="id" open="IN (" close=")">
          #{id}
      </foreach>
      AND a.city = #{city}
  </select>
```

可以看出其中最复杂的就是WHERE条件的编写，如果业务复杂一些，这里的SQL会更变态。但是基于自定义SQL结合Wrapper的玩法，我们就可以利用Wrapper来构建查询条件，然后手写SELECT及FROM部分，实现多表查询。
查询条件这样来构建：

```java
@Test
void testCustomJoinWrapper() {
    // 1.准备自定义查询条件
    QueryWrapper<User> wrapper = new QueryWrapper<User>()
            .in("u.id", List.of(1L, 2L, 4L))
            .eq("a.city", "北京");

    // 2.调用mapper的自定义方法
    List<User> users = userMapper.queryUserByWrapper(wrapper);

    users.forEach(System.out::println);
}
```

然后在UserMapper中自定义方法：

```java
@Select("SELECT u.* FROM user u INNER JOIN address a ON u.id = a.user_id ${ew.customSqlSegment}")
List<User> queryUserByWrapper(@Param("ew")QueryWrapper<User> wrapper);
```

当然，也可以在`UserMapper.xml`中写SQL：

```xml
<select id="queryUserByIdAndAddr" resultType="com.itheima.mp.domain.po.User">
    SELECT * FROM user u INNER JOIN address a ON u.id = a.user_id ${ew.customSqlSegment}
</select>
```

> ==总结:where条件可以使用wrapper构建，然后作为参数传递==

### 4.3 Service接口

MybatisPlus不仅提供了BaseMapper，还提供了通用的Service接口及默认实现，封装了一些常用的service模板方法。
通用接口为`IService`，默认实现为`ServiceImpl`，其中封装的方法可以分为以下几类：

- `save`：新增
- `remove`：删除
- `update`：更新
- `get`：查询单个结果
- `list`：查询集合结果
- `count`：计数
- `page`：分页查询

#### 4.3.1.CRUD

我们先俩看下基本的CRUD接口。
**新增**：
![image.png](https://img2.imgtp.com/2024/04/04/EHtTllxK.png)

- `save`是新增单个元素
- `saveBatch`是批量新增
- `saveOrUpdate`是根据id判断，如果数据存在就更新，不存在则新增
- `saveOrUpdateBatch`是批量的新增或修改

**删除：**
![image.png](https://img2.imgtp.com/2024/04/04/hTbeEW9j.png)

- `removeById`：根据id删除
- `removeByIds`：根据id批量删除
- `removeByMap`：根据Map中的键值对为条件删除
- `remove(Wrapper<T>)`：根据Wrapper条件删除
- `~~removeBatchByIds~~`：暂不支持

**修改：**
![image.png](https://img2.imgtp.com/2024/04/04/vmqY49oX.png)

- `updateById`：根据id修改
- `update(Wrapper<T>)`：根据`UpdateWrapper`修改，`Wrapper`中包含`set`和`where`部分
- `update(T，Wrapper<T>)`：按照`T`内的数据修改与`Wrapper`匹配到的数据
- `updateBatchById`：根据id批量修改

**Get：**
![image.png](https://img2.imgtp.com/2024/04/04/rtihGb60.png)

- `getById`：根据id查询1条数据
- `getOne(Wrapper<T>)`：根据`Wrapper`查询1条数据
- `getBaseMapper`：获取`Service`内的`BaseMapper`实现，某些时候需要直接调用`Mapper`内的自定义`SQL`时可以用这个方法获取到`Mapper`

**List：**
![image.png](https://img2.imgtp.com/2024/04/04/3InxWOnw.png)

- `listByIds`：根据id批量查询
- `list(Wrapper<T>)`：根据Wrapper条件查询多条数据
- `list()`：查询所有

**Count**：
![image.png](https://img2.imgtp.com/2024/04/04/7ZkniJuS.png)

- `count()`：统计所有数量
- `count(Wrapper<T>)`：统计符合`Wrapper`条件的数据数量

**getBaseMapper**：
当我们在service中要调用Mapper中自定义SQL时，就必须获取service对应的Mapper，就可以通过这个方法：
![image.png](https://img2.imgtp.com/2024/04/04/xxVjxhlY.png)

#### 4.3.2 基本用法

由于`Service`中经常需要定义与业务有关的自定义方法，因此我们不能直接使用`IService`，而是自定义`Service`接口，然后继承`IService`以拓展方法。同时，让自定义的`Service实现类`继承`ServiceImpl`，这样就不用自己实现`IService`中的接口了，如下图(**绿色为接口，蓝色为实现类**)

![](https://img2.imgtp.com/2024/04/04/eLZIQZta.png)

```java
//自定义接口继承IService接口，需要指定泛型
public interface IUserService extends IService<User>
```

```java
//自定义实现类继承ServiceImpl，实现自定义接口，需要指定对应的Mapper和泛型，对应的Mapper需要继承BaseMapper
public class UserServiceImpl extends ServiceImpl<UserMapper, User> implements IUserService
```

测试

```java
@Test
public void testSave() {
    User user = new User();
    //user.setId(5L);
    user.setUsername("kun_");
    user.setPassword("123");
    user.setPhone("18688990011");
    user.setBalance(2000);
    user.setInfo(UserInfo.of(24, "英语老师", "female"));
    user.setCreateTime(LocalDateTime.now());
    user.setUpdateTime(LocalDateTime.now());
    user.setStatus(UserStatus.NORMAL);
    userService.save(user);
}

@Test
public void testGet() {
    List<User> users = userService.list(new LambdaQueryWrapper<User>().select(User::getUsername, User::getBalance).le(User::getBalance, 999));
    users.forEach(System.out::println);
}
```

#### 4.3.3 批量新增

IService中的批量新增功能使用起来非常方便，但有一点注意事项，我们先来测试一下。
首先我们测试逐条插入数据：

```java
@Test
void testSaveOneByOne() {
    long b = System.currentTimeMillis();
    for (int i = 1; i <= 100000; i++) {
        userService.save(buildUser(i));
    }
    long e = System.currentTimeMillis();
    System.out.println("耗时：" + (e - b));
}

private User buildUser(int i) {
    User user = new User();
    user.setUsername("user_" + i);
    user.setPassword("123");
    user.setPhone("" + (18688190000L + i));
    user.setBalance(2000);
    user.setInfo("{\"age\": 24, \"intro\": \"英文老师\", \"gender\": \"female\"}");
    user.setCreateTime(LocalDateTime.now());
    user.setUpdateTime(user.getCreateTime());
    return user;
}
```

执行结果如下：
![image.png](https://img2.imgtp.com/2024/04/04/9hiuZHou.png)
可以看到速度非常慢。

然后再试试MybatisPlus的批处理：

```java
@Test
void testSaveBatch() {
    // 准备10万条数据
    List<User> list = new ArrayList<>(1000);
    long b = System.currentTimeMillis();
    for (int i = 1; i <= 100000; i++) {
        list.add(buildUser(i));
        // 每1000条批量插入一次
        if (i % 1000 == 0) {
            userService.saveBatch(list);
            list.clear();
        }
    }
    long e = System.currentTimeMillis();
    System.out.println("耗时：" + (e - b));
}
```

执行最终耗时如下：
![image.png](https://img2.imgtp.com/2024/04/04/3m6K4PzT.png)
可以看到使用了批处理以后，比逐条新增效率提高了10倍左右，性能还是不错的。

不过，我们简单查看一下`MybatisPlus`源码：

```java
@Transactional(rollbackFor = Exception.class)
@Override
public boolean saveBatch(Collection<T> entityList, int batchSize) {
    String sqlStatement = getSqlStatement(SqlMethod.INSERT_ONE);
    return executeBatch(entityList, batchSize, (sqlSession, entity) -> sqlSession.insert(sqlStatement, entity));
}
// ...SqlHelper
public static <E> boolean executeBatch(Class<?> entityClass, Log log, Collection<E> list, int batchSize, BiConsumer<SqlSession, E> consumer) {
    Assert.isFalse(batchSize < 1, "batchSize must not be less than one");
    return !CollectionUtils.isEmpty(list) && executeBatch(entityClass, log, sqlSession -> {
        int size = list.size();
        int idxLimit = Math.min(batchSize, size);
        int i = 1;
        for (E element : list) {
            consumer.accept(sqlSession, element);
            if (i == idxLimit) {
                sqlSession.flushStatements();
                idxLimit = Math.min(idxLimit + batchSize, size);
            }
            i++;
        }
    });
}
```

可以发现其实`MybatisPlus`的批处理是基于`PrepareStatement`的预编译模式，然后批量提交，最终在数据库执行时还是会有多条insert语句，逐条插入数据。SQL类似这样：

```java
Preparing: INSERT INTO user ( username, password, phone, info, balance, create_time, update_time ) VALUES ( ?, ?, ?, ?, ?, ?, ? )
Parameters: user_1, 123, 18688190001, "", 2000, 2023-07-01, 2023-07-01
Parameters: user_2, 123, 18688190002, "", 2000, 2023-07-01, 2023-07-01
Parameters: user_3, 123, 18688190003, "", 2000, 2023-07-01, 2023-07-01
```

而如果想要得到最佳性能，最好是将多条SQL合并为一条，像这样：

```sql
INSERT INTO user ( username, password, phone, info, balance, create_time, update_time )
VALUES 
(user_1, 123, 18688190001, "", 2000, 2023-07-01, 2023-07-01),
(user_2, 123, 18688190002, "", 2000, 2023-07-01, 2023-07-01),
(user_3, 123, 18688190003, "", 2000, 2023-07-01, 2023-07-01),
(user_4, 123, 18688190004, "", 2000, 2023-07-01, 2023-07-01);
```

该怎么做呢？

MySQL的客户端连接参数中有这样的一个参数：`rewriteBatchedStatements`。顾名思义，就是重写批处理的`statement`语句。参考文档：
[cj-conn-prop_rewriteBatchedStatements](https://dev.mysql.com/doc/connector-j/8.0/en/connector-j-connp-props-performance-extensions.html#cj-conn-prop_rewriteBatchedStatements)
这个参数的默认值是false，我们需要修改连接参数，将其配置为true

修改项目中的application.yml文件，在jdbc的url后面添加参数`&rewriteBatchedStatements=true`:

```yaml
spring:
  datasource:
    url: jdbc:mysql://127.0.0.1:3306/mp?useUnicode=true&characterEncoding=UTF-8&autoReconnect=true&serverTimezone=Asia/Shanghai&rewriteBatchedStatements=true
    driver-class-name: com.mysql.cj.jdbc.Driver
    username: root
    password: MySQL123
```

再次测试插入10万条数据，可以发现速度有非常明显的提升：
![image.png](https://img2.imgtp.com/2024/04/04/3w87AgNv.png)

在`ClientPreparedStatement`的`executeBatchInternal`中，有判断`rewriteBatchedStatements`值是否为true并重写SQL的功能：
![image.png](https://img2.imgtp.com/2024/04/04/K0vXKCWw.png)
最终，SQL被重写了：
![image.png](https://img2.imgtp.com/2024/04/04/9y7FQFXY.png)

> 总结:
>
> 1. 插入大量数据的时候，使用`saveBatch`批量插入一定数量的数据而不是在循环里面一条一条插入数据`save`
>
> 2. mysql配置文件中开启批处理
>
>    ```yaml
>    spring:
>      datasource:
>        url: jdbc:mysql://127.0.0.1:3306/mp？rewriteBatchedStatements=true #rewriteBatchedStatements=true 开启批处理
>    ```

#### 4.3.4 Lambda

Service中对`LambdaQueryWrapper`和`LambdaUpdateWrapper`的用法进一步做了简化。我们无需自己通过`new`的方式来创建`Wrapper`，而是直接调用`lambdaQuery`和`lambdaUpdate`方法：

基于Lambda查询：

```java
@Test
void testLambdaQuery() {
    // 1.查询1个
    User rose = userService.lambdaQuery()
            .eq(User::getUsername, "Rose")
            .one(); // .one()查询1个
    System.out.println("rose = " + rose);

    // 2.查询多个
    List<User> users = userService.lambdaQuery()
            .like(User::getUsername, "o")
            .list(); // .list()查询集合
    users.forEach(System.out::println);

    // 3.count统计
    Long count = userService.lambdaQuery()
            .like(User::getUsername, "o")
            .count(); // .count()则计数
    System.out.println("count = " + count);
}
```

可以发现lambdaQuery方法中除了可以构建条件，而且根据链式编程的最后一个方法来判断最终的返回结果，可选的方法有：

- `.one()`：最多1个结果
- `.list()`：返回集合结果
- `.count()`：返回计数结果

lambdaQuery还支持动态条件查询。比如下面这个需求：

> 定义一个方法，接收参数为username、status、minBalance、maxBalance，参数可以为空。
>
> - 如果username参数不为空，则采用模糊查询;
> - 如果status参数不为空，则采用精确匹配；
> - 如果minBalance参数不为空，则余额必须大于minBalance
> - 如果maxBalance参数不为空，则余额必须小于maxBalance

这个需求就是典型的动态查询，在业务开发中经常碰到，实现如下：

```java
@Test
void testQueryUser() {
    List<User> users = queryUser("o", 1, null, null);
    users.forEach(System.out::println);
}

public List<User> queryUser(String username, Integer status, Integer minBalance, Integer maxBalance) {
    return userService.lambdaQuery()
            .like(username != null , User::getUsername, username)
            .eq(status != null, User::getStatus, status)
            .ge(minBalance != null, User::getBalance, minBalance)
            .le(maxBalance != null, User::getBalance, maxBalance)
            .list();
}
```


基于Lambda更新：

```java
@Test
void testLambdaUpdate() {
    userService.lambdaUpdate()
            .set(User::getBalance, 800) // set balance = 800
            .eq(User::getUsername, "Jack") // where username = "Jack"
            .update(); // 执行Update
}
```

`lambdaUpdate()`方法后基于链式编程，可以添加`set`条件和`where`条件。但最后一定要跟上`update()`，否则语句不会执行。

lambdaUpdate()同样支持动态条件，例如下面的需求：

> 基于IService中的lambdaUpdate()方法实现一个更新方法，满足下列需求：
>
> - 参数为balance、id、username
> - id或username至少一个不为空，根据id或username精确匹配用户
> - 将匹配到的用户余额修改为balance
> - 如果balance为0，则将用户status修改为冻结状态

实现如下：

```java
@Test
void testUpdateBalance() {
    updateBalance(0L, 1L, null);
}

public void updateBalance(Long balance, Long id, String username){
    userService.lambdaUpdate()
            .set(User::getBalance, balance)
            .set(balance == 0, User::getStatus, 2)
            .eq(id != null, User::getId, id)
            .eq(username != null, User::getId, username)
            .update();
}
```

### 4.4.静态工具

有的时候Service之间也会相互调用，为了避免出现循环依赖问题，MybatisPlus提供一个静态工具类：`Db`，其中的一些静态方法与`IService`中方法签名基本一致，也可以帮助我们实现CRUD功能：
![image.png](https://img2.imgtp.com/2024/04/04/BsapLoQj.png)

示例：

```java
@Test
void testDbGet() {
    User user = Db.getById(1L, User.class);
    System.out.println(user);
}

@Test
void testDbList() {
    // 利用Db实现复杂条件查询
    List<User> list = Db.lambdaQuery(User.class)
            .like(User::getUsername, "o")
            .ge(User::getBalance, 1000)
            .list();
    list.forEach(System.out::println);
}

@Test
void testDbUpdate() {
    Db.lambdaUpdate(User.class)
            .set(User::getBalance, 2000)
            .eq(User::getUsername, "Rose");
}
```

## 5.拓展功能

### 5.1 代码生成插件

1. 安装插件

![image.png](https://img2.imgtp.com/2024/04/04/oZkvc41U.png)

2. 配置数据库

![image.png](https://img2.imgtp.com/2024/04/04/naMirTBz.png)

![image.png](https://img2.imgtp.com/2024/04/04/uHRd7Xky.png)

3. 生成代码

   ![image.png](https://img2.imgtp.com/2024/04/04/85YOQRj9.png)

![image.png](https://img2.imgtp.com/2024/04/04/dHdRGTLq.png)

### 5.2 逻辑删除

对于一些比较重要的数据，我们往往会采用逻辑删除的方案，即：

- 在表中添加一个字段标记数据是否被删除
- 当删除数据时把标记置为true
- 查询时过滤掉标记为true的数据

一旦采用了逻辑删除，所有的查询和删除逻辑都要跟着变化，非常麻烦。为了解决这个问题，MybatisPlus就添加了对逻辑删除的支持。
:::warning
**注意**，只有MybatisPlus生成的SQL语句才支持自动的逻辑删除，自定义SQL需要自己手动处理逻辑删除。
:::

例如，我们给`address`表添加一个逻辑删除字段：

```sql
alter table address
	add deleted bit default b'0' null comment '逻辑删除';
```

然后给`Address`实体添加`deleted`字段：
![image.png](https://img2.imgtp.com/2024/04/04/7yMg8Ned.png)


接下来，我们要在`application.yml`中配置逻辑删除字段：

```yaml
mybatis-plus:
  global-config:
    db-config:
      logic-delete-field: deleted # 全局逻辑删除的实体字段名(since 3.3.0,配置后可以忽略不配置步骤2)
      logic-delete-value: 1 # 逻辑已删除值(默认为 1)
      logic-not-delete-value: 0 # 逻辑未删除值(默认为 0)
```

测试：
首先，我们执行一个删除操作：

```java
@Test
void testDeleteByLogic() {
    // 删除方法与以前没有区别
    addressService.removeById(59L);
}
```

方法与普通删除一模一样，但是底层的SQL逻辑变了：
![image.png](https://img2.imgtp.com/2024/04/04/F764ALZ9.png)

查询一下试试：

```java
@Test
void testQuery() {
    List<Address> list = addressService.list();
    list.forEach(System.out::println);
}
```

会发现id为59的确实没有查询出来，而且SQL中也对逻辑删除字段做了判断：
![image.png](https://img2.imgtp.com/2024/04/04/iVAzYJEP.png)

综上， 开启了逻辑删除功能以后，我们就可以像普通删除一样做CRUD，基本不用考虑代码逻辑问题。还是非常方便的。

:::warning
**注意**：
逻辑删除本身也有自己的问题，比如：

- 会导致数据库表垃圾数据越来越多，从而影响查询效率
- SQL中全都需要对逻辑删除字段做判断，影响查询效率

因此，我不太推荐采用逻辑删除功能，如果数据不能删除，可以采用把数据迁移到其它表的办法。
:::


### 5.3 通用枚举

User类中有一个用户状态字段：
![image.png](https://img2.imgtp.com/2024/04/04/A2iNFo9N.png)
像这种字段我们一般会定义一个枚举，做业务判断的时候就可以直接基于枚举做比较。但是我们数据库采用的是`int`类型，对应的PO也是`Integer`。因此业务操作时必须手动把`枚举`与`Integer`转换，非常麻烦。

因此，MybatisPlus提供了一个处理枚举的类型转换器，可以帮我们**把枚举类型与数据库类型自动转换**。

#### 5.3.1.定义枚举

我们定义一个用户状态的枚举：
![image.png](https://img2.imgtp.com/2024/04/04/3zYvEl0h.png)
代码如下：

```java
package com.itheima.mp.enums;

import com.baomidou.mybatisplus.annotation.EnumValue;
import lombok.Getter;

@Getter
public enum UserStatus {
    NORMAL(1, "正常"),
    FREEZE(2, "冻结")
    ;
    private final int value;
    private final String desc;

    UserStatus(int value, String desc) {
        this.value = value;
        this.desc = desc;
    }
}

```

然后把`User`类中的`status`字段改为`UserStatus` 类型：
![image.png](https://img2.imgtp.com/2024/04/04/uOuWLie2.png)


要让`MybatisPlus`处理枚举与数据库类型自动转换，我们必须告诉`MybatisPlus`，枚举中的哪个字段的值作为数据库值。
`MybatisPlus`提供了`@EnumValue`注解来标记枚举属性：
![image.png](https://img2.imgtp.com/2024/04/04/2os8O1jy.png)

#### 5.3.2.配置枚举处理器

在application.yaml文件中添加配置：

```yaml
mybatis-plus:
  configuration:
    default-enum-type-handler: com.baomidou.mybatisplus.core.handlers.MybatisEnumTypeHandler
```

#### 5.3.3.测试

```java
@Test
void testService() {
    List<User> list = userService.list();
    list.forEach(System.out::println);
}
```

最终，查询出的`User`类的`status`字段会是枚举类型：
![image.png](https://img2.imgtp.com/2024/04/04/w6yhRekl.png)


### 5.4 字段类型处理器

数据库的user表中有一个`info`字段，是JSON类型：
![image.png](https://img2.imgtp.com/2024/04/04/aq5pnfGN.png)
格式像这样：

```json
{"age": 20, "intro": "佛系青年", "gender": "male"}
```

而目前`User`实体类中却是`String`类型：
![image.png](https://img2.imgtp.com/2024/04/04/bST1cToI.png)

这样以来，我们要读取info中的属性时就非常不方便。如果要方便获取，info的类型最好是一个`Map`或者实体类。
而一旦我们把`info`改为`对象`类型，就需要在写入数据库是手动转为`String`，再读取数据库时，手动转换为`对象`，这会非常麻烦。

因此MybatisPlus提供了很多特殊类型字段的类型处理器，解决特殊字段类型与数据库类型转换的问题。例如处理JSON就可以使用`JacksonTypeHandler`处理器。

接下来，我们就来看看这个处理器该如何使用。

#### 5.4.1 定义实体

首先，我们定义一个单独实体类来与info字段的属性匹配：
![image.png](https://img2.imgtp.com/2024/04/04/k7dLTXuX.png)
代码如下：

```java
package com.itheima.mp.domain.po;

import lombok.Data;

@Data
public class UserInfo {
    private Integer age;
    private String intro;
    private String gender;
}
```

#### 5.4.2 使用类型处理器

接下来，将User类的info字段修改为UserInfo类型，并声明类型处理器：
![image.png](https://img2.imgtp.com/2024/04/04/WgvyOE3Q.png)

测试可以发现，所有数据都正确封装到UserInfo当中了：
![image.png](https://img2.imgtp.com/2024/04/04/3vnjQq6c.png)

### 5.5配置加密

目前我们配置文件中的很多参数都是明文，如果开发人员发生流动，很容易导致敏感信息的泄露。所以MybatisPlus支持配置文件的加密和解密功能。

我们以数据库的用户名和密码为例。

#### 5.5.1.生成秘钥

首先，我们利用AES工具生成一个随机秘钥，然后对用户名、密码加密：

```java
package com.itheima.mp;

import com.baomidou.mybatisplus.core.toolkit.AES;
import org.junit.jupiter.api.Test;

class MpDemoApplicationTests {
    @Test
    void contextLoads() {
        // 生成 16 位随机 AES 密钥
        String randomKey = AES.generateRandomKey();
        System.out.println("randomKey = " + randomKey);

        // 利用密钥对用户名加密
        String username = AES.encrypt("root", randomKey);
        System.out.println("username = " + username);

        // 利用密钥对用户名加密
        String password = AES.encrypt("MySQL123", randomKey);
        System.out.println("password = " + password);

    }
}
```

打印结果如下：

```java
randomKey = 6234633a66fb399f
username = px2bAbnUfiY8K/IgsKvscg==
password = FGvCSEaOuga3ulDAsxw68Q==
```

#### 5.5.2.修改配置

修改application.yaml文件，把jdbc的用户名、密码修改为刚刚加密生成的密文：

```yaml
spring:
  datasource:
    url: jdbc:mysql://127.0.0.1:3306/mp?useUnicode=true&characterEncoding=UTF-8&autoReconnect=true&serverTimezone=Asia/Shanghai&rewriteBatchedStatements=true
    driver-class-name: com.mysql.cj.jdbc.Driver
    username: mpw:QWWVnk1Oal3258x5rVhaeQ== # 密文要以 mpw:开头
    password: mpw:EUFmeH3cNAzdRGdOQcabWg== # 密文要以 mpw:开头
```

#### 5.5.3.测试

在启动项目的时候，需要把刚才生成的秘钥添加到启动参数中，像这样：

```yaml
--mpw.key=6234633a66fb399f
```

单元测试的时候不能添加启动参数，所以要在测试类的注解上配置：
![image.png](https://img2.imgtp.com/2024/04/04/16rM2gf0.png)

然后随意运行一个单元测试，可以发现数据库查询正常。

## 6.插件功能

MybatisPlus提供了很多的插件功能，进一步拓展其功能。目前已有的插件有：

- `PaginationInnerInterceptor`：自动分页
- `TenantLineInnerInterceptor`：多租户
- `DynamicTableNameInnerInterceptor`：动态表名
- `OptimisticLockerInnerInterceptor`：乐观锁
- `IllegalSQLInnerInterceptor`：sql 性能规范
- `BlockAttackInnerInterceptor`：防止全表更新与删除

:::warning
**注意：**
使用多个分页插件的时候需要注意插件定义顺序，建议使用顺序如下：

- 多租户,动态表名
- 分页,乐观锁
- sql 性能规范,防止全表更新与删除
  :::

这里我们以分页插件为里来学习插件的用法。

## 6.1.分页插件

在未引入分页插件的情况下，`MybatisPlus`是不支持分页功能的，`IService`和`BaseMapper`中的分页方法都无法正常起效。
所以，我们必须配置分页插件。

### 6.1.1.配置分页插件

在项目中新建一个配置类：
![image.png](https://img2.imgtp.com/2024/04/04/9PzTCvqq.png)
其代码如下：

```java
package com.itheima.mp.config;

import com.baomidou.mybatisplus.annotation.DbType;
import com.baomidou.mybatisplus.extension.plugins.MybatisPlusInterceptor;
import com.baomidou.mybatisplus.extension.plugins.inner.PaginationInnerInterceptor;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class MybatisConfig {

    @Bean
    public MybatisPlusInterceptor mybatisPlusInterceptor() {
        // 初始化核心插件
        MybatisPlusInterceptor interceptor = new MybatisPlusInterceptor();
        // 添加分页插件
        interceptor.addInnerInterceptor(new PaginationInnerInterceptor(DbType.MYSQL));
        return interceptor;
    }
}
```

### 6.1.2.分页API

编写一个分页查询的测试：

```java
@Test
void testPageQuery() {
    // 1.分页查询，new Page()的两个参数分别是：页码、每页大小
    Page<User> p = userService.page(new Page<>(2, 2));
    // 2.总条数
    System.out.println("total = " + p.getTotal());
    // 3.总页数
    System.out.println("pages = " + p.getPages());
    // 4.数据
    List<User> records = p.getRecords();
    records.forEach(System.out::println);
}
```

运行的SQL如下：
![image.png](https://img2.imgtp.com/2024/04/04/5PN2uYu4.png)

这里用到了分页参数，Page，即可以支持分页参数，也可以支持排序参数。常见的API如下：

```java
int pageNo = 1, pageSize = 5;
// 分页参数
Page<User> page = Page.of(pageNo, pageSize);
// 排序参数, 通过OrderItem来指定
page.addOrder(new OrderItem("balance", false));

userService.page(page);
```

## 6.2.通用分页实体

现在要实现一个用户分页查询的接口，接口规范如下：

| **参数**             | **说明**    |
| -------------------- | ----------- |
| 请求方式             | GET         |
| 请求路径             | /users/page |
| 请求参数             | ```json     |
| {                    |             |
| "pageNo": 1,         |             |
| "pageSize": 5,       |             |
| "sortBy": "balance", |             |
| "isAsc": false       |             |
| }                    |             |

```json
{
    "total": 100006,
    "pages": 50003,
    "list": [
        {
            "id": 1685100878975279298,
            "username": "user_9****",
            "info": {
                "age": 24,
                "intro": "英文老师",
                "gender": "female"
            },
            "status": "正常",
            "balance": 2000
        },
        {
            "id": 1685100878975279299,
            "username": "user_9****",
            "info": {
                "age": 24,
                "intro": "英文老师",
                "gender": "female"
            },
            "status": "正常",
            "balance": 2000
        }
    ]
}
```

 |
| 特殊说明 | •如果排序字段为空，默认按照更新时间排序
•排序字段不为空，则按照排序字段排序 |


这里需要定义3个实体：

- `PageQuery`：分页查询条件的实体，包含分页、排序参数
- `PageDTO`：分页结果实体，包含总条数、总页数、当前页数据
- `UserVO`：用户页面视图实体

接下来我们就按照WEB开发的过程来实现这个接口。
首先，我们在项目中引入`spring-boot-starter-web`依赖：

```xml
<!-- web依赖 -->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
</dependency>
<!-- hutool 工具包-->
<dependency>
    <groupId>cn.hutool</groupId>
    <artifactId>hutool-all</artifactId>
    <version>5.8.11</version>
</dependency>
```

然后，按`alt+8`打开`service`控制台，然后添加一个`SpringBoot`启动项：
![image.png](https://img2.imgtp.com/2024/04/04/1DTOVtUk.png)
弹窗中选择`Spring Boot`：
![image.png](https://img2.imgtp.com/2024/04/04/ZmNq45SJ.png)
弹窗中填写信息：
![image.png](https://img2.imgtp.com/2024/04/04/E3jepma1.png)
其中不要忘了配置我们之前添加的数据加密的秘钥。

### 6.2.1.实体

首先是请求参数的`PageQuery`实体：
![image.png](https://img2.imgtp.com/2024/04/04/MrS9Q87H.png)
`PageQuery`是前端提交的查询参数，一般包含四个属性：

- `pageNo`：页码
- `pageSize`：每页数据条数
- `sortBy`：排序字段
- `isAsc`：是否升序

```java
package com.itheima.mp.domain.query;

import lombok.Data;

@Data
public class PageQuery {
    private Integer pageNo;
    private Integer pageSize;
    private String sortBy;
    private Boolean isAsc;
}
```

然后我们定义一个`UserVO`实体：
![image.png](https://img2.imgtp.com/2024/04/04/ZxSIuWqc.png)
代码如下：

```java
package com.itheima.mp.domain.vo;

import com.itheima.mp.domain.po.UserInfo;
import com.itheima.mp.enums.UserStatus;
import lombok.Data;

@Data
public class UserVO {

    /**
     * 用户id
     */
    private Long id;

    /**
     * 用户名
     */
    private String username;

    /**
     * 详细信息
     */
    private UserInfo info;

    /**
     * 使用状态（1正常 2冻结）
     */
    private UserStatus status;

    /**
     * 账户余额
     */
    private Integer balance;
}
```

最后，则是分页实体PageDTO:
![image.png](https://img2.imgtp.com/2024/04/04/LmM2zHnS.png)

代码如下：

```java
package com.itheima.mp.domain.dto;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.List;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class PageDTO<T> {
    private Integer total;
    private Integer pages;
    private List<T> list;
}
```

### 6.2.2.开发接口

我们定义一个`UserController`，在`controller`中我们定义分页查询用户的接口：

```java
package com.itheima.mp.controller;

import com.itheima.mp.domain.dto.PageDTO;
import com.itheima.mp.domain.query.PageQuery;
import com.itheima.mp.domain.vo.UserVO;
import com.itheima.mp.service.UserService;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("users")
@RequiredArgsConstructor
public class UserController {

    private final UserService userService;

    @GetMapping("/page")
    public PageDTO<UserVO> queryUserByPage(PageQuery query){
        return userService.queryUserByPage(query);
    }
}

```

然后在`UserService`中创建`queryUserByPage`方法：

```java
PageDTO<UserVO> queryUserByPage(PageQuery query);
```

接下来，在UserServiceImpl中实现该方法：

```java
@Override
public PageDTO<UserVO> queryUserByPage(PageQuery query) {
    // 1.构建条件
    // 1.1.分页条件
    Page<User> page = Page.of(query.getPageNo(), query.getPageSize());
    // 1.2.排序条件
    if (query.getSortBy() != null) {
        page.addOrder(new OrderItem(query.getSortBy(), query.getIsAsc()));
    }else{
        // 默认按照更新时间排序
        page.addOrder(new OrderItem("update_time", false));
    }
    // 2.查询
    page(page);
    // 3.数据非空校验
    List<User> records = page.getRecords();
    if (records == null || records.size() <= 0) {
        // 无数据，返回空结果
        return new PageDTO<>(page.getTotal(), page.getPages(), Collections.emptyList());
    }
    // 4.有数据，转换
    List<UserVO> list = BeanUtil.copyToList(records, UserVO.class);
    // 5.封装返回
    return new PageDTO<UserVO>(page.getTotal(), page.getPages(), list);
}
```

最后，为了让UserStatus枚举可以展示为文字描述，再给UserStatus中的desc字段添加`@JsonValue`注解：
![image.png](https://img2.imgtp.com/2024/04/04/7vsAS771.png)
启动项目，在页面查看：
![image.png](https://img2.imgtp.com/2024/04/04/bugqTciD.png)

### 6.2.3.改造PageQuery实体

在刚才的代码中，从`PageQuery`到`MybatisPlus`的`Page`之间转换的过程还是比较麻烦的。
我们完全可以在`PageQuery`这个实体中定义一个工具方法，简化开发。
像这样：

```java
package com.itheima.mp.domain.query;

import com.baomidou.mybatisplus.core.metadata.OrderItem;
import com.baomidou.mybatisplus.extension.plugins.pagination.Page;
import lombok.Data;

@Data
public class PageQuery {
    private Integer pageNo;
    private Integer pageSize;
    private String sortBy;
    private Boolean isAsc;

    public <T>  Page<T> toMpPage(OrderItem ... orders){
        // 1.分页条件
        Page<T> p = Page.of(pageNo, pageSize);
        // 2.排序条件
        // 2.1.先看前端有没有传排序字段
        if (sortBy != null) {
            p.addOrder(new OrderItem(sortBy, isAsc));
            return p;
        }
        // 2.2.再看有没有手动指定排序字段
        if(orders != null){
            p.addOrder(orders);
        }
        return p;
    }

    public <T> Page<T> toMpPage(String defaultSortBy, boolean isAsc){
        return this.toMpPage(new OrderItem(defaultSortBy, isAsc));
    }

    public <T> Page<T> toMpPageDefaultSortByCreateTimeDesc() {
        return toMpPage("create_time", false);
    }

    public <T> Page<T> toMpPageDefaultSortByUpdateTimeDesc() {
        return toMpPage("update_time", false);
    }
}

```

这样我们在开发也时就可以省去对从`PageQuery`到`Page`的的转换：

```java
// 1.构建条件
Page<User> page = query.toMpPageDefaultSortByCreateTimeDesc();
```

### 6.2.4.改造PageDTO实体

在查询出分页结果后，数据的非空校验，数据的vo转换都是模板代码，编写起来很麻烦。

我们完全可以将其封装到PageDTO的工具方法中，简化整个过程：

```java
package com.itheima.mp.domain.dto;

import cn.hutool.core.bean.BeanUtil;
import com.baomidou.mybatisplus.extension.plugins.pagination.Page;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.Collections;
import java.util.List;
import java.util.function.Function;
import java.util.stream.Collectors;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class PageDTO<V> {
    private Long total;
    private Long pages;
    private List<V> list;

    /**
     * 返回空分页结果
     * @param p MybatisPlus的分页结果
     * @param <V> 目标VO类型
     * @param <P> 原始PO类型
     * @return VO的分页对象
     */
    public static <V, P> PageDTO<V> empty(Page<P> p){
        return new PageDTO<>(p.getTotal(), p.getPages(), Collections.emptyList());
    }

    /**
     * 将MybatisPlus分页结果转为 VO分页结果
     * @param p MybatisPlus的分页结果
     * @param voClass 目标VO类型的字节码
     * @param <V> 目标VO类型
     * @param <P> 原始PO类型
     * @return VO的分页对象
     */
    public static <V, P> PageDTO<V> of(Page<P> p, Class<V> voClass) {
        // 1.非空校验
        List<P> records = p.getRecords();
        if (records == null || records.size() <= 0) {
            // 无数据，返回空结果
            return empty(p);
        }
        // 2.数据转换
        List<V> vos = BeanUtil.copyToList(records, voClass);
        // 3.封装返回
        return new PageDTO<>(p.getTotal(), p.getPages(), vos);
    }

    /**
     * 将MybatisPlus分页结果转为 VO分页结果，允许用户自定义PO到VO的转换方式
     * @param p MybatisPlus的分页结果
     * @param convertor PO到VO的转换函数
     * @param <V> 目标VO类型
     * @param <P> 原始PO类型
     * @return VO的分页对象
     */
    public static <V, P> PageDTO<V> of(Page<P> p, Function<P, V> convertor) {
        // 1.非空校验
        List<P> records = p.getRecords();
        if (records == null || records.size() <= 0) {
            // 无数据，返回空结果
            return empty(p);
        }
        // 2.数据转换
        List<V> vos = records.stream().map(convertor).collect(Collectors.toList());
        // 3.封装返回
        return new PageDTO<>(p.getTotal(), p.getPages(), vos);
    }
}

```

最终，业务层的代码可以简化为：

```java
@Override
public PageDTO<UserVO> queryUserByPage(PageQuery query) {
    // 1.构建条件
    Page<User> page = query.toMpPageDefaultSortByCreateTimeDesc();
    // 2.查询
    page(page);
    // 3.封装返回
    return PageDTO.of(page, UserVO.class);
}
```

如果是希望自定义PO到VO的转换过程，可以这样做：

```java
@Override
public PageDTO<UserVO> queryUserByPage(PageQuery query) {
    // 1.构建条件
    Page<User> page = query.toMpPageDefaultSortByCreateTimeDesc();
    // 2.查询
    page(page);
    // 3.封装返回
    return PageDTO.of(page, user -> {
        // 拷贝属性到VO
        UserVO vo = BeanUtil.copyProperties(user, UserVO.class);
        // 用户名脱敏
        String username = vo.getUsername();
        vo.setUsername(username.substring(0, username.length() - 2) + "**");
        return vo;
    });
}
```

最终查询的结果如下：
![image.png](https://img2.imgtp.com/2024/04/04/TISYE7wq.png)