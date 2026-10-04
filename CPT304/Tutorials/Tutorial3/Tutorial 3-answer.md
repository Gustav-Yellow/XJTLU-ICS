## Practical

## 1. 扩展汉堡店 (Factory Pattern)

**要求**：基于工厂模式示例，扩展代码以支持 **Chicken Burger** 。

```java
// 1. 实现具体产品类 [cite: 68, 73]
public class ChickenBurger implements Burger {
    @Override
    public void prepare() {
        System.out.println("Preparing Chicken Burger with crispy chicken fillet...");
    }
}

// 2. 实现具体工厂类 [cite: 74, 80]
public class ChickenBurgerRestaurant extends Restaurant {
    @Override
    public Burger createBurger() {
        return new ChickenBurger(); // 延迟实例化到子类 [cite: 63]
    }
}

// 3. 客户端调用示例 [cite: 80]
// 当需要 Chicken Burger 时，直接使用新的工厂类：
// Restaurant chickenRest = new ChickenBurgerRestaurant();
// chickenRest.orderBurger();
```

------

### 2. 文档管理系统 (Factory Pattern)

**要求**：设计一个支持 Word、PDF、Excel 等格式的系统，并确保未来能轻松引入新类型 。

```java
// 1. 定义抽象文档接口 [cite: 95]
interface IDocument {
    void open();
    void save();
    void close();
}

// 2. 具体文档实现 [cite: 96]
class WordDocument implements IDocument {
    public void open() { System.out.println("Opening Word document..."); }
    public void save() { System.out.println("Saving Word document..."); }
    public void close() { System.out.println("Closing Word document..."); }
}

// 3. 抽象工厂类 [cite: 102, 103]
abstract class DocumentFactory {
    public abstract IDocument createDocument();
    
    // 业务逻辑：封装初始化过程 [cite: 248]
    public void processDocument() {
        IDocument doc = createDocument();
        doc.open();
        doc.save();
        doc.close();
    }
}

// 4. 具体工厂：Word 工厂
class WordFactory extends DocumentFactory {
    public IDocument createDocument() { return new WordDocument(); }
}
```

------

### 3. 智能机器人 (Decorator Pattern)

**要求**：实现 `SmartRobotDecorator`，使机器人能同时具备 `Rational`（按性别分量）和 `Smart`（深度学习）的特性 。

```java
// 1. 实现 Smart 装饰器 [cite: 252]
public class SmartRobotDecorator extends RobotDecorator {
    public SmartRobotDecorator(Robot r) {
        super(r);
    }

    @Override
    public void Cook() {
        System.out.println("Applying Deep Learning to optimize cooking..."); [cite: 250]
        super.Cook(); 
    }
}

// 2. 演示“同时具备”特性 [cite: 253]
// 客户端代码示例
Robot basicRobot = new JapaneseRobot();
// 包装第一层：理性（分性别分量）
Robot rationalRobot = new RationalRobotDecorator(basicRobot, true); 
// 包装第二层：智能（深度学习）
Robot smartRationalRobot = new SmartRobotDecorator(rationalRobot);

smartRationalRobot.Cook(); 
// 输出结果将包含：深度学习优化 -> 性别判断分量 -> 制作日本菜 [cite: 208]
```

------

### 4. 咖啡馆场景 (Decorator Pattern)

**要求**：通过装饰器模式处理基础咖啡及其动态配料（牛奶、糖等）的成本计算 。

```java
// 1. 基础组件接口
interface Coffee {
    double getCost();
    String getDescription();
}

// 2. 具体组件：纯咖啡
class SimpleCoffee implements Coffee {
    public double getCost() { return 10.0; }
    public String getDescription() { return "Plain Coffee"; }
}

// 3. 装饰器基类 [cite: 167, 172]
abstract class CoffeeDecorator implements Coffee {
    protected Coffee decoratedCoffee;
    public CoffeeDecorator(Coffee c) { this.decoratedCoffee = c; }
}

// 4. 具体装饰器：牛奶
class MilkDecorator extends CoffeeDecorator {
    public MilkDecorator(Coffee c) { super(c); }
    public double getCost() { return decoratedCoffee.getCost() + 2.0; } [cite: 208]
    public String getDescription() { return decoratedCoffee.getDescription() + ", Milk"; }
}
```

------

### 5. 电商支付系统 (Adapter Pattern)

**要求**：使用适配器模式集成 PayPal、信用卡等具有不同 API 的支付系统 。

