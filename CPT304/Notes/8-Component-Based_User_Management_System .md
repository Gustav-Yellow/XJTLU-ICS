# 8 Building a Component-Based User Management System with Spring Boot

# 使用 Spring Boot 构建基于组件的用户管理系统

------

## 1. 本周主题 / Main Topic

**中文：**
Week 8 的核心是使用 **Spring Boot** 构建一个 **Component-Based User Management System**。这个系统围绕用户注册、用户查询和 Spring Security 身份认证展开。课件的重点不是单纯写代码，而是通过一个 Spring Boot 项目展示 **CBSE（Component-Based Software Engineering）** 的思想。

**English:**
The main focus of Week 8 is to build a **component-based user management system** using **Spring Boot**. The system includes user registration, user retrieval, and authentication through Spring Security. The purpose is not only to implement code, but also to show how **Component-Based Software Engineering (CBSE)** can be applied in a real Spring Boot application.

------

## 2. 本周体现的 CBSE 概念 / CBSE Concepts Illustrated

课件中明确列出了本项目体现的 CBSE 概念：

| English                           | 中文解释                                                     |
| --------------------------------- | ------------------------------------------------------------ |
| Modular Components                | 模块化组件，例如 `AuthService`、`UserService`、`Repository`。每个组件负责一个清晰的功能。 |
| Dependency Injection              | 依赖注入，由 Spring IoC container 管理组件之间的依赖关系。   |
| Interface-Driven Design           | 接口驱动设计，例如 `JPA Repository`、`UserDetailsService`。组件通过接口交互，而不是直接依赖具体实现。 |
| Security as Cross-Cutting Concern | 安全是横切关注点，它不是某一个业务模块独有的，而是会影响整个系统的请求处理流程。 |
| Proper Authentication Flow        | 正确的身份认证流程，包括请求拦截、用户查询、密码验证和授权检查。 |

**考试理解：**
如果题目问 “How does this Spring Boot system demonstrate CBSE principles?”，可以回答：

**中文答案：**
该系统通过分层组件体现 CBSE。`model` 负责数据结构，`repository` 负责数据访问，`service` 负责业务逻辑，`controller` 负责 API 入口，`config` 负责安全配置。各组件通过 Spring IoC 容器和依赖注入组合在一起，从而实现低耦合、高内聚和可替换性。

**English Answer:**
The system demonstrates CBSE by separating the application into different components. The model layer represents data, the repository layer handles data access, the service layer handles business logic, the controller layer exposes APIs, and the config layer manages security. These components are composed through Spring IoC and dependency injection, achieving loose coupling, high cohesion, and replaceability.

------

## 3. 系统总览 / System Overview

**中文：**
该系统是一个使用 Spring Boot 开发的用户管理系统，并使用 **Spring Security + HTTP Basic Authentication** 实现基本身份认证。

**English:**
This system is a Spring Boot user management application that uses **Spring Security with HTTP Basic Authentication**.

系统包含两个阶段：

| 阶段 / Stage                    | 中文说明                                              | English Explanation                                          |
| ------------------------------- | ----------------------------------------------------- | ------------------------------------------------------------ |
| Basic features without security | 先实现没有 Spring Security 的基本用户注册和查询功能。 | First build the basic user registration and retrieval features without Spring Security. |
| Add Spring Security             | 再加入 Spring Security，实现请求拦截、认证和授权。    | Then add Spring Security to intercept requests, authenticate users, and enforce authorization rules. |

------

## 4. Spring Security 请求处理流程 / Spring Security Request Flow

课件中给出了 Spring Security 的关键流程：

1. Client sends a request
2. Security filter chain intercepts the request
3. Authentication process
4. User detail lookup
5. Password verification
6. Authorization check
7. Response

**中文解释：**

当客户端发送 HTTP 请求时，请求不会直接进入 Controller，而是先经过 **Security Filter Chain**。Spring Security 会根据配置判断该请求是否需要登录。如果需要登录，它会通过 `UserDetailsService` 查找用户信息，然后验证密码。如果认证成功，还要检查该用户是否有权限访问目标 API。最后才会返回响应。

**English Explanation:**

When a client sends an HTTP request, the request does not directly reach the controller. It first passes through the **Security Filter Chain**. Spring Security checks whether the request requires authentication. If authentication is needed, it uses `UserDetailsService` to load user details and verifies the password. After authentication, it checks whether the user is authorized to access the requested API. Finally, the system returns a response.

------

## 5. 项目初始化 / Project Setup and Initial Configuration

### 5.1 Spring Initializr 设置 / Spring Initializr Configuration

**中文：**
在 `start.spring.io` 创建 Spring Boot 项目时，课件要求选择：

| 项目设置 / Setting | 内容 / Content                           |
| ------------------ | ---------------------------------------- |
| Project            | Maven                                    |
| Language           | Java                                     |
| Spring Boot        | Latest stable version or 3.4.4           |
| Dependencies       | Spring Web, Spring Data JPA, H2 Database |

**English:**
When creating the project on `start.spring.io`, select:

| Setting      | Content                                  |
| ------------ | ---------------------------------------- |
| Project      | Maven                                    |
| Language     | Java                                     |
| Spring Boot  | Latest stable version or 3.4.4           |
| Dependencies | Spring Web, Spring Data JPA, H2 Database |

