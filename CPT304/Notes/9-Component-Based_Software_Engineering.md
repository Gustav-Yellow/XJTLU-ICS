# 9 Component-Based Software Engineering 组件化软件工程复习笔记

## 0. 本周主题总览 / Topic Overview（Slide 1–2）

本周主题是 **Component-based Software Engineering, CBSE，组件化软件工程**。课件主要分成六个部分：

This week focuses on **Component-Based Software Engineering (CBSE)**. The lecture is divided into six parts:

| 大主题 / Main Topic                                          | 幻灯片 / Slides |
| ------------------------------------------------------------ | --------------- |
| Part 1: Introduction to CBSE / CBSE 介绍                     | Slide 3–19      |
| Part 2: Components in Spring Boot: Foundations / Spring Boot 中组件的基础 | Slide 20–36     |
| Part 3: Component Interfaces, Composition, and Lifecycle / 组件接口、组合与生命周期 | Slide 37–54     |
| Part 4: Advanced Component Features in Spring Boot / Spring Boot 高级组件特性 | Slide 55–71     |
| Part 5: Component-Based Architecture with Spring Boot / Spring Boot 中的组件化架构 | Slide 72–95     |
| Part 6: Challenges, Best Practices, and Wrap-Up / 总结       | Slide 96        |

------

# Part 1: Introduction to CBSE / CBSE 介绍（Slide 3–19）

## 1. CBSE 的定义 / Definition of CBSE（Slide 3）

**中文：**
CBSE 指的是一种主要基于 **软件组件 software components** 来开发软件的工程实践。它的核心思想不是把整个系统写成一个巨大的整体，而是把系统拆分成多个可以独立开发、复用、替换和组合的组件。

本节课重点关注三个核心原则：

1. **Components 组件**
2. **Interfaces 接口**
3. **Composition 组合**

除了这三个核心原则，课件还进一步讲解了：

- **Component Models 组件模型**
- **Middleware 中间件**
- 以及它们之间的关系。

**English:**
CBSE is a software engineering practice that develops software mainly based on **software components**. Instead of building one large monolithic system, CBSE decomposes the system into components that can be developed, reused, replaced, and composed independently.

The lecture focuses on three core principles:

1. **Components**
2. **Interfaces**
3. **Composition**

It also discusses:

- **Component Models**
- **Middleware**
- Their relationships in a CBSE system.

------

## 2. CBSE 的优点与挑战 / Benefits and Challenges（Slide 4）

### Benefits / 优点

| 中文                                                         | English                                                  |
| ------------------------------------------------------------ | -------------------------------------------------------- |
| **可复用性**：组件可以在不同系统中重复使用，减少开发时间和成本。 | **Reusability** reduces development time and cost.       |
| **模块化**：系统被拆分成独立模块，更容易维护和扩展。         | **Modularity** improves maintainability and scalability. |
| **易于测试和调试**：独立组件可以单独测试。                   | Isolated components are easier to test and debug.        |

### Challenges / 挑战

| 中文                                                         | English                                                      |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| **依赖管理和版本冲突**：组件之间可能依赖不同版本的库。       | Dependency management and version conflicts.                 |
| **组件通信开销**：组件之间通信可能产生额外开销。             | Overhead from inter-component communication.                 |
| **复用性与具体性平衡困难**：组件太通用可能不好用，太具体又难复用。 | Designing components that are reusable but still specific enough for practical use is difficult. |

------

## 3. Component 组件（Slide 5–7）

### 3.1 Component 的定义 / Definition（Slide 5）

**中文：**
在 CBSE 中，组件是一个 **模块化、可复用、可独立部署** 的软件单元。它封装了特定功能和数据，并通过清晰定义的接口向系统其他部分提供服务，同时隐藏内部实现细节。

**English:**
In CBSE, a component is a **modular, reusable, and independently deployable** software unit. It encapsulates specific functionality and data, provides services through well-defined interfaces, and hides internal implementation details.

### 3.2 Component 的特征 / Characteristics（Slide 6）

| 特征 / Characteristic | 中文解释                               | English Explanation                                          |
| --------------------- | -------------------------------------- | ------------------------------------------------------------ |
| Self-contained        | 每个组件封装自己的逻辑和数据。         | Each component encapsulates its own logic and data.          |
| Reusable              | 可以在不同系统或场景中复用。           | Designed to be used across different systems or contexts.    |
| Replaceable           | 只要接口一致，就可以替换成另一个组件。 | Can be swapped with another component that provides the same interface. |
| Interface-driven      | 组件只通过接口与其他组件交互。         | Components interact through defined interfaces only.         |

这也体现了软件设计中的 **low coupling 低耦合** 和 **high cohesion 高内聚**。

### 3.3 Spring Boot 中的组件 / Components in Spring Boot（Slide 7）

**中文：**
在 Spring Boot 中，组件通常是被以下注解标记的类：

- `@Component`
- `@Service`
- `@Repository`
- `@Controller`

这些注解会告诉 Spring 的 **IoC Container 控制反转容器** 来管理这些类，包括：

- 创建对象
- 注入依赖
- 管理生命周期

例如，`UserService` 是一个自包含组件，负责获取用户数据。其他部分可以使用它，而不需要知道它如何获取数据。

**English:**
In Spring Boot, components are usually classes annotated with:

- `@Component`
- `@Service`
- `@Repository`
- `@Controller`

These annotations tell the Spring **IoC container** to manage the class, including:

- Instantiation
- Dependency injection
- Lifecycle management

For example, `UserService` is a self-contained component that provides user data services. Other parts of the application can use it without knowing how it retrieves the data.

------

## 4. Interface 接口（Slide 8–9）

### 4.1 CBSE 中的 Interface / Interface in CBSE（Slide 8）

**中文：**
接口定义了组件必须遵守的 **契约 contract**。它说明组件提供什么服务，或者需要什么服务，但不暴露内部实现。

接口的作用是实现 **loose coupling 低耦合**。只要组件遵守同一个接口，就可以被替换。

**English:**
Interfaces define the **contract** that components must follow. They specify what services a component provides or requires without exposing internal implementation.

Interfaces enable **loose coupling** because components can be replaced as long as they follow the same interface.

### 4.2 Spring Boot 中的接口 / Interfaces in Spring Boot（Slide 9）

**中文：**
在 Spring 中，接口常用于定义服务契约，然后在运行时注入具体实现。例如，`UserRepository` 接口可以有不同实现，如：

- JPA
- JDBC
- In-memory implementation

服务层只依赖 `UserRepository` 这个接口，而不是具体实现。

**English:**
In Spring, interfaces are commonly used to define service contracts, with concrete implementations injected at runtime. For example, the `UserRepository` interface can be implemented by:

- JPA
- JDBC
- In-memory implementation

The service layer depends on the interface rather than concrete implementation.

------

## 5. Composition 组合（Slide 10–11）

### 5.1 CBSE 中的 Composition / Composition in CBSE（Slide 10）

**中文：**
组合是指通过组件之间的接口，把多个组件组装成一个完整系统。组件之间通过依赖关系连接起来，共同完成系统功能。

**English:**
Composition means assembling components into a complete system by connecting them through interfaces. Components are linked through dependencies to form a functional whole.

### 5.2 Spring Boot 中的 Composition / Composition in Spring Boot（Slide 11）