```java
// 1. 系统期望的统一接口 [cite: 222]
interface PaymentProcessor {
    void processPayment(double amount);
}

// 2. 第三方/不兼容的 API (Service) [cite: 223]
class PayPalService {
    public void makePayPalPayment(double amt) {
        System.out.println("Processing $" + amt + " via PayPal API.");
    }
}

// 3. 适配器类 [cite: 225, 226]
class PayPalAdapter implements PaymentProcessor {
    private PayPalService payPalService;

    public PayPalAdapter(PayPalService service) {
        this.payPalService = service;
    }

    @Override
    public void processPayment(double amount) {
        // 转换调用 [cite: 218]
        payPalService.makePayPalPayment(amount);
    }
}
```

## Theory

### Question 1: 日志文件写入控制

**场景描述**：所有部分需写入同一个日志文件，且同一时间只能有一个部分写入，以避免并发问题 。

- **建议模式**：**单例模式 (Singleton Pattern)** 。
- **理由**：
  - **全局访问点**：单例模式确保一个类只有一个实例，并提供一个全局访问点 。这保证了整个应用程序都在使用同一个 `Logger` 实例来操作同一个文件 。
  - **资源锁定**：通过单例，我们可以集中管理写入锁定机制，确保不会有多个实例同时尝试打开或写入文件，从而解决并发冲突 。

------

### Question 2: 视频流媒体缓冲与延迟加载

**场景描述**：视频流式传输开销巨大。初始仅持有引用，只有当用户点击观看时才从原始位置流式传输并缓冲数据 。

- **建议模式**：**代理模式 (Proxy Pattern)** 。
- **理由**：
  - **控制访问**：代理对象作为实际目标对象的替代品，用于控制对它的访问 。
  - **虚拟代理 (Virtual Proxy)**：在这种场景下，代理对象在视频真正被需要前充当占位符（即“引用”） 。它能够延迟加载资源密集型的操作（视频流传输），直到用户触发调用，从而减少带宽压力和服务器负载 。

------

### Question 3: 车辆租赁服务系统

**场景描述**：系统需要根据客户选择（汽车、卡车、摩托车）创建对应类型的对象。直接在应用内创建会导致重复且难以维护的代码 。

- **建议模式**：**工厂模式 (Factory Pattern)** 。
- **理由**：
  - **封装初始化**：该模式将对象创建的复杂过程封装在工厂类中，减少重复代码 。
  - **解耦**：允许子类决定实例化哪一个具体类（如 `Car` 或 `Truck`），使高层代码不依赖于具体的车辆实现 。

------

### Question 4: 多源数据分析工具

**场景描述**：工具需处理来自 SQL、NoSQL、CSV 和 JSON 等不同来源的数据，每种来源的访问方式和返回格式都不同。直接集成会导致代码杂乱且难以维护 。

- **建议模式**：**适配器模式 (Adapter Pattern)** 。
- **理由**：
  - **接口转换**：适配器模式充当两个不兼容接口之间的连接器 。
  - **统一协议**：您可以为各种数据源（SQL, CSV 等）编写适配器，将它们各异的查询方式和返回格式转换成系统内部统一的 `DataResult` 接口 。这样分析引擎就只需处理一个标准的接口，而无需关心后端数据的具体来源 。

------

### Question 5: 文件与目录层级系统

**场景描述**：系统包含“文件”（叶子节点，有内容和大小）和“目录”（可以包含文件或其他目录，大小为内容物总和） 。

- **建议模式**：**组合模式 (Composite Pattern)** 。
- **理由**：
  - **部分-整体层级**：该模式允许以相同的方式处理单个对象（文件）和对象的组合（目录） 。
  - **递归结构**：目录可以包含其他组件（即其他目录或文件），通过统一的接口调用 `getSize()` 时，目录可以递归计算其内部所有子项的大小之和，而客户端无需区分处理的是文件还是文件夹。

------

### Question 6: 文本编辑器格式化

**场景描述**：用户可以为纯文本独立或组合应用多种格式（加粗、斜体、下划线、删除线） 。

- **建议模式**：**装饰器模式 (Decorator Pattern)** 。
- **理由**：
  - **动态添加行为**：允许在不影响其他对象的情况下，动态地为单个对象添加功能 。
  - **避免类爆炸**：如果使用继承，处理加粗+斜体、加粗+下划线等组合会产生大量的子类。而装饰器通过“包装（Wrapping）”机制，让你可以像穿衣服一样，随意叠加多层格式化效果 。