### 5.2 依赖的作用 / Role of Dependencies

| Dependency      | 中文作用                               | English Role                                                 |
| --------------- | -------------------------------------- | ------------------------------------------------------------ |
| Spring Web      | 用来开发 REST Controller 和 HTTP API。 | Used to build REST controllers and HTTP APIs.                |
| Spring Data JPA | 提供 Repository 抽象，简化数据库访问。 | Provides repository abstraction and simplifies database access. |
| H2 Database     | 开发阶段使用的内存数据库。             | In-memory database used during development.                  |
| Spring Security | 后续加入，用来实现身份认证和授权。     | Added later to implement authentication and authorization.   |

### 5.3 导入 IDE 和运行检查 / Importing and Verification

**中文：**
下载项目后导入 IntelliJ、Eclipse 或 VS Code，等待 Maven 依赖解析完成。然后运行 main application class，如果控制台出现 Spring Boot banner 且没有启动错误，说明项目初始化成功。

**English:**
After downloading the project, import it into IntelliJ, Eclipse, or VS Code and wait for Maven dependencies to resolve. Then run the main application class. If the Spring Boot banner appears and no startup errors occur, the initial setup is successful.

------

## 6. 项目结构设计 / Project Structure Design

课件给出的项目结构如下：

| Package      | 中文说明                                    | English Explanation                                          |
| ------------ | ------------------------------------------- | ------------------------------------------------------------ |
| `config`     | 配置组件，例如 Spring Security 配置。       | Configuration components, such as Spring Security configuration. |
| `controller` | REST Controller，处理 API 请求。            | REST controllers that handle API requests.                   |
| `dto`        | Data Transfer Objects，用于前后端数据传输。 | Data Transfer Objects used for data transfer between frontend and backend. |
| `model`      | Entity classes，例如 User 实体。            | Entity classes, such as the User entity.                     |
| `repository` | 数据访问组件。                              | Data access components.                                      |
| `service`    | 业务逻辑组件。                              | Business logic components.                                   |

**中文总结：**
这个结构体现了高内聚和低耦合。每个 package 只负责一种类型的任务。例如，Controller 不应该直接操作数据库，而应该调用 Service；Service 不应该直接写 SQL，而应该依赖 Repository。

**English Summary:**
This structure supports high cohesion and low coupling. Each package has a specific responsibility. For example, controllers should not directly access the database; they should call services. Services should not write SQL directly; they should depend on repositories.

------

# 7. Basic Features：没有 Spring Security 的基础功能

# Basic Features Without Spring Security

课件先要求实现一个没有安全控制的基础版本，包括：

| Component                      | 中文说明             | English Explanation            |
| ------------------------------ | -------------------- | ------------------------------ |
| User Model                     | 用户实体类。         | User entity class.             |
| DTO                            | 前后端数据传输对象。 | Data transfer objects.         |
| UserRepository                 | 数据库访问接口。     | Interface for database access. |
| AuthService, UserService       | 业务逻辑层。         | Service layer.                 |
| AuthController, UserController | API 接口层。         | API endpoint layer.            |

------

## 8. User Model Component / 用户模型组件

### 8.1 CBSE 原则 / CBSE Principles

课件指出，`User` 类体现了两个 CBSE 原则：

| Principle      | 中文解释                            | English Explanation                                          |
| -------------- | ----------------------------------- | ------------------------------------------------------------ |
| Encapsulation  | `User` 类封装所有用户相关数据。     | The `User` class encapsulates all user-related data.         |
| Self-contained | `User` 类包含用户所需的信息和行为。 | The `User` class contains necessary user information and behavior. |

### 8.2 User 类注解 / User Class Annotations

**中文：**
`User` 类需要添加：

```java
@Entity
@Table(name = "users")
```

并且需要：

```java
no-argument constructor
all-argument constructor except id
```

**English:**
The `User` class should be annotated with:

```java
@Entity
@Table(name = "users")
```

It should also include:

```java
a no-argument constructor
an all-argument constructor except id
```

### 8.3 User 类属性 / User Class Properties

| Field       | Annotation                                                   | 中文说明                                                     | English Explanation                                          |
| ----------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `id`        | `@Id`, `@GeneratedValue(strategy = GenerationType.IDENTITY)` | 主键，自动生成。                                             | Primary key, automatically generated.                        |
| `username`  | `@Column(nullable = false, unique = true)`                   | 用户名，不能为空且唯一。                                     | Username, cannot be null and must be unique.                 |
| `email`     | `@Column(nullable = false, unique = true)`                   | 邮箱，不能为空且唯一。                                       | Email, cannot be null and must be unique.                    |
| `password`  | `@Column(nullable = false)`                                  | 密码，不能为空。                                             | Password, cannot be null.                                    |
| `firstname` | `@Column(name = "first_name", nullable = false)`             | 名字，不能为空。                                             | First name, cannot be null.                                  |
| `lastname`  | `@Column(name = "first_name", nullable = false)`             | 姓氏，不能为空。注意课件这里写成了 `first_name`，实际项目中通常应为 `last_name`。 | Last name, cannot be null. The slide writes `first_name`, but in a real project it is usually expected to be `last_name`. |
| `enabled`   | `@Column(nullable = false)`                                  | 用户是否启用。                                               | Whether the user is enabled.                                 |