**中文：**
Spring Boot 主要通过 **Dependency Injection, DI 依赖注入** 来完成组件组合。例如：

- `UserService` 需要 `UserRepository`
- Spring 通过构造器注入把 `UserRepository` 注入到 `UserService`
- IoC 容器在运行时根据接口连接组件

**English:**
Spring Boot composes components mainly through **Dependency Injection (DI)**. For example:

- `UserService` depends on `UserRepository`
- Spring injects `UserRepository` into `UserService` through constructor injection
- The IoC container connects components at runtime based on interfaces

------

## 6. Component Model 组件模型（Slide 12–15）

### 6.1 Component Model 的定义 / Definition（Slide 12）

**中文：**
组件模型是一套框架或标准，用来规定组件如何被定义、实现和组合。

它提供：

- **Conventions 约定**：如何创建组件，例如如何定义接口
- **Interaction Mechanisms 交互机制**：组件如何通信，例如方法调用、事件
- **Lifecycle Management 生命周期管理**：组件如何创建、使用和销毁

**English:**
A component model is a framework or set of standards that governs how components are defined, implemented, and composed.

It provides:

- **Conventions**: rules for creating components
- **Interaction mechanisms**: how components communicate
- **Lifecycle management**: how components are instantiated, used, and destroyed

### 6.2 Component Model 的例子 / Examples（Slide 13）

课件列出的例子包括：

- **Enterprise JavaBeans, EJB**
- **Microsoft COM**
- **Spring**

这些组件模型的作用是确保系统中的组件具有一致性和互操作性。

Examples include:

- **Enterprise JavaBeans (EJB)**
- **Microsoft COM**
- **Spring**

A component model ensures consistency and interoperability across a system.

### 6.3 Spring Component Model（Slide 14）

**中文：**
Spring 组件模型基于普通 Java 对象，即 **POJO, Plain Old Java Object**，并通过注解增强：

- `@Component` 及其派生注解用于识别组件
- `@Autowired` 用于声明依赖
- Spring Boot 的自动配置会根据 classpath 中的依赖自动设置组件

**English:**
The Spring component model relies on **Plain Old Java Objects (POJOs)** enhanced with annotations:

- `@Component` and its derivatives identify components
- `@Autowired` specifies dependencies
- Spring Boot auto-configuration sets up components based on classpath dependencies

### 6.4 Component 与 Component Model 的关系（Slide 15）

**中文：**
组件模型定义“游戏规则”，而组件是遵守这些规则的具体实例。组件模型确保组件能够被管理、组合和运行。

**English:**
The component model defines the “rules of the game,” while components are the concrete instances that follow these rules.

------

## 7. Middleware 中间件（Slide 16–19）

### 7.1 Middleware 的定义 / Definition（Slide 16）

**中文：**
中间件是位于操作系统和应用程序之间的软件，用来简化组件交互和系统集成。

它负责：

- **Communication 通信**：让组件通信，即使跨网络，例如 RPC 或 messaging
- **Data Management 数据管理**：抽象数据库访问或缓存
- **Infrastructure Services 基础服务**：安全、事务管理、负载均衡等

**English:**
Middleware is software that sits between the operating system and applications, providing services that simplify component interaction and system integration.

It handles:

- **Communication**
- **Data management**
- **Infrastructure services**

### 7.2 Spring 中的 Middleware 例子 / Middleware in Spring（Slide 17）

| Spring Middleware | 中文解释                                       | English Explanation                                          |
| ----------------- | ---------------------------------------------- | ------------------------------------------------------------ |
| Spring Data       | 提供统一的数据访问层，连接组件和数据库。       | Provides a consistent data access layer between components and databases. |
| Spring Cloud      | 提供服务发现、负载均衡、熔断等分布式系统能力。 | Provides service discovery, load balancing, and circuit breaking. |

例如，一个 Spring Boot 应用可以通过 Spring Cloud 连接不同服务器上的 `UserService` 和 `UserRepository`，从而隐藏网络复杂性。

### 7.3 三者关系 / Components, Component Models, and Middleware（Slide 18–19）

| 关系                          | 中文解释                                                     | English Explanation                                          |
| ----------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Components + Component Models | 组件模型定义组件结构和交互方式，组件是模型的具体实现。       | Component models define how components are structured and interact. Components are concrete realizations. |
| Components + Middleware       | 中间件提供组件运行所需的服务，例如数据库访问。               | Middleware provides runtime services that components rely on. |
| Component Models + Middleware | 组件模型通常依赖特定中间件环境，例如 Spring 与 Spring Cloud。 | Component models often assume a specific middleware environment. |

课件总结的分层关系是：

- **Components** deliver customized functionality
  组件提供具体功能
- **Component Models** standardize creation and composition
  组件模型标准化组件创建和组合
- **Middleware** enables execution and interaction
  中间件支持组件执行和交互

------

# Part 2: Components in Spring Boot: Foundations / Spring Boot 组件基础（Slide 20–36）

## 8. Part 2 学习目标 / Objectives（Slide 20）

**中文：**

- 理解 Spring Boot 如何实现 CBSE 原则
- 理解组件定义和基础依赖注入

**English:**

- Learn how Spring Boot implements CBSE principles
- Understand component definition and basic dependency injection

------

## 9. Spring Boot Overview（Slide 21）

**中文：**
Spring Boot 是 Spring Framework 的扩展，它通过减少配置复杂度和提供默认配置，让开发者更容易构建可投入生产的应用。

核心特性：

1. **Auto-configuration 自动配置**
   根据 classpath 中存在的依赖自动配置组件。
2. **Embedded Servers 嵌入式服务器**
   内置 Tomcat 或 Jetty，应用不需要外部服务器就能运行。
3. **Opinionated Defaults 有倾向性的默认设置**
   提供常见任务的预配置，开发者可以按需覆盖。

**English:**
Spring Boot is an extension of the Spring Framework that streamlines production-ready application development by reducing configuration complexity and providing sensible defaults.

Key features:

1. **Auto-configuration**
2. **Embedded servers**
3. **Opinionated defaults**

------

## 10. Spring Boot for CBSE（Slide 22）

**中文：**
Spring Boot 本身非常适合 CBSE，因为：

- 组件由 Spring IoC 容器管理，支持模块化和复用
- DI 促进组件之间低耦合
- 自动配置和 starter dependencies 简化组件集成和组合

**English:**
Spring Boot is naturally component-based because:

- Components are managed by the Spring IoC container
- Dependency injection promotes loose coupling
- Auto-configuration and starter dependencies simplify component composition

------

## 11. Spring Boot 中的 Component（Slide 23–24）

### 11.1 Core Annotations / 核心注解（Slide 23）

| 注解 / Annotation                 | 中文解释                 | English Explanation             |
| --------------------------------- | ------------------------ | ------------------------------- |
| `@Component`                      | 通用 Spring-managed bean | General Spring-managed bean     |
| `@Service`                        | 业务逻辑组件             | Business logic component        |
| `@Repository`                     | 数据访问组件             | Data access component           |
| `@Controller` / `@RestController` | HTTP 请求处理组件        | HTTP request handling component |

### 11.2 Component Scanning / 组件扫描（Slide 23）

**中文：**
Spring Boot 通过 **component scanning** 自动发现和注册组件。默认情况下，它扫描主应用类所在包及其子包。

