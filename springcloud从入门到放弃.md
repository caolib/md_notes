---
title: springcloud从入门到放弃
date: 2024-03-17 22:22:28
categories: 后端
tags: 
  - springcloud
  - gateway
cover: https://dogefs.s3.ladydaily.com/~/source/wallhaven/full/m3/wallhaven-m3y67m.jpg?w=2560&h=1440&fmt=webp
stick: 666
---

# springcloud从入门到放弃

## gateway

`Spring Cloud Gateway` 是一个基于 Spring 5、Spring Boot 2 和 Project Reactor 的 **API 网关**，以下是使用 Spring Cloud Gateway 的基本步骤：

1. **添加依赖**：在 Maven 的 `pom.xml` 文件中，添加 Spring Cloud Gateway 的依赖。

```xml
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-gateway</artifactId>
    <version>2.2.7.RELEASE</version>
</dependency>
```

2. **配置路由**：在 `application.yml` 或 `application.properties` 文件中，配置路由规则。例如，将所有以 `/reader/` 开头的请求转发到 `reader-service` 服务。

```yaml
spring:
  cloud:
    gateway:
      routes:
      - id: reader_route
        uri: lb://reader-service
        predicates:
        - Path=/reader/**
```

3. **添加拦截器**

```java
@Component
@RequiredArgsConstructor
@Slf4j
public class JwtTokenInterceptor implements GlobalFilter, Ordered {

    private final StringRedisTemplate redisTemplate;

    @Override
    public Mono<Void> filter(ServerWebExchange exchange, GatewayFilterChain chain) {
        String path = exchange.getRequest().getPath().value();
        // 不对/login和/register接口校验
        if (path.endsWith("/login") || path.endsWith("/register")) {
            log.debug("直接跳过...");
            return chain.filter(exchange);
        }

        log.debug("开始校验...");

        String token = exchange.getRequest().getHeaders().getFirst(Common.TOKEN);
        if (token == null || token.isEmpty()) {
            exchange.getResponse().setStatusCode(HttpStatus.UNAUTHORIZED);
            return exchange.getResponse().setComplete();
        }

        try {
            String redisToken = redisTemplate.opsForValue().get(token);
            if (redisToken == null) {
                throw new BaseException(Excep.TOKEN_ALREADY_EXPIRED);
            }
            Claims claims = JwtUtils.parseJWT(token);
            // 保存用户信息
            ThreadLocalUtil.set(claims);
        } catch (Exception e) {
            exchange.getResponse().setStatusCode(HttpStatus.UNAUTHORIZED);
            return exchange.getResponse().setComplete();
        }

        return chain.filter(exchange);
    }

    @Override
    public int getOrder() {
        return -100;
    }
}
```

3. **启动 Gateway**：运行 Spring Boot 应用，启动 Gateway。

4. **发送请求**：**发送请求到 Gateway**，Gateway 会根据配置的路由规则，将请求转发到对应的服务。

以上就是使用 Spring Cloud Gateway 的基本步骤。在实际使用中，可能还需要配置其他的功能，例如过滤器、限流、熔断等。

todo `openfeign`的使用