------

## 9. DTO / Data Transfer Objects / 数据传输对象

### 9.1 DTO 的定义 / Definition of DTO

**中文：**
DTO 是一个简化对象，用来在前端和后端之间传输数据。它不一定等同于数据库 Entity。DTO 的作用是避免直接暴露内部数据库结构。

**English:**
A DTO is a simplified object used to transfer data between the frontend and backend. It is not necessarily the same as the database entity. Its purpose is to avoid exposing the internal database structure directly.

### 9.2 Java Record / Java 记录类

课件指出，定义 DTO 时使用 Java 14 引入的 `record` 关键字。`record` 是一种不可变的数据载体类，会自动生成：

| 自动生成内容 / Auto-generated Content | 中文解释                                   |
| ------------------------------------- | ------------------------------------------ |
| Private final fields                  | 每个字段自动变成 private final。           |
| Public constructor                    | 自动生成公共构造函数。                     |
| Getter methods                        | 自动生成 getter，但方法名不带 `get` 前缀。 |
| `equals()`                            | 自动生成比较方法。                         |
| `hashCode()`                          | 自动生成哈希方法。                         |
| `toString()`                          | 自动生成字符串表示方法。                   |

### 9.3 Record 的限制 / Limitations of Record

| Limitation                  | 中文解释                                         |
| --------------------------- | ------------------------------------------------ |
| No setters                  | 因为 record 是 immutable，不允许修改字段。       |
| Cannot extend another class | 不能继承其他 class，但可以 implement interface。 |
| All fields are final        | 构造后字段不能被修改。                           |

课件图片中的 DTO 示例包括：

```java
public record UserDTO(
    Long id,
    String username,
    String email
) {}
```

另一个带验证注解的示例：

```java
public record UserDTO(
    @NotBlank(message = "Name is required")
    String name,

    @Email(message = "Invalid email format")
    String email,

    @Size(min = 8, max = 20, message = "Password must be 8-20 characters")
    String password,

    @PositiveOrZero(message = "Age cannot be negative")
    int age
) {}
```

### 9.4 本项目需要的两个 DTO / Two DTOs Required in This Project

| DTO Purpose       | Fields                                                   | 中文说明                           |
| ----------------- | -------------------------------------------------------- | ---------------------------------- |
| User registration | `username`, `email`, `password`, `firstname`, `lastname` | 用于用户注册请求。                 |
| User data         | `username`, `email`, `firstname`, `lastname`             | 用于返回用户信息，通常不返回密码。 |

### 9.5 DTO Validation / DTO 数据验证

课件中给出的注册 DTO 验证规则包括：

| Field       | Validation Annotation         | 中文说明                           |
| ----------- | ----------------------------- | ---------------------------------- |
| `username`  | `@NotBlank`                   | 用户名不能为空。                   |
| `email`     | `@Email`, `@NotBlank`         | 邮箱不能为空，且必须符合邮箱格式。 |
| `password`  | `@Size(min = 8)`, `@NotBlank` | 密码不能为空，且至少 8 位。        |
| `firstname` | `@NotBlank`                   | 名字不能为空。                     |
| `lastname`  | `@NotBlank`                   | 姓氏不能为空。                     |

**注意 / Note:**
这些验证注解依赖于 `jakarta.validation`。

------

## 10. Repository Component / Repository 组件

### 10.1 Repository 的 CBSE 原则 / CBSE Principles

| Principle               | 中文解释                                                     | English Explanation                                          |
| ----------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Interface-driven design | Repository 是接口，定义数据访问契约。                        | Repository is an interface that defines the data access contract. |
| Replaceability          | 可以把 JPA 换成 JDBC、MongoDB 等实现，而 Service 层不需要大改。 | The implementation can be replaced by JPA, JDBC, MongoDB, etc., without changing the service layer. |

### 10.2 UserRepository 实现步骤 / Implementation Steps

```java
@Repository
public interface UserRepository extends JpaRepository<User, Long> {
}
```

课件要求：

1. Define the interface named `UserRepository`
2. Extend `JpaRepository<User, Long>`
3. Annotate with `@Repository`

**中文解释：**
`JpaRepository<User, Long>` 表示该 Repository 操作的是 `User` 实体，主键类型是 `Long`。

**English Explanation:**
`JpaRepository<User, Long>` means the repository manages the `User` entity and the primary key type is `Long`.

### 10.3 Repository 方法签名 / Repository Method Signatures

课件图片中显示需要定义以下方法：

```java
Optional<User> findByUsername(String username);
Optional<User> findByEmail(String email);
boolean existsByUsername(String username);
boolean existsByEmail(String email);
```

| Method             | 中文作用               | English Role                              |
| ------------------ | ---------------------- | ----------------------------------------- |
| `findByUsername`   | 根据用户名查找用户。   | Finds a user by username.                 |
| `findByEmail`      | 根据邮箱查找用户。     | Finds a user by email.                    |
| `existsByUsername` | 检查用户名是否已存在。 | Checks whether a username already exists. |
| `existsByEmail`    | 检查邮箱是否已存在。   | Checks whether an email already exists.   |

------