**English:**
Spring Boot uses **component scanning** to automatically detect and register components. By default, it scans the package containing the main application class and its sub-packages.

### 11.3 `@Service` 例子 / Example（Slide 24）

课件展示了一个 `GreetingService`：

```java
@Service
public class GreetingService {
    public String greet() {
        return "Hello, World!";
    }
}
```

**中文解释：**
`@Service` 标记 `GreetingService` 是一个服务组件。Spring Boot 在组件扫描时发现它，并注册为 IoC 容器中的 bean。

**English Explanation:**
`@Service` marks `GreetingService` as a component. Spring Boot detects it during component scanning and registers it as a bean in the IoC container.

------

## 12. Inversion of Control, IoC 控制反转（Slide 25）

**中文：**
IoC 是 Spring 组件管理系统的核心思想。传统方式中，应用代码自己创建对象；而在 IoC 中，框架负责创建和管理对象。

IoC 容器的作用：

- 创建组件，也就是 beans
- 配置组件，注入依赖和属性
- 管理组件从创建到销毁的生命周期
- 把 beans 存储在 application context 中

**English:**
IoC means the framework takes control of creating and managing objects instead of the application code doing it manually.

The IoC container:

- Instantiates components, called beans
- Configures them by injecting dependencies and properties
- Manages lifecycle from creation to destruction
- Stores beans in the application context

------

## 13. Dependency Injection, DI 依赖注入（Slide 26–30）

### 13.1 DI 的定义 / Definition（Slide 26）

**中文：**
依赖注入是一种设计模式。组件所需要的依赖不是自己创建，而是由框架提供。

它可以提升：

- 模块化
- 可测试性
- 可维护性

**English:**
Dependency Injection is a design pattern where a component’s dependencies are provided by the framework rather than instantiated inside the component itself.

It improves:

- Modularity
- Testability
- Maintainability

### 13.2 DI 类型 / Types of DI（Slide 26–29）

| 类型 / Type           | 中文解释                                               | English Explanation                                          |
| --------------------- | ------------------------------------------------------ | ------------------------------------------------------------ |
| Constructor Injection | 构造器注入，适合 mandatory dependencies，是推荐方式。  | Recommended for mandatory dependencies.                      |
| Setter Injection      | Setter 注入，适合 optional dependencies 或运行时变化。 | Suitable for optional dependencies or runtime changes.       |
| Field Injection       | 直接注入字段，不太推荐，因为测试性较差。               | Direct field injection, less preferred due to testability concerns. |

### 13.3 代码例子 / Code Examples（Slide 27–29）

**Constructor Injection 构造器注入（Slide 27）**
课件中 `OrderService` 通过构造器接收 `PaymentService`。字段是 `final`，表示依赖一旦注入后不可变。

```java
@Service
public class OrderService {
    private final PaymentService paymentService;

    @Autowired
    public OrderService(PaymentService paymentService) {
        this.paymentService = paymentService;
    }
}
```

**Setter Injection Setter 注入（Slide 28）**
`NotificationService` 通过 setter 方法注入 `EmailService`。

```java
@Service
public class NotificationService {
    private EmailService emailService;

    @Autowired
    public void setEmailService(EmailService emailService) {
        this.emailService = emailService;
    }
}
```

**Field Injection 字段注入（Slide 29）**
`UserService` 直接在字段上使用 `@Autowired` 注入 `UserRepository`。

```java
@Service
public class UserService {
    @Autowired
    private UserRepository userRepository;
}
```

### 13.4 DI 的优点 / Advantages of DI（Slide 30）

| 优点 / Advantage | 中文解释                                   | English Explanation                                          |
| ---------------- | ------------------------------------------ | ------------------------------------------------------------ |
| Decoupling       | 组件不需要知道依赖如何被创建。             | Components are independent of how dependencies are created.  |
| Testability      | 测试时可以 mock 或 stub 依赖。             | Dependencies can be mocked or stubbed in tests.              |
| Flexibility      | 可以替换或重新配置依赖，而不用改组件代码。 | Dependencies can be swapped or reconfigured without changing component code. |

------

## 14. Component Discovery and Customization 组件发现与自定义（Slide 31–32）

### 14.1 `@ComponentScan`（Slide 31）

**中文：**
默认情况下，Spring 扫描主应用类所在包和子包。可以通过 `@ComponentScan` 自定义扫描路径。

课件代码表达的是：

```java
@SpringBootApplication
@ComponentScan(basePackages = {
    "com.example.services",
    "com.example.repositories"
})
public class MyApplication {
    public static void main(String[] args) {
        SpringApplication.run(MyApplication.class, args);
    }
}
```

**English:**
Spring scans the main application package and sub-packages by default. `@ComponentScan` customizes scanning paths.

### 14.2 `@Bean` 显式定义 Bean（Slide 32）

**中文：**
可以在配置类中用 `@Bean` 明确定义 bean。这个方式适合：

- 第三方类
- 需要更多控制的对象

课件例子中，`AppConfig` 使用 `@Bean` 创建 `HikariDataSource`。

```java
@Configuration
public class AppConfig {
    @Bean
    public DataSource dataSource() {
        return new HikariDataSource();
    }
}
```

**English:**
Beans can be explicitly defined in a configuration class using `@Bean`. This is useful for third-party classes or when more control is needed.

------

## 15. Practical Example: Simple REST API（Slide 33–36）

课件用一个简单 REST API 展示 Spring Boot 组件如何组合。

### 15.1 Product Model（Slide 33）

**中文：**
`Product` 类包含：

- `id`
- `name`
- `price`

并提供：

- 构造器
- getter/setter

**English:**
The `Product` class contains:

- `id`
- `name`
- `price`

It also provides a constructor and getter/setter methods.

### 15.2 ProductService（Slide 34）

**中文：**
`ProductService` 被 `@Service` 标记，负责返回产品列表。课件中为了简单起见，数据是 hardcoded：

- Laptop: 999.99
- Smartphone: 499.99

**English:**
`ProductService` is annotated with `@Service` and returns a list of products. For simplicity, the data is hardcoded:

- Laptop: 999.99
- Smartphone: 499.99

### 15.3 ProductController（Slide 35）

**中文：**
`ProductController` 被标记为：

- `@RestController`
- `@RequestMapping("/api/products")`

它通过构造器注入 `ProductService`，并用 `@GetMapping` 提供获取产品列表的接口。

**English:**
`ProductController` is annotated with:

- `@RestController`
- `@RequestMapping("/api/products")`

It receives `ProductService` through constructor injection and exposes a `@GetMapping` endpoint.

### 15.4 Main Application（Slide 36）

**中文：**
主程序类使用：

- `@SpringBootApplication`
- `SpringApplication.run(ProductApplication.class, args)`

启动应用。

**English:**
The main application class uses:

- `@SpringBootApplication`
- `SpringApplication.run(ProductApplication.class, args)`

to start the application.

------

# Part 3: Component Interfaces, Composition, and Lifecycle / 组件接口、组合与生命周期（Slide 37–54）

## 16. Part 3 学习目标 / Objectives（Slide 37）

**中文：**

- 理解接口如何实现组件抽象
- 理解组件组合技术和生命周期管理

**English:**

- Understand interfaces for component abstraction
- Explore component composition and lifecycle management

------

