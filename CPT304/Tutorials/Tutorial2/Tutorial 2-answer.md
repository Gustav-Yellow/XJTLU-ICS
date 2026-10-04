### 1. Modify the following code to improve its cohesion.

**问题分析**：原有的 `Staff` 类同时负责处理 `Speaker`（演讲者）和 `Product`（产品）的增删改查逻辑。这违反了高内聚的定义（代码应该狭窄且专注）。 **改进方案**：将不相关的功能拆分到各自独立的类中。

```java
// 改进后：高内聚的代码
public class SpeakerService {
    public Speaker saveSpeaker(Speaker speaker) { /* ... */ return null;}
    public boolean removeSpeaker(int speakerId) { /* ... */ return true;}
    public Speaker findById(int speakerId) { /* ... */ return null;}
    public void updateSpeakerPhoto(int speakerId, String photoUrl) { /* ... */ }
}

public class ProductService {
    public Product saveProduct(Product product) { /* ... */ return null;}
    public void deleteProducts(List<Integer> productsId) { /* ... */ }
    public boolean deleteProduct(int productId) { /* ... */ return true;}
}
```

### 2. Modify the following code to lower its coupling.

**问题分析**：

1. `Payroll` 类直接依赖于具体的 `ParttimeStaff` 类 ，这是强耦合（Tight coupling）。
2. `Traveler` 类内部直接使用 `new Car()` 实例化了具体的车辆对象 ，导致它无法使用其他交通工具。

**改进方案**：依赖于接口（Interface）以实现松耦合 ，并通过构造函数注入依赖。

```java
// --- Payroll 与 Staff 的解耦 ---
public interface Staff {
    double getWorkedHours();
}

public class ParttimeStaff implements Staff {
    @Override
    public double getWorkedHours() { /* ... */ return 0;}
}

public class Payroll {
    private Staff staff; // 依赖抽象接口

    public Payroll(Staff staff) {
        this.staff = staff;
    }

    public double CalculatePay() {
        return staff.getWorkedHours() * 100; // 假设时薪
    }
}

// --- Traveler 与 Car 的解耦 ---
public interface Vehicle {
    void move();
}

public class Car implements Vehicle {
    @Override
    public void move() {
        System.out.println("Car is moving");
    }
}

public class Traveler {
    private Vehicle vehicle; // 依赖抽象接口

    // 依赖注入
    public Traveler(Vehicle vehicle) {
        this.vehicle = vehicle;
    }

    public void startJourney() {
        vehicle.move();
    }
}
```

### 3. According to SOLID principles, which is the most suitable situation to use inheritance?

**解答**：在需要实现**可替换性（Substitutability）**时，最适合使用继承 。即如果类 B 的对象可以无缝替换类 A 的对象被使用（而不破坏客户端代码），那么就应该使用继承 。

### 4. A software system is considered to have a "good design" if the cost of changing it is minimized. Discuss how Cohesion and Coupling contribute to this.

**解答**：

- **内聚 (Cohesion)**：高内聚确保相关的函数聚集在一起，当软件演进时，这可以减少代码变更的频率 。如果内聚度低，哪怕做一个微小的改动，也需要深入多个不同的类中去修改代码 。
- **耦合 (Coupling)**：低（松）耦合防止了对一个类的修改强迫其他类发生级联式的连锁反应 。通过依赖接口而不是具体类，系统的变更成本被大幅降低 。

### 5. Explain the "combinatorial explosion" problem... and describe how using Composition can solve it.

**解答**：

- **组合爆炸 (Combinatorial Explosion)**：当使用继承来对多个独立的特性（如：移动方式和战斗能力）进行建模时，为了覆盖每一种可能的特性组合（如 FlyLaser, SwimRifle 等），必须创建指数级数量的子类 。
- **如何通过组合解决**：组合允许在运行时动态组合不同的行为，而无需为每种组合创建一个新类 。通过将 `Movement` 和 `Weapon` 提取为独立接口，`Machine` 类只需将它们组合（Has-a 关系）起来即可避免爆炸 。