## 11. Convention-over-Configuration / 约定优于配置

课件重点解释了 Spring Data JPA 的命名规则：

```java
Optional<User> findByUsername(String username)
```

| Part                | 中文解释                                  | English Explanation                                  |
| ------------------- | ----------------------------------------- | ---------------------------------------------------- |
| `Optional<User>`    | 查询结果可能有 0 或 1 条。                | The query may return 0 or 1 record.                  |
| `findBy`            | 表示查询记录。                            | Indicates a query operation.                         |
| `Username`          | 对应 `User` entity 中的 `username` 字段。 | Refers to the `username` field in the `User` entity. |
| `(String username)` | 用参数匹配 username 字段。                | The parameter is used to match the username field.   |

对应 SQL 类似于：

```sql
SELECT * FROM users WHERE username = ?1;
```

### 11.1 其他命名示例 / Other Examples

```java
Optional<User> findByUsernameAndEmail(String username, String email);
List<User> findByUsernameNot(String name);
List<User> findByUsernameLike(String pattern);
List<User> findByUsernameContaining(String s);
List<Sales> findByIdOrderByAmountDesc(Long id);
```

**中文：**
如果查询比较复杂，可以使用 `@Query` 自定义 SQL 或 JPQL。

**English:**
For more complex queries, use `@Query`.

### 11.2 Spring Data JPA Magic / Spring Data JPA 的“魔法”

课件指出，Repository 不需要写实现类，因为 Spring Data JPA 会：

| English                              | 中文解释                       |
| ------------------------------------ | ------------------------------ |
| Generates proxy classes              | 自动生成代理类。               |
| Derives queries from method names    | 根据方法名推导查询逻辑。       |
| Delegates execution to JPA/Hibernate | 把执行过程交给 JPA/Hibernate。 |

------

## 12. Service Layer Components / 服务层组件

### 12.1 Service 层体现的 CBSE 原则 / CBSE Principles

| Principle                       | 中文解释                                             | English Explanation                                          |
| ------------------------------- | ---------------------------------------------------- | ------------------------------------------------------------ |
| Single Responsibility Principle | 每个 Service 只处理特定业务逻辑。                    | Each service handles specific business logic.                |
| Dependency Injection            | Service 通过构造器注入 Repository。                  | Services are composed with repositories through constructor injection. |
| Loose Coupling                  | Service 依赖 `UserRepository` 接口，而不是具体实现。 | Services depend on the `UserRepository` interface rather than concrete implementations. |

本项目包含两个 Service：

| Service       | 中文作用               | English Role                           |
| ------------- | ---------------------- | -------------------------------------- |
| `AuthService` | 提供用户注册服务。     | Provides user registration service.    |
| `UserService` | 提供一般用户查询服务。 | Provides general user-related service. |

------

## 13. AuthService / 认证服务组件

课件要求 `AuthService` 包含以下内容：

```java
@Service
public class AuthService {
    private final UserRepository userRepository;

    public UserDataDto userRegistration(UserRegistrationDto dto) {
        // check username
        // check email
        // create User
        // save User
        // return UserDataDto
    }
}
```

### AuthService 的职责 / Responsibilities of AuthService

| Step                         | 中文说明                       | English Explanation                                 |
| ---------------------------- | ------------------------------ | --------------------------------------------------- |
| Annotate with `@Service`     | 让 Spring 管理该业务组件。     | Let Spring manage it as a service component.        |
| Inject `UserRepository`      | 通过 DI 注入数据访问组件。     | Inject the data access component through DI.        |
| Define `userRegistration`    | 定义用户注册方法。             | Define user registration method.                    |
| Return `UserDataDto`         | 注册成功后返回用户数据 DTO。   | Return user data DTO after successful registration. |
| Accept `UserRegistrationDto` | 接收注册请求数据。             | Accept registration request data.                   |
| Check username exists        | 检查用户名是否已存在。         | Check whether username already exists.              |
| Check email exists           | 检查邮箱是否已存在。           | Check whether email already exists.                 |
| Instantiate and save User    | 创建 User 对象并保存到数据库。 | Create a User object and save it into the database. |

------

## 14. UserService / 用户服务组件

课件要求 `UserService` 包含以下内容：

```java
@Service
public class UserService {
    private final UserRepository userRepository;

    public UserDataDto getUserById(Long userId) {
        // retrieve user by id
        // return UserDataDto
    }
}
```

### UserService 的职责 / Responsibilities of UserService

| Step                     | 中文说明                                  | English Explanation                            |
| ------------------------ | ----------------------------------------- | ---------------------------------------------- |
| Annotate with `@Service` | 标记为 Service 组件。                     | Mark it as a service component.                |
| Inject `UserRepository`  | 注入 Repository。                         | Inject repository.                             |
| Define `getUserById`     | 定义根据 ID 查询用户的方法。              | Define method to retrieve user by ID.          |
| Return `UserDataDto`     | 返回用户数据 DTO，而不是直接返回 Entity。 | Return `UserDataDto`, not the entity directly. |
| Accept `userId`          | 接收用户 ID。                             | Accept user ID.                                |
| Retrieve user by ID      | 使用 Repository 查询用户。                | Retrieve the user using repository.            |

------

## 15. Controller Components / 控制器组件