## 17. Interfaces in CBSE and Spring Boot（Slide 38–41）

### 17.1 接口的作用 / Role of Interfaces（Slide 38–39）

**中文：**
接口是 CBSE 的核心，因为它建立组件必须遵守的契约。接口说明组件提供的能力和需要的依赖。

接口带来三个好处：

- **Polymorphism 多态**：同一个接口可以有不同实现
- **Loose Coupling 低耦合**：组件依赖抽象，而不是具体类
- **Testability 可测试性**：测试时可以 mock 接口

**English:**
Interfaces are central to CBSE because they establish contracts. They specify component capabilities and dependencies.

They provide:

- **Polymorphism**
- **Loose coupling**
- **Testability**

### 17.2 PaymentProcessor 例子（Slide 40）

课件例子：

- `PaymentProcessor` 是接口
- `CreditCardProcessor` 和 `PayPalProcessor` 是具体实现
- 它们都可以被互换使用

**中文：**
这说明业务代码不需要关心具体支付方式，只需要调用 `PaymentProcessor` 的方法即可。

**English:**
This shows that business code does not need to know the concrete payment method. It only depends on the `PaymentProcessor` interface.

### 17.3 Benefits of Interfaces（Slide 41）

| Benefit       | 中文解释                                     | English Explanation                                          |
| ------------- | -------------------------------------------- | ------------------------------------------------------------ |
| Flexibility   | 可以从信用卡切换到 PayPal。                  | Switch from credit card to PayPal by injecting another implementation. |
| Extensibility | 可以增加 CryptoProcessor，而不用改已有代码。 | Add `CryptoProcessor` without modifying existing code.       |
| Testability   | 测试时可以 mock `PaymentProcessor`。         | Mock `PaymentProcessor` in tests.                            |

------

## 18. Composition Techniques 组合技术（Slide 42–43）

### 18.1 Composition 的定义 / Definition（Slide 42）

**中文：**
组合是把多个组件通过接口连接起来，形成一个可运行系统。Spring Boot 主要通过 DI 自动提供依赖。

**English:**
Composition means assembling components into a working system through interfaces. Spring Boot primarily achieves this through DI.

### 18.2 DI Best Practice（Slide 43）

**中文：**

- 优先使用 **Constructor Injection**，因为它适合必须依赖，并且更明确、更不可变。
- 少用 **Setter Injection**，只在可选依赖或可重新配置依赖中使用。
- 推荐使用构造器注入或 setter 注入来提高可测试性和可维护性。

**English:**

- Prefer **Constructor Injection** for mandatory dependencies.
- Use **Setter Injection** sparingly for optional or reconfigurable dependencies.
- Constructor or setter injection improves testability and maintainability.

------

## 19. Component Lifecycle Management 组件生命周期管理（Slide 44–48）

### 19.1 生命周期管理的定义 / Definition（Slide 44）

**中文：**
Spring Boot 的 IoC 容器管理 bean 的完整生命周期，从创建到销毁。理解生命周期可以让开发者在合适时间执行初始化任务和清理任务。

**English:**
Spring Boot’s IoC container manages the complete lifecycle of beans from instantiation to destruction. Understanding it helps developers perform initialization and cleanup tasks properly.

### 19.2 生命周期阶段 / Lifecycle Phases（Slide 45）

| 阶段 / Phase         | 中文解释                              | English Explanation                                          |
| -------------------- | ------------------------------------- | ------------------------------------------------------------ |
| Creation             | IoC 容器创建 bean 实例。              | The IoC container creates the bean instance.                 |
| Dependency Injection | 根据构造器、setter 或字段注入依赖。   | Dependencies are injected through constructor, setter, or field injection. |
| Initialization       | 依赖注入后执行初始化逻辑。            | Initialization logic runs after dependency injection.        |
| Usage                | bean 完全初始化，可以被其他组件使用。 | The bean is fully initialized and available for use.         |
| Destruction          | 应用关闭前执行销毁逻辑。              | Destruction logic runs before the application context closes. |

关键注解：

- `@PostConstruct`：bean 构造和依赖注入完成后执行
- `@PreDestroy`：bean 销毁前执行

### 19.3 Lifecycle Code Example（Slide 46）

课件中展示了 `CacheService`：

- 用 `HashMap` 存储缓存数据
- `@PostConstruct init()` 在启动时初始化缓存
- `put()` 和 `get()` 用于操作缓存
- `@PreDestroy cleanup()` 在关闭时清空缓存

**中文：**
这个例子说明生命周期钩子可以用来加载资源和释放资源。

**English:**
This example shows lifecycle hooks can be used for loading resources and releasing resources.

### 19.4 为什么生命周期管理重要 / Why Lifecycle Management Matters（Slide 47）

| 原因 / Reason           | 中文解释                               | English Explanation                                          |
| ----------------------- | -------------------------------------- | ------------------------------------------------------------ |
| Resource Initialization | 建立连接、加载配置、预加载缓存。       | Set up connections, load configuration, or pre-populate cache. |
| Resource Cleanup        | 释放数据库连接、文件句柄、内存等资源。 | Release database connections, file handles, and memory.      |
| Controlled Behavior     | 确保组件优雅启动和停止。               | Ensure components start and stop gracefully.                 |

### 19.5 Component Design Best Practices（Slide 48）

中文与英文对应如下：

| Best Practice                     | 中文解释                                 |
| --------------------------------- | ---------------------------------------- |
| Define Interfaces for Abstraction | 用接口实现抽象。                         |
| Favor Constructor Injection       | 优先使用构造器注入。                     |
| Single Responsibility Principle   | 每个组件只负责一个职责。                 |
| Leverage Lifecycle Hooks          | 使用 `@PostConstruct` 和 `@PreDestroy`。 |
| Avoid Circular Dependencies       | 避免循环依赖。                           |
| Document Interfaces               | 用 JavaDoc 等方式记录接口说明。          |

------

## 20. Practical Example: Composing Components with Interfaces（Slide 49–54）

### 20.1 Scenario 场景（Slide 49）

**中文：**
`OrderService` 依赖：

- `PaymentProcessor` 接口，有多个实现
- `NotificationService`

系统下单时处理付款并发送通知。

**English:**
`OrderService` depends on:

- `PaymentProcessor` interface with multiple implementations
- `NotificationService`

The system processes payment and sends notifications when an order is placed.

### 20.2 PaymentProcessor Interface（Slide 49）

```java
public interface PaymentProcessor {
    void processPayment(double amount);
}
```

**中文：**
这是支付组件的统一接口。

**English:**
This is the common interface for payment components.

### 20.3 Concrete Payment Processors（Slide 50）

课件中有两个实现：

- `CreditCardProcessor`
- `PayPalProcessor`

它们都实现 `PaymentProcessor`，并提供自己的 `processPayment()` 逻辑。

**中文：**
这体现了接口驱动设计：不同支付方式可以互换。

**English:**
This demonstrates interface-driven design: different payment methods are interchangeable.

### 20.4 NotificationService（Slide 51）

`NotificationService` 提供 `sendNotification(String message)`，用于发送通知。

**中文：**
这个组件负责通知逻辑，符合单一职责原则。

**English:**
This component handles notification logic, following the Single Responsibility Principle.

### 20.5 OrderService Composition（Slide 52）

`OrderService` 通过构造器注入：