### 6. According to SOLID principles, which is the most suitable situation to use composition?

**解答**：当对象 B 需要**使用**对象 A 的功能，而不是作为 A 的替代品时，应该使用组合 。此外，它适合用作多重继承的替代方案，或者在需要在运行时动态改变行为时使用 。

### 7. Explain in detail the problem when the return type in an override method of a subclass is a long data type while the return type in the method of the superclass is an int data type?

**解答**：这违反了里氏替换原则（LSP）的第二条规则 。LSP 规定，子类方法的返回类型必须与超类的返回类型匹配或者是其子类型（更具体）。因为 `long` 的范围比 `int` 大且不兼容，期待返回 `int` 的客户端代码如果接收到 `long` 将会引发数据溢出或编译错误，从而破坏了多态和可替换性。

### 8. Discuss the Single Responsibility Principle (SRP) and provide an example...

**解答**：SRP 规定一个类应该有且只有一个引起它变化的原因，即一个类只完全封装一项职责 。

- **示例**：一个 `Employee` 类既包含获取员工姓名的数据逻辑，又包含打印工时表（`printTimeSheetReport`）的逻辑。这增加了复杂性。将其拆分为 `Employee`（负责数据）和专门的 `TimeSheetReport` 类（负责打印），即可遵循 SRP 。

### 9. How does the Open/Closed Principle (OCP) contribute to software maintainability... Provide a real-world example...

**解答**：OCP 要求软件实体对扩展开放，对修改关闭 。这通过防止实现新功能时破坏现有代码，大幅提升了系统的可维护性 。

- **示例**：在一个订单运费计算系统中，如果直接在 `Order` 类中使用 `if` 语句判断“陆运”或“空运”，每次增加新运输方式都要改动该类 。通过定义一个 `Shipping` 接口并让不同的运输方式实现它，添加新运输方式时只需新建类，无需修改原有代码 。

### 10. Detail the Liskov Substitution Principle (LSP) and explain its significance...

**解答**：LSP 规定，在扩展类时，应能够用子类的对象无缝替换父类的对象，且不会破坏客户端代码 。

- **重要性**：它确保了继承被正确使用（做出了正确的抽象）。如果违反 LSP，客户端代码将被迫使用 `instanceof` 来检查特定子类，导致代码被条件判断语句弄得混乱且难以维护 。

### 11. Explain the Interface Segregation Principle (ISP) and discuss its role...

**解答**：ISP 规定客户端不应被迫依赖它们不使用的接口 。

- **作用**：它的作用是通过将臃肿的接口（包含了过多不同功能的接口）拆分为多个独立、细粒度的接口，来降低系统的复杂性和发生副作用的概率 。

### 12. Describe how the Dependency Inversion Principle (DIP) helps to decouple...

**解答**：DIP 规定高层模块和底层模块都应该依赖于抽象（接口），而不是高层依赖于底层 。这通过引入一个抽象层将两者解耦，使得高层逻辑变得可重用，并且完全不受底层技术（如更换数据库驱动）变更的影响 。

### 13. What is the problem with the following interface? Improve it.

**问题分析**：提供的 `FileStorage` 接口严重违反了**接口隔离原则 (ISP)** 。它将文件操作（如 `storeFile`, `removeFile`）与完全无关的 JWT 身份验证操作（如 `decodeJWT`, `GenerateJWT`）强行绑定在了一起。不需要处理认证的普通文件存储系统将被迫实现这些无关的 JWT 方法。

**改进方案**：将臃肿的接口拆分为两个职责单一的细粒度接口。

```java
// 改进后：分离文件职责与认证职责
public interface FileStorage {
    String storeFile(MultipartFile file, FileType fileType, Integer id);
    Resource loadFileAsResource(String fileName, FileType fileType);
    boolean removeFile(String fileName, FileType fileType);
}

public interface JwtAuthenticationService {
    DecodedJWT decodeJWT(String jwtString) throws Exception;
    String GenerateJWT(UserDetails user);
    String GenerateRefreshJWT(UserDetails user);
}
```