### 15.1 Controller 层体现的 CBSE 原则

| Principle       | 中文解释                               | English Explanation                                |
| --------------- | -------------------------------------- | -------------------------------------------------- |
| Modularity      | Controller 只处理 API 请求相关逻辑。   | Controllers handle API concerns only.              |
| Composition     | Controller 通过 DI 组合 Service 组件。 | Controllers are composed with services through DI. |
| Interface-based | 使用 DTO 作为输入输出契约。            | DTOs are used as input/output contracts.           |

本项目有两个 Controller：

| Controller       | Base Path    | 中文作用           |
| ---------------- | ------------ | ------------------ |
| `AuthController` | `/api/auth`  | 处理注册相关请求。 |
| `UserController` | `/api/users` | 处理用户查询请求。 |

------

## 16. AuthController / 认证控制器

课件要求 `AuthController` 包含：

```java
@RestController
@RequestMapping("/api/auth")
public class AuthController {
    private final AuthService authService;

    @PostMapping("/register")
    public ResponseEntity<UserDataDto> register(@RequestBody UserRegistrationDto dto) {
        return ResponseEntity.ok(authService.userRegistration(dto));
    }
}
```

### AuthController 重点 / Key Points

| Item                                 | 中文解释                                          | English Explanation                                     |
| ------------------------------------ | ------------------------------------------------- | ------------------------------------------------------- |
| `@RestController`                    | 表示这是 REST API 控制器。                        | Marks the class as a REST API controller.               |
| `/api/auth`                          | 所有认证相关 API 的基础路径。                     | Base path for authentication-related APIs.              |
| Inject `AuthService`                 | Controller 不直接处理注册逻辑，而是调用 Service。 | Controller delegates registration logic to the service. |
| POST `/register`                     | 创建注册接口。                                    | Creates the registration endpoint.                      |
| Return `ResponseEntity<UserDataDto>` | 返回 HTTP 响应和用户数据。                        | Returns HTTP response and user data.                    |

------

## 17. UserController / 用户控制器

课件要求 `UserController` 包含：

```java
@RestController
@RequestMapping("/api/users")
public class UserController {
    private final UserService userService;

    @GetMapping("/{id}")
    public ResponseEntity<UserDataDto> getUserById(@PathVariable Long id) {
        return ResponseEntity.ok(userService.getUserById(id));
    }
}
```

### UserController 重点 / Key Points

| Item                   | 中文解释                  | English Explanation                  |
| ---------------------- | ------------------------- | ------------------------------------ |
| `@RestController`      | REST Controller。         | REST Controller.                     |
| `/api/users`           | 用户相关 API 的基础路径。 | Base path for user-related APIs.     |
| `@GetMapping("/{id}")` | 根据 ID 查询用户。        | Retrieves user by ID.                |
| `@PathVariable`        | 从 URL 中获取 ID。        | Gets ID from the URL path.           |
| `UserService`          | 查询逻辑交给 Service。    | Query logic is delegated to service. |

------

## 18. 测试基础实现 / Testing the Basic Implementation

在未加入 Spring Security 前，用户可以自由访问：

```text
/api/auth/register
/api/users/{id}
```

**中文：**
此时系统没有安全保护，所以注册和查询接口都可以直接访问。

**English:**
At this stage, no security has been implemented, so both registration and user retrieval endpoints can be accessed freely.

------

# 19. Adding Spring Security / 加入 Spring Security

## 19.1 Security Filter Chain 图示理解

课件中的图示显示了请求经过 Spring Security 的路径：

```text
Client
  ↓
Security Filter Chain
  ↓
Auth Rules
  ↓
UserDetailsService
  ↓
UserDetails
  ↓
API Endpoints
```

**中文解释：**
客户端请求先进入 Security Filter Chain。Auth Rules 决定哪些路径可以公开访问，哪些路径必须登录。需要认证时，系统会调用 `UserDetailsService`，根据用户名加载 `UserDetails`，然后验证密码，最后决定是否允许访问 API。

**English Explanation:**
The client request first enters the Security Filter Chain. Auth rules decide which paths are public and which require authentication. When authentication is required, the system calls `UserDetailsService` to load `UserDetails` by username, verifies the password, and then decides whether the API can be accessed.

------

## 20. 添加 Spring Security 依赖 / Adding Spring Security Dependency

课件要求在 `pom.xml` 中添加：

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-security</artifactId>
</dependency>
```

**中文：**
加入该依赖后，再访问之前的接口时，系统会要求登录。

**English:**
After adding this dependency, accessing the previous endpoints will require login.

------

## 21. Implement UserDetails in User Class / 让 User 实现 UserDetails

课件要求修改 `User` 类：

```java
public class User implements UserDetails {
}
```

并实现 `UserDetails` 接口要求的所有方法。

**中文解释：**
Spring Security 认识的用户类型是 `UserDetails`。因此，如果希望系统使用我们自己定义的 `User` 实体来登录，就需要让 `User` 实现 `UserDetails` 接口。

**English Explanation:**
Spring Security recognizes users through the `UserDetails` interface. Therefore, if we want Spring Security to use our custom `User` entity for login, the `User` class must implement `UserDetails`.

常见需要实现的方法包括：

```java
getAuthorities()
getPassword()
getUsername()
isAccountNonExpired()
isAccountNonLocked()
isCredentialsNonExpired()
isEnabled()
```

------

## 22. CustomUserDetailsService / 自定义用户详情服务

课件要求定义一个组件：

```java
@Service
public class CustomUserDetailsService implements UserDetailsService {
    private final UserRepository userRepository;