- `PaymentProcessor`
- `NotificationService`

下单方法 `placeOrder()` 会：

1. 调用支付组件处理金额
2. 调用通知组件发送成功消息

**English:**
`OrderService` uses constructor injection to receive:

- `PaymentProcessor`
- `NotificationService`

`placeOrder()` processes payment and sends a success notification.

### 20.6 Resolving Multiple Implementations: `@Primary`（Slide 53）

**中文：**
当一个接口有多个实现时，Spring 不知道应该注入哪一个。可以使用 `@Primary` 指定默认实现。

例如把 `CreditCardProcessor` 标记为 `@Primary`，Spring 默认选择它。

**English:**
When multiple beans implement the same interface, Spring may not know which one to inject. `@Primary` specifies the default implementation.

### 20.7 Resolving Multiple Implementations: `@Qualifier`（Slide 54）

**中文：**
`@Qualifier` 可以指定具体要注入哪个 bean。例如在构造器参数中使用：

```java
@Qualifier("creditCardProcessor")
```

这样可以明确选择信用卡支付实现。

**English:**
`@Qualifier` specifies the exact bean to inject, for example:

```java
@Qualifier("creditCardProcessor")
```

This explicitly selects the credit card payment implementation.

------

# Part 4: Advanced Component Features in Spring Boot / Spring Boot 高级组件特性（Slide 55–71）

## 21. Part 4 学习目标 / Objectives（Slide 55）

**中文：**
本部分学习 Spring Boot 中高级组件管理技术，包括：

- Custom scopes 自定义作用域
- Lazy loading 延迟加载
- Dynamic dependency injection 动态依赖注入
- Conditional bean creation 条件式 bean 创建

目标是设计灵活、可扩展，并符合 CBSE 原则的应用。

**English:**
This part explores advanced Spring Boot component management techniques:

- Custom scopes
- Lazy loading
- Dynamic dependency injection
- Conditional bean creation

The goal is to design flexible and scalable applications aligned with CBSE principles.

------

## 22. Advanced Features Overview（Slide 56）

本部分包括：

1. **Component Scopes with Real-World Scenarios**
2. **Advanced Dependency Resolution**
3. **Programmatic Bean Definition with Conditions**

这些概念可以解决现实问题，例如：

- 循环依赖
- 运行时配置
- 动态选择组件

These concepts solve real-world problems such as:

- Circular dependencies
- Runtime configuration
- Dynamic component selection

------

## 23. Component Scopes 组件作用域（Slide 57–59）

### 23.1 Standard Scopes / 标准作用域（Slide 57）

| Scope     | 中文解释                                             | English Explanation                                 |
| --------- | ---------------------------------------------------- | --------------------------------------------------- |
| Singleton | 每个 ApplicationContext 只有一个实例，是默认作用域。 | One instance per ApplicationContext, default scope. |
| Prototype | 每次请求创建一个新实例。                             | New instance per request.                           |

### 23.2 Web-Specific Scopes / Web 特定作用域（Slide 57）

| Scope       | 中文解释                       | English Explanation              |
| ----------- | ------------------------------ | -------------------------------- |
| Request     | 每个 HTTP request 一个实例。   | One instance per HTTP request.   |
| Session     | 每个用户 session 一个实例。    | One instance per user session.   |
| Application | 每个 ServletContext 一个实例。 | One instance per ServletContext. |

### 23.3 Custom Scopes / 自定义作用域（Slide 57）

**中文：**
可以定义自定义 scope，例如：

- thread-local scope
- transaction-specific scope

**English:**
Custom scopes can be defined for special cases, such as:

- thread-local scope
- transaction-specific scope

### 23.4 Request Scope Examples（Slide 58）

**Request Scope 适合：**

1. **Tracking Request-Specific Metrics**
   例如在电商 API 中跟踪每个请求的处理时间、数据库查询次数。
2. **Temporary User Input Validation**
   例如用户提交复杂表单时，只在当前请求中验证和处理数据。

**English:**
Request scope is suitable for:

1. Tracking request-specific metrics
2. Temporary user input validation

### 23.5 Session Scope Examples（Slide 59）

**Session Scope 适合：**

1. **Shopping Cart Management**
   用户跨多个请求添加商品到购物车，直到 checkout。
2. **Multi-Step User Registration Wizard**
   用户分步骤完成注册，例如个人信息、地址、支付信息。

**English:**
Session scope is suitable for:

1. Shopping cart management
2. Multi-step user registration wizard

------

## 24. Advanced Dependency Resolution 高级依赖解析（Slide 60–67）

### 24.1 为什么需要高级依赖管理 / Why It Is Needed（Slide 60–62）

**中文：**
随着应用变复杂，基本的 `@Autowired` 可能不够。大型系统中可能出现复杂关系、运行时条件、灵活性和可维护性需求。

需要高级技术：

- `@Lazy`
- `ObjectProvider`
- `@Qualifier`
- Programmatic bean definitions

**English:**
As applications grow, basic `@Autowired` may not be enough. Complex systems require advanced dependency management techniques such as:

- `@Lazy`
- `ObjectProvider`
- `@Qualifier`
- Programmatic bean definitions

### 24.2 主要问题 / Main Problems（Slide 61–62）

| 问题 / Problem                      | 中文解释                                        | English Explanation                                          |
| ----------------------------------- | ----------------------------------------------- | ------------------------------------------------------------ |
| Ambiguity                           | 多个 bean 实现同一个接口，Spring 不知道选哪个。 | Multiple beans implement the same interface.                 |
| Circular Dependencies               | 两个 bean 互相依赖，Spring 启动时可能失败。     | Two beans depend on each other and Spring may fail during initialization. |
| Dynamic or Conditional Dependencies | 根据配置、环境或用户输入选择依赖。              | Select dependencies based on configuration, environment, or user input. |
| Performance Optimization            | 大系统中 eager initialization 会拖慢启动。      | Eager initialization may slow startup in large systems.      |
| Scalability and Flexibility         | 硬编码依赖限制系统扩展。                        | Hardcoded dependencies reduce adaptability.                  |
| Testing and Maintenance             | 紧耦合依赖让 mock 和替换更困难。                | Tightly coupled dependencies make mocking and replacement harder. |

### 24.3 Ambiguity Resolution: `@Primary`, `@Qualifier`, `ObjectProvider`（Slide 63–64）

**中文：**
当多个 bean 实现同一个接口时，可以用：

- `@Primary`：指定默认实现
- `@Qualifier`：指定具体实现
- `ObjectProvider`：在运行时动态获取候选 bean，更灵活

**Slide 64 图中代码含义：**
`DynamicOrderService` 注入 `ObjectProvider<PaymentProcessor>`，然后根据 `paymentType` 从多个 processor 中筛选匹配的实现，再调用 `process(amount)`。`OrderController` 接收 `amount` 和 `paymentType`，调用 service 下单。

**English:**
When multiple beans implement the same interface, we can use:

- `@Primary`
- `@Qualifier`
- `ObjectProvider`

In Slide 64, `DynamicOrderService` injects `ObjectProvider<PaymentProcessor>`, selects a processor based on `paymentType`, and processes the payment. `OrderController` receives `amount` and `paymentType`.

### 24.4 Circular Dependencies 循环依赖（Slide 65–67）

**Scenario / 场景（Slide 65）：**

- `ProductService` 需要 `InventoryService` 来检查库存
- `InventoryService` 又需要 `ProductService` 来获取产品详情

这会形成循环依赖。

**Using `@Lazy` / 使用 `@Lazy`（Slide 66）：**

**中文：**
如果依赖被标记为 `@Lazy`，Spring 启动时不会立刻注入真正的目标 bean，而是注入一个 proxy object 代理对象。等真正使用时再创建目标 bean。

Slide 66 的表格含义：

| Step | Action                                                       | ProductService | InventoryService |
| ---- | ------------------------------------------------------------ | -------------- | ---------------- |
| 1    | Spring 开始创建 ProductService                               | Instantiating  | Not Started      |
| 2    | 发现 ProductService 需要 `@Lazy InventoryService`，创建 proxy 后继续创建 ProductService | Created        | Not Started      |
| 3    | Spring 开始创建 InventoryService                             | Created        | Instantiating    |
| 4    | InventoryService 需要 ProductService，Spring 从缓存中找到已创建的 ProductService 并注入 | Created        | Created          |

**Without `@Lazy` / 不使用 `@Lazy`（Slide 67）：**

Slide 67 的表格说明：

1. Spring 尝试初始化 ProductService，状态 pending
2. ProductService 需要 InventoryService，于是暂停并寻找 InventoryService
3. Spring 尝试初始化 InventoryService，状态 pending
4. InventoryService 又需要 ProductService，于是再寻找 ProductService
5. Spring 发现 ProductService 仍在创建中，最终 crash

**English:**
`@Lazy` solves circular dependencies by injecting a proxy instead of the actual target bean during startup. Without `@Lazy`, Spring may crash because each service waits for the other to finish creation.

------

## 25. Programmatic Bean Definition with Conditions 条件式编程定义 Bean（Slide 68–71）

### 25.1 定义 / Definition（Slide 68）

**中文：**
Programmatic bean definition 是指通过 Java 代码显式创建和配置 bean，通常使用：

- `@Configuration`
- `@Bean`

也可以配合：

- `@Conditional`：根据运行时条件创建 bean
- `BeanPostProcessor`：全局自定义 bean 创建过程

**English:**
Programmatic bean definition means explicitly creating and configuring beans using Java code, usually with:

- `@Configuration`
- `@Bean`

It can also use:

- `@Conditional`
- `BeanPostProcessor`

### 25.2 为什么需要 / Why Needed（Slide 69）

| 原因 / Reason                   | 中文解释                                        | Example                           |
| ------------------------------- | ----------------------------------------------- | --------------------------------- |
| Fine-Grained Control            | 自动扫描的自定义能力有限。                      | 配置第三方对象。                  |
| Dynamic or Conditional Creation | 根据运行时条件创建不同 bean。                   | 根据 property file 加载不同实现。 |
| Third-Party Library Integration | 第三方库没有 Spring 注解，需要手动包装成 bean。 | HikariCP 数据库连接池。           |

### 25.3 Conditional Bean Example（Slide 70）

**中文：**
课件场景：只在 production 环境启用 logging service。

代码含义：

- 在配置类中用 `@Bean` 创建 `LoggingService`
- 使用类似 `@ConditionalOnProperty(name = "app.environment", havingValue = "prod")`
- 只有配置为 `prod` 时才创建该 bean
- `LoggingService` 中用 `@PostConstruct` 打印初始化信息

**English:**
Scenario: enable a logging service only in production.

The bean is created only when the property `app.environment` has value `prod`.

### 25.4 Third-Party Library Bean Example（Slide 71）

**中文：**
课件场景：电商 API 需要集成第三方支付 SDK，例如 Stripe，但 Stripe SDK 没有 Spring 注解。

解决方式：

- 在 `PaymentConfig` 中使用 `@Bean` 创建 `StripeRequestOptions`
- 配置 API key、连接超时、读取超时等参数
- `PaymentService` 通过构造器注入 `StripeRequestOptions`
- 然后用这个第三方 SDK 配置处理支付

**English:**
Scenario: integrate a third-party payment SDK such as Stripe.

Solution:

- Use `@Bean` in `PaymentConfig` to create `StripeRequestOptions`
- Configure API key, connection timeout, and read timeout
- Inject the configuration into `PaymentService`

------

# Part 5: Component-Based Architecture with Spring Boot / Spring Boot 中的组件化架构（Slide 72–95）

## 26. Part 5 学习目标 / Objectives（Slide 72–73）

**中文：**
本部分介绍 Spring Boot 中的高级架构模式，包括：

- **Domain-Driven Design, DDD 领域驱动设计**
- **Hexagonal Architecture 六边形架构 / Ports and Adapters 架构**

目标是构建一个稳健、模块化，并符合 CBSE 原则的电商系统。

**English:**
This part explores advanced architectural patterns in Spring Boot:

- **Domain-Driven Design (DDD)**
- **Hexagonal Architecture / Ports and Adapters**

The goal is to create a robust, modular e-commerce system aligned with CBSE principles.

------

## 27. Domain-Driven Design, DDD 领域驱动设计（Slide 74–86）

### 27.1 DDD 的定义 / Definition（Slide 74）

**中文：**
DDD 是一种让软件结构与业务领域对齐的设计方法。它强调根据真实业务概念来设计系统，从而提升模块化和清晰度。

核心概念：

- **Entities 实体**
- **Aggregates 聚合**
- **Bounded Contexts 限界上下文**

**English:**
DDD is a design approach that aligns software structure with business domains, promoting modularity and clarity.

Key concepts:

- **Entities**
- **Aggregates**
- **Bounded Contexts**

------

## 28. Entity 实体（Slide 75–76）

### 28.1 Entity 的定义 / Definition（Slide 75）

**中文：**
Entity 是领域模型中具有明确身份和生命周期的对象。它通过唯一标识符，例如 ID，来区分，即使它的状态改变，身份仍然不变。

实体表示领域中需要被单独追踪的“东西”。

**English:**
An entity is an object in the domain model that has a distinct identity and lifecycle. It is identified by a unique identifier, such as an ID, that persists across state changes.

### 28.2 Product Entity Example（Slide 76）

Slide 76 中的 `Product` 实体包含：

- `id`
- `name`
- `price`
- `stock`

并包含业务方法：

- `reduceStock(int quantity)`
  如果库存不足，会抛出异常；否则减少库存。
- `updatePrice(double newPrice)`
  如果价格为负数，会抛出异常；否则更新价格。

**中文：**
这个例子说明 entity 不只是数据容器，它也可以包含与自身相关的业务规则。

**English:**
This example shows that an entity is not just a data container. It can also contain business rules related to itself.

------

## 29. Aggregate 聚合（Slide 77–78）

### 29.1 Aggregate 的定义 / Definition（Slide 77）

**中文：**
Aggregate 是一组相关 entity 和 value object 的集合，它们被当作一个整体来维护数据一致性和事务边界。

每个 aggregate 都有一个 **aggregate root 聚合根**。外部对象应该通过聚合根访问整个聚合。

**English:**
An aggregate is a cluster of related entities and value objects treated as a single unit for data consistency and transactional boundaries.

Each aggregate has an **aggregate root**, which serves as the entry point.

### 29.2 Order Aggregate Example（Slide 77–78）

课件中的电商例子：