    @Override
    public UserDetails loadUserByUsername(String username) {
        return userRepository.findByUsername(username)
            .orElseThrow(() -> new UsernameNotFoundException("User not found"));
    }
}
```

### 重点解释 / Key Explanation

| Item                            | 中文解释                                | English Explanation                                          |
| ------------------------------- | --------------------------------------- | ------------------------------------------------------------ |
| `implements UserDetailsService` | 实现 Spring Security 查找用户的接口。   | Implements the interface used by Spring Security to load users. |
| Inject `UserRepository`         | 通过 Repository 根据用户名查找用户。    | Uses repository to find user by username.                    |
| `loadUserByUsername`            | 登录时自动调用，类似 hook。             | Automatically called during login, like a hook.              |
| Return `UserDetails`            | 返回 Spring Security 能识别的用户对象。 | Returns a user object recognized by Spring Security.         |

**考试重点：**
`loadUserByUsername` 不是普通业务方法，而是 Spring Security 在认证过程中自动调用的方法。

------

## 23. SecurityConfig / 安全配置组件

课件要求定义 `SecurityConfig`：

```java
@Configuration
@EnableWebSecurity
public class SecurityConfig {
}
```

### 23.1 SecurityFilterChain Bean

```java
@Bean
public SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
    http
        .csrf(csrf -> csrf.disable())
        .authorizeHttpRequests(auth -> auth
            .requestMatchers("/api/auth/**").permitAll()
            .requestMatchers("/api/users/**").authenticated()
            .anyRequest().denyAll()
        )
        .userDetailsService(userDetailsService)
        .httpBasic(basic -> {});

    return http.build();
}
```

课件图片中的授权配置大意如下：

```java
http
    .csrf(csrf -> csrf.disable())
    .authorizeHttpRequests(auth -> auth
        .requestMatchers("/api/auth/**").permitAll()
        .requestMatchers("/api/users/**").authenticated()
        .anyRequest().denyAll()
    )
    .userDetailsService(userDetailsService)
    .httpBasic(basic -> {});