- `Order` 是 aggregate root
- `OrderItem` 是聚合内部的 entity
- `Order` 包含多个 `OrderItem`
- 订单总金额必须与所有 item 的数量和单价一致
- 库存预留必须以原子方式完成

Slide 78 代码图展示：

`Order` 类包含：

- `id`
- `orderItems`
- `status`
- `addItem()`
- `calculateTotal()`

`OrderItem` 类包含：

- `id`
- `productId`
- `quantity`
- `unitPrice`
- `order`

**中文：**
Aggregate 的重点是控制一致性。比如订单和订单项不能随便分开修改，应该通过 `Order` 这个聚合根统一管理。

**English:**
The key purpose of an aggregate is consistency. For example, `Order` and `OrderItem` should be managed through the `Order` aggregate root.

------

## 30. Bounded Context 限界上下文（Slide 79–86）

### 30.1 Bounded Context 的定义 / Definition（Slide 79–80）

**中文：**
Bounded Context 是一个边界，在这个边界内，一个领域模型才有明确含义和适用范围。

它把大型复杂领域拆分成更小、更可管理的部分。每个 bounded context 都有自己的：

- Domain Model 领域模型
- Ubiquitous Language 通用语言
- Rules and Assumptions 规则和假设

它可以避免整个系统形成一个庞大、混乱、过度泛化的领域模型。

**English:**
A bounded context is a boundary within which a domain model is defined and applicable.

Each bounded context has its own:

- Domain model
- Ubiquitous language
- Rules and assumptions

It prevents the domain model from becoming a monolithic and overly generalized mess.

### 30.2 E-commerce Example: ProductCatalog（Slide 81–82）

**ProductCatalog 负责：**

- 维护产品详情，例如 name、price、stock
- 管理库存水平，例如减少库存
- 向其他上下文提供产品信息

**Ubiquitous Language：**

| Term         | 中文解释           | English Meaning                         |
| ------------ | ------------------ | --------------------------------------- |
| Product      | 库存中可出售的商品 | An item in inventory available for sale |
| Stock        | 商品可购买数量     | Quantity available for purchase         |
| Reduce Stock | 为订单预留库存     | Reserve stock for an order              |
| Restock      | 从供应商补充库存   | Add more units from supplier            |

**Boundaries：**

| Included            | Excluded         |
| ------------------- | ---------------- |
| Product definitions | Order processing |
| Stock management    | Customer details |
| Catalog operations  | Payment handling |

### 30.3 E-commerce Example: OrderManagement（Slide 83–84）

**OrderManagement 负责：**

- 创建和管理订单
- 根据下单时的产品价格计算订单总额
- 跟踪订单状态，例如 pending、confirmed、shipped

**Ubiquitous Language：**

| Term          | 中文解释                 | English Meaning                           |
| ------------- | ------------------------ | ----------------------------------------- |
| Order         | 客户购买产品的请求       | A customer’s request to purchase products |
| Order Item    | 订单中的一行商品         | A line item in an order                   |
| Total Amount  | 根据订单项计算出的总金额 | Calculated cost of the order              |
| Confirm Order | 验证后最终确认订单       | Finalize the order after validation       |

**Boundaries：**

| Included          | Excluded                  |
| ----------------- | ------------------------- |
| Order creation    | Stock management          |
| Total calculation | Product catalog updates   |
| Status tracking   | Product inventory details |

### 30.4 Benefits of Bounded Context（Slide 85）

| Benefit          | 中文解释                                         | English Explanation                                          |
| ---------------- | ------------------------------------------------ | ------------------------------------------------------------ |
| Clarity          | “Product” 在不同上下文中含义清晰。               | “Product” has clear meaning in each context.                 |
| Modularity       | 每个 context 可以独立演化。                      | Each context can evolve independently.                       |
| Reduced Coupling | 不共享数据库或模型，通过接口或事件通信。         | No shared database or model; communicate via interfaces or events. |
| Scalability      | ProductCatalog 和 OrderManagement 可以分开部署。 | Contexts can be deployed separately, aligning with microservices. |

### 30.5 Challenges of Bounded Context（Slide 86）

| Challenge              | 中文解释                                                     | English Explanation                                          |
| ---------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Context Mapping        | 需要定义不同 context 的关系，例如 client/supplier。          | Need to define how contexts relate.                          |
| Other Mapping Patterns | 可能使用 Anticorruption Layer 或 Published Language with Event-Driven Integration。 | Possible mapping patterns include Anticorruption Layer and Published Language with Event-Driven Integration. |
| Duplication            | 某些数据会重复，例如 OrderItem 中保存 product name。         | Some data may be duplicated intentionally.                   |
| Integration Overhead   | REST 或 message queue 会增加复杂度。                         | REST calls or message queues add latency and error handling complexity. |

------

## 31. Hexagonal Architecture / Ports and Adapters 六边形架构（Slide 87–95）

### 31.1 定义 / Definition（Slide 87）

**中文：**
六边形架构由 Alistair Cockburn 提出。它是一种将应用业务逻辑核心与外部系统解耦的架构风格。

外部系统包括：

- 数据库
- 用户界面
- API
- 第三方服务

它通过两个概念实现解耦：

- **Ports 端口**：接口，说明核心需要什么或提供什么
- **Adapters 适配器**：具体实现，把端口连接到外部系统

**English:**
Hexagonal architecture, introduced by Alistair Cockburn, decouples application business logic from external systems such as databases, user interfaces, and APIs.

It uses:

- **Ports**: interfaces specifying what the core needs or provides
- **Adapters**: concrete implementations connecting ports to external systems

### 31.2 Core, Ports, and Adapters（Slide 88）

**中文：**
业务逻辑位于中心，也就是 “hexagon”。外部系统只能通过清晰边界与核心交互。

Ports 分为：

| Port Type      | 中文解释                                                     | English Explanation                          |
| -------------- | ------------------------------------------------------------ | -------------------------------------------- |
| Inbound Ports  | 核心向外界提供的服务，例如 API endpoint 对应的业务服务接口。 | Services the core provides to the outside.   |
| Outbound Ports | 核心需要外部提供的服务，例如数据持久化接口。                 | Services the core requires from the outside. |

Adapters 包括：

- REST controllers
- JPA repositories
- Redis adapters
- Third-party service adapters

### 31.3 Product Example Diagram（Slide 89）

Slide 89 图中展示了一个 Product 例子：

- `ProductController` 是 **inbound adapter**
- `ProductServicePort` 是核心对外提供的入口接口
- `ProductService` 是 **business logic**
- `ProductPort` 是 outbound port
- `JpaProductAdapter` 和 `RedisProductAdapter` 是 outbound adapters
- `ProductJpaRepository` 和 `RedisTemplate` 是外部技术细节

**中文：**
这个图强调核心业务逻辑不直接依赖数据库或 Redis，而是依赖 `ProductPort` 接口。

**English:**
The diagram shows that core business logic does not directly depend on JPA or Redis. It depends on the `ProductPort` interface.

### 31.4 Ports Code（Slide 90）

Slide 90 中展示了两个接口：

**Outbound Port:**

```java
public interface ProductPort {
    Product findById(Long id);
    void save(Product product);
}
```

**Inbound Port:**

```java
public interface ProductServicePort {
    Product updateStock(Long id, int quantity);
}
```