```

### 23.2 配置解释 / Configuration Explanation

| Code                            | 中文解释                           | English Explanation                                       |
| ------------------------------- | ---------------------------------- | --------------------------------------------------------- |
| `csrf.disable()`                | 关闭 CSRF，适合当前简单 API 测试。 | Disables CSRF, suitable for simple API testing here.      |
| `/api/auth/**.permitAll()`      | 注册等认证接口允许所有人访问。     | Authentication endpoints such as registration are public. |
| `/api/users/**.authenticated()` | 用户查询接口必须登录后才能访问。   | User endpoints require authentication.                    |
| `anyRequest().denyAll()`        | 其他请求全部拒绝。                 | All other requests are denied.                            |
| `userDetailsService(...)`       | 指定自定义用户查询服务。           | Specifies the custom user loading service.                |
| `httpBasic(...)`                | 使用 HTTP Basic Authentication。   | Uses HTTP Basic Authentication.                           |
| `http.build()`                  | 生成 `SecurityFilterChain` 对象。  | Builds the `SecurityFilterChain` object.                  |

------

## 24. PasswordEncoder / 密码编码器

课件要求定义另一个 Bean：

```java
@Bean
public PasswordEncoder passwordEncoder() {
    return new BCryptPasswordEncoder();
}
```

**中文解释：**
`BCryptPasswordEncoder` 是 Spring Security 库中的普通类，不是自动被 Spring 管理的组件。因此需要在 `@Configuration` 类中用 `@Bean` 显式注册。

**English Explanation:**
`BCryptPasswordEncoder` is a regular class from the Spring Security library. It is not automatically managed by Spring. Therefore, it must be explicitly registered as a bean in a `@Configuration` class.

------

## 25. @Bean 和 @Autowired 的区别 / Difference Between @Bean and @Autowired

| Annotation   | 中文解释                                             | English Explanation                                          |
| ------------ | ---------------------------------------------------- | ------------------------------------------------------------ |
| `@Bean`      | 用在配置类的方法上，告诉 Spring 创建并管理这个对象。 | Used on methods in configuration classes to tell Spring to create and manage an object. |
| `@Autowired` | 告诉 Spring 把已经存在的 Bean 注入进来。             | Tells Spring to inject an existing bean.                     |

**中文例子：**
`PasswordEncoder` 没有 `@Component`，所以 Spring 不会自动创建它。我们先用 `@Bean` 创建它，然后其他类才可以通过依赖注入使用它。

**English Example:**
`PasswordEncoder` is not annotated with `@Component`, so Spring will not create it automatically. We first define it with `@Bean`, and then other classes can inject it.

------

## 26. Password Encoding / 密码加密

课件最后要求修改 `AuthService`：

```java
@Service
public class AuthService {
    private final UserRepository userRepository;
    private final PasswordEncoder passwordEncoder;

    public UserDataDto userRegistration(UserRegistrationDto dto) {
        String encodedPassword = passwordEncoder.encode(dto.password());

        User user = new User(
            dto.username(),
            dto.email(),
            encodedPassword,
            dto.firstname(),
            dto.lastname(),
            true
        );

        userRepository.save(user);
        return new UserDataDto(
            user.getUsername(),
            user.getEmail(),
            user.getFirstname(),
            user.getLastname()
        );
    }
}
```

**中文解释：**
注册用户时，不能直接把明文密码保存到数据库。应该先调用：

```java
passwordEncoder.encode(password)
```

把密码编码后再保存。

**English Explanation:**
When registering a user, the plain-text password should not be saved directly into the database. The password should first be encoded using:

```java
passwordEncoder.encode(password)
```

and then saved.

------

# 27. 整体架构总结 / Overall Architecture Summary

```text
Client
  ↓
Controller Layer
  - AuthController
  - UserController
  ↓
Service Layer
  - AuthService
  - UserService
  ↓
Repository Layer
  - UserRepository
  ↓
Database
  - H2 Database
```

加入 Security 后：

```text
Client
  ↓
Security Filter Chain
  ↓
Authentication & Authorization
  ↓
Controller
  ↓
Service
  ↓
Repository
  ↓
Database
```

**中文总结：**
基础版本中，用户请求直接进入 Controller。加入 Spring Security 后，请求会先进入 Security Filter Chain，只有通过认证和授权后才会进入 Controller。

**English Summary:**
In the basic version, requests directly reach the controller. After adding Spring Security, requests first pass through the Security Filter Chain. Only authenticated and authorized requests can reach the controller.

------

# 28. 关键注解总结 / Key Annotation Summary

| Annotation               | 中文说明                   | English Explanation                           |
| ------------------------ | -------------------------- | --------------------------------------------- |
| `@Entity`                | 标记 JPA 实体类。          | Marks a JPA entity class.                     |
| `@Table(name = "users")` | 指定数据库表名。           | Specifies the database table name.            |
| `@Id`                    | 标记主键。                 | Marks the primary key.                        |
| `@GeneratedValue`        | 主键自动生成。             | Automatically generates primary key values.   |
| `@Column`                | 配置数据库字段属性。       | Configures database column properties.        |
| `@Repository`            | 标记数据访问组件。         | Marks a data access component.                |
| `@Service`               | 标记业务逻辑组件。         | Marks a business logic component.             |
| `@RestController`        | 标记 REST API 控制器。     | Marks a REST API controller.                  |
| `@RequestMapping`        | 设置 Controller 基础路径。 | Sets the base path for a controller.          |
| `@PostMapping`           | 处理 POST 请求。           | Handles POST requests.                        |
| `@GetMapping`            | 处理 GET 请求。            | Handles GET requests.                         |
| `@PathVariable`          | 从 URL 路径中读取参数。    | Reads parameters from URL path.               |
| `@RequestBody`           | 从请求体读取 JSON 数据。   | Reads JSON data from request body.            |
| `@Configuration`         | 标记配置类。               | Marks a configuration class.                  |
| `@EnableWebSecurity`     | 启用 Spring Security。     | Enables Spring Security.                      |
| `@Bean`                  | 显式注册 Spring 管理对象。 | Explicitly registers a Spring-managed object. |
| `@NotBlank`              | 字段不能为空白。           | Field cannot be blank.                        |
| `@Email`                 | 字段必须是邮箱格式。       | Field must be a valid email.                  |
| `@Size(min = 8)`         | 字段长度至少为 8。         | Field length must be at least 8.              |

------

# 29. 本周常见考试题 / Possible Exam or Tutorial Questions

## Question 1

**How does the Week 8 project demonstrate Component-Based Software Engineering?**
**Week 8 项目如何体现 CBSE？**

**Answer / 答案：**
The project separates the system into independent components: `model`, `dto`, `repository`, `service`, `controller`, and `config`. Each component has a clear responsibility. The repository provides data access, the service layer handles business logic, the controller exposes APIs, and the config layer manages security. Spring IoC composes these components through dependency injection. This demonstrates modularity, interface-driven design, loose coupling, and high cohesion.

该项目把系统划分为多个独立组件：`model`、`dto`、`repository`、`service`、`controller` 和 `config`。每个组件都有明确职责。Repository 负责数据访问，Service 负责业务逻辑，Controller 暴露 API，Config 负责安全配置。Spring IoC 通过依赖注入组合这些组件。因此该系统体现了模块化、接口驱动设计、低耦合和高内聚。

------

## Question 2

**Why should the controller not directly access the repository?**
**为什么 Controller 不应该直接访问 Repository？**

**Answer / 答案：**
The controller should only handle HTTP requests and responses. Business logic should be placed in the service layer. If the controller directly accesses the repository, API logic, business logic, and data access logic become mixed together, which reduces cohesion and increases coupling. Using a service layer makes the system easier to maintain, test, and extend.

Controller 应该只处理 HTTP 请求和响应。业务逻辑应该放在 Service 层。如果 Controller 直接访问 Repository，API 逻辑、业务逻辑和数据访问逻辑会混在一起，导致低内聚和高耦合。使用 Service 层可以提高系统的可维护性、可测试性和可扩展性。

------

## Question 3

**What is the purpose of DTOs in this project?**
**DTO 在本项目中的作用是什么？**

**Answer / 答案：**
DTOs are used to transfer data between frontend and backend. They prevent the system from exposing internal entity structures directly. For example, `UserRegistrationDto` receives registration data, while `UserDataDto` returns user information without exposing the password. This improves security, modularity, and interface clarity.

DTO 用于在前端和后端之间传输数据，避免直接暴露内部 Entity 结构。例如，`UserRegistrationDto` 接收注册数据，而 `UserDataDto` 返回用户信息但不暴露密码。这提高了安全性、模块化程度和接口清晰度。

------

## Question 4

**Explain how Spring Data JPA implements convention-over-configuration.**
**解释 Spring Data JPA 如何体现“约定优于配置”。**

**Answer / 答案：**
Spring Data JPA can generate queries based on method names. For example, `findByUsername(String username)` means searching the `users` table by the `username` field. Developers do not need to manually implement the method. Spring Data JPA generates proxy classes, derives the query from the method name, and delegates execution to JPA/Hibernate.

Spring Data JPA 可以根据方法名自动生成查询。例如，`findByUsername(String username)` 表示根据 `username` 字段查询用户。开发者不需要手写实现类。Spring Data JPA 会自动生成代理类，根据方法名推导查询逻辑，并交给 JPA/Hibernate 执行。

------

## Question 5

**Why does User need to implement UserDetails?**
**为什么 User 类需要实现 UserDetails？**

**Answer / 答案：**
Spring Security uses the `UserDetails` interface to represent authenticated users. If we want Spring Security to authenticate users using our custom `User` entity, then the `User` class must implement `UserDetails`. This allows Spring Security to read the username, password, enabled status, and authorities from our user object.

Spring Security 使用 `UserDetails` 接口表示认证用户。如果希望 Spring Security 使用我们自定义的 `User` 实体进行登录认证，那么 `User` 类必须实现 `UserDetails`。这样 Spring Security 才能从用户对象中读取用户名、密码、启用状态和权限信息。

------

## Question 6

**What is the role of UserDetailsService?**
**UserDetailsService 的作用是什么？**

**Answer / 答案：**
`UserDetailsService` is used by Spring Security to load user information during authentication. Its key method is `loadUserByUsername`. In this project, `CustomUserDetailsService` uses `UserRepository` to find a user by username and returns it as a `UserDetails` object.

`UserDetailsService` 用于在认证过程中加载用户信息。它的核心方法是 `loadUserByUsername`。在本项目中，`CustomUserDetailsService` 使用 `UserRepository` 根据用户名查找用户，并把用户作为 `UserDetails` 对象返回。

------

## Question 7

**Explain the authorization configuration in SecurityConfig.**
**解释 SecurityConfig 中的授权配置。**

**Answer / 答案：**
The configuration disables CSRF, allows all users to access `/api/auth/**`, requires authentication for `/api/users/**`, and denies all other requests. This means registration is public, but retrieving user information requires login. The configuration also connects Spring Security to the custom `UserDetailsService` and enables HTTP Basic Authentication.

该配置关闭 CSRF，允许所有用户访问 `/api/auth/**`，要求 `/api/users/**` 必须登录后才能访问，并拒绝其他所有请求。这意味着注册接口是公开的，但查询用户信息需要登录。配置还把 Spring Security 连接到自定义 `UserDetailsService`，并启用 HTTP Basic Authentication。

------

## Question 8

**Why should passwords be encoded before saving?**
**为什么保存密码前必须进行编码？**

**Answer / 答案：**
Passwords should not be stored as plain text because this creates a serious security risk. If the database is leaked, attackers can directly read user passwords. By using `BCryptPasswordEncoder`, the system stores encoded passwords instead. During login, Spring Security compares the raw password with the encoded password securely.

密码不能以明文形式保存，因为这会造成严重安全风险。如果数据库泄露，攻击者可以直接读取用户密码。使用 `BCryptPasswordEncoder` 后，系统保存的是编码后的密码。登录时，Spring Security 会安全地比较原始密码和编码密码。

------

# 30. 最终速记版 / Quick Revision Summary

**中文速记：**

Week 8 的核心是：用 Spring Boot 实现一个基于组件的用户管理系统。系统分为 `model`、`dto`、`repository`、`service`、`controller`、`config`。基础阶段先实现注册和用户查询；安全阶段加入 Spring Security。Spring Security 会通过 Security Filter Chain 拦截请求，使用 `UserDetailsService` 加载用户，使用 `PasswordEncoder` 验证密码，并根据授权规则决定是否允许访问 API。该项目体现了 CBSE 的模块化、接口驱动、依赖注入、低耦合和高内聚。

**English Quick Summary:**

Week 8 focuses on building a component-based user management system with Spring Boot. The system is divided into `model`, `dto`, `repository`, `service`, `controller`, and `config`. The basic stage implements user registration and user retrieval. The security stage adds Spring Security. Spring Security intercepts requests through the Security Filter Chain, loads users through `UserDetailsService`, verifies passwords with `PasswordEncoder`, and checks authorization rules before allowing API access. The project demonstrates CBSE concepts such as modularity, interface-driven design, dependency injection, loose coupling, and high cohesion.