**中文：**
`ProductPort` 表示核心需要外部提供的数据访问能力。
`ProductServicePort` 表示核心对外提供的业务能力。

**English:**
`ProductPort` represents data access services required by the core.
`ProductServicePort` represents business services provided by the core.

### 31.5 ProductService and Jpa Adapter（Slide 91）

Slide 91 展示：

- `ProductService implements ProductServicePort`
- `ProductService` 依赖 `ProductPort`
- `JpaProductAdapter implements ProductPort`
- `JpaProductAdapter` 内部使用 `ProductJpaRepository`

**中文：**
这样业务逻辑只知道 `ProductPort`，不知道具体是 JPA、Redis 还是别的存储技术。

**English:**
The business logic only knows `ProductPort`, not whether persistence is implemented by JPA, Redis, or another technology.

### 31.6 ProductController Inbound Adapter（Slide 92）

Slide 92 展示 `ProductController`：

- 标记为 `@RestController`
- 路径为 `/api/products`
- 通过构造器注入 `ProductService`
- 提供 `PUT /{id}/stock` 接口更新库存

**中文：**
Controller 是 inbound adapter，它把 HTTP 请求转换成对核心业务服务的调用。

**English:**
The controller is an inbound adapter. It converts HTTP requests into calls to the core service.

### 31.7 Additional Implementation: Redis Adapter（Slide 93）

Slide 93 展示了 `RedisProductAdapter`：

- 实现 `ProductPort`
- 使用 `RedisTemplate`
- 用 `product:<id>` 作为 key 查找和保存 Product

**中文：**
这说明只要实现同一个 port，就可以增加新的基础设施实现，例如从 JPA 切换到 Redis，而不改业务核心。

**English:**
This shows that as long as a class implements the same port, we can add new infrastructure implementations such as Redis without modifying the business core.

### 31.8 Payment Example（Slide 94）

Slide 94 的支付图展示：

- `OrderController` 是 inbound adapter
- `OrderServicePort` 是 inbound port
- `OrderService` 是 business logic
- `PaymentPort` 是 outbound port
- `StripePaymentAdapter` 和 `PayPalAdapter` 是 outbound adapters
- 外部组件包括 `PayUsingStripe` 和 `PayPalComponent`

**中文：**
这个例子说明支付服务可以被替换。核心订单逻辑只依赖 `PaymentPort`，不直接依赖 Stripe 或 PayPal。

**English:**
This example shows payment services can be replaced. The core order logic depends only on `PaymentPort`, not directly on Stripe or PayPal.

### 31.9 Hexagonal Architecture Benefits（Slide 95）

| Benefit     | 中文解释                                                 | English Explanation                               |
| ----------- | -------------------------------------------------------- | ------------------------------------------------- |
| Decoupling  | 业务逻辑独立于基础设施。比如更换数据库不需要改核心代码。 | Business logic is independent of infrastructure.  |
| Testability | 可以 mock adapters，单独测试核心逻辑。                   | Mock adapters to test the core in isolation.      |
| Flexibility | 可以添加新 adapter，例如从 JPA 切换到 MongoDB。          | Add new adapters without changing business logic. |

------

# Part 6: Final Words 总结（Slide 96）

## 32. CBSE 如何改进软件开发 / How CBSE Improves Software Development

课件最后总结，CBSE 改进软件开发主要体现在：

| 中文                         | English                                                 |
| ---------------------------- | ------------------------------------------------------- |
| **Modularity 模块化**        | The system is split into clear components.              |
| **Reusability 可复用性**     | Components can be reused in different contexts.         |
| **Flexibility 灵活性**       | Implementations can be replaced or extended.            |
| **Maintainability 可维护性** | Components are easier to change and test independently. |

## 33. Spring Boot 中体现的 CBSE 知识点 / CBSE in Spring Boot

课件总结 Spring Boot 中的 CBSE 体现包括：

| 中文                                         | English                                        |
| -------------------------------------------- | ---------------------------------------------- |
| 定义 components，包括 bean                   | Define components, including beans             |
| IoC 和 DI                                    | IoC and DI                                     |
| 多个实现带来的灵活性                         | Flexibility of having multiple implementations |
| 使用 middleware，例如 JPA 和 Spring Security | Use middleware such as JPA and Spring Security |
| DDD 和 Hexagonal Architecture                | DDD and Hexagonal pattern                      |

------

# Week 9 考试复习重点 / Exam-Focused Key Points

## 1. CBSE 三个核心原则

**中文：**
CBSE 的三个核心原则是：

1. Component：封装功能和数据的独立单元
2. Interface：定义组件之间的契约
3. Composition：通过接口把组件组装成完整系统

**English:**
The three core principles of CBSE are:

1. Component: independent unit encapsulating functionality and data
2. Interface: contract between components
3. Composition: assembling components through interfaces

------

## 2. Spring Boot 为什么适合 CBSE？

**中文：**
因为 Spring Boot 使用 IoC 容器管理组件，通过 DI 组合组件，并通过注解、自动配置、组件扫描和 middleware 简化组件开发。

**English:**
Spring Boot is suitable for CBSE because it manages components through the IoC container, composes components through DI, and simplifies component development through annotations, auto-configuration, component scanning, and middleware.

------

## 3. Constructor Injection 为什么推荐？

**中文：**
因为构造器注入适合 mandatory dependencies，可以让依赖更明确，也可以让字段设置为 `final`，提升不可变性、测试性和维护性。

**English:**
Constructor injection is recommended because it is suitable for mandatory dependencies, makes dependencies explicit, supports immutability with `final` fields, and improves testability and maintainability.

------

## 4. `@Primary` 和 `@Qualifier` 的区别

**中文：**

- `@Primary`：指定默认 bean
- `@Qualifier`：明确指定某一个 bean

**English:**

- `@Primary`: specifies the default bean
- `@Qualifier`: explicitly selects a specific bean

------

## 5. `@Lazy` 如何解决循环依赖？

**中文：**
`@Lazy` 不会在启动阶段立刻注入真实对象，而是注入代理对象。这样可以让一个 bean 先完成创建，避免两个 bean 互相等待导致 Spring 启动失败。

**English:**
`@Lazy` injects a proxy object instead of the actual target bean during startup. This allows one bean to finish creation first and prevents Spring from failing due to circular dependency.

------

## 6. DDD 中 Entity、Aggregate、Bounded Context 的区别

| Concept         | 中文解释                                                  | English Explanation                                 |
| --------------- | --------------------------------------------------------- | --------------------------------------------------- |
| Entity          | 有唯一身份和生命周期的领域对象。                          | Domain object with identity and lifecycle.          |
| Aggregate       | 一组相关对象组成的一致性边界，有 aggregate root。         | Consistency boundary with an aggregate root.        |
| Bounded Context | 一个领域模型适用的边界，每个 context 有自己的模型和语言。 | Boundary where a domain model has specific meaning. |

------

## 7. Hexagonal Architecture 的核心思想

**中文：**
核心业务逻辑放在中心，外部技术细节放在外层。核心通过 ports 定义接口，外部通过 adapters 实现这些接口。这样可以降低耦合，提高测试性和灵活性。

**English:**
The core business logic is placed at the center, while external technologies stay outside. The core defines ports, and external systems implement adapters. This reduces coupling and improves testability and flexibility.